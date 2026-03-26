# -*- coding: utf-8 -*-
"""
Simulateur de SIM-3000
Paul Guertin, janvier 2024
"""

import FreeSimpleGUI as sg
VERSION = "1.1"

####################################################################
# Pour pouvoir exÃ©cuter ce programme, le module "freesimplegui" doit
# Ãªtre installÃ©. S'il ne l'est pas, vous pouvez probablement taper
# la commande "pip install freesimplegui" (sans les guillemets) dans
# la console Python.
####################################################################

# Taille max d'un programme et taille de la RAM
PROGSIZE = 50
RAMSIZE = 50

# Instructions
INSTRUCTIONS = ["LOAD", "ADD", "SUB", "STORE", "READ", "JUMP", "JZERO", "JNEG", "NOP"]

def readfile(filename):
    try:
        errmsg = f"Fichier {filename} impossible Ã  ouvrir"
        with open(filename, "r", encoding="utf8") as f:
            instructions = []
            for (i, line) in enumerate(f):
                instr = line.strip().upper()
                if "#" in instr:
                    instr = instr[0:instr.find("#")]
                instr = instr.strip()
                if instr == "":
                    continue
                if len(instr.split()) != 2:
                    errmsg = f"Ligne {i}: erreur de syntaxe {instr}"
                op, arg = instr.split()
                if op not in INSTRUCTIONS:
                    errmsg = f"Ligne {i}: instruction {op} invalide"
                    raise AssertionError
                errmsg = f"Ligne {i}: argument {arg} invalide"
                if not (arg=="MEM" or arg.isnumeric() or arg[0]=="-" and arg[1:].isnumeric()):
                    raise AssertionError
                instructions.append(instr)
        instructions = instructions[:PROGSIZE]
        while len(instructions) < PROGSIZE:
            instructions.append("NOP 0")
            window["erreur"].update(f"Fichier {filename} rÃ©cupÃ©rÃ©")
        return instructions
    except (IOError, AssertionError, TypeError, ValueError):
        window["erreur"].update(errmsg)
        return None

def ramtext(ram):
    return "\n".join(f"{i:02} : {ram[i]}" for i in range(RAMSIZE))

def progtext(prog):
    return "\n".join(f"{i:02} : {instr}" for i, instr in enumerate(prog))

def popup_setpc():
    col_layout = [[sg.Button("OK", bind_return_key=True), sg.Button('Annuler')]]
    layout = [
        [sg.Text("Entrez la valeur du PC: "), sg.InputText(key="newpc", focus=True)],
        [sg.Column(col_layout, expand_x=True, element_justification='right')],
    ]
    window = sg.Window("Modifier le PC", layout, use_default_focus=False, finalize=True, modal=True)
    event, values = window.read()
    window.close()
    return values['newpc'] if event == 'OK' else None

def popup_setram(oldram):
    col_layout = [[sg.Button("OK", bind_return_key=True), sg.Button('Annuler')]]
    layout = [
        [sg.Text("Adresse de dÃ©part: "), sg.InputText(key="adresse", focus=True)],
        [sg.Text("Valeurs sÃ©parÃ©es par des espaces: "), sg.InputText(key="valeurs")],
        [sg.Column(col_layout, expand_x=True, element_justification='right')],
    ]
    window = sg.Window("Modifier la RAM", layout, use_default_focus=False, finalize=True, modal=True)
    event, values = window.read()
    window.close()
    newram = oldram.copy()
    try:
        debut = int(values["adresse"])
        vals = [int(x) for x in values["valeurs"].split()]
        for (i, v) in enumerate(vals):
            newram[debut+i] = v
    except:
        pass
    return newram if event == 'OK' else None

def reset():
    global pc, acc, adr
    pc = acc = adr = 0
    window["pc"].update(pc)
    window["adr"].update(adr)
    window["acc"].update(acc)
    window["pgm"].update(progtext(prog))
    window["ram"].update(ramtext(ram))

def execute():
    '''ExÃ©cute la prochaine instruction'''
    global pc, adr, acc

    if not (0 <= pc < PROGSIZE):
        return
    opcode, arg = prog[pc].split()
    arg = ram[adr] if arg == "MEM" else int(arg)

    if opcode == "LOAD":
        acc = arg
        window["acc"].update(acc)
        pc += 1
    elif opcode == "ADD":
        acc += arg
        window["acc"].update(acc)
        pc += 1
    elif opcode == "SUB":
        acc -= arg
        window["acc"].update(acc)
        pc += 1
    elif opcode == "STORE":
        ram[arg] = acc
        window["ram"].update(ramtext(ram))
        pc += 1
    elif opcode == "READ":
        adr = arg
        window["adr"].update(adr)
        pc += 1
    elif opcode == "JUMP":
        pc = arg
    elif opcode == "JZERO":
        pc = arg if acc == 0 else pc + 1
    elif opcode == "JNEG":
        pc = arg if acc < 0 else pc + 1
    elif opcode == "NOP":
        pc += 1
    if pc >= PROGSIZE or pc < 0:
        pc = 0

# =============================================================================
# DÃ©finition de l'interface principale
# =============================================================================

left_col = sg.Column([[sg.Text("Programme")],
                      [sg.Multiline(size=(30,PROGSIZE), key="pgm", no_scrollbar=True, disabled=True)]], element_justification="center")
mid_col = sg.Column([
        [sg.Text("PC")],
        [sg.Multiline(size=(7,1), key="pc", font="Any 14", no_scrollbar=True, disabled=True, justification="right")],
        [sg.Text("Acc")],
        [sg.Multiline(size=(7,1), key="acc", font="Any 14", no_scrollbar=True, disabled=True, justification="right")],
        [sg.Text("Adr")],
        [sg.Multiline(size=(7,1), key="adr",font="Any 14", no_scrollbar=True, disabled=True, justification="right")],
        [sg.HorizontalSeparator(pad=(20,20))],
        [sg.Slider(range=(1,10), orientation="h", size=(20,20), key="speed", enable_events=True)],
        [sg.HorizontalSeparator(pad=(20,20))],
        [sg.Button("ExÃ©cuter le programme", key="run")],
        [sg.Button("ExÃ©cuter une instruction", key="step")],
        [sg.HorizontalSeparator(pad=(20,20))],
        [sg.Button("ZÃ©roter le PC", key="zeropc")],
        [sg.Button("Modifier le PC", key="setpc")],
        [sg.HorizontalSeparator(pad=(20,20))],
        [sg.Button("ZÃ©roter la RAM", key="zeroram")],
        [sg.Button("Modifier la RAM", key="setram")],
    ], element_justification="center")

right_col = sg.Column([[sg.Text("RAM")], [sg.Multiline(size=(30,RAMSIZE), key="ram", no_scrollbar=True, disabled=True)]], element_justification="center")

layout = [[sg.Text("SIMSIM - Le simulateur de SIM-3000", font="Any 12")],
          [sg.Text("Programme:"), sg.InputText(enable_events=True, key="load", size=(70,1)), sg.FileBrowse("Choisir", target="load")],
          [left_col, mid_col, right_col],
          [sg.Text(VERSION, key="erreur")]]

window = sg.Window("SIM-3000", layout, finalize=True, location=(0,0))

ml = window["pgm"]
widget = ml.Widget
widget.tag_config("HIGHLIGHT", foreground="white", background="blue")

# Valeurs initiales

pc = 0
adr = 0
acc = 0
ram = [0]*RAMSIZE
prog = ["NOP 0"] * PROGSIZE
vitesse = 10
running = False
defaultcolor = window["run"].ButtonColor
reset()
widget.tag_add("HIGHLIGHT", "1.0", "1.2")

# Boucle principale

while True:
    event, values = window.read(timeout=vitesse**3)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "load":
        prog = readfile(values["load"])
        if prog:
            reset()
            widget.tag_add("HIGHLIGHT", "1.0", "1.2")
        else:
            window["pgm"].update("")
    elif event == "zeroram":
        ram = [0]*RAMSIZE
        window["ram"].update(ramtext(ram))
    elif event == "zeropc":
        widget.tag_remove("HIGHLIGHT", f"{pc+1}.0", f"{pc+1}.2")
        pc = 0
        window["pc"].update(pc)
        widget.tag_add("HIGHLIGHT", "1.0", "1.2")
    elif event == "setpc":
        newpc = popup_setpc()
        if newpc:
            widget.tag_remove("HIGHLIGHT", f"{pc+1}.0", f"{pc+1}.2")
            try:
                pc = int(newpc)
                if pc < 0:
                    pc = 0
                if pc >= PROGSIZE:
                    pc = PROGSIZE-1
            except:
                pass
            window["pc"].update(pc)
            widget.tag_add("HIGHLIGHT", f"{pc+1}.0", f"{pc+1}.2")
    elif event == "setram":
        newram = popup_setram(ram)
        if newram:
            for i in range(len(newram)):
                ram[i] = newram[i]
        window["ram"].update(ramtext(ram))
    elif event == "step" or (running and event == "__TIMEOUT__"):
        widget.tag_remove("HIGHLIGHT", f"{pc+1}.0", f"{pc+1}.2")
        execute()
        window["pc"].update(pc)
        widget.tag_add("HIGHLIGHT", f"{pc+1}.0", f"{pc+1}.2")
    elif event == "speed":
        vitesse = 10 - int(values["speed"])
    elif event == "run":
        running = not running
        if running:
            window["run"].update(button_color = ('white','red'))
        else:
            window["run"].update(button_color = defaultcolor)

window.close()
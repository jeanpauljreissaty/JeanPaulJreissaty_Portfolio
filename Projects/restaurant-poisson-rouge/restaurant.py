#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:26 2024

@author: jp
"""

#Daniel Zgardan, Jean-Paul Jressity

import random
from tkinter import *
import tkinter as tk
import pygame
from PIL import ImageTk, Image
from datetime import datetime
import pyglet
from meteostat import Point, Daily

# La réservation

#Tant que c'est vrai essaye d'afficher la question et gere les exceptions 
while True:
    try:
        prenom, nom = input("Bienvenue au Poisson Rouge, la réservation est au nom de qui (prénom nom)? ").split()
        if nom.isalpha() == False or prenom.isalpha() == False:         #si le nom et prenom n'incluent pas des lettres
            print("Veuillez utiliser que des lettres! ")
        else:
            break        #sinon arrete de boucler
    except:
        ValueError       #a cause du split
        print("Veuillez taper votre prénom suivit d'un espace et de votre nom!")



#La confirmation

fen = Tk()
fen.geometry("500x500")
fen.maxsize(500,500)
fen.minsize(500, 500)
fen.title("Restaurant Poisson Rouge")

valide = False
#Validation du nom et du prénom
def action():      
    while True:
        if EntreNom.get() == nom and EntrePrenom.get() == prenom :
            salle.create_rectangle(table, outline="black", fill = "dark grey")  #change la couleur de la case une fois que la coordonnée choisit
            print("VALIDÉ! Veuillez vous asseoir.")
            global valide                                                       
            valide = True       # change valide pour True pour actionner le bouton sassoir
            
                 

            for element in dicts_tables.keys():
                if table == element:
                    chiffre = dicts_tables[table]
                    chiffre.config(font = police, bg = "dark grey")
                       
            
        else:
            print("INVALIDE! Veuillez réessayer.")
            
        break

#Activation du bouton SASSOIR
def fermer():
    if valide == True:              # si valide == True, alors actionne le bouton pour détruire la fenêtre
        fen.destroy()
    else:
        print("Vous ne pouvez pas vous asseoir!")
        
police = ("Comic sans MS", 15, "bold")              #font 1



#Texte Nom
affiche_nom = Label(fen, text = "Nom")
affiche_nom.config(font = police)
affiche_nom.place(relx = 0.2, rely = 0.2, anchor = CENTER)

#Entre Nom
EntreNom = Entry(fen, width = 15)
EntreNom.config(font = police)
EntreNom.place(relx=0.2, rely=0.3, anchor= CENTER)


#Texte Prenom
affiche_prenom = Label(fen, text = "Prénom")
affiche_prenom.config(font = police)
affiche_prenom.place(relx=0.2, rely= 0.4, anchor=CENTER)

#Entre Prenom
EntrePrenom = Entry(fen, width = 15)
EntrePrenom.config(font = police)
EntrePrenom.place(relx=0.2, rely=0.5, anchor= CENTER)




#Boutton Valider
bouton_valider = Button(fen, text = "VALIDER", command = action)
bouton_valider.config(font = police)
bouton_valider.place(relx=0.2, rely=0.8, anchor= CENTER)




#Création du Canevas
salle= Canvas(width=240, height=240, bg="white")
salle.place(relx= 0.7, rely = 0.4, anchor = CENTER )



#Création des tables
salle.create_rectangle(2,2, 80, 80, outline="black" )     

#affichage de chiffre
chiffre1 = Label(fen, text = "1")
chiffre1.config(font = police, bg = "white")
chiffre1.place(x = 260, y = 110)

#Création des tables
salle.create_rectangle(160,2, 80, 80, outline="black" )  

#affichage de chiffre
chiffre2 = Label(fen, text = "2")
chiffre2.config(font = police, bg = "white")
chiffre2.place(x = 340, y = 110)

#Création des tables
salle.create_rectangle(241,2, 160, 80, outline="black" )    

#affichage de chiffre
chiffre3 = Label(fen, text = "3")
chiffre3.config(font = police, bg = "white")
chiffre3.place(x = 420, y = 110)

#Création des tables
salle.create_rectangle(2,160, 80, 80, outline="black" )   

#affichage de chiffre
chiffre4 = Label(fen, text = "4")
chiffre4.config(font = police, bg = "white")
chiffre4.place(x = 260, y = 190)

#Création des tables
salle.create_rectangle(160,160, 80, 80, outline="black" )    

#affichage de chiffre
chiffre5 = Label(fen, text = "5")
chiffre5.config(font = police, bg = "white")
chiffre5.place(x = 340, y = 190)


#Création des tables
salle.create_rectangle(241,160, 160, 80, outline="black" )    

#affichage de chiffre
chiffre6 = Label(fen, text = "6", )
chiffre6.config(font = police, bg = "white")
chiffre6.place(x = 420, y = 190)

#Création des tables
salle.create_rectangle(2, 241, 80, 160, outline="black" )    

#affichage de chiffre
chiffre7 = Label(fen, text = "7")
chiffre7.config(font = police, bg = "white")
chiffre7.place(x = 260, y = 265)

#Création des tables
salle.create_rectangle(160,241, 80, 160, outline="black" )    

#affichage de chiffre
chiffre8 = Label(fen, text = "8")
chiffre8.config(font = police,bg = "white")
chiffre8.place(x = 340, y = 265)

#Création des tables
salle.create_rectangle(241,241, 160, 160, outline="black" )  

#affichage de chiffre
chiffre9 = Label(fen, text = "9")
chiffre9.config(font = police, bg = "white")
chiffre9.place(x = 420, y = 265)




#choisir la table
liste_coord_table = [(2,2, 80, 80), (160,2, 80, 80), (241,2, 160, 80), 
                      (2,160, 80, 80), (160,160, 80, 80), (241,160, 160, 80),         #liste des coordonnees des tables 
                      (2, 241, 80, 160), (160,241, 80, 160), (241,241, 160, 160)]

table = random.choice(liste_coord_table)    #Pige une coordonnees de la  liste


dicts_tables = {(2,2, 80, 80): chiffre1, (160,2, 80, 80):chiffre2, (241,2, 160, 80): chiffre3,
                (2,160, 80, 80):  chiffre4, (160,160, 80, 80):chiffre5, (241,160, 160, 80): chiffre6,
                (2, 241, 80, 160): chiffre7, (160,241, 80, 160): chiffre8, (241,241, 160, 160): chiffre9}



#Boutton sassoir
bouton_sassoir = Button(fen, text = "SASSOIR", command = fermer)
bouton_sassoir.config(font = police)
bouton_sassoir.place(relx=0.7, rely=0.8, anchor= CENTER)





fen.mainloop()











#Le menu

fen3 = Tk()
fen3.geometry("500x500")
fen3.maxsize(500,500)
fen3.minsize(500, 500)
fen3.title("Menu")

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
couleur = rgb_to_hex(255, 233, 192)   #transforme la couleur choisit en variable
couleur2 = rgb_to_hex(159, 91, 30)

def fermer2():       #fonction pour detruire la fenêtre une fois le bouton commander actionner
    fen3.destroy()


police2 = ("Ariel", 15, "underline", "bold")            #font 2
police3 = ("Comic sans MS", 11)

image_menu = ImageTk.PhotoImage(Image.open("menu_parchemin.png").resize((600, 600)))

canvas1 = Canvas(width=500, height=500)
canvas1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
canvas1.create_image(250, 250 , image = image_menu, anchor= CENTER)


#Entrées au choix 
Entrees_au_choix = Label(fen3, text = "Entrées au choix", bg = couleur )
Entrees_au_choix.config(font = police2)
Entrees_au_choix.place(relx = 0.5, rely = 0.22, anchor = CENTER)

#Soupe à l'oignon texte
soupe_txt = Label(fen3, text = "#1 Soupe à l’oignon non gratinée 6.99$, gratinée 7.99$", bg = couleur)
soupe_txt.config(font = police3)
soupe_txt.place(relx = 0.5, rely = 0.28, anchor = CENTER)

#Croquette texte
croquettes_txt = Label(fen3, text = "#2 Croquettes de thon, 8.99$", bg = couleur)
croquettes_txt.config(font = police3)
croquettes_txt.place(relx = 0.5, rely = 0.33, anchor = CENTER)


#Repas au choix 
Repas_au_choix = Label(fen3, text = "Repas au choix", bg = couleur)
Repas_au_choix.config(font = police2)
Repas_au_choix.place(relx = 0.5, rely = 0.42, anchor = CENTER)

#poisson texte
poisson_txt = Label(fen3, text = "#1 Poisson avec des pommes de terre, 21.99$", bg = couleur)
poisson_txt.config(font = police3)
poisson_txt.place(relx = 0.5, rely = 0.48, anchor = CENTER)

#steak texte
steak_txt = Label(fen3, text = "#2 Steak avec des légumes du jardin, 29.99$", bg = couleur)
steak_txt.config(font = police3)
steak_txt.place(relx = 0.5, rely = 0.53, anchor = CENTER)

#Desserts au choix
Desserts_au_choix = Label(fen3, text = "Desserts au choix", bg = couleur)
Desserts_au_choix.config(font = police2)
Desserts_au_choix.place(relx = 0.5, rely = 0.62, anchor = CENTER)

#cafe texte
cafe_txt = Label(fen3, text = "#1 Café, 3.29$", bg = couleur)
cafe_txt.config(font = police3)
cafe_txt.place(relx = 0.5, rely = 0.68, anchor = CENTER)

#gateau texte
gateau_txt = Label(fen3, text = "#2 Un quart de gâteau au fromage, 4.25$", bg = couleur)
gateau_txt.config(font = police3)
gateau_txt.place(relx = 0.5, rely = 0.73, anchor = CENTER)


#Boutton COMMANDER
bouton_commander = Button(fen3, text = "COMMANDER", command = fermer2, activebackground = couleur2, bg = couleur2)
bouton_commander.config(font = police)
bouton_commander.place(relx=0.5, rely=0.94, anchor= CENTER)

fen3.mainloop()














#Le service

#Configuration de la fênetre tkinter
fen1 = Tk()
def rgb_to_hex(r, g, b):
    """Fonction retournant la couleur en héxadécimal"""
    return f'#{r:02x}{g:02x}{b:02x}'

couleur_serv = rgb_to_hex(193, 125, 66)

fen1.geometry("500x500")
fen1.title("Le service")
fen1.configure(bg= "orange")
fen1.minsize(500, 500)
fen1.maxsize(500, 500)




def action2 ():
    """"fonction permettant d'enregister les choix de l'utilisateur à l'aide des Chekbuttons et d'affichage ses choix
    Les variables choix1, choix2 et choix3 sont des Labels qui vont être mis à jour en fonction des cases choisies """

    if bool1.get()==1 and bool2.get()==1:     # si l'usager coche 2 cases
        choix1.config(text="Un choix seulement s'il vous plait")

    if bool1.get()==0 and bool2.get()==0:     # si l'usager décide de ne plus cocher la case 1 et 2
        choix1.place_forget()
        choix2.place_forget()
        c3.place_forget()

    if bool1.get() == 0 and bool2.get() == 1:   # Si l'usager coche la case 2
        choix1.config(text="Croquettes !")
        choix1.place(relx=0.75, rely=0.40, anchor=CENTER)
        choix2.place_forget()
        c3.place_forget()

    if bool1.get()==1 and bool2.get()==0:       # Si l'usager coche la case 1
        choix1.config(text="Soupe a l'oignon chosie !")
        choix1.place(relx=0.75, rely=0.40, anchor=CENTER)
        c3.place(relx=0.75, rely=0.45, anchor=CENTER)
        choix2.place(relx=0.75, rely=0.50, anchor=CENTER)
        if bool3.get()==0:
            choix2.config(text="pas gratinnée")

        if bool3.get()==1:
            choix2.config(text="Soupe gratinnée a l'oignon !")

    if bool4.get()==1 and bool5.get()==1:     # si l'usager coche 2 cases
        choix3.config(text="1 Choix seulement s'il vous plait")

    if bool4.get()==1 and bool5.get()==0:     # si l'usager coche la case 4
        choix3.config(text="Poisson !")
        choix3.place(relx=0.75, rely=0.60, anchor=CENTER)

    if bool4.get()==0 and bool5.get()==1:     # si l'usager coche la case 5
        choix3.config(text="Steak !")
        choix3.place(relx=0.75, rely=0.60, anchor=CENTER)

    if bool4.get()==0 and bool5.get()==0:     # si l'usager décide de ne plus cocher aucune case
        choix3.place_forget()


    if bool6.get() == 1 and bool7.get() == 1:   # # si l'usager coche 2 cases
        choix4.config(text="1 Choix seulement s'il vous plait")

    if bool6.get() ==0 and bool7.get()==0:       # si l'usager décide de ne plus cocher aucune case
        choix4.place_forget()

    if bool6.get() == 1 and bool7.get() == 0:   # si l'usager coche la case 6
        choix4.config(text="Café !")
        choix4.place(relx=0.75, rely=0.75, anchor=CENTER)

    if bool6.get() == 0 and bool7.get() == 1:    # si l'usager coche la case 7
        choix4.config(text="Quart de gateau !")
        choix4.place(relx=0.75, rely=0.75, anchor=CENTER)


def action3():
    """Fonction permettant d'afficher le texte_anno ainsi que le bouton "Commander" """
    global choix_entree
    global choix_repas
    global choix_dessert

    global texte_anno

    choix_entree = bool1.get()  ^ bool2.get()    #XOR un "ou"  exclusif
    choix_repas = bool5.get()  ^ bool4.get()
    choix_dessert = bool6.get() ^ bool7.get()

    if choix_repas and choix_entree and choix_dessert:

        #Conditions à remplir avant l'affichage
        texte_anno = Label(fen1, text="Merci, ça ne sera pas long !", bg=couleur_serv)
        texte_anno.place(relx= 0.25, rely= 0.85, anchor=CENTER)
        BT_1.config(command=fermer3)


          

def choix():
    """Fonction permettant de retourner les choix effectués par l'utilisateur """
    global liste_choix
    #Dictionnaire qui associe toute les options du menu à une varibale booléenne
    dict_var = {"Soupe à l'oignon":bool1.get(), "Croquettes":bool2.get(), "Soupe à l'oignon gratinée":bool3.get(), "Poisson":bool4.get(), "Steak":bool5.get(),
                "Café":bool6.get(), "Quart de Gateau":bool7.get()}
    liste_choix = []
    for i in dict_var.keys():     # On verifie si le booléen a été coché pour le mettre son option du menu dans la liste
        if dict_var[i] == True:
            liste_choix.append(i)
    if liste_choix[1] == "Soupe à l'oignon gratinée":  # on retire l'option  de la liste "Soupe à l'oignon" si "Soupe à l'oignon gratinée" est présent
        liste_choix.remove("Soupe à l'oignon")
   
    return liste_choix
   

def fermer3():
    """Fonction qui détruit la fenêtre """
    fen1.destroy()


#liste de nom des serveurs/serveuses
liste_de_nom = ["Vanessa", "Ray", "Anais", "Andrew"]
nom = random.choice(liste_de_nom)

#Presentation des serveurs/serveuses
if nom == "Vanessa" or nom == "Anais":
    texte_pres = Label(fen1, text= f"Bonjour, je m'appelle {nom} et je serai votre serveuse, aujourd'hui!")
    image_pres = ImageTk.PhotoImage(Image.open("serveuse.png").resize((250, 250)))

else:
    texte_pres = Label(fen1, text=f"Bonjour, je m'appelle {nom} et je serai votre serveur, aujourd'hui!")
    image_pres = ImageTk.PhotoImage(Image.open("serveur2.png").resize((250, 250)))


#Canvas image serveur
canvas = Canvas(width=250, height=250, bg= "orange")
canvas.place(relx = 0.25, rely= 0.5, anchor =CENTER)
canvas.create_image(125, 125 , image = image_pres, anchor= CENTER)

#canvas image carnet
image_carnet = ImageTk.PhotoImage(Image.open("notepad2.png").resize((250, 300)))
canvas2 = Canvas(width=250, height=300, bd=1, bg="orange")
canvas2.place(relx = 0.75, rely=0.55, anchor=CENTER)
canvas2.create_image(125, 150, image = image_carnet, anchor =CENTER)


#Texte presentation serveur
police1 =  ("Comic sans MS", 12)
texte_pres.config(font = police1, bg = "orange", fg= "black")
texte_pres.place(relx=0.5, rely= 0.075, anchor=CENTER)

#Texte il est temps de chosir
texte_pres2 = Label(fen1, text="Il est temps de choisr !", bg= "orange")
texte_pres2.config(font=police1)
texte_pres2.place(relx=0.75, rely=0.175, anchor=CENTER)

#Texte annoncant que la nourriture arrive
# texte_anno = Label(fen1, text="Merci, ça ne sera pas long !", bg=couleur_serv)


#Choix entrée
choix1= Label(fen1, bg="orange")

#choix gratinée ou pas
choix2 = Label(fen1, bg="orange")

#choix repas
choix3 = Label(fen1, bg="orange")

#choix dessert
choix4 = Label(fen1, bg="orange")

# variables des booléens requis pour faire le choix de menu
bool1 = BooleanVar()
bool2 = BooleanVar()
bool3 = BooleanVar()
bool4 = BooleanVar()
bool5 = BooleanVar()
bool6 = BooleanVar()
bool7 = BooleanVar()

#Chekbutton #1
c1 = tk.Checkbutton(fen1, text="Entrée 1", variable=bool1, onvalue=1, offvalue=0, command=action2)
c1.place(relx=0.65, rely=0.35, anchor=CENTER)

#Chekbutton #2
c2 = tk.Checkbutton(fen1, text="Entrée 2", variable=bool2, onvalue=1, offvalue=0, command=action2)
c2.place(relx=0.85, rely=0.35, anchor=CENTER)

#Chekbutton #3
c3 = tk.Checkbutton(fen1, text="Gratinée ?", variable=bool3, onvalue=1, offvalue=0, command=action2)

#Chekbutton #4
c4 = tk.Checkbutton(fen1, text="Repas 1", variable=bool4, onvalue=1, offvalue=0, command=action2)
c4.place(relx=0.65, rely=0.55, anchor=CENTER)

#Chekbutton #5
c5 = tk.Checkbutton(fen1, text="Repas 2", variable=bool5, onvalue=1, offvalue=0, command=action2)
c5.place(relx=0.85, rely=0.55, anchor=CENTER)

#Chekbutton #6
c6 = tk.Checkbutton(fen1, text="Dessert 1", variable=bool6, onvalue=1, offvalue=0, command=action2)
c6.place(relx=0.65, rely=0.70, anchor=CENTER)

#Chekbutton #7
c7 = tk.Checkbutton(fen1, text="Dessert 2", variable=bool7, onvalue=1, offvalue=0, command=action2)
c7.place(relx=0.85, rely=0.70, anchor=CENTER)

#Bouton "Servir"
BT_1 = Button(fen1, text= "SERVIR", font= 13, fg= "black", bg=couleur_serv, activebackground="orange")
BT_1.place(relx = 0.5, rely = 0.95, anchor =CENTER)

#Bouton "Commander"
bt2 = Button(fen1, text = "COMMANDER", fg="black", bg=couleur_serv, activebackground="orange", command=lambda:[action3(), choix()])
bt2.place(relx = 0.75, rely = 0.90, anchor =CENTER)


#Fonctions permettant le changement de couleur des boutons
def outBT_1(event):
    BT_1["bg"] = couleur_serv

def hoverBT_1(event):
    BT_1["bg"] = "orange"

def outbt2(event):
    bt2["bg"] = couleur_serv

def hoverbt2(event):
    bt2["bg"] = "orange"

#Asssocier aux boutons les fonctions "out" et "hover"
BT_1.bind("<Enter>", hoverBT_1)
BT_1.bind("<Leave>", outBT_1)

bt2.bind("<Enter>", hoverbt2)
bt2.bind("<Leave>", outbt2)

fen1.mainloop()






#Repas à table
pygame.init()


LARGEUR, HAUTEUR = 500, 500
ECRAN = pygame.display.set_mode((LARGEUR,HAUTEUR))

Largeur = ECRAN.get_width()
Hauteur = ECRAN.get_height()
ECRAN.fill((240, 240, 240))
pygame.display.set_caption("Repas à table")


#Couleur utilisé
brun_foncee = (101, 67, 33)
gris = (192, 192, 192)
beige = (220, 205, 183)
rouge = (200, 0, 0)
rouge_foncee = (139, 0, 0)
orange = (255, 165, 0)
orange_foncee = (160, 64, 0)
beige_foncee = (160, 64, 0)
vert = (0, 128, 0)
vert_foncee = (24, 106, 59)
jaune_claire = (247, 220, 111)
jaune = (255, 223, 0)
jaune_foncee =(255, 200, 0)
bleu = (102, 178, 255)
patate_brun = (210, 180, 140)
blanc = (255,255,255)
gris_claire = (244, 205, 166)

#Fonction pour la soupe non gratinée 
def soupe():
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Soupe à l’oignon non gratinée
    pygame.draw.ellipse(ECRAN, gris, (135, 185, 230, 130), 13)
    pygame.draw.ellipse(ECRAN, jaune, (150, 200, 200, 100))
    pygame.draw.ellipse(ECRAN, orange_foncee, (150, 210, 200, 90), 5)
    pygame.draw.arc(ECRAN, brun_foncee, (170, 220, 160, 60), 0, 3.14, 3)
    # oignon vert
    pygame.draw.circle(ECRAN, vert, (175, 230), 7)
    pygame.draw.circle(ECRAN, vert, (240, 220), 5)
    pygame.draw.circle(ECRAN, vert, (260, 215), 7)
    pygame.draw.circle(ECRAN, vert, (290, 240), 5)
    pygame.draw.circle(ECRAN, vert, (240, 270), 5)
    pygame.draw.circle(ECRAN, vert, (290, 215), 5)
    pygame.draw.circle(ECRAN, vert, (220, 270), 5)
    pygame.draw.circle(ECRAN, vert, (215, 200), 5)
    pygame.draw.circle(ECRAN, vert, (190, 260), 7)
    pygame.draw.circle(ECRAN, vert, (280, 260), 7)




#Fonction pour la soupe gratinée 
def soupe_gratinee():
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Soupe à l’oignon gratinée
    pygame.draw.ellipse(ECRAN, gris, (135, 185, 230, 130), 12)
    pygame.draw.ellipse(ECRAN, jaune_claire, (150, 200, 200, 100))
    pygame.draw.ellipse(ECRAN, orange_foncee, (150, 210, 200, 90), 5)
    pygame.draw.arc(ECRAN, brun_foncee, (170, 220, 160, 60), 0, 3.14, 3)
    # oignon vert
    pygame.draw.circle(ECRAN, vert, (175, 230), 7)
    pygame.draw.circle(ECRAN, vert, (240, 220), 5)
    pygame.draw.circle(ECRAN, vert, (260, 215), 7)
    pygame.draw.circle(ECRAN, vert, (290, 240), 5)
    pygame.draw.circle(ECRAN, vert, (240, 270), 5)
    pygame.draw.circle(ECRAN, vert, (290, 215), 5)
    pygame.draw.circle(ECRAN, vert, (220, 270), 5)
    pygame.draw.circle(ECRAN, vert, (215, 200), 5)
    pygame.draw.circle(ECRAN, vert, (190, 260), 7)
    pygame.draw.circle(ECRAN, vert, (280, 260), 7)
    # fromage jaune
    pygame.draw.line(ECRAN, jaune_foncee, (170, 220), (170, 270), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (190, 220), (190, 280), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (210, 210), (210, 290), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (230, 200), (230, 290), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (250, 210), (250, 290), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (270, 210), (270, 290), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (290, 210), (290, 295), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (310, 210), (310, 290), 5)
    pygame.draw.line(ECRAN, jaune_foncee, (330, 220), (330, 280), 5)
    # fromage orange
    pygame.draw.line(ECRAN, orange, (180, 220), (180, 270), 5)
    pygame.draw.line(ECRAN, orange, (200, 220), (200, 280), 5)
    pygame.draw.line(ECRAN, orange, (220, 210), (220, 290), 5)
    pygame.draw.line(ECRAN, orange, (240, 200), (240, 290), 5)
    pygame.draw.line(ECRAN, orange, (260, 210), (260, 290), 5)
    pygame.draw.line(ECRAN, orange, (280, 210), (280, 290), 5)
    pygame.draw.line(ECRAN, orange, (300, 210), (300, 295), 5)
    pygame.draw.line(ECRAN, orange, (320, 210), (320, 290), 5)
    pygame.draw.line(ECRAN, orange, (340, 220), (340, 280), 5)




#Fonction pour les croquettes
def croquettes():
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Croquettes de thon
    pygame.draw.ellipse(ECRAN, gris, (135, 170, 230, 130), 70)
    pygame.draw.circle(ECRAN, (241, 196, 15), (280, 200), 30)
    pygame.draw.circle(ECRAN, (212, 172, 13), (280, 200), 25)
    pygame.draw.circle(ECRAN, (241, 196, 15), (220, 200), 30)
    pygame.draw.circle(ECRAN, (212, 172, 13), (220, 200), 25)
    pygame.draw.circle(ECRAN, (241, 196, 15), (280, 240), 30)
    pygame.draw.circle(ECRAN, (212, 172, 13), (280, 240), 25)
    pygame.draw.circle(ECRAN, (241, 196, 15), (220, 240), 30)
    pygame.draw.circle(ECRAN, (212, 172, 13), (220, 240), 25)



#Fonction pour le steak
def steak():
    
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Steak avec des légumes du jardin
    pygame.draw.ellipse(ECRAN, gris, (135, 170, 230, 130), 50)
    pygame.draw.ellipse(ECRAN, rouge, (150, 220, 200, 50))
    pygame.draw.ellipse(ECRAN, rouge_foncee, (140, 215, 180, 50), 5)
    pygame.draw.arc(ECRAN, brun_foncee, (170, 220, 160, 60), 0, 3.14, 3)
    # Carrot
    pygame.draw.circle(ECRAN, orange, (230, 205), 15)
    pygame.draw.circle(ECRAN, orange_foncee, (230, 205), 8)
    pygame.draw.circle(ECRAN, orange, (260, 205), 15)
    pygame.draw.circle(ECRAN, orange_foncee, (260, 205), 8)
    pygame.draw.circle(ECRAN, orange, (290, 210), 15)
    pygame.draw.circle(ECRAN, orange_foncee, (290, 210), 8)
    # poids vert
    pygame.draw.circle(ECRAN, vert, (175, 230), 10)
    pygame.draw.circle(ECRAN, vert, (190, 220), 10)
    pygame.draw.circle(ECRAN, vert, (205, 215), 10)
    # piment vert
    pygame.draw.ellipse(ECRAN, vert_foncee, (305, 200, 30, 70))
    pygame.draw.polygon(ECRAN, vert, [(340, 190), (320, 190), (320, 200)])


#Fonction pour le poisson
def poisson():
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Poisson avec des pommes de terre
    pygame.draw.circle(ECRAN, gris, (250, 245), 140)
    pygame.draw.ellipse(ECRAN, bleu, (180, 170, 150, 70))
    pygame.draw.polygon(ECRAN, bleu, [(160, 180), (190, 205), (160, 230)])
    pygame.draw.circle(ECRAN, (0, 0, 0), (300, 200), 5)
    pygame.draw.ellipse(ECRAN, patate_brun, (200, 250, 50, 30))
    pygame.draw.ellipse(ECRAN, patate_brun, (300, 250, 50, 30))
    pygame.draw.ellipse(ECRAN, patate_brun, (250, 270, 50, 30))
    pygame.draw.ellipse(ECRAN, patate_brun, (210, 300, 50, 30))




#Fonction pour la tasse de café
def cafe():
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Tasse de café
    pygame.draw.ellipse(ECRAN, gris, (140, 230, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 220, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 210, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 200, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 190, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 180, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 170, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 160, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 150, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 140, 160, 100))
    pygame.draw.ellipse(ECRAN, gris, (140, 130, 160, 100))
    pygame.draw.ellipse(ECRAN, (255, 255, 255), (150, 140, 140, 80))
    pygame.draw.ellipse(ECRAN, brun_foncee, (155, 150, 130, 60))
    pygame.draw.arc(ECRAN, gris, (280, 160, 80, 160), 0, 30, 10)
   




##Fonction pour le gateau 
def gateau():
   
            
    #table
    pygame.draw.ellipse(ECRAN, brun_foncee, (30, 30, 450, 450))
    pygame.draw.ellipse(ECRAN, patate_brun, (45, 45, 420, 420))
    pygame.draw.rect(ECRAN, gris_claire, (100, 100, 300, 300))
    
    # Quart de gateau
    pygame.draw.circle(ECRAN, gris, (290, 245), 155)
    pygame.draw.line(ECRAN, beige, (150, 230), (150, 300), 4)
    pygame.draw.line(ECRAN, beige_foncee, (150, 300), (400, 280), 20)
    pygame.draw.line(ECRAN, beige, (150, 230), (400, 200), 10)
    pygame.draw.line(ECRAN, beige, (150, 240), (400, 210), 30)
    pygame.draw.line(ECRAN, beige, (150, 265), (400, 240), 30)
    pygame.draw.line(ECRAN, beige, (150, 280), (400, 260), 30)
    pygame.draw.line(ECRAN, beige, (150, 230), (300, 100), 12)
    pygame.draw.line(ECRAN, beige, (160, 230), (310, 110), 22)
    pygame.draw.line(ECRAN, beige, (190, 235), (325, 130), 45)
    pygame.draw.line(ECRAN, beige, (240, 235), (315, 145), 70)
    pygame.draw.line(ECRAN, beige_foncee, (400, 200), (400, 290), 20)
    pygame.draw.line(ECRAN, beige_foncee, (300, 95), (400, 200), 20)
    pygame.draw.ellipse(ECRAN, "blue", (300, 130, 40, 40), 50)
    pygame.draw.ellipse(ECRAN, "red", (295, 150, 90, 70), 50)
    pygame.draw.ellipse(ECRAN, "blue", (260, 150, 40, 40), 50)
    
   


idx_pres = 0
#Associe le mot de la nourriture à sa fonction
dict_var = {"Soupe à l'oignon":soupe, "Croquettes":croquettes, "Soupe à l'oignon grattinée":soupe_gratinee, "Poisson":poisson, "Steak":steak,
                "Café":cafe, "Quart de Gateau":gateau}


#Copy la liste de choix pour ne pas modifier l'original 
liste_choix2 = liste_choix.copy()


def changement_de_repas():
    """Fonction qui fait en sorte que l'écran change de repas"""

    global idx_pres
    global dict_var
    ECRAN.fill((240, 240, 240))   # on nettoie l'écran
    if liste_choix2[0] == "Soupe à l'oignon" or liste_choix2[0] =="Soupe à l'oignon grattinée" or liste_choix2[0] == "Croquettes":   # on avait besoin de supprimé l'entrée car sinon elle apparaisait après
        del liste_choix2[0]                                                                                                          # qu'on aille cliqué sur "Manger"

   
    if idx_pres < len(liste_choix2):        #on verifie si l'index est plus petit que la liste
        nourriture = liste_choix2[idx_pres]    # on choisit la nourriture par rapport à l'index présent (liste est en ordre des repas chosies)
        if nourriture in dict_var:             # on cherche notre nourriture dans le dictionnaire
            dict_var[nourriture]()             # on call la fonction qui dessine le plat que nous allons manger
            idx_pres += 1                      # on passe au plat suivant
    else:
        return
    

#paramètres du bouton "MANGER"
txt_police = pygame.font.SysFont("Comic sans MS", 15)
txt_bouton = txt_police.render("MANGER", True, (0,0,0))
coordonnees_bouton = pygame.Rect(205,390,110,40)
bouton_surface = pygame.Surface((coordonnees_bouton.width, coordonnees_bouton.height))


LANCEMENT = True

press_counter = 0      # on initialise un press counter

while LANCEMENT:
    if press_counter < 3:   # si on a appuyer plus que 3 fois, la fenêtre se ferme

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

            if liste_choix2[0] == "Soupe à l'oignon" or liste_choix2[0] == "Soupe à l'oignon grattinée" or liste_choix2[
                0] == "Croquettes":           # on affiche le premier plat à manger dès l'ouverture de la fenêtre
                nourriture2 = liste_choix2[0]
                dict_var[nourriture2]()


            if event.type == pygame.MOUSEBUTTONDOWN:

                if coordonnees_bouton.collidepoint(event.pos):     # bouton "Manger"
                    changement_de_repas()              #appel la fonction quand on appuie dessus
                    press_counter +=1
                    
                    sound = pyglet.media.load('manger.mp3')       #son quand on mange
                    sound.play()
                   
                    

        if coordonnees_bouton.collidepoint(pygame.mouse.get_pos()):       # paramètres bouton "Manger"
            bouton_surface.fill((185,185,185))

        else:
            bouton_surface.fill((210, 210, 210))

        ECRAN.blit(bouton_surface, coordonnees_bouton)
        ECRAN.blit(txt_bouton , (225, 400))


    else:
        break


    pygame.display.flip()
pygame.quit()       #Fermeture de la fenêtre
     








#Conception d’une facture
fen2 = tk.Tk()
fen2.geometry("500x500")
fen2.maxsize(500,500)
fen2.minsize(500, 500)
fen2.title("La facture")
fen2.configure(bg="white")

heure_actuelle = datetime.now()                         #Prend l'heure actuelle et l'associe à la variable
heure_actuelle = heure_actuelle.strftime("%H:%M")           #modifie la fonction pour afficher que l'heure et les minutes 


# Créez un point pour la ville de Québec
location = Point(46.8139, -71.2082)  # Québec
start = datetime(2024, 10, 1)         #en date du 1 au 31 octobre
end = datetime(2024, 10, 31)

# Obtenez les données météo quotidiennes
data = Daily(location, start, end)
data = data.fetch()

if not data.empty:  # Vérifiez si les données ne sont pas vides
        temperature_max = data['tmax'].max()      #prend la temperature la plus haute
        temperature_min = data['tmax'].min()         #prend la temperature la plus bas
        
        temperature_moy = (temperature_max + temperature_min)/2     #Prend la temperature moyenne
print(temperature_moy)
                               
police4 = ("Helvetica", 10)                         #font 3
police5 = ("Helvetica", 20, "bold")



#variable pour calculer le montant
addition = 0




#dictionnaire qui associe les chiffres afficher aux coordonnees de la table qui les relies 
dicts_tables = {(2,2, 80, 80): 1, (160,2, 80, 80):2, (241,2, 160, 80): 3,
                (2,160, 80, 80):  4, (160,160, 80, 80):5, (241,160, 160, 80): 6,
                (2, 241, 80, 160): 7, (160,241, 80, 160): 8, (241,241, 160, 160): 9}


numero_table = dicts_tables[table]              #Prend le chiffre de la coordonnee de la table choisis dans la confirmation 


#affiche table avec son chiffre  
numero_table_txt = Label(fen2, text = f"TABLE Nº{numero_table}", bg = "white")
numero_table_txt.config(font = police4)
numero_table_txt.place(relx = 0.5, rely = 0.1, anchor = CENTER)


for element in liste_choix:              #Parcourt les elements de la liste du choix selon ce que l'usagé a decidé de commandé                           
    

   
    
    if element == "Soupe à l'oignon":                                                    #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.2
        soupe = Label(fen2, text = f"1 SOUPE À L'OIGNON NON GRATINÉE", bg = "white")
        soupe.config(font = police4)
        soupe.place(relx = 0.29, rely = position, anchor = CENTER)
        
        soupe_prix = Label(fen2, text = f"6,99$",  bg = "white")                        #affiche le prix de la nourriture 
        soupe_prix.config(font = police4)
        soupe_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 6.99                                                                    #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
                        
    if element == "Soupe à l'oignon grattinée":                                                     #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.2              
        soupe_gratinee = Label(fen2, text = f"1 SOUPE À L'OIGNON GRATINÉE",  bg = "white")                      
        soupe_gratinee.config(font = police4)
        soupe_gratinee.place(relx = 0.26, rely = position, anchor = CENTER)
        
        soupe_gratinee_prix = Label(fen2, text = f"7,99$",  bg = "white")                           #affiche le prix de la nourriture 
        soupe_gratinee_prix.config(font = police4)
        soupe_gratinee_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 7.99                                                                     #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
    if element == "Croquettes":                                                             #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.2
        croquette = Label(fen2, text = f"1 CROQUETTES DE THON",  bg = "white")
        croquette.config(font = police4)
        croquette.place(relx = 0.22, rely = position, anchor = CENTER)
        
        croquette_prix = Label(fen2, text = f"8,99$",  bg = "white")                        #affiche le prix de la nourriture 
        croquette_prix.config(font = police4)
        croquette_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 8.99                                                                       #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
    if element == "Poisson":                                                                    #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.26 
        poisson = Label(fen2, text = f"1 POISSON AVEC POMMES DE TERRE",  bg = "white")
        poisson.config(font = police4)
        poisson.place(relx = 0.3, rely = position, anchor = CENTER)
        
        poisson_prix = Label(fen2, text = f"21,99$",  bg = "white")                                 #affiche le prix de la nourriture 
        poisson_prix.config(font = police4)
        poisson_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 21.99                                                                          #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
    if element == "Steak":                                                                          #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.26
        steak = Label(fen2, text = f"1 STEAK AVEC DES LÉGUMES DU JARDIN",  bg = "white")
        steak.config(font = police4)
        steak.place(relx = 0.32, rely = position, anchor = CENTER)
        
        steak_prix = Label(fen2, text = f"29,99$",  bg = "white")                                       #affiche le prix de la nourriture 
        steak_prix.config(font = police4)
        steak_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 29.99                                                                               #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
    if element == "Café":                                                                               #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.32
        cafe = Label(fen2, text = f"1 CAFÉ",  bg = "white")
        cafe.config(font = police4)
        cafe.place(relx = 0.1, rely = position, anchor = CENTER)
        
        cafe_prix = Label(fen2, text = f"3,29$",  bg = "white")                                     #affiche le prix de la nourriture 
        cafe_prix.config(font = police4)
        cafe_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 3.29                                                                           #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
    if element == "Quart de Gateau":                                                                #si la nourriture choisit equivaut au mot de la nourriture = affiche ce texte 
        position = 0.32
        gateau = Label(fen2, text = "1 QUART DE GÂTEAU AU FROMAGE",  bg = "white")
        gateau.config(font = police4)
        gateau.place(relx = 0.285, rely = position, anchor = CENTER)
        
        gateau_prix = Label(fen2, text = f"4,25$",  bg = "white")                                   #affiche le prix de la nourriture 
        gateau_prix.config(font = police4)
        gateau_prix.place(relx = 0.8, rely = position, anchor = CENTER)
        addition += 4.25                                                                               #si l'usager a choisit ce plat = additionne le prix à la variable addition  
        
        
        

#affiche le texte SOUS-TOTAL
S_total_txt = Label(fen2, text = "SOUS-TOTAL",  bg = "white")
S_total_txt.config(font = police4)
S_total_txt.place(relx = 0.2, rely = 0.4, anchor = CENTER)

#affiche l'addition de la nourriture choisit
addition = round(addition, 2)                                               #arrondit le totale à de chiffre après la virgule 
S_total_chiffre = Label(fen2, text = f"{addition} $",  bg = "white")
S_total_chiffre.config(font = police4)
S_total_chiffre.place(relx = 0.8, rely = 0.4, anchor = CENTER)


#calcule des taxes 
taxe_tps = round(addition * 0.05, 2)         #arrondit le totale à de chiffre après la virgule 
taxe_tvq = round(addition * 0.0975, 2)


#addition des taxes 
addition_taxe = round(addition + taxe_tps + taxe_tvq, 2)


#affiche texte TPS
TPS = Label(fen2, text = "TPS",  bg = "white")
TPS.config(font = police4)
TPS.place(relx = 0.15, rely = 0.46, anchor = CENTER)

#affiche le montant de la taxe
TPS_chiffre = Label(fen2, text = f"{taxe_tps} $",  bg = "white")
TPS_chiffre.config(font = police4)
TPS_chiffre.place(relx = 0.8, rely = 0.46, anchor = CENTER)


#affiche texte TVQ
TVQ = Label(fen2, text = "TVQ",  bg = "white")
TVQ.config(font = police4)
TVQ.place(relx = 0.154, rely = 0.51, anchor = CENTER)


#affiche le motant de la taxe
TVQ_chiffre = Label(fen2, text = f"{taxe_tvq} $",  bg = "white")
TVQ_chiffre.config(font = police4)
TVQ_chiffre.place(relx = 0.8, rely = 0.51, anchor = CENTER)

#affiche texte TOTAL
total = Label(fen2, text = "TOTAL",  bg = "white")
total.config(font = police5)
total.place(relx = 0.2, rely = 0.57, anchor = CENTER)

#affiche le nouveau montant suite à l'addition de la taxe
addition_taxe_txt = Label(fen2, text = f"{addition_taxe} $",  bg = "white")
addition_taxe_txt.config(font = police4)
addition_taxe_txt.place(relx = 0.8, rely = 0.57, anchor = CENTER)

#Affiche texte de l'heure
heure_actuelle_txt = Label(fen2, text = f" Heure: {heure_actuelle} ",  bg = "white")
heure_actuelle_txt.config(font = police4)
heure_actuelle_txt.place(relx = 0.5, rely = 0.69, anchor = CENTER)
        


tps_txt = Label(fen2, text = "TPS:  00000000 RT0001",  bg = "white")
tps_txt.config(font = police4)
tps_txt.place(relx = 0.5, rely = 0.75, anchor = CENTER)



tvq_txt = Label(fen2, text = "TVQ:  0000000000 TQ0001",  bg = "white")
tvq_txt.config(font = police4)
tvq_txt.place(relx = 0.5, rely = 0.81, anchor = CENTER)


#affiche texte service 
service_txt = Label(fen2, text = f"VOUS AVEZ ÉTÉ SERVI",  bg = "white")
service_txt.config(font = police4)
service_txt.place(relx = 0.5, rely = 0.90, anchor = CENTER)

#affiche le nom du serveur/serveuse 
service_nom_txt = Label(fen2, text = f"PAR: {nom}",  bg = "white")
service_nom_txt.config(font = police4)
service_nom_txt.place(relx = 0.5, rely = 0.96, anchor = CENTER)

#affiche l'image du terminal
image_terminal = ImageTk.PhotoImage(Image.open("terminal.png").resize((100, 100)))
image_terminal_affiche = tk.Label(fen2, image=image_terminal)
image_terminal_affiche.place(x = 400, y = 400)


meteo_txt = Label(fen2, text = f"Température moyenne: {temperature_moy}°C",  bg = "white")
meteo_txt.config(font = police4)
meteo_txt.place(relx = 0.5, rely = 0.05, anchor = CENTER)


fen2.mainloop()














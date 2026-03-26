# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:31:35 2024

@author: JP
"""

#JeanPaul Jreissaty
#Daniel Zgardan

from tkinter import*
import random
import sqlite3
import time 
from datetime import datetime
import pyglet
from PIL import ImageTk, Image

connexion = sqlite3.connect("admin.db")
cursor = connexion.cursor()

requete = """CREATE TABLE IF NOT EXISTS membres(
numero_compte INTEGER PRIMARY KEY AUTOINCREMENT, 
argent TEXT NOT NULL, MDP TEXT NOT NULL, phrase TEXT NOT NULL)"""

cursor.execute(requete)

liste = []
active = 0

num_compte_dispo = list(range(101, 111))                        #Ajout de tout les comptes possibles


def placeDISPO():                                               #Parcous la base pour savoir si il y a 10 comptes, sinon affiche tapez A
    global nb_compte
    connexion = sqlite3.connect("admin.db")
    contenu = cursor.execute("select*from membres ")

    
    cursor.execute("SELECT * FROM membres")
    nb_compte = len(cursor.fetchall())
    
placeDISPO()
    
print("Bonjour: ")
if nb_compte < 10:
    while True:         #Tant que c'est vrai, ca va boucler pour gerer les erreurs
             
            tape = input("""-Tapez A, pour vous connecter a l'Application.
-Tapez U, pour un nouvel Utilisateur. 
""")
            
            tape = tape.capitalize()
            if tape == "A" or tape == "U":
                break
            else:
                print("Attention! Veuillez tapez soit A soit U.")
if nb_compte == 10:
    while True:         #Tant que c'est vrai, ca va boucler pour gerer les erreurs
             
            tape = input("""-Tapez A, pour vous connecter a l'Application. """)
            
            tape = tape.capitalize()
            if tape == "A":
                break
            else:
                print("Attention! Veuillez tapez A.")
    
    
    
    
contenu = list(cursor.execute("select*from membres "))      #Ajoute les comptes crees dans une liste 

if tape == "U":

    for row in contenu:             #Ajoute le premier compte dans une liste
        liste.append(row[0])
        
    for element in liste:                               #Parcours la liste et si le compte est dans la liste des comptes disponibles, on l'enleve
            num_compte_dispo.remove(element)
            
    if len(liste) == 10 :           #Si la liste contient 10 comptes active devient 1 et empeche la suite
        active = 1

    if active == 0:
        numero_compte = random.choice(num_compte_dispo)         #Choisit un numero de compte aleatoirement
     
        argent = random.randrange(100, 501)
        
        print(f"Bienvenue, voici votre numero de compte {numero_compte}")
        
        while True:
            mdp = input("Choisissez votre mot de passe et tapez sur ENTRÉE: ")
            
            if mdp == "":
                print("Veuillez taper un mot de passe!")
            
            else:
                break
                
        while True:
            mdp_confirmation = input("Confirmez votre mot de passe puis pressez sur ENTRÉE : ")
            
            if mdp == mdp_confirmation:
                break
            else:
                print("Attention! Veuillez choisir un mot de passe identique. ")
        
 
        while True:
            phrase = input("Indiquez un mot ou une phrase pour vous en rappeler et pressez sur ENTRÉE. ")
            
            if phrase == "":
                print("Veuillez taper un mot ou une phrase!")
            
            else:
                break

        print(f"Compte créé avec succès! Votre solde est de {argent}$.")              
        
        requete = """INSERT INTO membres(numero_compte, argent, MDP, phrase)                   
        VALUES
        (?,?,?,?)"""            #Insert les comtpes dans la base 
        
        cursor.execute(requete,(numero_compte, argent, mdp,phrase))
        connexion.commit()
        

dicts1 = {row[0]:(row[1], row[2], row[3]) for row in contenu}                   #Cree un dictionnaire avec le compte comme cle et un tuple de l'argent, du mdp et de la phrase
    

if tape == "U":
    try:
        dicts1[numero_compte] = (argent, mdp, phrase)                               
    except NameError:
        pass


def general():
    global police3
    #Mode General
    fen = Tk()
    fen.geometry("300x300")
    fen.maxsize(300, 300)
    fen.minsize(300, 300)
    fen.title("General")
    
    #texte banque grasseene
    police1 = ("Times New Roman", 20)
    txt_bq = Label(fen, text = "Banque Grasséenne")
    txt_bq.config(font = police1)
    txt_bq.place(relx = 0.4, rely = 0.1, anchor = CENTER)
    
    logo = ImageTk.PhotoImage(Image.open("logo1.jpg").resize((50, 50)))       #load le logo de la banque
    canvas = Canvas(width=50, height=50)
    canvas.place(relx = 0.87, rely= 0.1, anchor =CENTER)
    canvas.create_image(25, 20, image = logo, anchor= CENTER)
    
    def option():                                                   
        global num_tape
        if variable.get() == "1":                                       #si le button radio est appuie sur le mode client 
            try:
                num_tape = int(champ_num.get())                         #prend le numero de compte que l'utilisateur a taper
                
            except ValueError:
                num_tape = 0                                            #Sinon associe 0 pour generer erreur
                
            mdp_tape = champ_mdp.get()                              #prend le mdp que l'utilisateur a taper
    
            liste2 = list(dicts1.keys())                                    #Ajoute les comptes cree dans une liste
           
            if num_tape not in liste2 or mdp_tape != dicts1[num_tape][1]:      #si le compte n'est pas dans la liste ou si le mdp n'est pas le meme que dans le dictionnaire 
                top = Toplevel(fen)
                top.title("Renseignements d'ouverture de session erronés")          #ouvre un TOPLEVEL
                top.geometry("300x100")
                top.resizable(0, 0)
                
                #texte sur top level
                police = ("Times New Roman", 10)
                texte = Label(top, text = "Veuillez vérifier vos données de connexion et réessayer")
                texte.config(font = police)
                texte.place(relx = 0.5, rely = 0.4, anchor = CENTER)
                
                #bouton ok        
                bouton_ok = Button(top, text = "OK", font = police, command = top.destroy)
                bouton_ok.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                top.mainloop()
                
            else:
                fen.destroy()                           #Sinon detruit la fenetre et appelle une autre fonction
                client()
                
                
        if variable.get() == "2":                         #si le button radio est appuie sur le mode admin 
             try:
                 num_tape = champ_num.get()                   #prend le numero de compte que l'utilisateur a taper
                 mdp_tape = champ_mdp.get()                     #prend le mdp que l'utilisateur a taper
                 
             except ValueError:
                 num_tape = 0                      #Sinon associe 0 pour generer erreur
                 
             if num_tape != "adm" and mdp_tape != "123":                #Si le compte n'est pas = a adm et si le mdp n'est pas 123
                 top = Toplevel(fen)
                 top.title("Renseignements d'ouverture de session erronés")             #ouvre un TOPLEVEL
                 top.geometry("300x100")
                 top.resizable(0, 0)
    
                 # texte sur top level
                 police = ("Times New Roman", 10)
                 texte = Label(top, text="Veuillez vérifier vos données de connexion et réessayer")
                 texte.config(font=police)
                 texte.place(relx=0.5, rely=0.4, anchor=CENTER)
    
                 # bouton ok
                 bouton_ok = Button(top, text="OK", font=police, command=top.destroy)
                 bouton_ok.place(relx=0.5, rely=0.7, anchor=CENTER)
                 top.mainloop()
                 
                 
             if num_tape == "adm" and mdp_tape == "123":                        #si oui, alors ca appelle la fonction admin
                 fen.destroy()
                 admin()
                 
    def tete_en_air():                                  #Mot de passe oublie
        liste2 = list(dicts1.keys())                    #La liste des comptes 

        while True:
            numero_compte_potentiel = int(input("Quel est votre numero de compte? "))       
            phrase_potentiel = input("Quel est votre phrase/mot? ")
            
          

            if numero_compte_potentiel in liste2 and phrase_potentiel == dicts1[numero_compte_potentiel][2]:      #Si le numero de compte que l'utilisateur a taper est = a celui dans la liste
                print(f"Votre mot de passe est : {dicts1[numero_compte_potentiel][1]}")                           #Si la phrase que l'utilisateur a taper est = a celui dans le dictionnaire 
                break
            else:
                print("Erreur! Veuillez réessayer .")
    
    
    
    def limitation(entre_texte):
        if len(entre_texte.get()) > 3:                      #Limite le champ de texte a 3 chiffre/lettre
            entre_texte.set(entre_texte.get()[:3])
    
    #bouton radio
    police2 = ("Times New Roman", 15)
    variable = StringVar(fen, "1")
  
    
    R1 = Radiobutton(fen, text = "CLIENT", variable = variable, value = "1")            #Radio bouton de client et admin
    R2 = Radiobutton(fen, text = "ADMIN", variable = variable, value = "2")
    
    R1.config(font = police2)
    R2.config(font = police2)
    
    R1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    R2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    
    
    #limitation 
    entre_texte = StringVar() 
    entre_texte.trace("w", lambda *arg: limitation(entre_texte)) 
    
    #Champ d'entre
    police3 = ("Ariel", 10)
    champ_num = Entry(fen, font = police3, textvariable = entre_texte)
    champ_num.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    
    
    champ_mdp = Entry(fen, font = police3, show = "*")
    champ_mdp.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    num_compte_txt = Label(fen, text = "NUM", font = police2)
    num_compte_txt.place(relx = 0.15, rely = 0.5, anchor = CENTER)
    
    mdp_txt = Label(fen, text = "MDP", font = police2)
    mdp_txt.place(relx = 0.15, rely = 0.6, anchor = CENTER)
    
    #bouton ouvrir session
    bouton = Button(fen, text = "Ouvrir une session", font = police3, command = option)
    bouton.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    
    #bouton mdp oublier
    bouton_mdp = Button(fen, text = "Mot de passe oublié?", font = police3, command = tete_en_air)
    bouton_mdp.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    fen.mainloop()
        

virement = 0  
active1 = 0
def client():  
    global virement, active1
    
    def fermer():
        fen1.destroy()
        
        
        
    def validation():
        global virement, active1
        
        try:
            transfer = int(scale.get())                         #cherche la valeur du scale que l'utilisateur a choisit
        except ValueError:
            print("Erreur! Veuillez taper un montant!")
        
        solde = int(dicts1[num_tape][0])                        #Prend le solde actuel du compte 
    
        valeur_selectionnee = variable.get()                #prend la variable du compte 
                     
        for compte, val in dicts2.items():                  #parcours les comptes et les valeurs du dictionnaires 
            if str(val) == valeur_selectionnee:             #Si la variable = a la valeur selectionne
                compte_cible = compte                       #On prend le compte
        try:
            if transfer < solde + 1 and transfer >= 1:          #Si le transfer et plus grand que 1 et plus petit que le solde
                solde = solde - transfer
                
                dicts1[num_tape] = (solde, dicts1[num_tape][1], dicts1[num_tape][2])                    #update le dictionnaire 
                dicts1[compte_cible] = (int(dicts1[compte_cible][0]) + transfer, dicts1[compte_cible][1], dicts1[compte_cible][2])      #update le dictionnaire du compte cible 
                
                for compte, (nouveau_solde, mdp, phrase) in dicts1.items():         #parcour le dicionnaire 
                    requete = """UPDATE membres
                            SET argent = ?, MDP = ?, phrase = ?
                            WHERE numero_compte = ?"""
                    cursor.execute(requete, (nouveau_solde, mdp, phrase, compte))           #update la base apres les transactions
                    connexion.commit()
                    
                time.sleep(1)                       #ajout d'un delai
                fen1.destroy()
                print("Virement effectué avec succes!")
    
                sound = pyglet.media.load('argent.mp3')         #ajout de son
                sound.play()    
               
                virement += 1                   #update la variable virement 
                active1 = 1
                client()  
                if active1 == 1:
                    general()
                   
        except UnboundLocalError:
 
                print("Veuillez selectionner un compte")
            
       
            
    #FEN CLIENT
    
    fen1 = Tk()
    fen1.title("Mode Client")
    can = Canvas(width = 400, height = 600)
    can.pack()
    
    heure_actuelle = datetime.now()                         #Prend l'heure actuelle et l'associe à la variable
    heure_actuelle = heure_actuelle.strftime("%H:%M") 
    
    liste2 = list(dicts1.keys())                        #liste des comptes 
    
    variable = StringVar(fen1, "0")                 #Variable pour radio bouton
    dicts2 = {}
    
    #texte banque grasseene
    police2 = ("Times New Roman", 20, "underline")
    txt_bq = Label(can, text = "Banque Grasséenne")
    txt_bq.config(font = police2)
    txt_bq.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    #texte de l'heure
    police5 = ("Helvetica", 10)
    heure_actuelle_txt = Label(fen1, text = f" Heure: {heure_actuelle} ")
    heure_actuelle_txt.config(font = police5)
    heure_actuelle_txt.place(relx = 0.5, rely = 0.1, anchor = CENTER)
            
    
    #texte Mon compte
    police4 = ("Helvetica", 15, "bold")
    txt_mc = Label(can, text = "Mon Compte")
    txt_mc.config(font = police4)
    txt_mc.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    police5 =  ("Helvetica", 12)
    txt_compte = Label(can, text = f"Numero de compte: {num_tape}")
    txt_compte.config(font = police5)
    txt_compte.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    txt_solde = Label(can, text = f"Votre solde: {dicts1[num_tape][0]}$")
    txt_solde.config(font = police5)
    txt_solde.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    
    txt_nb_v = Label(can, text = f"Nombre de virement effectués: {virement}")
    txt_nb_v.config(font = police5)
    txt_nb_v.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
    
    txt_v = Label(can, text = "Virements")
    txt_v.config(font = police4)
    txt_v.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    x1 = 20
    y1 = 260
    chiffre = 0
    for element in dicts1.keys():               #parcour les elements du dictionnaire 
        x1 += 50                                #Ajoute 50 a x1
        if x1 > 270:                            #Si x1 est supperieur a 270, alors il change de ligne
            y1 = 300
            x1 = 70
        if element != num_tape:                 #Si l'element n'est pas = au compte du client
            chiffre += 1
            r = Radiobutton(fen1, text = f"{element}", variable = variable, value = f"{chiffre}")       #affiche et place un apres l'autre les radio boutons
            r.place(x = x1, y = y1)
            dicts2[element] = chiffre             #Ajoute le numero de compte comme cle et sa variable de radio bouton comme valeur
                
    
      
    variable1 = DoubleVar()     
    
    scale = Scale( fen1, variable= variable1, from_=1, to= dicts1[num_tape][0], orient=HORIZONTAL)                  #widget tkinter pour afficher un scale 
    scale.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    #Bouton valider
    bouton_v = Button(can, text = "VALIDER", font = police3, command = validation)
    bouton_v.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    
    txt_f= Label(can, text = "Fermer la session")
    txt_f.config(font = police4)
    txt_f.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
    bouton_fermer = Button(can, text = "FERMER", font = police3, command = fermer)
    bouton_fermer.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    
    #Image de client
    client_img = ImageTk.PhotoImage(Image.open("client.png").resize((80, 80)))
    canvas = Canvas(width=150, height=150)
    canvas.place(relx = 0.95, rely= 0.98, anchor =CENTER)
    canvas.create_image(50, 45, image = client_img, anchor= CENTER)
    
    fen1.mainloop()
    if active1 == 0:
        general()













#ADMIN
info_text= None

#affiche la base sur le menu
def rub1(fen2):
    global info_text
    ajout=""

    connexion = sqlite3.connect("admin.db")
    curseur = connexion.cursor()
    contenu = curseur.execute("SELECT * FROM membres")

    for index in contenu:
        ajout = ajout + "NUMERO DE COMPTE:"+  f"{index[0]}" + "      MOT DE PASSE: "+ f"{index[2]}" + "\n"

    if info_text is not None:
        info_text.destroy()
    info_text = Text(fen2, height=10, width=50)

    info_text.insert("1.0", ajout)
    info_text.pack(side=TOP)
    connexion.close()



text_supp = None
entree_sup = None
bt_supp = None
text_numcompte = None
Entre2 = None
text_montant = None
succes_sup = None
erreur_sup = None
erreur_label = None
Entre_montant = None
bt_ajouter = None
succes_label = None
bt3 = None


#efface les textes, boutons, entry des canevas du menu
def efface_texte():
    global text_supp, entree_sup, bt_supp, text_numcompte, Entre2, text_montant, succes_sup, erreur_sup, erreur_label, text_montant, Entre_montant, bt_ajouter, succes_label, bt3

    if text_montant:
        text_montant.destroy()
        text_montant = None

    if Entre_montant:
        Entre_montant.destroy()
        Entre_montant = None

    if bt_ajouter:
        bt_ajouter.destroy()
        bt_ajouter = None

    if succes_label:
        succes_label.destroy()
        succes_label = None


    if text_supp:
        text_supp.destroy()
        text_supp = None

    if entree_sup:
        entree_sup.destroy()
        entree_sup = None

    if bt_supp:
        bt_supp.destroy()
        bt_supp = None

    if text_numcompte:
        text_numcompte.destroy()
        text_numcompte = None

    if Entre2:
        Entre2.destroy()
        Entre2 = None

    if text_montant:
        text_montant.destroy()
        text_montant = None

    if succes_sup:
        succes_sup.destroy()
        succes_sup = None

    if erreur_sup:
        erreur_sup.destroy()
        erreur_sup = None

    if erreur_label:
        erreur_label.destroy()
        erreur_label = None

    if bt3:
        bt3.destroy()
        bt3 = None



def modifier(fen2):
    global text_numcompte, Entre2, text_montant, bt3

    efface_texte()
    label_liste= []

    def reset():                # delete les widgets lorsque qu'on relance la fonction
        for label in label_liste:
            label.destroy()
        label_liste.clear()



    def limitation(entre_texte):
          if len(entre_texte.get()) > 3:                      #Limite le champ de texte a 3 chiffre/lettre
              entre_texte.set(entre_texte.get()[:3])

    #Trouver le numéro de compte
    text_numcompte = Label(fen2, text="Entrer le numéro de compte: ")
    text_numcompte.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    label_liste.append(text_numcompte)
    
    #limitation 
    entre_texte = StringVar() 
    entre_texte.trace("w", lambda *arg: limitation(entre_texte)) 
    
    Entre2 = Entry(fen2, textvariable= entre_texte)
    Entre2.place(relx=0.5, rely=0.25, anchor=CENTER)
    label_liste.append(Entre2)

    erreur_labels = []
    
    
    
    def clear_messages():
        for label in erreur_labels:
            label.destroy()
        erreur_labels.clear()


    def verifier():
      global erreur_label, text_montant, Entre_montant, bt_ajouter
      # Effacer les messages d'erreurs
      clear_messages()

      numero_compte = Entre2.get()
      if not numero_compte:     #demande à l'usager de mettre un numéro de compte valide
          print("Entrer un numéro de compte valide")
          return

      connexion = sqlite3.connect("admin.db")     # connexion database
      curseur = connexion.cursor()
      curseur.execute("SELECT 1 FROM membres WHERE numero_compte = ?", (numero_compte,))
      resultat = curseur.fetchone()
      connexion.close()

      if resultat:                              # si le compte existe
          text_numcompte.place_forget()
          Entre2.delete(0, END)
          Entre2.place_forget()
          bt3.place_forget()

          #Ce que l'usager voit sur la fenetre
          text_montant = Label(fen2, text="Montant à ajouter: ")
          text_montant.place(relx=0.5, rely=0.2, anchor=CENTER)
          Entre_montant = Entry(fen2)
          Entre_montant.place(relx=0.5, rely=0.25, anchor=CENTER)
          label_liste.append(Entre_montant)


          def ajoute_montant():
                """Cette fonction sert à ajouter de l'argent dans la base de données"""
                global erreur_label3, succes_label
                montant = Entre_montant.get()

                if not montant.isdigit():         #vérifie si l'entrée est un nombre
                    print("Veuillez entrer un nombre")

                    return

                montant = int(montant)

                connexion = sqlite3.connect("admin.db")
                curseur = connexion.cursor()
                curseur.execute("UPDATE membres SET argent = argent + ? WHERE numero_compte = ?",
                                (montant, numero_compte))
                connexion.commit()
                connexion.close()

                Entre_montant.delete(0, END)
                succes_label = Label(fen2, text=f"Montant ajouté avec succès! Nouveau solde: {montant}", fg="green")
                succes_label.place(relx=0.5, rely=0.5, anchor=CENTER)
                erreur_labels.append(succes_label)



    
          bt_ajouter = Button(fen2, text="Ajouter Montant", command=ajoute_montant)    #bouton qui appel la fonction ajouter()
          bt_ajouter.place(relx=0.5, rely=0.35, anchor=CENTER)
          label_liste.append(bt_ajouter)



      else:
         print("Numéro introuvable. Entrez un numéro de compte existant")


    bt3 = Button(fen2, text="Vérifier", command=verifier)
    bt3.place(relx=0.5, rely=0.35, anchor=CENTER)
    label_liste.append(bt3)





#Fait le choix selon la variable choisit 
def choix(ma_variable, fen2):
    if ma_variable.get()=="1":
        modifier(fen2)


    elif ma_variable.get()=="2":
       supprimer(fen2)




#creer les radio bouton de la section mise a jour du menu
def miseajour(fen2):
    if info_text is not None:
        info_text.destroy()

    texte_miseajour = Label(fen2, text="CENTRE DE CONTROLE DE LA BANQUE", )
    texte_miseajour.place(relx=0.5, rely=0.05, anchor=CENTER)

    ma_variable = StringVar(fen2, "0")
    R1 = Radiobutton(fen2, text= "MODIFIER", variable=ma_variable, value="1", command=lambda: choix(ma_variable, fen2))
    R2 = Radiobutton(fen2, text="SUPPRIMER", variable=ma_variable, value="2", command=lambda: choix(ma_variable, fen2))

    R1.place(relx=0.5, rely=0.1, anchor=CENTER)
    R2.place(relx=0.5, rely=0.15, anchor=CENTER)





def detruit():
    fen2.destroy()    
    general()


def admin():
    global fen2
    """Ouvre le mode administrateur"""
    fen2 = Tk()
    fen2.title("Mode admin")
    fen2.geometry("400x600")
    fen2.resizable(0,0)


    # Menu
    Mon_menu = Menu(fen2) #widget de type fenetre
    fen2.config(menu=Mon_menu)


    # Menu "base de données"
    accueil = Menu(Mon_menu, tearoff=0)
    accueil.add_command(label="Afficher les membres", command=lambda: rub1(fen2))
    Mon_menu.add_cascade(label="Base de données", menu=accueil)

    #connexion base de donnees
    connexion = sqlite3.connect("admin.db")
    cursor = connexion.cursor()
    #verifier le nombre de compte existants
    cursor.execute("SELECT COUNT(*) FROM membres")
    nombre_de_comptes = cursor.fetchone()[0]

    if nombre_de_comptes >= 10:
        print("La limite de 10 comptes a été atteinte. Aucun nouveau compte a été créé.")

    else:
        #ajout d'un compte
        numeros = list(range(101, 111)) # tous les numéros possibles

        # récupère les numéros déja dans la base
        liste_db = []
        for row in contenu:
            liste_db.append(row[0])

        # Choisir un numéro exclusif
        exclusifs = [num for num in numeros if num not in liste_db]
        if not exclusifs:
            print("Tous les numéros sont attribués.")
            return

        
        nouv_numero = random.choice(exclusifs)
        print(f"Voici le nouveau numéro de compte: {nouv_numero}")

        #Générer des données pour le nouveau compte
        nouv_montant = random.randrange(100, 501)
        print(f"Voici le montant dans votre solde: {nouv_montant}")
        
        while True:
            nouv_mdp = input("Choissisez un mot de passe pour ce compte: ")
            
            if nouv_mdp == "":
                print("Veuillez taper un mot de passe!")
            
            else:
                break
        while True:
            nouv_phrase = input("Choissisez une phrase en cas d'oublie du mot de passe: ")
            
            if nouv_phrase == "":
                print("Veuillez taper un mot ou une phrase!")
            
            else:
                break
        #Insérer dans la base
        requete = """INSERT INTO membres(numero_compte, argent, MDP, phrase)
        VALUES
        (?,?,?,?)"""

        cursor.execute(requete, (nouv_numero, nouv_montant, nouv_mdp, nouv_phrase))
        connexion.commit()
        print("Ce compte a été ajouté avec succès !")
    connexion.close()

    #Mise à jour
    Mon_menu.add_command(label= "Mise à jour", command=lambda: miseajour(fen2))

    #Quitter
    Mon_menu.add_command(label="Quitter", command= detruit)


    fen2.mainloop()



def verifier2(fen2, numero_compte):
    global succes_sup, erreur_sup

    succes_sup = Label(fen2, text="Le compte a été supprimé avec succès.", fg="green")
    erreur_sup = Label(fen2, text="Le numéro de compte n'existe pas.", fg="red")

    connexion = sqlite3.connect("admin.db")
    curseur = connexion.cursor()

  #Verifie si les comptes existes
    curseur.execute("SELECT 1 FROM membres WHERE numero_compte = ?", (numero_compte,))
    result = curseur.fetchone()

    if result:  #si le compte existe
        # delete le compte
        curseur.execute("DELETE FROM membres WHERE numero_compte = ?", (numero_compte,))
        connexion.commit()
        # affiche le texte de succes
        succes_sup.place(relx=0.5, rely=0.5, anchor=CENTER)

    if not result:
        print("Le compte n'apparait pas dans la base de données")

    # ferme la base
    connexion.close()

def limitation(entre_texte):
      if len(entre_texte.get()) > 3:                      #Limite le champ de texte a 3 chiffre/lettre
          entre_texte.set(entre_texte.get()[:3])

def supprimer(fen2):
    global entree_sup, text_supp, bt_supp
    efface_texte()
    text_supp = Label(fen2, text="Entrer le numéro du compte à supprimer:")
    text_supp.place(relx=0.5, rely=0.2, anchor = CENTER)
    
    #limitation 
    entre_texte = StringVar() 
    entre_texte.trace("w", lambda *arg: limitation(entre_texte)) 
    
    
    entree_sup = Entry(fen2, textvariable= entre_texte)
    entree_sup.place(relx=0.5, rely=0.25, anchor = CENTER)

    bt_supp = Button(fen2, text="SUPPRIMER LE COMPTE", command=lambda: verifier2(fen2, entree_sup.get()))
    bt_supp.place(relx=0.5, rely=0.35, anchor = CENTER)








    
general()
connexion.commit()
connexion.close()
   

    

    
    
    
    
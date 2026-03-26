# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:46:47 2024

@author: JP
"""

#TP3 Samuel Carrière, giorgio, Jean-paul, Daniel
from logging import Manager
import pygame
import pygame_menu
import sqlite3
import time
import random
import sys
import pygame_gui
from pygame import Clock
from time import strftime
from datetime import datetime

pygame.init()

# Dimensions écran
ECRAN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Discipline Olympique")
FONT = pygame.font.Font(None, 40)
db_file = "Olympic21322112.db"

# couleur utilisé à travers le tp
BLANC = (255, 255, 255)
BLEU = (0, 102, 204)
VERT = (0, 204, 102)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

current_screen = 'menu'
########################################################################################################################
#                                           La base de données                                                         #
########################################################################################################################
def base_donnee():
    """Initialise la base de données pour gérer les participants et les résultats."""
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Création de la table des participants
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prenom TEXT NOT NULL,
            nom TEXT NOT NULL,
            nation TEXT NOT NULL,
            temps INTEGER,
            UNIQUE(prenom, nom))
    """)

    connection.commit()
    connection.close()

def ajouter_participant(prenom, nom, nation):
    """Ajoute un participant dans la base si on repond au critère"""
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Vérifie si le participant existe déjà dans la base de donnée
    cursor.execute("SELECT * FROM participants WHERE prenom = ? AND nom = ?", (prenom, nom))
    if cursor.fetchone() is not None:
        print(f"Le participant '{prenom} {nom}' existe déjà.")
        return False

    # Vérifie si la nation est utilisé par au moins deux participants
    cursor.execute("SELECT COUNT(*) FROM participants WHERE nation = ?", (nation,))
    count = cursor.fetchone()[0]
    if count >= 2:
        print(f"La nation '{nation}' est déjà utilisée par au moins deux participants.")
        return False

    # Insérer le participant dans la base de donnée
    cursor.execute("INSERT INTO participants (prenom, nom, nation) VALUES (?, ?, ?)", (prenom, nom, nation))
    connection.commit()
    print(f"Participant ajouté : {prenom} {nom} représente : {nation}")
    connection.close()
    return True

def ajouter_record():
    """Fonction qui affiche les 5 meilleurs temps ."""
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Récupérer les 5 meilleurs temps
    cursor.execute("""
            SELECT prenom, nom, nation, temps
            FROM participants
            WHERE temps IS NOT NULL
            ORDER BY temps ASC
            LIMIT 5
        """)
    meilleurs_temps = cursor.fetchall()
    connection.close()

    if meilleurs_temps:
        print("Top 5 des meilleurs temps :")
        for i, (prenom, nom, nation, temps) in enumerate(meilleurs_temps, start=1):
            print(f"{i}. {prenom} {nom} avec ({nation}) - {temps:.2f} secondes")
    else:
        print("Aucun temps enregistré.")

def enregistrer_temps(prenom, nom, temps):
    """Met à jour le temps du participant dans la base de données."""
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Mettre à jour le temps du joueur
    cursor.execute("""UPDATE participants SET temps = ? WHERE prenom = ? AND nom = ?""", (temps, prenom, nom))

    connection.commit()
    connection.close()


########################################################################################################################
#                                   La fenêtre pygame en mode Solo                                                     #
########################################################################################################################
def mode_solo():
    # Effacer tout ce que pygame_menu a dessiné
    ECRAN.fill(BLANC)
    pygame.display.flip()  # Mettre à jour l'écran pour appliquer le changement immédiatement
    nations = ["Canada", "États-Unis", "France", "Allemagne", "Nigéria", "Niger", "Japon", "Chine", "Australie"]

    coordonne_nation = [
        (80, 100), (300, 100), (520, 100),
        (80, 180), (300, 180), (520, 180),
        (80, 260), (300, 260), (520, 260)
    ]

    # Créer les boutons pour les nations
    boutons = []
    for i, nation in enumerate(nations):
        x, y = coordonne_nation[i]
        rect = pygame.Rect(x, y, 200, 50)
        boutons.append({"rect": rect, "nation": nation, "selected": False})

    # Champs de texte pour prénom et nom
    texte_prenom = ""
    texte_nom = ""
    champ_prenom = pygame.Rect(150, 450, 200, 40)  # Champ d'entrée pour prénom
    champ_nom = pygame.Rect(450, 450, 200, 40)  # Champ d'entrée pour nom
    actif_prenom = False
    actif_nom = False

    # Bouton "Valider"
    bouton_valider = pygame.Rect(300, 520, 200, 50)


    LANCEMENT = True
    while LANCEMENT:
        ECRAN.fill(BLANC)

        # les boutons pour les nations avec couleurs si ont clique dessus
        for bouton in boutons:
            if bouton["selected"]:
                couleur = VERT
            else:
                couleur = BLEU
            pygame.draw.rect(ECRAN, couleur, bouton["rect"])
            texte_surface = FONT.render(bouton["nation"], True, BLANC)
            texte_rect = texte_surface.get_rect(center=bouton["rect"].center)
            ECRAN.blit(texte_surface, texte_rect)

        # Dessiner les champs de texte
        if actif_prenom:
            couleur_prenom = pygame.Color("dodgerblue")
        else:
            couleur_prenom = pygame.Color("lightskyblue")
        if actif_nom:
            couleur_nom = pygame.Color("dodgerblue")
        else:
            couleur_nom = pygame.Color("lightskyblue")
        pygame.draw.rect(ECRAN, couleur_prenom, champ_prenom, 2)
        pygame.draw.rect(ECRAN, couleur_nom, champ_nom, 2)

        # Texte des champs de texte
        surface_prenom = FONT.render(texte_prenom, True, NOIR)
        surface_nom = FONT.render(texte_nom, True, NOIR)
        ECRAN.blit(surface_prenom, (champ_prenom.x + 5, champ_prenom.y + 5))
        ECRAN.blit(surface_nom, (champ_nom.x + 5, champ_nom.y + 5))

        # Placeholder des champs
        placeholder_prenom = FONT.render("Prénom", True, pygame.Color("gray"))
        placeholder_nom = FONT.render("Nom", True, pygame.Color("gray"))
        if not texte_prenom:
            ECRAN.blit(placeholder_prenom, (champ_prenom.x + 5, champ_prenom.y + 5))
        if not texte_nom:
            ECRAN.blit(placeholder_nom, (champ_nom.x + 5, champ_nom.y + 5))

        # le bouton "Valider"
        pygame.draw.rect(ECRAN, BLEU, bouton_valider)
        surface_valider = FONT.render("COMMENCER", True, BLANC)
        rect_valider = surface_valider.get_rect(center=bouton_valider.center)
        ECRAN.blit(surface_valider, rect_valider)

        pygame.display.flip()

        # Gérer les intéraction avec clique
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # Activer/désactiver les champs de texte
                if champ_prenom.collidepoint(evenement.pos):
                    actif_prenom = True
                    actif_nom = False
                elif champ_nom.collidepoint(evenement.pos):
                    actif_nom = True
                    actif_prenom = False
                else:
                    actif_prenom = False
                    actif_nom = False

                # Sélectionner une nation
                for bouton in boutons:
                    if bouton["rect"].collidepoint(evenement.pos):
                        # Désélectionner tous les autres boutons
                        for b in boutons:
                            b["selected"] = False
                        # Sélectionner uniquement le bouton cliqué
                        bouton["selected"] = True
                        nation_selectionnee = bouton["nation"]

                # Cliquer sur le bouton "Commencer"
                if bouton_valider.collidepoint(evenement.pos):
                    if nation_selectionnee and texte_prenom and texte_nom:
                        succes = ajouter_participant(texte_prenom, texte_nom, nation_selectionnee)
                        if succes:   # si notre fonction ajouter_participant return True
                            jeu_solo(texte_prenom, texte_nom, nation_selectionnee)
                            LANCEMENT = False  # Arrêter la boucle mode_solo
                    else:
                        print("Remplissez tous les champs et sélectionnez une nation.")

            if evenement.type == pygame.KEYDOWN:
                # Gestion du texte dans les champs actifs
                if actif_prenom:
                    if evenement.key == pygame.K_BACKSPACE:
                        texte_prenom = texte_prenom[:-1]
                    else:
                        texte_prenom += evenement.unicode
                elif actif_nom:
                    if evenement.key == pygame.K_BACKSPACE:
                        texte_nom = texte_nom[:-1]
                    else:
                        texte_nom += evenement.unicode
########################################################################################################################
#                                      L'interface qualification                                                       #
########################################################################################################################
def mode_duo():
    # Effacer tout ce que pygame_menu a dessiné
    ECRAN.fill(BLANC)
    pygame.display.flip()

    font = pygame.font.Font('freesansbold.ttf', 14)

    # Classe pour gérer les boutons
    class Button:
        def __init__(self, text, x, y, enabled=True):
            self.text = text
            self.x = x
            self.y = y
            self.width = 80
            self.height = 40
            self.enabled = enabled
            self.selected = False

        def dessiner(self):
            # Créer le rectangle du bouton
            button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            if self.selected:
                color = VERT
            else:
                color = BLEU
            pygame.draw.rect(ECRAN, color, button_rect, 0, 5)
            pygame.draw.rect(ECRAN, NOIR, button_rect, 2, 5)
            button_text = font.render(self.text, True, BLANC)
            text_rect = button_text.get_rect(center=button_rect.center)
            ECRAN.blit(button_text, text_rect)

        def click(self, pos):
            # Vérifier si le bouton est cliqué
            button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            if button_rect.collidepoint(pos):
                return True
            return False

    # Coordonnées et nations
    nations = ["France", "Canada", "États-Unis", "Allemagne", "Nigéria", "Niger", "Japon", "Chine", "Australie"]
    coordonnees_joueur_1 = [(80, 50), (175, 50), (270, 50),(80, 115), (175, 115), (270, 115),(80, 180), (175, 180), (270, 180)]
    coordonnees_joueur_2 = [(450, 50), (545, 50), (640, 50),(450, 115), (545, 115), (640, 115),(450, 180), (545, 180), (640, 180)]

    # Créer les boutons des nations à mettre sous forme d'image
    boutons_joueur_1 = [Button(nations[i], x, y) for i, (x, y) in enumerate(coordonnees_joueur_1)]
    boutons_joueur_2 = [Button(nations[i], x, y) for i, (x, y) in enumerate(coordonnees_joueur_2)]

    # Champs de texte pour les noms et noms de famille avec un module de gestionnaire
    gestionnaire_ui = pygame_gui.UIManager((800, 600))
    champ_prenom_joueur_1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(100, 450, 200, 40), manager=gestionnaire_ui)
    champ_nom_joueur_1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(100, 500, 200, 40), manager=gestionnaire_ui)
    champ_prenom_joueur_2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(500, 450, 200, 40), manager=gestionnaire_ui)
    champ_nom_joueur_2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(500, 500, 200, 40), manager=gestionnaire_ui)

    # texte pour indiquer les champs
    text_prenom1 = font.render('Prenom: 1', True, BLEU)
    text_nom1 = font.render('Nom: 1', True, BLEU)
    text_prenom2 = font.render('Prenom: 2', True, BLEU)
    text_nom2 = font.render('Nom: 2', True, BLEU)

    texte_joueur1 = font.render('Joueur: 1', True, BLEU)
    texte_joueur2 = font.render('Joueur: 2', True, BLEU)
    # Bouton "CONTINUER"
    bouton_valider = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 550, 200, 50), text="CONTINUER", manager=gestionnaire_ui)

    # Gestion des sélections
    nation_joueur_1 = None
    nation_joueur_2 = None

    clock = pygame.time.Clock()
    LANCEMENT = True
    while LANCEMENT:
        temps_refresh = clock.tick(60) / 1000.0
        ECRAN.fill(BLANC)
        # Ligne rouge au millieu
        pygame.draw.line(ECRAN, (255, 0, 0), (400, 0), (400, 580), 5)
        # Afficher le texte
        ECRAN.blit(text_prenom1, (30,460))
        ECRAN.blit(text_nom1, (50, 512))
        ECRAN.blit(text_prenom2, (430, 460))
        ECRAN.blit(text_nom2, (450, 512))
        ECRAN.blit(texte_joueur1, (160, 430))
        ECRAN.blit(texte_joueur2, (560, 430))
        # Dessiner les boutons des deux joueurs
        for bouton in boutons_joueur_1:
            bouton.dessiner()
        for bouton in boutons_joueur_2:
            bouton.dessiner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Pour choisir une seul nation à la fois
                for bouton in boutons_joueur_1:
                    if bouton.click(event.pos):
                        for b in boutons_joueur_1:
                            b.selected = False
                        bouton.selected = True
                        nation_joueur_1 = bouton.text

                # Pour choisir une seul nation du 2e joueur
                for bouton in boutons_joueur_2:
                    if bouton.click(event.pos):
                        for b in boutons_joueur_2:
                            b.selected = False
                        bouton.selected = True
                        nation_joueur_2 = bouton.text

            # Recupérer le texte seulement quand le bouton est pressé
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == bouton_valider:
                prenom_joueur_1 = champ_prenom_joueur_1.get_text()
                nom_joueur_1 = champ_nom_joueur_1.get_text()
                prenom_joueur_2 = champ_prenom_joueur_2.get_text()
                nom_joueur_2 = champ_nom_joueur_2.get_text()

                if nation_joueur_1 and nation_joueur_2 and prenom_joueur_1 and nom_joueur_1 and prenom_joueur_2 and nom_joueur_2:
                    # Étape 1 : Vérification des deux joueurs
                    joueur_1_valide = ajouter_participant(prenom_joueur_1, nom_joueur_1, nation_joueur_1)
                    joueur_2_valide = ajouter_participant(prenom_joueur_2, nom_joueur_2, nation_joueur_2)

                    # Étape 2 : Si un joueur existe déja on doit suprimer l'autre joueur qui vient d'être créer
                    if not joueur_1_valide or not joueur_2_valide:
                        if joueur_1_valide:
                            # Supprimer le joueur 1 si l'ajout a réussi mais que le joueur 2 échoue
                            connection = sqlite3.connect(db_file)
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM participants WHERE prenom = ? AND nom = ? AND nation = ?",(prenom_joueur_1, nom_joueur_1, nation_joueur_1))
                            connection.commit()
                            connection.close()
                            print(f"{prenom_joueur_1} {nom_joueur_1} a été retiré , mais peut être réutilisé ")
                        if joueur_2_valide:
                            # Supprimer le joueur 2 si l'ajout a réussi mais que le joueur 1 échoue
                            connection = sqlite3.connect(db_file)
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM participants WHERE prenom = ? AND nom = ? AND nation = ?",(prenom_joueur_2, nom_joueur_2, nation_joueur_2))
                            connection.commit()
                            connection.close()
                            print(f"{prenom_joueur_2} {nom_joueur_2} à été retiré, mais peut être réutilisé  ")
                    else:
                        jeu_duo(prenom_joueur_1, nom_joueur_1, nation_joueur_1, prenom_joueur_2, nom_joueur_2, nation_joueur_2)
                        LANCEMENT = False
                else:
                    print("Réessayer : Tous les critères ne sont pas remplis")

            gestionnaire_ui.process_events(event)
        gestionnaire_ui.update(temps_refresh)
        gestionnaire_ui.draw_ui(ECRAN)

        pygame.display.flip()

    pygame.quit()
########################################################################################################################
#                                          ÉCRAN de chargement                                                         #
########################################################################################################################
def ecran_chargement():
    '''Ecran de chargement avant de lancer le jeu'''
    # Effacer tout ce qu'il y avait sur l'écran
    ECRAN.fill(NOIR)
    pygame.display.flip()

    font = pygame.font.SysFont("comicsansms", 25)

    progress = 0

    def chargement(progress):
        '''Fonction qui va afficher le texte en dessous de la barre '''
        if progress < 100:
            text_surface = font.render(f"Chargement {str(int(progress))} %", True, VERT)
        else:
            text_surface = font.render(f"Chargement {str(100)} %", True, VERT)

        # Positionner le texte en dessous de la barre de chargement
        text_rect = text_surface.get_rect(center=(400, 350))
        ECRAN.blit(text_surface, text_rect)

    # Boucle de chargement
    while progress < 100:
        augmenter = random.randint(9, 19)
        progress += augmenter
        if progress > 100:
            progress = 100

        # Remplir l'écran de noir
        ECRAN.fill(NOIR)

        # Les dimensions pour la barre
        barre_largeur, barre_hauteur = 400, 50
        bordure_epaisseur = 4
        x_bordure, y_bordure = 196, 271

        # Dessiner la bordure de la barre
        pygame.draw.rect(ECRAN, VERT, [x_bordure, y_bordure, barre_largeur + bordure_epaisseur * 2,barre_hauteur + bordure_epaisseur * 2])
        # Dessiner l'intérieur
        pygame.draw.rect(ECRAN, NOIR, [200, 275, 400, 50])

        # Dessiner la barre de chargement
        largeur_chargee = (progress / 100) * barre_largeur
        pygame.draw.rect(ECRAN, VERT, [200, 275, largeur_chargee, 50])

        chargement(progress)
        pygame.display.flip()
        time.sleep(0.3)     # vitesse du chargement
########################################################################################################################
#                                            Les règles du jeu                                                         #
########################################################################################################################
def interface_regle():
    #POLICE
    police = pygame.font.SysFont("Calibri", 30)

    bouton_solo = pygame.Rect(400,500,100,30)
    bouton_multi = pygame.Rect(300,500,100,30)
    bouton_commence_partie = pygame.Rect(10, 50, 110, 75)

    #Regle pour le mode SOLO
    def regle_solo():
        ECRAN.fill((240, 240, 240))

        # Regle
        regle = pygame.font.SysFont("Times new roman", 20, bold=False)
        regle= regle.render("REGLE DU JEU", True, (0, 0, 0))
        ECRAN.blit(regle, (230, 10))

        # Regle 1
        regle_1 = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_1 = regle_1.render("1- IL FAUT TERMINER LA COURSE DANS LES 3 MINUTES DE JEU.", True, (0, 0, 0))
        ECRAN.blit(regle_1, (230, 50))

        # Regle 2
        regle_2 = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_2 = regle_2.render("3- DES QU'UN FRANCHIT LA LIGNE, LE JEU EST FINI POUR TOUS.", True, (0, 0, 0))
        ECRAN.blit(regle_2, (230, 90))

        # Regle 3
        regle_3 = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_3 = regle_3.render("4- AUCUN REPOS N'EST PERMIS.", True, (0, 0, 0))
        ECRAN.blit(regle_3, (230, 130))

        pygame.display.flip()

        # Regle 4
        regle_4 = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_4 = regle_4.render("5- RESPECT DES TRAJECTOIRES DEFINIE PAR LA COURSE.", True, (0, 0, 0))
        ECRAN.blit(regle_4, (230, 170))

        # Comment jouer


        regle_princ = pygame.font.SysFont("Times new roman", 20, bold=False)
        regle_princ = regle_princ.render("COMMENT JOUER", True, (0, 0, 0))
        ECRAN.blit(regle_princ, (230, 210))

        #avancer

        regle_avance = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_avance = regle_avance.render("POUR AVANCER, LA TOUCHE « W »", True, (0, 0, 0))
        ECRAN.blit(regle_avance, (230, 250))
        #reculer

        regle_recule = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_recule = regle_recule.render("POUR RECULER, LA TOUCHE « S »", True, (0, 0, 0))
        ECRAN.blit(regle_recule, (230, 290))

        # droite

        regle_droite = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_droite = regle_droite.render("POUR LA DROITE, LA TOUCHE « D »", True, (0, 0, 0))
        ECRAN.blit(regle_droite, (230, 330))

        # gauche

        regle_gauche = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_gauche = regle_gauche.render("POUR LA GAUCHE, LA TOUCHE « A »", True, (0, 0, 0))
        ECRAN.blit(regle_gauche, (230, 370))

    def regle_multi():
        ECRAN.fill((240, 240, 240))
        # Regle 1

        # afficher un objet de type police de caractere
        regle_1 = pygame.font.SysFont("Times new roman", 12, bold=False)

        # indiquer le texte et le transformer en image
        regle_1 = regle_1.render("1- IL EST INTERDIT DE BLOQUER LES AUTRES ADVERSAIRES.", True, (0, 0, 0))

        # afficher la regle aux coordonees indiquees
        ECRAN.blit(regle_1, (230, 10))

        # Regle
        regle_2 = pygame.font.SysFont("Times new roman", 12, bold=True)
        regle_2 = regle_2.render("2- IL FAUT TERMINER LA COURSE DANS LES 3 MINUTES DE JEU.", True, (0, 0, 0))
        ECRAN.blit(regle_2, (230, 50))

        # Regle 3
        regle_3 = pygame.font.SysFont("Times new roman", 12, bold=True)
        regle_3 = regle_3.render("3- DES QU'UN FRANCHIT LA LIGNE, LE JEU EST FINI POUR TOUS.", True, (0, 0, 0))
        ECRAN.blit(regle_3, (230, 90))

        # Regle 4
        regle_4 = pygame.font.SysFont("Times new roman", 12, bold=True)
        regle_4 = regle_4.render("4- AUCUN REPOS N'EST PERMIS.", True, (0, 0, 0))
        ECRAN.blit(regle_4, (230, 130))

        pygame.display.flip()

        # Regle 5
        regle_5 = pygame.font.SysFont("Times new roman", 12, bold=True)
        regle_5 = regle_5.render("5- RESPECT DES TRAJECTOIRES DEFINIE PAR LA COURSE.", True, (0, 0, 0))
        ECRAN.blit(regle_5, (230, 170))

        # Regle 6
        regle_6 = pygame.font.SysFont("Times new roman", 12, bold=True)
        regle_6 = regle_6.render("6- LES COLLISIONS AVEC LES JOUEURS SONT INTERDITES.", True, (0, 0, 0))
        ECRAN.blit(regle_6, (230, 210))

        # Comment jouer

        regle_princ = pygame.font.SysFont("Times new roman", 20, bold=False)
        regle_princ = regle_princ.render("COMMENT JOUER", True, (0, 0, 0))
        ECRAN.blit(regle_princ, (320, 250))

        #JOUEUR 1

        joueur = pygame.font.SysFont("Times new roman", 12, bold=False)
        joueur = joueur.render("JOUEUR 1", True, (0, 0, 0))
        ECRAN.blit(joueur, (250, 275))

        # avancer
        regle_avance = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_avance = regle_avance.render("POUR AVANCER, LA TOUCHE W", True, (0, 0, 0))
        ECRAN.blit(regle_avance, (180, 310))

        # reculer
        regle_recule = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_recule = regle_recule.render("POUR RECULER, LA TOUCHE S", True, (0, 0, 0))
        ECRAN.blit(regle_recule, (180, 350))

        # droite
        regle_droite = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_droite = regle_droite.render("POUR LA DROITE, LA TOUCHE D", True, (0, 0, 0))
        ECRAN.blit(regle_droite, (180, 390))

        # gauche
        regle_gauche = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_gauche = regle_gauche.render("POUR LA GAUCHE, LA TOUCHE A", True, (0, 0, 0))
        ECRAN.blit(regle_gauche, (180, 430))

        # JOUEUR 2
        joueur = pygame.font.SysFont("Times new roman", 12, bold=False)
        joueur = joueur.render("JOUEUR 2", True, (0, 0, 0))
        ECRAN.blit(joueur, (495, 275))

        # avancer
        regle_avance = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_avance = regle_avance.render("POUR AVANCER, LA FLECHE DU HAUT", True, (0, 0, 0))
        ECRAN.blit(regle_avance, (410, 310))
        # reculer

        regle_recule = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_recule = regle_recule.render("POUR RECULER, LA FLECHE DU BAS", True, (0, 0, 0))
        ECRAN.blit(regle_recule, (410, 350))

        # droite
        regle_droite = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_droite = regle_droite.render("POUR LA DROITE, LA FLECHE DE DROITE", True, (0, 0, 0))
        ECRAN.blit(regle_droite, (410, 390))

        # gauche
        regle_gauche = pygame.font.SysFont("Times new roman", 12, bold=False)
        regle_gauche = regle_gauche.render("POUR LA GAUCHE, LA FLECHE DE GAUCHE", True, (0, 0, 0))
        ECRAN.blit(regle_gauche, (410, 430))

    LANCEMENT = True
    mode_jeu = None

    # Boucle de lancement
    while LANCEMENT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if bouton_solo.collidepoint(pos):
                    mode_jeu = 'solo'
                    regle_solo()  # Affiche les règles du mode solo
                elif bouton_multi.collidepoint(pos):
                    mode_jeu = 'multi'
                    regle_multi()  # Affiche les règles du mode multi
                elif bouton_commence_partie.collidepoint(pos):
                    LANCEMENT = False

        if mode_jeu is None:
            Nom_du_jeu = pygame.font.SysFont("Times new roman", 40, bold=False)
            heure_actuelle = strftime("%H:%M:%S")  # Utilisation de `time` pour l'heure
            date_actuelle = datetime.now().strftime("%d/%m/%Y")  # Utilisation de `datetime` pour la date
            jeu = Nom_du_jeu.render("LA COURSE AUX OBSTACLES !", True, (255, 0, 0))
            ECRAN.fill((240, 240, 240))
            texte_heure = police.render(heure_actuelle, True, (0, 0, 0))
            texte_date = police.render(date_actuelle, True, (0, 0, 0))
            ECRAN.blit(texte_heure, (340, 85))
            ECRAN.blit(texte_date, (320, 135))
            ECRAN.blit(jeu, (145, 250))

        # Dessiner les boutons
        pygame.draw.rect(ECRAN, (0, 255, 0), bouton_solo)
        pygame.draw.rect(ECRAN, (255, 0, 0), bouton_multi)
        pygame.draw.rect(ECRAN, (0, 0, 255), bouton_commence_partie)

        # Afficher le texte sur les boutons
        font = pygame.font.SysFont("Times new roman", 20, bold=True)
        texte_solo = font.render("Solo", True, (0, 0, 0))
        texte_multi = font.render("Multi", True, (0, 0, 0))
        texte_partie1 = font.render("DEBUTER", True, (255, 255, 255))
        texte_partie2 = font.render("LA", True, (255, 255, 255))
        texte_partie3 = font.render("PARTIE", True, (255, 255, 255))

        ECRAN.blit(texte_solo, (bouton_solo.x + 30, bouton_solo.y + 5))
        ECRAN.blit(texte_multi, (bouton_multi.x + 25, bouton_multi.y + 5))
        ECRAN.blit(texte_partie1, (bouton_commence_partie.x + 10, bouton_commence_partie.y + 5))
        ECRAN.blit(texte_partie2, (bouton_commence_partie.x + 40, bouton_commence_partie.y + 25))
        ECRAN.blit(texte_partie3, (bouton_commence_partie.x + 20, bouton_commence_partie.y + 45))

        pygame.display.flip()
########################################################################################################################
#                                               Jeu en solo                                                           #
########################################################################################################################
def jeu_solo(prenom, nom, nation):
    interface_regle()
    ecran_chargement()
    # Effacer tout
    ECRAN.fill(BLANC)
    pygame.display.flip()
    # image terrain
    terrain = pygame.image.load("coureur_duo_1.png")
    terrain = pygame.transform.scale(terrain, (800, 500))  # Redimensionner l'image

    clock = pygame.time.Clock()

    class Courreur:
        def __init__(self, x, y):
            self.size = 30
            self.x = x
            self.y = y
            self.x_min = 120
            self.y_min = 50
            self.x_max = 640
            self.y_max = 440
            self.speed = random.randint(2, 3)
            self.image = pygame.image.load("coureur_duo_1.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.image.set_colorkey(BLANC)

        def draw(self, ECRAN):
            ECRAN.blit(self.image, (self.x, self.y))

        def deplacement_wasd(self, keys):
            if keys[pygame.K_w] and self.y > self.y_min:  # Haut
                self.y -= self.speed
            if keys[pygame.K_s] and self.y < self.y_max - 20:  # Bas
                self.y += self.speed
            if keys[pygame.K_a] and self.x > self.x_min:  # Gauche
                self.x -= self.speed
            if keys[pygame.K_d] and self.x < self.x_max - 20:  # Droite
                self.x += self.speed

    class Projectile:
        def __init__(self, x, y, vitesse):
            self.x = x
            self.y = y
            self.rayon = 20
            self.color = ROUGE
            self.vitesse = vitesse

        def draw(self, ECRAN):
            pygame.draw.circle(ECRAN, self.color, (self.x, self.y), self.rayon)

        def mouvement(self):
            self.y += self.vitesse
            if self.y > 440:
                self.y = 20
                self.x = random.randint(120, 640)

    def collision(coureur, projectile):
        coureur_rect = pygame.Rect(coureur.x, coureur.y, coureur.size, coureur.size)
        projectile_rect = pygame.Rect(projectile.x - projectile.rayon,projectile.y - projectile.rayon,projectile.rayon * 2,projectile.rayon * 2,)
        return coureur_rect.colliderect(projectile_rect)

    # Initialisation du coureur et des projectiles
    coureur = Courreur(400, 440)
    projectiles = []
    for _ in range(9):
        x = random.randint(120, 640)
        y = random.randint(-100, 0)
        speed = random.randint(3, 6)
        projectile = Projectile(x, y, speed)
        projectiles.append(projectile)

    # Chronomètre
    start_time = pygame.time.get_ticks()  # Temps de départ en millisecondes
    ligne_arrive = 110  # Limite d'arrivée en `y`

    LANCEMENT = True
    while LANCEMENT:
        clock.tick(60)

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

        # Gérer les touches
        keys = pygame.key.get_pressed()
        coureur.deplacement_wasd(keys)

        # Vérifier les collisions avec les projectiles
        for projectile in projectiles:
            projectile.mouvement()
            if collision(coureur, projectile):
                coureur.x, coureur.y = 400, 440  # Réinitialiser la position du coureur au début

        # Vérifier si le coureur a atteint la limite d'arrivée
        if coureur.y <= ligne_arrive:
            finish_time = pygame.time.get_ticks()  # Temps à l'arrivée
            elapsed_time = (finish_time - start_time) / 1000  # mettre en secondes
            enregistrer_temps(prenom, nom, elapsed_time)
            LANCEMENT = False

        # les différents objets du jeu
        ECRAN.blit(terrain, (0, 0))
        for projectile in projectiles:
            projectile.draw(ECRAN)
        coureur.draw(ECRAN)

        # Afficher le temps
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        timer_surface = pygame.font.Font(None, 36).render(f"Temps: {elapsed_time:.2f}s", True, NOIR)
        ECRAN.blit(timer_surface, (0, 10))

        # Afficher les informations du joueur
        joueur_surface = pygame.font.Font(None, 36).render(f"{prenom} {nom} - Nation: {nation}", True, NOIR)
        ECRAN.blit(joueur_surface, (240, 570))


        pygame.display.flip()

    # Affichage final après fin du jeu
    ECRAN.fill(BLANC)
    fin_ecran = pygame.font.Font(None, 50).render(f"Bien joué! Vous avez réussie en: {elapsed_time:.2f}s", True, NOIR)
    ECRAN.blit(fin_ecran, (100, 250))
    pygame.display.flip()
    pygame.time.wait(3000)  # Pause de 3 secondes avant de fermer
    pygame.quit()
    
    
        
##################################################################################################################################
#                                       podium
##################################################################################################################################

def afficher_ecran_final(ECRAN, podium_data):
    """
    Affiche le cinquième écran avec le podium et le bouton "TERMINER".
    """
    
    pygame.init()
  
    LARGEUR, HAUTEUR = 500, 500
    ECRAN = pygame.display.set_mode((LARGEUR,HAUTEUR))                  
  
    pygame.display.set_caption("PODIUM")
   
    # Couleurs
    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    BLEU = (173, 216, 230)
    GRIS = (200, 200, 200)
    OR = (255, 215, 0)
    ARGENT = (192, 192, 192)
    BRONZE = (205, 127, 50)
    largeur = 500
    hauteur = 500

    podium_colors = [OR, ARGENT, BRONZE]

    # Police
    police = pygame.font.SysFont(None, 20)
    petite_police = pygame.font.SysFont(None, 20)

    # Fond
    ECRAN.fill(BLEU)

    # Public (on simule le public avec des cercles colorés)
    for _ in range(50):
        x = random.randint(50, largeur - 50)
        y = random.randint(50, 200)
        pygame.draw.circle(ECRAN, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), (x, y), 10)

    # Podium
    podium_x = largeur // 2 - 150
    podium_y = hauteur // 2 - 100
    podium_width = 300
    podium_height = 200

    pygame.draw.rect(ECRAN, GRIS, (podium_x, podium_y, podium_width, podium_height))

    # Marches du podium
    marches = [
        {"x": podium_x + 100, "y": podium_y - 60, "w": 100, "h": 60, "color": (255, 215, 0)},  # Or
        {"x": podium_x + 30, "y": podium_y, "w": 70, "h": 60, "color": (192, 192, 192)},  # Argent
        {"x": podium_x + 200, "y": podium_y, "w": 70, "h": 60, "color": (205, 127, 50)},  # Bronze
    ]

    for marche in marches:
        pygame.draw.rect(ECRAN, marche["color"], (marche["x"], marche["y"], marche["w"], marche["h"]))

    for i, data in enumerate(podium_data):
        nom, drapeau = data
        marche = marches[i]
        
        # Dessiner la marche
        pygame.draw.rect(ECRAN, podium_colors[i], (marche["x"], marche["y"], marche["w"], marche["h"]))

        # Afficher le drapeau
        try:
            flag_img = pygame.image.load(drapeau)
            flag_img = pygame.transform.scale(flag_img, (marche["w"], 30))
            ECRAN.blit(flag_img, (marche["x"], marche["y"] - 40))
        except pygame.error:
            print(f"Erreur : Impossible de charger l'image du drapeau '{drapeau}'")

        # Afficher le nom
        petite_police = pygame.font.Font(None, 20)
        texte_nom = petite_police.render(nom, True, NOIR)
        texte_nom_rect = texte_nom.get_rect(center=(marche["x"] + marche["w"] // 2, marche["y"] + 30))
        ECRAN.blit(texte_nom, texte_nom_rect)

    # Bouton TERMINER
    bouton_x = largeur // 2 - 100
    bouton_y = hauteur - 100
    bouton_width = 200
    bouton_height = 50
    pygame.draw.rect(ECRAN, NOIR, (bouton_x, bouton_y, bouton_width, bouton_height))
    texte_bouton = police.render("TERMINER", True, BLANC)
    ECRAN.blit(texte_bouton, (bouton_x + 25, bouton_y + 5))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Attendre l'interaction avec le bouton
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if bouton_x <= mouse_x <= bouton_x + bouton_width and bouton_y <= mouse_y <= bouton_y + bouton_height:
                    running = False  # Retourner à l'écran ACCUEIL

    pygame.quit()







########################################################################################################################
#                                               Jeu en duo                                                           #
########################################################################################################################
def jeu_duo(prenom1, nom1, nation1, prenom2, nom2, nation2):
    ecran_chargement()
    ECRAN.fill(BLANC)
    pygame.display.flip()
    # image terrain
    terrain = pygame.image.load("coureur_duo_1.png")
    terrain = pygame.transform.scale(terrain, (800, 500))  # Redimensionner l'image
    clock = pygame.time.Clock()
    
 
   

    class Courreur_duo_1:
        def __init__(self, x, y):
            self.size = 30
            self.x = x
            self.y = y
            self.x_min = 120
            self.y_min = 50
            self.x_max = 640
            self.y_max = 440
            self.speed = random.randint(2, 3)
            self.image1 = pygame.image.load("coureur_duo_1.png")
            self.image1 = pygame.transform.scale(self.image1, (30, 30))
            self.image1.set_colorkey((255, 255, 255))

        def draw(self, ECRAN):
            ECRAN.blit(self.image1, (self.x, self.y))

        def deplacement_wasd(self, keys):
            if keys[pygame.K_w] and self.y > self.y_min:  # Haut
                self.y -= self.speed
            if keys[pygame.K_s] and self.y < self.y_max - 20:  # Bas
                self.y += self.speed
            if keys[pygame.K_a] and self.x > self.x_min:  # Gauche
                self.x -= self.speed
            if keys[pygame.K_d] and self.x < self.x_max - 20:  # Droite
                self.x += self.speed
    
    
    class Projectile:
        def __init__(self, x, y, vitesse):
            self.x = x
            self.y = y
            self.rayon = 20
            self.color = ROUGE
            self.vitesse = vitesse

        def draw(self, ECRAN):
            pygame.draw.circle(ECRAN, self.color, (self.x, self.y), self.rayon)

        def mouvement(self):
            self.y += self.vitesse
            if self.y > 440:
                self.y = 20
                self.x = random.randint(120, 640)

    
    
    def collision(coureur1, projectile):
        coureur1_rect = pygame.Rect(coureur1.x, coureur1.y, coureur1.size, coureur1.size)
        projectile_rect = pygame.Rect(projectile.x - projectile.rayon,projectile.y - projectile.rayon,projectile.rayon * 2,projectile.rayon * 2,)
        return coureur1_rect.colliderect(projectile_rect)
    
    # Initialisation du coureur et des projectiles
    coureur1 = Courreur_duo_1(400, 440)
    projectiles = []
    for _ in range(9):
        x = random.randint(120, 640)
        y = random.randint(-100, 0)
        speed = random.randint(3, 6)
        projectile = Projectile(x, y, speed)
        projectiles.append(projectile)

    # Chronomètre
    start_time = pygame.time.get_ticks()  # Temps de départ en millisecondes
    ligne_arrive = 80  # Limite d'arrivée en `y`

    running = True
    while running:
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        if elapsed_time >= 60:
            running = False
            message_fin = f"Temps écoulé ! Vous avez joué {elapsed_time:.2f}s"
            break
        # Gérer les touches
        keys = pygame.key.get_pressed()
        coureur1.deplacement_wasd(keys)

        # Vérifier les collisions avec les projectiles
        for projectile in projectiles:
            projectile.mouvement()
            if collision(coureur1, projectile):
                coureur1.x, coureur1.y = 400, 440  # Réinitialiser la position du coureur au début

        # Vérifier si le coureur a atteint la limite d'arrivée
        if coureur1.y <= ligne_arrive:
            finish_time = pygame.time.get_ticks()  # Temps à l'arrivée
            elapsed_time = (finish_time - start_time) / 1000  # mettre en secondes
            enregistrer_temps(prenom1, nom1, elapsed_time)
            message_fin = f"Bien joué! Vous avez réussi en: {elapsed_time:.2f}s"
            running = False

        # les différents objets du jeu
        ECRAN.blit(terrain, (0, 0))
        for projectile in projectiles:
            projectile.draw(ECRAN)
        coureur1.draw(ECRAN)

        # Afficher le temps
        timer_surface = pygame.font.Font(None, 36).render(f"Temps: {elapsed_time:.2f}s", True, NOIR)
        ECRAN.blit(timer_surface, (0, 10))

        # Afficher les informations du joueur
        joueur_surface = pygame.font.Font(None, 36).render(f"{prenom1} {nom1} - Nation: {nation1}", True, NOIR)
        ECRAN.blit(joueur_surface, (280, 570))


        pygame.display.flip()
        

    ECRAN.fill(BLANC)
    fin_ecran = pygame.font.Font(None, 50).render(message_fin, True, NOIR)
    ECRAN.blit(fin_ecran, (100, 250))
    pygame.display.flip()
    pygame.time.wait(3000)
    temps1 = elapsed_time





    class Courreur_duo_2:
        def __init__(self, x, y):
            self.size = 30
            self.x = x
            self.y = y
            self.x_min = 120
            self.y_min = 50
            self.x_max = 640
            self.y_max = 440
            self.speed = random.randint(2, 3)
            self.image2 = pygame.image.load("coureur._duo_2.png")
            self.image2 = pygame.transform.scale(self.image2, (30, 30))
            self.image2.set_colorkey((255, 255, 255))

        def draw(self, ECRAN):
            ECRAN.blit(self.image2, (self.x, self.y))

        def deplacement_wasd(self, keys):
            if keys[pygame.K_w] and self.y > self.y_min:  # Haut
                self.y -= self.speed
            if keys[pygame.K_s] and self.y < self.y_max - 20:  # Bas
                self.y += self.speed
            if keys[pygame.K_a] and self.x > self.x_min:  # Gauche
                self.x -= self.speed
            if keys[pygame.K_d] and self.x < self.x_max - 20:  # Droite
                self.x += self.speed
    
    
    class Projectile:
        def __init__(self, x, y, vitesse):
            self.x = x
            self.y = y
            self.rayon = 20
            self.color = ROUGE
            self.vitesse = vitesse

        def draw(self, ECRAN):
            pygame.draw.circle(ECRAN, self.color, (self.x, self.y), self.rayon)

        def mouvement(self):
            self.y += self.vitesse
            if self.y > 440:
                self.y = 20
                self.x = random.randint(120, 640)



    def collision(coureur2, projectile):
        coureur2_rect = pygame.Rect(coureur2.x, coureur2.y, coureur2.size, coureur2.size)
        projectile_rect = pygame.Rect(projectile.x - projectile.rayon,projectile.y - projectile.rayon,projectile.rayon * 2,projectile.rayon * 2,)
        return coureur2_rect.colliderect(projectile_rect)
    
    # Initialisation du coureur et des projectiles
    coureur2 = Courreur_duo_2(400, 440)
    projectiles = []
    for _ in range(9):
        x = random.randint(120, 640)
        y = random.randint(-100, 0)
        speed = random.randint(3, 6)
        projectile = Projectile(x, y, speed)
        projectiles.append(projectile)

    # Chronomètre
    start_time = pygame.time.get_ticks()  # Temps de départ en millisecondes
    ligne_arrive = 80  # Limite d'arrivée en `y`

    running = True
    while running:
        clock.tick(60)
                        
        if elapsed_time >= 60:
            running = False
            message_fin = f"Temps écoulé ! Vous avez joué {elapsed_time:.2f}s"
            break
        
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gérer les touches
        keys = pygame.key.get_pressed()
        coureur2.deplacement_wasd(keys)

        # Vérifier les collisions avec les projectiles
        for projectile in projectiles:
            projectile.mouvement()
            if collision(coureur2, projectile):
                coureur2.x, coureur2.y = 400, 440  # Réinitialiser la position du coureur au début

        # Vérifier si le coureur a atteint la limite d'arrivée
        if coureur2.y <= ligne_arrive:
            finish_time = pygame.time.get_ticks()  # Temps à l'arrivée
            elapsed_time = (finish_time - start_time) / 1000  # mettre en secondes
            enregistrer_temps(prenom2, nom2, elapsed_time)
            message_fin = f"Bien joué! Vous avez réussi en: {elapsed_time:.2f}s"
            running = False

        # les différents objets du jeu
        ECRAN.blit(terrain, (0, 0))
        for projectile in projectiles:
            projectile.draw(ECRAN)
        coureur2.draw(ECRAN)

        # Afficher le temps
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        timer_surface = pygame.font.Font(None, 36).render(f"Temps: {elapsed_time:.2f}s", True, NOIR)
        ECRAN.blit(timer_surface, (0, 10))

        # Afficher les informations du joueur
        joueur_surface = pygame.font.Font(None, 36).render(f"{prenom2} {nom2} - Nation: {nation2}", True, NOIR)
        ECRAN.blit(joueur_surface, (280, 570))


        pygame.display.flip()
    ECRAN.fill(BLANC)
    fin_ecran = pygame.font.Font(None, 50).render(message_fin, True, NOIR)
    ECRAN.blit(fin_ecran, (100, 250))
    pygame.display.flip()
    pygame.time.wait(3000)
    temps2 = elapsed_time
    
    
    
    class Courreur_IA:
        def __init__(self, x, y):
            self.size = 30
            self.x = x
            self.y = y
            self.x_min = 120
            self.y_min = 50
            self.x_max = 640
            self.y_max = 440
            self.speed = random.randint(2, 3)
            self.image_IA = pygame.image.load("cpu.png")
            self.image_IA = pygame.transform.scale(self.image_IA, (30, 30))
            self.image_IA.set_colorkey((255, 255, 255))

        def draw(self, ECRAN):
            ECRAN.blit(self.image_IA, (self.x, self.y))

        def deplacement_IA(self, projectiles):
            # Fuit les projectiles proches
            for projectile in projectiles:
                if abs(self.x - projectile.x) < 50 and abs(self.y - projectile.y) < 50:
                    if self.x < projectile.x and self.x > self.x_min:
                        self.x -= self.speed  # Va à gauche pour éviter
                    elif self.x > projectile.x and self.x < self.x_max:
                        self.x += self.speed  # Va à droite pour éviter
                    if self.y > projectile.y and self.y < self.y_max:
                        self.y += self.speed  # Va vers le bas pour éviter
        
            # Continue vers le haut si aucun projectile n'est proche
            if self.y > self.y_min:
                self.y -= self.speed

    
    class Projectile:
        def __init__(self, x, y, vitesse):
            self.x = x
            self.y = y
            self.rayon = 20
            self.color = ROUGE
            self.vitesse = vitesse

        def draw(self, ECRAN):
            pygame.draw.circle(ECRAN, self.color, (self.x, self.y), self.rayon)

        def mouvement(self):
            self.y += self.vitesse
            if self.y > 440:
                self.y = 20
                self.x = random.randint(120, 640)

    
    
    def collision(coureur_IA, projectile):
        coureurIA_rect = pygame.Rect(coureur_IA.x, coureur_IA.y, coureur_IA.size, coureur_IA.size)
        projectile_rect = pygame.Rect(projectile.x - projectile.rayon,projectile.y - projectile.rayon,projectile.rayon * 2,projectile.rayon * 2,)
        return coureurIA_rect.colliderect(projectile_rect)
    
    nations = ["France", "Canada", "États-Unis", "Allemagne", "Nigéria", "Niger", "Japon", "Chine", "Australie"]
    while True:
        nation = random.choice(nations)
        if nation != nation1 and nation != nation2:
            prenom = f"CPU {nation}"
            nom = ""
            break
        
    
    # Initialisation du coureur et des projectiles
    coureurIA = Courreur_IA(400, 440)
    projectiles = []
    for _ in range(9):
        x = random.randint(120, 640)
        y = random.randint(-100, 0)
        speed = random.randint(3, 6)
        projectile = Projectile(x, y, speed)
        projectiles.append(projectile)

    # Chronomètre
    start_time = pygame.time.get_ticks()  # Temps de départ en millisecondes
    ligne_arrive = 80  # Limite d'arrivée en `y`

    running = True
    while running:
        clock.tick(60)
        if elapsed_time >= 60:
            running = False
            message_fin = f"Temps écoulé ! Vous avez joué {elapsed_time:.2f}s"
            break

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gérer les touches
        keys = pygame.key.get_pressed()
        coureurIA.deplacement_IA(projectiles)

        # Vérifier les collisions avec les projectiles
        for projectile in projectiles:
            projectile.mouvement()
            if collision(coureurIA, projectile):
                coureurIA.x, coureurIA.y = 400, 440  # Réinitialiser la position du coureur au début

        # Vérifier si le coureur a atteint la limite d'arrivée
        if coureurIA.y <= ligne_arrive:
            finish_time = pygame.time.get_ticks()  # Temps à l'arrivée
            elapsed_time = (finish_time - start_time) / 1000  # mettre en secondes
            enregistrer_temps(prenom, nom, elapsed_time)
            message_fin = f"Bien joué! Vous avez réussi en: {elapsed_time:.2f}s"
            running = False

        # les différents objets du jeu
        ECRAN.blit(terrain, (0, 0))
        for projectile in projectiles:
            projectile.draw(ECRAN)
        coureurIA.draw(ECRAN)

        # Afficher le temps
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        timer_surface = pygame.font.Font(None, 36).render(f"Temps: {elapsed_time:.2f}s", True, NOIR)
        ECRAN.blit(timer_surface, (0, 10))

        # Afficher les informations du joueur
        joueur_surface = pygame.font.Font(None, 36).render(f"{prenom}  -  Nation: {nation}", True, NOIR)
        ECRAN.blit(joueur_surface, (280, 570))


        pygame.display.flip()
        
    ECRAN.fill(BLANC)
    fin_ecran = pygame.font.Font(None, 50).render(message_fin, True, NOIR)
    ECRAN.blit(fin_ecran, (100, 250))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    temps3 = elapsed_time
    
    data_joueurs  = [
    (temps1, prenom1 + " " + nom1, "drapeau_" + nation1 + ".png"),
    (temps2, prenom2 + " " + nom2, "drapeau_" + nation2 + ".png"),
    (temps3, prenom + " " + nom, "drapeau_" + nation + ".png")]
    data_joueurs_triees = sorted(data_joueurs, key=lambda x: x[0])
    podium_data = [(joueur[1], joueur[2]) for joueur in data_joueurs_triees]
    
    afficher_ecran_final(ECRAN, podium_data)

    
########################################################################################################################
#                                           Menu Principal                                                             #
########################################################################################################################
base_donnee()

# Menu fait avec le module pygame_menu
menu = pygame_menu.Menu(title="Discipline Olympique",width=800, height=600,theme=pygame_menu.themes.THEME_BLUE)

menu.add.label("Bienvenue dans la course aux obstacles!", max_char=-1, font_size=35, font_color=(0, 0, 0))
menu.add.button("Record Mondial", ajouter_record)
menu.add.button("Solo", mode_solo)
menu.add.button("Qualification", mode_duo)
menu.add.button("Quitter", pygame_menu.events.EXIT)

while True:
    if current_screen == "menu":
        # Gérer le menu principal
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ECRAN.fill(NOIR)
        menu.update(events)
        menu.draw(ECRAN)
        pygame.display.flip()

    elif current_screen == "solo":
        mode_solo()
    elif current_screen == 'qualification':
        mode_duo()
        


















# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:37:43 2024

@author: Alex Hoang, Jean-Paul JREISSATY, Meher KHACHKHECHYAN et Simon GONZALEZ
"""

import numpy
import turtle
from graphelib import Graphe
from pilefile import File, Pile
import math

# Trouve et affiche un trajet permettant d'arriver à la destination voulue
class metro_trajet:
    def __init__(self):
        self._graphe_metro = Graphe(oriente = False)
        self._stations = "Metro_line_graphe_pondere.txt"
        self._couleur_arete = {}
        self._couleurs = {"yellow":"jaune", "green":"verte", "blue": "bleue", "orange": "orange"}
    
    def lire_fichier_arete(self):
        """
        Lis un fichier et crée les arêtes du graphe « self._graphe_metro »
        ainsi qu'un dictionnaire qui relie une arête à la couleur de sa ligne.
        """
        with open(self._stations) as fichier:
            lignes = fichier.read().split("\n\n")
            for ligne in lignes:
                ligne = ligne.split("\n")
                # Tous les premiers éléments des « lignes » sont: 
                # « {insert couleur} line: »
                # ligne[0][-6] permets de seulement sélectionner la couleur
                couleur = ligne[0][:-6] 
                for arete in ligne[1:]:
                    (orig, dest, poids) = arete.split()
                    self._graphe_metro.ajouteArete(orig, dest, float(poids))
                    self._couleur_arete[frozenset((orig, dest))] = couleur  
            return self._graphe_metro
                
    def dijkstra(self, G, debut, fin):
      """
      Algorithme Dijkstra modifié qui arrête de chercher quand la valeur voulue
      est trouvée.
      """
      exterior = set(G.listeSommets())
      dist = {s : math.inf for s in exterior}
      dist[debut] = 0
      while len(exterior) > 0:
        dmin = math.inf
        for s in exterior:
          if dist[s] < dmin:
            (a, dmin) = (s, dist[s])
        exterior.remove(a)
        if a == fin:  # Une valeur a été trouvé pour la destination finale
            break     # Peut arrêter la boucle
        for b in a.listeVoisins():
          if b in exterior:
             dist[b] = min( dist[b], dist[a] + a.poids(b) ) 
      return dist
  
    def chemin(self, dist, debut, fin):
        """
        Recrée le chemin conduisant à la destination voulue tout en indiquant
        le changement de ligne.
        """
        trajet_inverse = Pile()
        actuel = fin
        
        while actuel != debut:
            # Regarde les précédentes stations potentiels de
            # « actuel » dans « listeVoisins ».
            for prec in actuel.listeVoisins():
                if dist[prec] + prec.poids(actuel) == dist[actuel]:
                    trajet_inverse.empile((prec, actuel))
                    actuel = prec
                    break
        
        couleur = None
        trajet = []
        
        # Transition d'une Pile() à une liste
        while not trajet_inverse.estvide():
            (orig, dest) = trajet_inverse.depile()
            if couleur != self._couleur_arete[frozenset((str(orig), str(dest)))]:
                # La ligne de métro a changé. 
                # La couleur de la ligne est ajouté à trajet.
                couleur = self._couleur_arete[frozenset((str(orig), str(dest)))]
                trajet.append(couleur)
            trajet.append(str(orig))
        # Ajoute la destination finale à trajet
        trajet.append(str(dest))
        
        return trajet
  
    def affiche_chemin(self, debut, fin):
        """
        Affiche le chemin déterminé par le « début » et la « fin » 
        de l'argument.
        """
        stations = self.lire_fichier_arete()
        debut = stations.sommet(debut)
        fin = stations.sommet(fin)

        if debut == fin:
            print(f"Allez directement vers la station {str(fin)}.", end = "")
        
        else:
            # La distance la plus courte
            solution = self.dijkstra(stations, debut, fin)
            
            # Chemin station par station, entrecoupé des fois par des couleurs
            chemin = self.chemin(solution, debut, fin)
            
            # Des conditions permettant un bon format pour l'affiche du chemin
            for num, i in enumerate(chemin):
                # Changement de ligne
                if num != 0 and i in self._couleurs:
                    print(f"Puis changer à la ligne {self._couleurs[i]}", end = "")
                    print(" et empruntez la ou les stations: ", end = "")
                    continue
                elif i in self._couleurs:
                    print(f"Prenez la ligne {self._couleurs[i]}", end = "")
                    print(" et empruntez la ou les stations: ", end = "")
                    continue
                # Stations
                if chemin[num-1] in self._couleurs:
                    if chemin[num+1] in self._couleurs:
                        print(f"{i} et {chemin[num+2]}. ", end = "")
                    else:
                        print(i, end = "")
                else:
                    if (num + 1) <= (len(chemin)-1) and chemin[num+1] in self._couleurs:
                        print(f", {i} et {chemin[num+2]}. ", end = "")
                    elif num == len(chemin)-1:
                        print(f" et {i}.", end = "")
                    else:
                        print(f", {i}", end = "")
                    
# Dessine les lignes de métros
class ligne_metro:
    def __init__(self, color):
        self._coordonnees = "Metro_station_coordonnee.txt"
        self._couleur = color.lower()
        self._ligne = {}
    
    def lire_fichier_coordonnee(self):
        """
        Lis un fichier et crée un dictionnaire reliant une station 
        à ses coordonnées (x, y).
        """
        with open(self._coordonnees) as fichier:
            lignes = fichier.read().split("\n\n")
            for ligne in lignes:
                ligne = ligne.split("\n")
                if self._couleur in ligne[0]:
                    for coordonnee in ligne[1:]:
                        (station, x, y) = coordonnee.split()
                        self._ligne[station] = (int(x), int(y))
            return self._ligne

    def dessine_station(self):
        """
        Dessine the stations (the cercles) sur la carte, ainsi que leur nom
        """
        station_noire = ["Snowdon", "Vendome", "Lionel-Groulx", 
                         "Lucien-L'Allier", "Bonaventure",
                         "Berri-UQUAM", "Jean-Talon", "Sauve", 
                         "DeLaConcorde", "Parc", "Pie-IX"]
        focus.pensize(1)
        station_coordonnee = self.lire_fichier_coordonnee()
        for station in station_coordonnee:
            if "Intersection" not in station:
                if station in station_noire:
                    focus.fillcolor("black")
                    focus.pencolor("black")
                    r = 10
                else:
                    focus.fillcolor("white")
                    focus.pencolor("white")
                    r = 7.5
                # Cercle
                focus.penup()
                focus.goto(station_coordonnee[station])
                focus.right(90)
                focus.forward(r)
                focus.left(90)
                focus.pendown()
                focus.begin_fill()
                focus.circle(r)
                focus.end_fill()
                turtle.penup()
                focus.right(-90)
                focus.forward(r)
                focus.left(-90)
                focus.pendown()
                
    def dessine_ligne(self):
        """
        Dessine les lignes de métro avec les bonnes couleurs.
        """
        focus.pensize(20)
        focus.pencolor(self._couleur)
        station_coordonnee = self.lire_fichier_coordonnee()
        for i, station in enumerate(station_coordonnee):
            if i == 0:
                focus.penup()
                focus.goto(station_coordonnee[station])
                focus.pendown()
            else:
                focus.goto(station_coordonnee[station])
                
    def dessine_nom(self):
        """
        Dessine les noms sur la carte.
        """
        station_coordonnee = self.lire_fichier_coordonnee()
        for station in station_coordonnee:
            if "Intersection" not in station:
                focus.penup()
                focus.goto(station_coordonnee[station])
                focus.penup()
                focus.setheading(90)
                focus.forward(10)
                focus.pendown()
                focus.pencolor("Black")
                focus.write(station, align="center", font=("Arial", 7, "normal"))
    
    def dessine(self):
        """
        Dessine les lignes de métro, puis leurs stations ainsi que 
        leur nom.
        """
        self.dessine_ligne()
        self.dessine_station()
        self.dessine_nom()
 
# Dessine sur la carte le trajet de l'utilisateur
class utilisateur_trajet_carte(metro_trajet):
    def __init__(self, x, y, fin):
        super().__init__()
        self._coordonnee = "Metro_station_coordonnee.txt"
        self._x = x
        self._y = y
        self._fin = fin
        self._couleur_station = {}
        self._station_coordonnee = {} # station: (x, y)
        self._coordonnee_station = {} # (x, y): station
        
    def lire_fichier_coordonnee(self):
        """
        Lis un fichier pour créer trois dictionnaires:
        « station: (x, y) », « (x, y): station » et « color: [stations] ».
        """
        with open(self._coordonnee) as fichier:
            lignes = fichier.read().split("\n\n")
            for ligne in lignes:
                ligne = ligne.split("\n")
                color = ligne[0][:-6]
                for coordonnee in ligne[1:]:
                    (station, x, y) = coordonnee.split()
                    self._station_coordonnee[station] = (int(x), int(y))
                    if color not in self._couleur_station:
                        self._couleur_station[color] = [station]
                    else:
                        self._couleur_station[color].append(station)
                    if "Intersection" not in station:
                        self._coordonnee_station[(int(x), int(y))] = station
    
    def plus_proche_station(self, x, y):
        """
        Trouve la station la plus proche d'une position (x, y) donnée.
        """
        liste_coordonnees = list(self._coordonnee_station.keys())
        utilisateur = (x, y)
        
        coordonnees = numpy.array(liste_coordonnees).T
        
        d = ((coordonnees[0]-utilisateur[0])**2+(coordonnees[1]-utilisateur[1])**2)**0.5
        
        plus_proche_coordonnee_id = numpy.argmin(d)
        
        plus_proche_coordonnee = liste_coordonnees[plus_proche_coordonnee_id]
        
        return self._coordonnee_station[plus_proche_coordonnee]
        
    def trajet_sur_carte(self):
        """
        Affiche sur la carte le trajet de l'utilisateur
        """
        # Crée les dictionnaires
        self.lire_fichier_coordonnee()
        
        plus_proche_station = self.plus_proche_station(self._x, self._y)
        
        # Affiche le chemin dans la console
        self.affiche_chemin(plus_proche_station, self._fin)
        
        # Toute la section en-dessous est pour le trajet de l'utilisateur
        # sur la carte
        stations = self.lire_fichier_arete()
        debut = stations.sommet(plus_proche_station)
        fin = stations.sommet(self._fin)    
        
        # Va à la position initial de l'utilisateur
        usager.penup()
        usager.goto(self._x, self._y)
        usager.pendown()
        
        # N'a pas besoin de mettre le métro
        # Va directement en marchant vers la station voulue
        if debut == fin:
            usager.goto(self._station_coordonnee[str(fin)])   
        
        # Prend le métro
        else:
            solution = self.dijkstra(stations, debut, fin)
            chemin = self.chemin(solution, debut, fin)
            stations_importantes = File()
            
            # Enfile les éléments importants pour la construction du trajet
            for index, element in enumerate(chemin): 
                # On enfile la couleur, et la station si l'élément précédent
                # est une couleur ou si c'est la dernière station
                if (element in self._couleurs or index == (len(chemin)-1)
                      or chemin[index-1] in self._couleurs):
                    stations_importantes.enfile(element)
                # Si le prochain élément est une couleur
                if index + 1 <= len(chemin)-1 and chemin[index+1] in self._couleurs:
                    # On empile la station juste après la couleur
                    stations_importantes.enfile(chemin[index+2])
                    
            
            # Trajet sur la carte
            while not stations_importantes.estvide():  
                if stations_importantes.premier() in self._couleurs:
                    couleur = stations_importantes.defile()
                station1 = stations_importantes.defile()
                station2 = stations_importantes.defile()    
                # Regarde la liste d'une ligne selon la couleur
                ligne = self._couleur_station[couleur]
                # Ajuste la liste selon les stations importantes défilées
                if ligne.index(station1) > ligne.index(station2):
                    liste_stations = ligne[ligne.index(station2):ligne.index(station1)+1][::-1]
                else:
                    liste_stations = ligne[ligne.index(station1):ligne.index(station2)+1]
                # Dessine le trajet selon la liste ajustée
                # Les intersections sont inclus
                for station in liste_stations:
                    usager.goto(self._station_coordonnee[station])

class decors_sur_carte:
    def dessine_metro_decor(self):
        """
        Fonction regroupant plusieurs fonctions permettant le dessin de 
        plusieurs structures.
        """
        crayon = turtle.Turtle()
        crayon.speed(0)
        crayon.hideturtle()
    
        def dessine_fleuve():
            """
            Dessine le fleuve en bas de la carte
            """
            crayon.color('cyan')
            crayon.penup()
            crayon.goto(-600, -400)
            crayon.pendown()
            crayon.begin_fill()
            crayon.goto(-600, -380)
            crayon.goto(0, -345)
            crayon.goto(25, -335)
            crayon.goto(600, -320)
            crayon.goto(600, -400)
            crayon.goto(-600, -400)
            crayon.end_fill()
    
        Points_cles = {"Mont-Royal": (12, -25),
                       "Vieux Port": (240, -75),
                       "Jardin botanique": (280, 184),}
    
        def dessine_points_cles():
            """
            Marque les points cles
            """
            for lieu, pos in Points_cles.items():
                crayon.penup()
                crayon.goto(pos)
                crayon.dot(15, "pink")
                crayon.color('black')
                crayon.write(lieu, align="center", font=("Arial", 7, "normal"))
              

        def verdure1():
            """
            Dessin la zone approximatif autour du Mont-Royal
            """
            crayon.color("chartreuse4")
            crayon.penup()
            crayon.goto((-70, -120))
            crayon.left(35)
            crayon.pendown()
            crayon.begin_fill()
            crayon.setheading(0)
            crayon.left(33)
            for _ in range(2):
                crayon.forward(170)
                crayon.left(118)
                crayon.forward(60)
                crayon.left(62)
            crayon.end_fill()

        def maison(x, y, longueur, hauteur):
            """
            Dessine une maison
            """
            crayon.penup()
            crayon.goto((x, y))
            crayon.down()
            crayon.setheading(90)
            crayon.fillcolor("gray")
            crayon.begin_fill()
            for _ in range(2):
                crayon.forward(hauteur)
                crayon.right(90)
                crayon.forward(longueur)
                crayon.right(90)
            crayon.end_fill()
            crayon.forward(hauteur)
            (x, y) = crayon.pos()
            (x_autre_cote, y_autre_cote) = (x+longueur, y)
            (x_sommet, y_sommet) = (x+longueur/2, y+hauteur/2)
            crayon.fillcolor("red")
            crayon.begin_fill()
            crayon.goto((x_sommet, y_sommet))
            crayon.goto((x_autre_cote, y_autre_cote))
            crayon.goto((x, y))
            crayon.end_fill()
        
        
        maison(-400, 20, 50, 40)
        maison(-300, -40, 50, 40)
        maison(-200, -10, 50, 40)
        maison(-250, 170, 50, 40)
        maison(-150, 100, 50, 40)
        maison(-350, 130, 50, 40)
        maison(-275, 90, 50, 40)
        maison(-30, 210, 50, 40)
        maison(70, 146, 50, 40)
        maison(150, 120, 50, 40)
        maison(-30, 60, 50, 40)
        maison(-427, -100, 50, 40)
        maison(-300, -160, 50, 40)
        maison(-352, -124, 50, 40)
        maison(-200, -230, 50, 40)
        maison(142, -230, 50, 40)
        maison(200, -190, 50, 40)
        verdure1()
        dessine_points_cles()
        dessine_fleuve()
    
    
class GUI:
    def __init__(self):
        self._coordonnee = "Metro_station_coordonnee.txt"
        self._couleurs = ["blue", "yellow", "green", "orange"]
        self._tous_stations = []
        
    def lire_fichier_tous_station(self):
        """
        Lis un fichier et met dans une liste toutes les stations
        """
        with open(self._coordonnee) as fichier:
            lignes = fichier.read().split("\n\n")
            for ligne in lignes:
                ligne = ligne.split("\n")
                for coordonnee in ligne[1:]:
                    (station, x, y) = coordonnee.split()
                    if (station not in self._tous_stations and 
                       "Intersection" not in station):
                        self._tous_stations.append(station)
            return self._tous_stations 
    
    def metro_google_map(self):
        """
        Programme principal qui prend des données de l'utilisateur
        afin de lui afficher le trajet, autant sur la console que sur la carte.
        """
        for couleur in self._couleurs:
            y = ligne_metro(couleur)
            y.dessine()
        
        decors = decors_sur_carte()
        decors.dessine_metro_decor()
        
        tous_stations = self.lire_fichier_tous_station()
        
        avis = "OUI"
        
        while avis == "OUI":
            while True:
                try:
                    x = int(input("Veuillez mettre la coordonnée en « x » (De -600 à 600): "))
                    y = int(input("Veuillez mettre la coordonnée en « y » (De -400 à 400): "))
                    break
                except ValueError:
                    print("Veuillez mettre un nombre.")
            
            print("ATTENTION: ne pas mettre d'espace ou d'accent. ", end = "")
            print("Les majuscules et autres signes spéciaux tels que « - »", end = "")
            print(" sont tout de même obligatoire.")
            
            fin= input("Station d'arrivée: ")
            
            while fin not in tous_stations:
                print("La station que vous essayez d'atteindre n'existe pas.")
                fin= input("Station d'arrivée: ")
                continue
                
            path_on_map = utilisateur_trajet_carte(x, y, fin)
            
            path_on_map.trajet_sur_carte()
            
            print("\n")
            
            while True:
                avis = input("Voulez-vous continuer? (OUI/NON) ")
                avis = avis.upper()
                
                if avis not in ["OUI", "NON"]:
                    print("Réponse invalide. Réessayez.")
                    continue
                else:
                    break
                
            print()
            
            usager.clear()
        
        turtle.Screen().bye()
        print("Je vous souhaite un bon voyage.")

window = turtle.Screen()
window.setup(width=1200, height=800)
window.title("Metro map")

# Turtle qui dessine les lignes de métro
focus = turtle.Turtle()
focus.hideturtle()
focus.pensize(20)
focus.speed(0)

# L'usager
usager = turtle.Turtle()
usager.shape("circle")
usager.shapesize(0.5)
usager.color("DarkGray")
usager.pensize(5)
usager.pencolor("DarkGray")
usager.speed(2)

programme = GUI()
programme.metro_google_map()
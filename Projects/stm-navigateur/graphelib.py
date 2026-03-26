#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:10:51 2024

@author: jp
"""


# Classes pour reprÃ©senter les graphes
# On dÃ©finit deux classes: Sommet et Graphe

# Un sommet connaÃ®t son nom (une chaÃ®ne) et ses voisins (un
# dictionnaire qui associe des sommets Ã  des poids d'arÃªtes)

# version 2: supporte les graphes orientÃ©s et non orientÃ©s

class Sommet:
  def __init__(self, nom):
    '''CrÃ©e un sommet reliÃ© Ã  aucune arÃªte'''
    self._nom = nom
    self._voisins = {}

  def ajouteVoisin(self, v, poids=1):
    '''Ajoute ou modifie une arÃªte entre moi et v'''
    self._voisins[v] = poids

  def listeVoisins(self):
    '''Liste tous les voisins'''
    return self._voisins.keys()

  def estVoisin(self, v):
    '''Retourne un boolÃ©en: True si je suis voisin de v, False sinon'''
    return v in self._voisins

  def poids(self, v):
    '''Retourne le poids de l'arÃªte qui me connecte Ã  v'''
    if v in self._voisins:
      return self._voisins[v]
    return None

  def __str__(self):
    '''Retourne mon nom'''
    return str(self._nom)

# Un graphe connaÃ®t ses sommets
# C'est un dictionnaire qui associe des noms avec des sommets

class Graphe:
  def __init__(self, oriente=True):
    '''CrÃ©e un graphe vide'''
    self._sommets = {}
    self._oriente = oriente

  def estOriente(self):
    return self._oriente

  def sommet(self, nom):
    '''Retourne le sommet de ce nom'''
    if nom in self._sommets:
      return self._sommets[nom]
    return None
      
  def listeSommets(self, noms=False):
    '''Liste tous les sommets'''
    if noms:
      return list(self._sommets.keys())
    else:
      return list(self._sommets.values())
    
  def ajouteSommet(self, nom):
    '''Ajoute un nouveau sommet'''
    if nom in self._sommets:
      return None      # sommet dÃ©jÃ  prÃ©sent
    nouveauSommet = Sommet(nom)
    self._sommets[nom] = nouveauSommet

  def ajouteArete(self, origine, destination, poids=1):
    '''Relie les deux sommets par une arÃªte. 
       CrÃ©e les sommets s'ils n'existent pas dÃ©jÃ '''
    self.ajouteSommet(origine)      # ne fait rien si les
    self.ajouteSommet(destination)  # sommets existent dÃ©jÃ 
    s1 = self.sommet(origine)
    s2 = self.sommet(destination)
    s1.ajouteVoisin(s2, poids)
    if not self._oriente and origine != destination:
      s2.ajouteVoisin(s1, poids)

  def listeAretes(self, noms=False):
    '''Liste toutes les arÃªtes'''
    aretes = []
    for origine in self.listeSommets():
      for dest in origine.listeVoisins():
        if not self.estOriente() and str(origine) > str(dest):
          continue   # compter chaque arÃªte une seule fois si non oriente
        if noms:
          aretes.append( (str(origine), str(dest), origine.poids(dest)) )
        else:
          aretes.append( (origine, dest, origine.poids(dest)) )
    return aretes
                    
  def __str__(self):
    '''ReprÃ©sente le graphe comme une chaÃ®ne'''
    return ', '.join(a+b+':'+str(c) for (a,b,c) in self.listeAretes(True))
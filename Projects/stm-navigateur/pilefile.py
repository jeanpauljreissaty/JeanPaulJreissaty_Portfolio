#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:08:25 2024

@author: jp
"""

class Pile:
    def __init__(self):
        self._data = []
        
    def taille(self):
        return len(self._data)
    
    def estvide(self):
        return self.taille() == 0
    
    def empile(self, s):
        self._data.append(s)
        
    def depile(self):
        if self.estvide():
            raise LookupError("La pile est vide")
        return self._data.pop()
    
    def sommet(self):
        if self.estvide():
            raise LookupError("La pile est vide")
        return self._data[-1]
    
    def change_sommet(self, s):
        if self.estvide():
            raise LookupError("La pile est vide")
        self._data[-1] = s
        
    def __str__(self):
        return "Pile" + ", ".join([str(item) for item in self._data])
    
# p = Pile()
# p.empile("avion")
# p.empile("bicyclette")
# print(p)
# print(p.depile())
# print(p.sommet())
# p.empile("camion")
# print(p.depile())
# print(p.depile())
# print(p.taille())

class File:
    def __init__(self):
        self._data = []
        
    def taille(self):
        return len(self._data)
    
    def estvide(self):
        return self.taille() == 0
    
    def enfile(self, s):
        self._data.append(s)
        
    def defile(self):
        if self.estvide():
            raise LookupError("La file est vide")
        return self._data.pop(0)
    
    def premier(self):
        if self.estvide():
            raise LookupError("La file est vide")
        return self._data[0]
    
    def change_premier(self, s):
        if self.estvide():
            raise LookupError("La file est vide")
        self._data[0] = s
        
    def __str__(self):
        return "Pile" + ", ".join([str(item) for item in self._data])
    
 
# f = File()
# f.enfile("avion")
# f.enfile("bicyclette")
# print(f.defile())
# print(f.premier())
# f.enfile("camion")
# print(f.defile())
# print(f.defile())
# print(f.taille())




def entier_vers_binaire(nombre_entier):
    p = Pile()
    
    while nombre_entier > 0:
        reste_division = nombre_entier % 2
        p.empile(reste_division)
        nombre_entier //= 2      
    nombre_binaire = ""
    while not p.estvide():
        nombre_binaire += str(p.depile())
    return nombre_binaire
    
# nombre_entier = 6
# representation_binaire = entier_vers_binaire(nombre_entier)
# print(f"Le nombre binaire correspondant a {nombre_entier} est: {representation_binaire} ")
# print(int(entier_vers_binaire(nombre_entier), 2))
# print(bin(nombre_entier))

def entier_vers_binaire2(nombre_entier):
    f = File()
    while nombre_entier > 0:
        reste_division = nombre_entier % 2
        f.enfile(reste_division)
        nombre_entier //=2
    nombre_binaire = ""
  
    while not f.estvide():
        nombre_binaire += str(f.defile())
    return nombre_binaire




def est_parentheses_equilibres(expression):
    p = Pile()
    f = File()
    parentheses = {"(": ")", "{": "}", "[":"]"}
    for char in expression:
        if char in parentheses:
            p.empile(char)
        
        elif char in parentheses.values():
            f.enfile(char)
            
    while not p.estvide() and not f.estvide():
        if parentheses[p.depile()] != f.defile():
            return False
    return True
    
    
# expression_1 = "({([{()}])})"
# expression_2 = "[{()]}"
# print("L'expression 1 est equilibree: ", est_parentheses_equilibres(expression_1))    





























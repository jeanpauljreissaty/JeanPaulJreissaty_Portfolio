# ⚙️ Microprocesseur SIM-3000 — Programmation en Assembleur

Implémentation de trois algorithmes classiques en **langage assembleur personnalisé** sur le microprocesseur fictif SIM-3000.  
Le simulateur (`SIM3000.py`) permet de charger et d'exécuter les programmes instruction par instruction avec visualisation de la RAM et des registres en temps réel.

---

## 🎯 Algorithmes implémentés

### 1. 📐 Plus Grand Commun Diviseur (`pgcd.py`)
Calcule le PGCD de deux nombres en utilisant l'algorithme de soustraction répétée (méthode d'Euclide simplifiée).
- Détecte automatiquement quel nombre est le plus grand et les inverse si nécessaire
- Soustrait le plus petit du plus grand jusqu'à obtenir 0 ou un négatif
- Le PGCD final est stocké dans `RAM[2]`

### 2. 🌀 Suite de Fibonacci (`Suite_Fibonacci.py`)
Génère les K premiers termes de la suite de Fibonacci et les stocke séquentiellement en RAM.
- Initialise `RAM[10] = 0` et `RAM[11] = 1` comme conditions de départ
- Stocke chaque terme calculé dans `RAM[12]`, `RAM[13]`, `RAM[14]`...
- Utilise l'adressage indirect (`READ MEM`) pour écrire dynamiquement en mémoire

### 3. 🔢 Tri d'une liste (`Tri_d_une_liste.py`)
Trie une liste de nombres stockée en RAM par ordre croissant (algorithme de tri par sélection).
- Compare les éléments deux à deux et les inverse si nécessaire
- Boucle jusqu'à ce que toute la liste soit triée
- Détecte la fin de liste via une valeur sentinelle `0`

---

## 🚀 Installation & lancement du simulateur

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/sim3000-assembleur.git
cd sim3000-assembleur

# 2. Installer les dépendances
pip install freesimplegui

# 3. Lancer le simulateur
python SIM3000.py
```

Une fois le simulateur ouvert :
1. Clique sur **"Choisir"** pour charger un fichier `.py` (ex: `pgcd.py`)
2. Modifie la **RAM** avec les valeurs d'entrée via **"Modifier la RAM"**
3. Clique **"Exécuter le programme"** ou **"Exécuter une instruction"** pour avancer pas à pas

---

*Projet réalisé dans le cadre du cours Architecture des ordinateurs — Collège André-Grasset, 2025*

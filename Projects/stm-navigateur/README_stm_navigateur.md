# 🚇 Navigateur STM — Algorithme de Dijkstra

Application de navigation du réseau de métro de Montréal.  
L'utilisateur entre ses coordonnées et une station de destination — le programme calcule le **trajet optimal** et le visualise sur une carte graphique en temps réel.

---

## Fonctionnalités

- Algorithme de **Dijkstra** sur un graphe pondéré du réseau STM
- Détection automatique de la **station la plus proche** par coordonnées (distance euclidienne + NumPy)
- Affichage du trajet **station par station** avec indication des changements de ligne
- Visualisation graphique du trajet sur une **carte du métro** (Turtle)
- Support des 4 lignes : 🟡 Jaune · 🟢 Verte · 🔵 Bleue · 🟠 Orange
- Mode interactif : plusieurs trajets à la suite

---

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/stm-navigateur.git
cd stm-navigateur

# 2. Installer les dépendances
pip install numpy

# 3. Lancer le programme
python navigateur.py
```

Le programme demande :
- Coordonnées `x` (de -600 à 600) et `y` (de -400 à 400)
- Station de destination (ex: `Berri-UQAM`, `Jean-Talon`)

---

*Projet réalisé en équipe de 4 — Collège André-Grasset, 2024*

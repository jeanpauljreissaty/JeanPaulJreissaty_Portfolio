# 🍽️ Restaurant Poisson Rouge — Simulation complète

Simulation complète d'une expérience en restaurant, de la réservation jusqu'à la facture.  
Application multi-fenêtres développée en Python avec Tkinter et Pygame.

---

## Fonctionnalités

- **Réservation** : saisie et validation du nom du client
- **Plan de salle** : attribution aléatoire d'une table sur un plan interactif
- **Menu graphique** : affichage sur fond parchemin (image PIL)
- **Prise de commande** : sélection entrée / plat / dessert via checkboxes
- **Rendu des plats** : chaque plat est dessiné en Pygame (formes géométriques)
- **Facture complète** : calcul TPS (5%) + TVQ (9.75%), heure actuelle, nom du serveur
- **Données météo** : température moyenne intégrée via API `meteostat`
- Son joué à chaque bouchée avec `pyglet`

---

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/restaurant-poisson-rouge.git
cd restaurant-poisson-rouge

# 2. Installer les dépendances
pip install pygame pillow pyglet meteostat

# 3. Lancer l'application
python restaurant.py
```

---

*Projet réalisé en équipe de 2 — Collège André-Grasset, 2024*

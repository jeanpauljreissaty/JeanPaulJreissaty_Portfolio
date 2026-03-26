# 🏅 Olympiade — Course aux obstacles

Jeu de course olympique solo et multijoueur avec un adversaire contrôlé par IA.  
Les joueurs s'inscrivent, choisissent leur nation, et s'affrontent dans un parcours d'obstacles.

---

## Fonctionnalités

- **Mode Solo** : un joueur contre des projectiles aléatoires
- **Mode Qualification (Duo)** : deux joueurs + un adversaire IA jouent en séquence
- **IA adversaire** : algorithme de fuite — l'agent détecte les projectiles proches et les esquive en temps réel
- **Base de données SQLite** : enregistrement des participants et des temps
- Classement des **5 meilleurs temps** (records mondiaux)
- **Écran de chargement** animé avec barre de progression
- **Podium final** avec affichage des 3 meilleurs
- Menu principal avec `pygame_menu`
- Validation des données : unicité des participants, max 2 joueurs par nation

---

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/olympiade.git
cd olympiade

# 2. Installer les dépendances
pip install pygame pygame_menu pygame_gui

# 3. Lancer le jeu
python Olympiade.py
```

---

*Projet réalisé en équipe de 4 — Collège André-Grasset, 2024*

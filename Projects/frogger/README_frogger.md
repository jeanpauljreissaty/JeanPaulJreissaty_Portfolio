# 🐸 Frogger — Recréation en Python

Recréation complète du jeu classique **Frogger** (1981) en Python avec Pygame.  
Le joueur guide une grenouille à travers des voies de circulation et une rivière pour atteindre la zone de victoire.

---

## Fonctionnalités

- Moteur de déplacement avec contrôles au clavier (↑ ↓ ← →)
- 4 voies de route avec voitures à vitesses aléatoires
- 4 voies de rivière avec bûches de bois mouvantes
- Détection de collisions par rectangles (`pygame.Rect`)
- Système de 3 vies avec réinitialisation de position
- Condition de victoire (atteindre la zone finale)
- Code structuré en modules indépendants (POO)

---

##  Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/frogger-pygame.git
cd frogger

# 2. Installer les dépendances
pip install pygame==2.6.0

# 3. Lancer le jeu
python main.py
```

---
*Projet réalisé dans le cadre du cours INF1007 — Polytechnique Montréal, 2025*

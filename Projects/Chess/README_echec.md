# ♟️ Jeu d'Échecs — C++ / Qt6

Implémentation complète d'un jeu d'échecs en C++ avec interface graphique Qt6. Le joueur déplace les pièces en cliquant sur l'échiquier, avec validation complète des règles incluant la détection d'échec et d'échec et mat.

## Fonctionnalités

* Interface graphique Qt6 avec échiquier cliquable (sélection + déplacement en 2 clics)
* 6 types de pièces implémentées : Roi, Reine, Tour, Fou, Cavalier, Pion
* Validation complète des mouvements par pièce (`estMouvementValide`)
* Détection de chemin libre pour les pièces glissantes (tour, fou, reine)
* Détection d'échec (`roiEstEnEchec`) et d'échec et mat (`roiEstEnEchecEtMat`)
* Simulation RAII des coups pour vérifier qu'un mouvement ne met pas son propre roi en échec
* 4 positions de départ configurables via menu déroulant (partie complète, fin de partie, roi+tour vs roi, roi+reine vs roi)
* Exception personnalisée `RoiException` si plus de 2 rois sont placés sur le plateau
* Suite de tests unitaires avec `assert` (cavalier, tour, validité de coup)
* Architecture séparée en deux namespaces : `logique` (règles) et `application` (interface)

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/echec-qt.git
cd echec

# 2. Prérequis : Qt6 et CMake
# Sur Ubuntu/Debian :
sudo apt install cmake qt6-base-dev

# 3. Compiler avec CMake
mkdir build && cd build
cmake ..
cmake --build .

# 4. Lancer
./ProjetTest
```


Projet réalisé dans le cadre du cours INF1015 — Polytechnique Montréal, 2026  
Auteurs : Léo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)

# 🧾 Caisse Enregistreuse — C++ / Qt6

Application de caisse enregistreuse avec interface graphique Qt6. L'utilisateur ajoute des articles (description, prix, taxable ou non), retire les éléments sélectionnés et consulte en temps réel le sous-total, les taxes et le total.

## Fonctionnalités

* Interface Qt6 (QMainWindow) avec formulaire de saisie d'articles
* Ajout d'articles avec description, prix et option taxable
* Retrait multi-sélection depuis la liste (`QListWidget` en mode `ExtendedSelection`)
* Réinitialisation complète de la commande
* Calcul automatique du sous-total, des taxes (14,975 % — taux QC+CA) et du total
* Architecture MVC : `MainWindow` (vue) ↔ `CaisseModele` (modèle `QObject`) via signaux Qt (`commandeModifiee`)
* Deux exceptions personnalisées : `DescriptionVideException` et `PrixNulException`
* Mise à jour de l'affichage déclenchée par signal Qt à chaque modification du modèle

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/caisse-qt.git
cd TD6_Equipe1_11

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
Auteurs : Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)

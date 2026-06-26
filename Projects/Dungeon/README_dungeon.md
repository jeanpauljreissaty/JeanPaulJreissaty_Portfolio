# 🗡️ Dungeon Crawler — Aventure Textuelle C++

Jeu d'aventure textuelle en C++ dans lequel le joueur explore un donjon en entrant des commandes au clavier. Il navigue entre des zones interconnectées, interagit avec des objets et déverrouille de nouveaux passages.

## Fonctionnalités

* Navigation en 4 directions : `n`, `s`, `e`, `w` (ou `north`, `south`, `east`, `west`)
* Commandes `look` (décrire la zone) et `use <objet>` (interagir avec un élément)
* Système d'éclairage par zone : les pièces non éclairées masquent description et objets
* 3 types d'objets polymorphes héritant de `ObjetInteractif` :
  * `ObjetSimple` — retourne un message prédéfini
  * `ObjetEclairage` — bascule l'éclairage d'une zone cible
  * `ObjetDeverrouillage` — crée une connexion bidirectionnelle entre deux zones
* Aiguillage des commandes via `unordered_map<string, function>` et lambdas
* Carte construite par code (zones, connexions, objets) dans `Carte`
* Gestion de l'état courant (zone du joueur) encapsulée dans `EtatJeu`
* Architecture entièrement en C++ standard (pas de dépendances externes)

## Compilation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/dungeon-crawler.git
cd LV2_2448189_2462433

# 2. Compiler (g++ ou clang++)
g++ -std=c++20 -o dungeon main.cpp carte.cpp zone.cpp jeu.cpp etatjeu.cpp \
    direction.cpp objetinteractif.cpp objetsimple.cpp objeteclairage.cpp objetdeverrouillage.cpp

# 3. Lancer
./dungeon
```

## Exemple de session

```
>>>>> INF1015 DUNGEON CRAWLER 2026 <<<<<
> > > > GAME OF THE YEAR EDITION < < < <

-- Entrée du donjon --
Une grande salle de pierre...
La Salle Obscure is to the North (n)

> n
-- Salle Obscure --
It is near pitch black and you cannot discern any details.

> use torche
La torche illumine la pièce !
```


Projet réalisé dans le cadre du cours INF1015 — Polytechnique Montréal, 2026  
Auteurs : Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)

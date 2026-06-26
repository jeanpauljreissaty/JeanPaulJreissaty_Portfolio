/*
* Fichier: etatjeu.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la classe EtatJeu qui encapsule l'état courant du jeu (zone actuelle du joueur).
*/

#pragma once

#include "zone.hpp"

class EtatJeu {
public:
    explicit EtatJeu(Zone* depart);

    Zone* getZoneActuelle() const;
    void  deplacerVers(Zone* zone);

private:
    Zone* zoneActuelle_;
};

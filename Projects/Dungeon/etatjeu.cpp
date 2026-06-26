/*
* Fichier: etatjeu.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la classe EtatJeu.
*/

#include "etatjeu.hpp"

EtatJeu::EtatJeu(Zone* depart) : zoneActuelle_(depart) {}

Zone* EtatJeu::getZoneActuelle() const {
    return zoneActuelle_;
}

void EtatJeu::deplacerVers(Zone* zone) {
    zoneActuelle_ = zone;
}

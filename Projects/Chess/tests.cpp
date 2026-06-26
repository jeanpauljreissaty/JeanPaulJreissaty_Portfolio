/*
* Fichier: tests.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier pour tester des logique de jeu
*/

#include "jeu.hpp"
#include "cavalier.hpp"
#include "tour.hpp"
#include "roi.hpp"
#include "reine.hpp"
#include "fou.hpp"
#include "pion.hpp"
#include <cassert>

void testerCavalier() {
    logique::Cavalier c(logique::Couleur::Blanc, 4, 4);
    assert(c.estMouvementValide(5, 6) == true);   // L valide
    assert(c.estMouvementValide(6, 5) == true);   // L valide
    assert(c.estMouvementValide(5, 5) == false);  // diagonal invalide
    assert(c.sauteParDessus() == true);
}

void testerTour() {
    logique::Tour t(logique::Couleur::Blanc, 4, 4);
    assert(t.estMouvementValide(4, 7) == true);   // même colonne
    assert(t.estMouvementValide(7, 4) == true);   // même ligne
    assert(t.estMouvementValide(5, 5) == false);  // diagonal invalide
    assert(t.estMouvementValide(4, 4) == false);  // même case invalide
}

void testerJoueurCoup() {
    logique::Jeu jeu;
    jeu.reinitialiser(logique::PositionDepart::RoiEtTourVsRoi);
    // Tour blanche en (0,7) vers (0,5) — chemin libre
    assert(jeu.jouerCoup(0, 7, 0, 5) == true);
}

// etc. pour Roi, Reine, Fou, Pion, roiEstEnEchec, cheminLibre...

int lancerTests() {
    testerCavalier();
    testerTour();
    testerJoueurCoup();
    // ...
    return 0;
}
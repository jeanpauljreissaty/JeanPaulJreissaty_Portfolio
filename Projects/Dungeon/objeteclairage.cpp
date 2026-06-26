/*
* Fichier: objeteclairage.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation d'ObjetEclairage.
*/

#include "objeteclairage.hpp"
#include "zone.hpp"

ObjetEclairage::ObjetEclairage(std::string nom, std::string description, std::vector<std::string> motsCles, Zone* zoneCible)
    : ObjetInteractif(std::move(nom), std::move(description), std::move(motsCles)) , zoneCible_(zoneCible) {}

std::string ObjetEclairage::utiliser() {
    zoneCible_->setEclairee(!zoneCible_->estEclairee());

    if (zoneCible_->estEclairee())

        return zoneCible_->getNom() + " is now lit.";

    else
        return zoneCible_->getNom() + " is now dark.";
}

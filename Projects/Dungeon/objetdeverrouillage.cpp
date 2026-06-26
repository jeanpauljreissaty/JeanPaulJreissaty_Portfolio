/*
* Fichier: objetdeverrouillage.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation d'ObjetDeverrouillage.
*/

#include "objetdeverrouillage.hpp"
#include "zone.hpp"

ObjetDeverrouillage::ObjetDeverrouillage(std::string nom, std::string description, std::vector<std::string> motsCles, Zone* zoneA, Direction dirAversB, Zone* zoneB, Direction                dirBversA)
  : ObjetInteractif(std::move(nom), std::move(description), std::move(motsCles)) , zoneA_(zoneA) , dirAversB_(dirAversB) , zoneB_(zoneB) ,dirBversA_(dirBversA) {}

std::string ObjetDeverrouillage::utiliser() {
    if (dejaUtilise_)
        return "Nothing happens. The connection is already open.";

    zoneA_->connecter(dirAversB_, zoneB_);

    zoneB_->connecter(dirBversA_, zoneA_);

    dejaUtilise_ = true;

    return zoneA_->getNom() + " is now connected to " + zoneB_->getNom() + ".";
}

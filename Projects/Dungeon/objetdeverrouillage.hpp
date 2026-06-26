/*
* Fichier: objetdeverrouillage.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration d'ObjetDeverrouillage : objet qui crée une connexion bidirectionnelle entre deux zones lors de son utilisation.
*/

#pragma once

#include "objetinteractif.hpp"
#include "direction.hpp"

class Zone; 

class ObjetDeverrouillage : public ObjetInteractif {
public:
    ObjetDeverrouillage(std::string nom, std::string description, std::vector<std::string> motsCles, Zone* zoneA, Direction dirAversB, Zone* zoneB, Direction dirBversA);

    std::string utiliser() override;

private:
    Zone* zoneA_;
    Direction dirAversB_;
    Zone* zoneB_;
    Direction dirBversA_;
    bool dejaUtilise_ = false;
};

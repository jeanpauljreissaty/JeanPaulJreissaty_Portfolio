/*
* Fichier: objetsimple.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration d'ObjetSimple : objet interactif sans effet sur le monde, retournant un message prédéfini à l'utilisation.
*/

#pragma once

#include "objetinteractif.hpp"


class ObjetSimple : public ObjetInteractif {
public:
    ObjetSimple(std::string nom, std::string description, std::vector<std::string> motsCles, std::string messageUtilisation);

    std::string utiliser() override;

private:
    std::string messageUtilisation_;
};

/*
* Fichier: objeteclairage.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration d'ObjetEclairage : objet qui bascule l'éclairage d'une zone cible lors de son utilisation.
*/

#pragma once

#include "objetinteractif.hpp"

class Zone;

class ObjetEclairage : public ObjetInteractif {
public:
    ObjetEclairage(std::string nom, std::string description, std::vector<std::string> motsCles, Zone* zoneCible);

    std::string utiliser() override;

private:
    Zone* zoneCible_;
};

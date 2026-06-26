/*
* Fichier: objetinteractif.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la classe abstraite ObjetInteractif.
*/

#include "objetinteractif.hpp"

ObjetInteractif::ObjetInteractif(std::string nom, std::string description, std::vector<std::string> motsCles) 
    : nom_(std::move(nom)) , description_(std::move(description)) , motsCles_(std::move(motsCles)) {}

const std::string& ObjetInteractif::getNom() const {

    return nom_;
}

const std::string& ObjetInteractif::getDescription() const {

    return description_;
}

bool ObjetInteractif::correspondA(const std::string& terme) const {

    for (const std::string& motCle : motsCles_) {

        if (terme.find(motCle) != std::string::npos)
            return true;
    }
    return false;
}

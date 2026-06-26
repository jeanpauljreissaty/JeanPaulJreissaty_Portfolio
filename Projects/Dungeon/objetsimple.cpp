/*
* Fichier: objetsimple.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation d'ObjetSimple.
*/

#include "objetsimple.hpp"

ObjetSimple::ObjetSimple(std::string nom, std::string description, std::vector<std::string> motsCles, std::string messageUtilisation)
    : ObjetInteractif(std::move(nom), std::move(description), std::move(motsCles)) , messageUtilisation_(std::move(messageUtilisation)) {}

std::string ObjetSimple::utiliser() {

    return messageUtilisation_;
}

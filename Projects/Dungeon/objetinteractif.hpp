/*
* Fichier: objetinteractif.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la classe abstraite ObjetInteractif. Tous les objets du monde de jeu en héritent.
*/

#pragma once

#include <string>
#include <vector>

class ObjetInteractif {
public:
    ObjetInteractif(std::string nom, std::string description, std::vector<std::string> motsCles);
    virtual ~ObjetInteractif() = default;

    const std::string& getNom() const;

    const std::string& getDescription() const;

    bool correspondA(const std::string& terme) const;

    virtual std::string utiliser() = 0;

protected:
    std::string nom_;
    std::string description_;
    std::vector<std::string> motsCles_;
};

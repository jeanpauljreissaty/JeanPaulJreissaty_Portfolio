/*
* Fichier: carte.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la classe Carte représentant l'ensemble des zones du monde de jeu et leurs connexions.
*/

#pragma once

#include "zone.hpp"

#include <memory>
#include <vector>


class Carte {
public:
    Carte();

    Zone* getDepart() const;

private:
    std::vector<std::unique_ptr<Zone>> zones_;
    Zone* depart_ = nullptr;

    
    Zone* creerZone(std::string nom, std::string description, bool eclairee = true);

    
    void initialiserZones();
    void initialiserConnexions();
    void initialiserObjets();
};

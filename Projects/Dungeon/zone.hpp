/*
* Fichier: zone.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la classe Zone représentant une case du monde de jeu (nom, description, connexions, objets, état d'éclairage).
*/

#pragma once

#include "direction.hpp"
#include "objetinteractif.hpp"

#include <map>
#include <memory>
#include <string>
#include <vector>

class Zone {
public:
    Zone(std::string nom, std::string description, bool eclairee = true);

    const std::string& getNom() const;
    const std::string& getDescription() const;
    bool estEclairee() const;
    void setEclairee(bool eclairee);

    
    void  connecter(Direction dir, Zone* voisin);

    Zone* getVoisin(Direction dir) const;

   
    const std::map<Direction, Zone*>& getConnexions() const;

   
    void ajouterObjet(std::unique_ptr<ObjetInteractif> objet);

  
    ObjetInteractif* trouverObjet(const std::string& terme) const;

    const std::vector<std::unique_ptr<ObjetInteractif>>& getObjets() const;

private:
    std::string nom_;
    std::string description_;
    bool eclairee_;

    std::map<Direction, Zone*> connexions_;
    std::vector<std::unique_ptr<ObjetInteractif>> objets_;
};

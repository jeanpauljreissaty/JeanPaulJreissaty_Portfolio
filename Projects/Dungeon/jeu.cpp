/*
* Fichier: jeu.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la classe Jeu (logique, affichage, aiguillage des commandes).
*/

#include "jeu.hpp"
#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>


Jeu::Jeu() : etat_(carte_.getDepart())
{
    initialiserCommandes();
}



void Jeu::lancer() {

    afficherBanniere();

    afficherZone(etat_.getZoneActuelle());

    while (enCours_) {
        std::cout << "\n> ";
        std::string ligne;

        if (!std::getline(std::cin, ligne)) {

            enCours_ = false;
            break;
        }
        traiterLigne(ligne);
    }
}


void Jeu::initialiserCommandes() {
    
    commandes_["n"] = [this](const std::string& a) { cmdNaviguer(Direction::Nord, a); };
    commandes_["north"] = [this](const std::string& a) { cmdNaviguer(Direction::Nord, a); };
    commandes_["s"] = [this](const std::string& a) { cmdNaviguer(Direction::Sud, a); };
    commandes_["south"] = [this](const std::string& a) { cmdNaviguer(Direction::Sud, a); };
    commandes_["e"] = [this](const std::string& a) { cmdNaviguer(Direction::Est, a); };
    commandes_["east"] = [this](const std::string& a) { cmdNaviguer(Direction::Est, a); };
    commandes_["w"] = [this](const std::string& a) { cmdNaviguer(Direction::Ouest, a); };
    commandes_["west"] = [this](const std::string& a) { cmdNaviguer(Direction::Ouest, a); };

   
    commandes_["look"] = [this](const std::string& a) { cmdLook(a); };
    commandes_["use"] = [this](const std::string& a) { cmdUse(a); };

   
    commandes_["exit"] = [this](const std::string& a) { cmdQuitter(a); };
    commandes_["quit"] = [this](const std::string& a) { cmdQuitter(a); };
}



void Jeu::afficherBanniere() const {
    std::cout << ">>>>> INF1015 DUNGEON CRAWLER 2026 <<<<<\n";
    std::cout << "> > > > GAME OF THE YEAR EDITION < < < <\n";
}

void Jeu::afficherZone(const Zone* zone) const {
    std::cout << "\n-- " << zone->getNom() << " --\n";

    if (!zone->estEclairee()) {
       
        std::cout << "It is near pitch black and you cannot discern any details. "
                     "You can only see the access to adjacent areas.\n";
    } else {
        std::cout << zone->getDescription() << "\n";

        
        const auto& objets = zone->getObjets();

        if (!objets.empty()) {
            std::cout << "You notice :\n";

            for (const auto& objet : objets)
                std::cout << "    " << objet->getNom() << "\n";
        }
    }

    
    for (const auto& [dir, voisin] : zone->getConnexions())

        std::cout << voisin->getNom() << " is to the "
                  << nomDirection(dir) << " (" << abrevDirection(dir) << ")\n";
}



void Jeu::traiterLigne(const std::string& ligne) {
    std::istringstream flux(ligne);
    std::string motCommande;
    flux >> motCommande;

    if (motCommande.empty())
        return;

    
    std::string args;

    std::getline(flux, args);
    size_t debut = args.find_first_not_of(" \t");
    args = (debut != std::string::npos) ? args.substr(debut) : "";

    args = normaliser(args);

   
    auto it = commandes_.find(normaliser(motCommande));

    if (it != commandes_.end())
        it->second(args);

    else
        std::cout << "I do not know that.\n";
}



void Jeu::cmdNaviguer(Direction dir, const std::string& /*args*/) {
    Zone* destination = etat_.getZoneActuelle()->getVoisin(dir);

    if (destination == nullptr) {

        std::cout << "Cannot go there.\n";
        return;
    }

    std::cout << "Going " << nomDirection(dir) << "\n";
    etat_.deplacerVers(destination);
    afficherZone(destination);
}

void Jeu::cmdLook(const std::string& args) {
    if (args.empty()) {
        
        afficherZone(etat_.getZoneActuelle());
        return;
    }

    
    Zone* zone  = etat_.getZoneActuelle();

    if (!zone->estEclairee()) {          
        std::cout << "It is too dark to see anything.\n";
        return;
    }

    ObjetInteractif* objet = zone->trouverObjet(args);

    if (objet == nullptr) {
        std::cout << "There is nothing like that here.\n";
        return;
    }

    std::cout << objet->getDescription() << "\n";
}

void Jeu::cmdUse(const std::string& args) {
    if (args.empty()) {
        std::cout << "The 'use' command requires an object name or keyword.\n";
        return;
    }

    Zone* zone = etat_.getZoneActuelle();

    if (!zone->estEclairee()) {         
        std::cout << "It is too dark to find anything.\n";
        return;
    }

    ObjetInteractif* objet = zone->trouverObjet(args);

    if (objet == nullptr) {
        std::cout << "There is nothing like that here.\n";
        return;
    }

    
    std::cout << objet->utiliser() << "\n";
}

void Jeu::cmdQuitter(const std::string& /*args*/) {
    std::cout << "\nOk game done now, go away!\n";
    enCours_ = false;
}



std::string Jeu::normaliser(std::string s) {
    std::transform(s.begin(), s.end(), s.begin(),
        [](unsigned char c) { return static_cast<char>(std::tolower(c)); });
    return s;
}

/*
* Fichier: jeu.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la classe Jeu qui gère la logique, l'affichage et l'aiguillage des commandes du joueur.
*/

#pragma once

#include "carte.hpp"
#include "etatjeu.hpp"

#include <functional>
#include <string>
#include <unordered_map>

class Jeu {
public:
    Jeu();
    void lancer();

private:
    using CommandeFunc = std::function<void(const std::string&)>;

    Carte carte_;
    EtatJeu etat_;
    bool enCours_ = true;

    
    std::unordered_map<std::string, CommandeFunc> commandes_;

    void initialiserCommandes();

    
    void afficherBanniere() const;
    void afficherZone(const Zone* z) const;

    
    void traiterLigne(const std::string& ligne);

    
    void cmdNaviguer(Direction dir, const std::string& args);

    void cmdLook (const std::string& args);

    void cmdUse (const std::string& args);

    void cmdQuitter (const std::string& args);

    
    static std::string normaliser(std::string s);
};

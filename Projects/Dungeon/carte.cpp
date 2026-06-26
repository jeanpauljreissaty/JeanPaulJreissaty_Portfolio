/*
* Fichier: carte.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la classe Carte. Toutes les données du monde (zones, connexions, objets) sont isolées dans les trois méthodes d'initialisation.
*/

#include "carte.hpp"
#include "objetdeverrouillage.hpp"
#include "objeteclairage.hpp"
#include "objetsimple.hpp"

#include <memory>


Carte::Carte() {
    initialiserZones();
    initialiserConnexions();
    initialiserObjets();
}   

Zone* Carte::getDepart() const {
    return depart_;
}


Zone* Carte::creerZone(std::string nom, std::string description, bool eclairee) {
    zones_.push_back(std::make_unique<Zone>(std::move(nom), std::move(description), eclairee));
    return zones_.back().get();
}



void Carte::initialiserZones() {
    
    creerZone("Foyer",
        "This is the entrance of the house. There is a sturdy carpet on the floor.");

    
    creerZone("Main Hallway",
        "This is the main hallway. There is a bunch of boxes against the wall.");

    
    creerZone("Kitchen",
        "This is the kitchen. The smell of old coffee lingers in the air.");

    
    creerZone("Small Bedroom",
        "This is the small bedroom. It is not particularly clean or well organised. "
        "There is a small window.");

    
    creerZone("Bathroom",
        "A cramped bathroom with a cracked mirror above the sink.");

   
    creerZone("Living Room",
        "This is the living room. There is a computer desk with cameras and a "
        "bluescreen. Next to it is a TV and a couch.",
        false);

    
    creerZone("Room R",
        "This is a strange room with red walls. The air feels heavy.");

    depart_ = zones_[0].get();
}

void Carte::initialiserConnexions() {
    
    Zone* foyer = zones_[0].get();
    Zone* couloir = zones_[1].get();
    Zone* cuisine = zones_[2].get();
    Zone* pChambre = zones_[3].get();
    Zone* sdBains = zones_[4].get();
    Zone* salon = zones_[5].get();
    

    // (N/S)
    foyer->connecter(Direction::Nord, couloir);
    couloir->connecter(Direction::Sud, foyer);

    // (E/W)
    foyer->connecter(Direction::Est, salon);
    salon->connecter(Direction::Ouest, foyer);

    // (N/S)
    couloir->connecter(Direction::Nord, cuisine);
    cuisine->connecter(Direction::Sud, couloir);

    //(W/E)
    couloir->connecter(Direction::Ouest, pChambre);
    pChambre->connecter(Direction::Est, couloir);

    // (S/N) 
    pChambre->connecter(Direction::Sud, sdBains);
    sdBains->connecter(Direction::Nord, pChambre);

    //  (E/W)          
    cuisine->connecter(Direction::Est, sdBains);
    sdBains->connecter(Direction::Ouest, cuisine);

  
}

void Carte::initialiserObjets() {
    Zone* foyer = zones_[0].get();
    Zone* couloir = zones_[1].get();
    Zone* cuisine = zones_[2].get();
    Zone* salon = zones_[5].get();
    Zone* salleR = zones_[6].get();

    //  Foyer 
    foyer->ajouterObjet(std::make_unique<ObjetSimple>(
        "A pair of old shoes",
        "A worn-out pair of men's shoes sitting by the door.",
        std::vector<std::string>{"shoes", "shoe"},
        "You try on the shoes. They fit surprisingly well."
    ));

    //  Couloir 
    couloir->ajouterObjet(std::make_unique<ObjetEclairage>(
        "A light switch",
        "A standard light switch mounted on the wall.",
        std::vector<std::string>{"switch", "light"},
        salon
    ));

    //  Cuisine 
    cuisine->ajouterObjet(std::make_unique<ObjetSimple>(
        "A cookbook",
        "A thick cookbook with many recipe stains on the pages.",
        std::vector<std::string>{"cookbook", "book", "cook"},
        "You flip through the cookbook. You feel hungry."
    ));

    //  Salon 
   
    salon->ajouterObjet(std::make_unique<ObjetDeverrouillage>(
        "A red button",
        "A large, ominous red button mounted on the wall.",
        std::vector<std::string>{"button", "red"},
        couloir, Direction::Est,
        salleR, Direction::Ouest
    ));

    salon->ajouterObjet(std::make_unique<ObjetSimple>(
        "A cheap electric piano",
        "This is an old entry-level Yamaha with 61 keys. "
        "It looks like any cheap stuff from the late 90s.",
        std::vector<std::string>{"piano", "electric", "yamaha"},
        "You play some chords on the piano. It does not sound very well."
    ));

    // Salle R 
    salleR->ajouterObjet(std::make_unique<ObjetSimple>(
        "A mysterious note",
        "A crumpled piece of paper with barely readable handwriting: 'They were here.'",
        std::vector<std::string>{"note", "paper"},
        "You read the note again. It sends a chill down your spine."
    ));
}

/*
* Fichier: direction.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation des fonctions utilitaires de direction.
*/

#include "direction.hpp"

std::string nomDirection(Direction dir) {
    switch (dir) {
    case Direction::Nord: return "North";
    case Direction::Est: return "East";
    case Direction::Sud: return "South";
    case Direction::Ouest: return "West";
    }

    return "";
}

std::string abrevDirection(Direction dir) {
    switch (dir) {
    case Direction::Nord: return "N";
    case Direction::Est: return "E";
    case Direction::Sud: return "S";
    case Direction::Ouest: return "W";
    }

    return "";
}

Direction directionOpposee(Direction dir) {
    switch (dir) {
    case Direction::Nord: return Direction::Sud;
    case Direction::Sud: return Direction::Nord;
    case Direction::Est: return Direction::Ouest;
    case Direction::Ouest: return Direction::Est;
    }

    return dir;
}

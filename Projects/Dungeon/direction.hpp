/*
* Fichier: direction.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration du type énuméré Direction et des fonctions de conversion associées.
*/

#pragma once

#include <string>


enum class Direction { Nord, Est, Sud, Ouest };


std::string nomDirection(Direction dir);
std::string abrevDirection(Direction dir);

Direction directionOpposee(Direction dir);

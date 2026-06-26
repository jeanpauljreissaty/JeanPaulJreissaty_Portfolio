/*
* Fichier: article.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration de la structure Article.
*/


#pragma once

#include <string>

struct Article {
    std::string description;
    double prix = 0.0;
    bool taxable = false;
};

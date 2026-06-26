/*
* Fichier: modele.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Déclaration du modèle de caisse enregistreuse.
*/



#pragma once

#include "article.hpp"
#include <QObject>
#include <stdexcept>
#include <vector>




class DescriptionVideException : public std::invalid_argument {
public:
    DescriptionVideException() : invalid_argument("La description ne peut pas etre vide.") {}
};


class PrixNulException : public std::invalid_argument {
public:
    PrixNulException() : std::invalid_argument("Le prix ne peut pas etre nul ou invalide.") {}
};


class CaisseModele : public QObject {
    Q_OBJECT

public:
    static constexpr double TAUX_TAXES = 0.14975;

    explicit CaisseModele(QObject* parent = nullptr);

    void ajouterArticle(const std::string& description, double prix, bool taxable);

  
    void retirerArticles(const std::vector<Article>& articlesARetirer);

    
    void reinitialiser();

    double calculerSousTotal() const;
    double calculerTaxes() const;
    double calculerTotal() const;

    const std::vector<Article>& getArticles() const;

signals:
   
    void commandeModifiee();

private:
    std::vector<Article> articles_;
    double sousTotal_ = 0.0;
};

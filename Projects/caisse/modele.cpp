/*
* Fichier: modele.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation du modèle de caisse enregistreuse.
*/



#include "modele.hpp"

#include <algorithm>
#include <numeric>

CaisseModele::CaisseModele(QObject* parent) : QObject(parent) {}

void CaisseModele::ajouterArticle(const std::string& description, double prix, bool taxable)
{
    if (description.empty())
        throw DescriptionVideException{};
    if (prix == 0.0)
        throw PrixNulException{};

    articles_.push_back({description, prix, taxable});
    sousTotal_ += prix;
    emit commandeModifiee();
}

void CaisseModele::retirerArticles(const std::vector<Article>& articlesARetirer) {
    for (const Article& aRetirer : articlesARetirer) {
        
        auto it = std::find_if(articles_.begin(), articles_.end(),
            [&aRetirer](const Article& a) {
                return a.description == aRetirer.description && a.prix == aRetirer.prix && a.taxable == aRetirer.taxable; });

        if (it != articles_.end())
            sousTotal_ -= it->prix;
            articles_.erase(it);
    }
    emit commandeModifiee();
}

void CaisseModele::reinitialiser() {
    articles_.clear();
    sousTotal_ = 0.0;
    emit commandeModifiee();
}

double CaisseModele::calculerSousTotal() const {
        return sousTotal_;
       
}

double CaisseModele::calculerTaxes() const {
    
    return std::accumulate(articles_.begin(), articles_.end(), 0.0, [](double acc, const Article& a) {
            return acc + (a.taxable ? a.prix * CaisseModele::TAUX_TAXES : 0.0);
        });
}

double CaisseModele::calculerTotal() const {
    return calculerSousTotal() + calculerTaxes();
}

const std::vector<Article>& CaisseModele::getArticles() const {
    return articles_;
}

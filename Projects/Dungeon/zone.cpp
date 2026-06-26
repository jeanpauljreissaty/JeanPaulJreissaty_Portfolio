/*
* Fichier: zone.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la classe Zone.
*/

#include "zone.hpp"

#include <algorithm>

Zone::Zone(std::string nom, std::string description, bool eclairee) : nom_(std::move(nom)) , description_(std::move(description)) , eclairee_(eclairee) {}

const std::string& Zone::getNom() const { return nom_; }
const std::string& Zone::getDescription() const { return description_; }

bool Zone::estEclairee() const { return eclairee_; }
void Zone::setEclairee(bool e) { eclairee_ = e; }

void Zone::connecter(Direction dir, Zone* voisin) {
    connexions_[dir] = voisin;
}

Zone* Zone::getVoisin(Direction dir) const {
    auto it = connexions_.find(dir);

    return (it != connexions_.end()) ? it->second : nullptr;
}

const std::map<Direction, Zone*>& Zone::getConnexions() const {
    return connexions_;
}

void Zone::ajouterObjet(std::unique_ptr<ObjetInteractif> objet) {

    objets_.push_back(std::move(objet));
}

ObjetInteractif* Zone::trouverObjet(const std::string& terme) const {
    auto it = std::find_if(objets_.begin(), objets_.end(),

        [&terme](const std::unique_ptr<ObjetInteractif>& objet) {
            return objet->correspondA(terme);
        });
    return (it != objets_.end()) ? it->get() : nullptr;
}

const std::vector<std::unique_ptr<ObjetInteractif>>& Zone::getObjets() const {
    return objets_;
}

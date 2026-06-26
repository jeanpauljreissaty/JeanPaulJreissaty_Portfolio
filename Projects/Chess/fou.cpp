/*
* Fichier: fou.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation du fou d'un jeu d'echec.
*/

#include "fou.hpp"
#include <cmath>

namespace logique {
	Fou::Fou(Couleur couleur, int x, int y) : Piece(couleur, x, y) {}
	bool Fou::estMouvementValide(int newX, int newY) const {
		int deltaX = std::abs(newX - x);
		int deltaY = std::abs(newY - y);

		if (deltaX == deltaY && deltaX > 0) {
			return true;
		}

		return false;
	}
	QString Fou::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♗" : "♝";
	}
}
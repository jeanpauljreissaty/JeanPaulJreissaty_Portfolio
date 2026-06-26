/*
* Fichier: pion.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la piece pion d'un jeu d'echec.
*/

#include "pion.hpp"
#include <cmath>

namespace logique {
	Pion::Pion(Couleur couleur, int x, int y) : Piece(couleur, x, y), estPremierMouvement(true) {}

	bool Pion::estMouvementValide(int newX, int newY) const {
		int deltaX = newX - x;
		int deltaY = newY - y;
		
		int direction = (couleur == Couleur::Blanc) ? -1 : 1;

		if (deltaX == 0 && deltaY == direction) {
			return true;
		}

		if (estPremierMouvement && deltaX == 0 && deltaY == 2 * direction) {
			return true;
		}

		if (std::abs(deltaX) == 1 && deltaY == direction) {
			return true;
		}

		return false;
	}

	void Pion::setPosition(int newX, int newY) {
		Piece::setPosition(newX, newY);
		estPremierMouvement = false;
	}

	QString Pion::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♙" : "♟";
	}
}
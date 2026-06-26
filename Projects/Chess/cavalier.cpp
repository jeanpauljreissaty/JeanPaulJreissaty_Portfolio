/*
* Fichier: cavalier.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la piece cavalier d'un jeu d'echec.
*/

#include "cavalier.hpp"
#include <cmath>

namespace logique {
	Cavalier::Cavalier(Couleur couleur, int x, int y) : Piece(couleur, x, y) {}

	bool Cavalier::estMouvementValide(int newX, int newY) const {
		int deltaX = std::abs(newX - x);
		int deltaY = std::abs(newY - y);

		return (deltaX == 1 && deltaY == 2) || (deltaX == 2 && deltaY == 1);
	}

	bool Cavalier::sauteParDessus() const {
		return true;
	}

	QString Cavalier::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♘" : "♞";
	}
}

/*
* Fichier: reine.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la piece reine d'un jeu d'echec.
*/

#include "reine.hpp"

namespace logique {
	Reine::Reine(Couleur couleur, int x, int y) : Piece(couleur, x, y) {}

	bool Reine::estMouvementValide(int newX, int newY) const {
		int deltaX = std::abs(newX - x);
		int deltaY = std::abs(newY - y);

		bool mouvementTour = (deltaX == 0 || deltaY == 0);

		bool mouvementFou = (deltaX == deltaY);

		return mouvementTour || mouvementFou;
	}

	QString Reine::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♕" : "♛";
	}
}

/*
* Fichier: tour.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la piece tour d'un jeu d'echec.
*/

#include "tour.hpp"

namespace logique {
	Tour::Tour(Couleur couleur, int x, int y) : Piece(couleur, x, y) {}

	bool Tour::estMouvementValide(int newX, int newY) const {
		bool memeColonne = (newX == x) && (newY != y);
		bool memeLigne   = (newY == y) && (newX != x);

		return memeColonne || memeLigne;
	}

	QString Tour::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♖" : "♜";
	}
}

/*
* Fichier: tour.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la piece tour d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Tour : public Piece {
	public:
		Tour(Couleur couleur, int x, int y);
		~Tour() override = default;

		bool estMouvementValide(int newX, int newY) const override;
		QString getSymbole() const override;
	};
}

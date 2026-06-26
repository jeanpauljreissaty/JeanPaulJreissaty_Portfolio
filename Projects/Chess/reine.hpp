/*
* Fichier: reine.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la piece reine d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Reine : public Piece {
	public:
		Reine(Couleur couleur, int x, int y);
		~Reine() override = default;

		bool estMouvementValide(int newX, int newY) const override;
		QString getSymbole() const override;
	};
}

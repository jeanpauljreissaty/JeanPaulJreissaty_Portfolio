/*
* Fichier: fou.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: fichier d'en tete de l'Implementation du fou d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Fou : public Piece {
	public:
		Fou(Couleur couleur, int x, int y);
		~Fou() override = default;

		bool estMouvementValide(int newX, int newY) const override;
		QString getSymbole() const override;
	};
}

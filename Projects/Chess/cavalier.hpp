/*
* Fichier: cavalier.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la piece cavalier d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Cavalier : public Piece {
	public:
		Cavalier(Couleur couleur, int x, int y);
		~Cavalier() override = default;

		bool estMouvementValide(int newX, int newY) const override;
		bool sauteParDessus() const override;
		QString getSymbole() const override;
	};
}

/*
* Fichier: pion.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la piece pion d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Pion : public Piece {

	public:
		Pion(Couleur couleur, int x, int y);
		~Pion() override = default;

		bool estMouvementValide(int newX, int newY) const override;
		void setPosition(int newX, int newY) override;
		void marquerJouee() override { estPremierMouvement = false; }
		QString getSymbole() const override;

	private:
		bool estPremierMouvement;
	};
}
/*
* Fichier: roi.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la piece roi d'un jeu d'echec.
*/

#pragma once
#include "piece.hpp"

namespace logique {
	class Roi : public Piece {
	private:
		static int nRois;
	public:
		Roi(Couleur couleur, int x, int y); 
		~Roi() override; 
		bool estMouvementValide(int newX, int newY) const override; 
		QString getSymbole() const override;
	};
}
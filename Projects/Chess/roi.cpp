/*
* Fichier: roi.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la piece roi d'un jeu d'echec.
*/

#include "roi.hpp"
#include "roiException.hpp"
#include <cmath>

namespace logique {

	int Roi::nRois =0;

	Roi::Roi(Couleur couleur, int x, int y) : Piece(couleur, x, y) {
		nRois++;
		if (nRois > N_ROIS_MAX) {
			nRois--;
			throw RoiException("Erreur : Impossible d'avoir plus de 2 rois sur l'echiquier.");
		}
	}
	Roi::~Roi() {
		nRois--;
	}
	bool Roi::estMouvementValide(int newX, int newY) const {
		int deltaX = std::abs(newX - x);
		int deltaY = std::abs(newY - y);
		return (deltaX <= 1 && deltaY <= 1) && !(deltaX == 0 && deltaY == 0);
	}

	QString Roi::getSymbole() const {
		return (couleur == Couleur::Blanc) ? "♔" : "♚";
	}
}
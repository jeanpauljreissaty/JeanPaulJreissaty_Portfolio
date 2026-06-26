
/*
* Fichier: jeu.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: ficher d'en-tete Implementation de la logique pour un jeu d'echec.
*/
#pragma once
#include <array>
#include <memory>
#include "piece.hpp"

namespace logique {

	enum class PositionDepart {
		PartieComplete,
		FinPartieClassique,
		RoiEtTourVsRoi,
		RoiEtReineVsRoi
	};

	class Jeu {

	public:
		Jeu();
		~Jeu() = default;

		const Piece* getPiece(int x, int y) const;

		bool jouerCoup(int x1, int y1, int x2, int y2);
		bool roiEstEnEchec(Couleur couleur) const;
		bool cheminLibre(int x1, int y1, int x2, int y2) const;
		bool roiEstEnEchecEtMat(Couleur couleur);

		void reinitialiser(PositionDepart position);

	private:
		// on va utiliser une simple liste au lieu d'une liste 2D
		std::array<std::unique_ptr<Piece>, N_CASES> plateau;

		Couleur tourActuel;

		int getIndex(int x, int y) const {
			return y * TAILLE_PLATEAU + x;
		}

	
	};
}
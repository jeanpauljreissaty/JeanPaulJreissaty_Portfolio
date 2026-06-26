/*
* Fichier: deplacement.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en-tete de l'implementation de la logique de deplacement pour un jeu d'echec.
*/

#pragma once
#include <array>
#include <memory>
#include "Piece.hpp"


namespace logique {
	class Deplacement {

	public:
		Deplacement(int indexDepart, int indexArrivee, std::array<std::unique_ptr<Piece>, N_CASES>& plateau);
		~Deplacement();

	private:
		std::array<std::unique_ptr<Piece>, N_CASES>& plateauReference;
		int indexDepart;
		int indexArrivee;
		std::unique_ptr<Piece> pieceCapturee;

	};
}
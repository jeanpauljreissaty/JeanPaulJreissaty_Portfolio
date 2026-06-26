/*
* Fichier: deplacement.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la logique de deplacement pour un jeu d'echec.
*/

#include "deplacement.hpp"

namespace logique {
	Deplacement::Deplacement(int indexDepart, int indexArrivee, std::array<std::unique_ptr<Piece>, N_CASES>& plateau)
		: plateauReference(plateau), indexDepart(indexDepart), indexArrivee(indexArrivee) {

		pieceCapturee = std::move(plateau.at(indexArrivee));
		plateau.at(indexArrivee) = std::move(plateau.at(indexDepart));

		if (plateauReference.at(indexArrivee) != nullptr) {
			plateauReference.at(indexArrivee)->setPosition(indexArrivee % TAILLE_PLATEAU, indexArrivee / TAILLE_PLATEAU);
		}
	}

	Deplacement::~Deplacement() {
		plateauReference.at(indexDepart) = std::move(plateauReference.at(indexArrivee));

		if (plateauReference.at(indexDepart) != nullptr) {
			plateauReference.at(indexDepart)->setPosition(indexDepart % TAILLE_PLATEAU, indexDepart / TAILLE_PLATEAU);
		}

		plateauReference.at(indexArrivee) = std::move(pieceCapturee);
	}
}
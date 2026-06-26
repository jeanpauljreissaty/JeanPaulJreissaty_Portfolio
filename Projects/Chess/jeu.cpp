/*
* Fichier: jeu.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la logique pour un jeu d'echec.
*/

#include "jeu.hpp"
#include "roi.hpp"
#include "fou.hpp"
#include "pion.hpp"
#include "tour.hpp"
#include "cavalier.hpp"
#include "reine.hpp"
#include "deplacement.hpp"

namespace logique {

	Jeu::Jeu() : tourActuel(Couleur::Blanc) {
		reinitialiser(PositionDepart::PartieComplete);
	}

	const Piece* Jeu::getPiece(int x, int y) const {
		return plateau[getIndex(x, y)].get();
	}

	bool Jeu::jouerCoup(int x1, int y1, int x2, int y2) {
		int indexDepart = getIndex(x1, y1);
		int indexArrivee = getIndex(x2, y2);
		Piece* piece = plateau.at(indexDepart).get();

		if (piece == nullptr) {
			return false;
		}

		if (piece->getCouleur() != tourActuel) {
			return false;
		}

		if (!piece->estMouvementValide(x2, y2)) {
			return false;
		}

		if (!piece->sauteParDessus() && !cheminLibre(x1, y1, x2, y2)) {
			return false;
		}

		Piece* pieceArrivee = plateau.at(indexArrivee).get();
		if (pieceArrivee != nullptr && pieceArrivee->getCouleur() == tourActuel) {
			return false;
		}

		if (dynamic_cast<Pion*>(piece) != nullptr) {
			bool toutDroit = (x1 == x2);
			if (toutDroit) {
				if (pieceArrivee != nullptr) return false;
			}
			else {
				if (pieceArrivee == nullptr) return false;
			}
		}

		// RAII
		{
			Deplacement simulation(indexDepart, indexArrivee, plateau);

			if (roiEstEnEchec(tourActuel)) {
				return false;
			}
		}

		plateau.at(indexArrivee) = std::move(plateau.at(indexDepart));
		if (plateau.at(indexArrivee)) {
			plateau.at(indexArrivee)->setPosition(x2, y2);
			plateau.at(indexArrivee)->marquerJouee();
		}

		tourActuel = (tourActuel == Couleur::Blanc) ? Couleur::Noir : Couleur::Blanc;

		return true;
	}

	bool Jeu::roiEstEnEchec(Couleur couleur) const {
		int roiX = POSITION_INVALIDE, roiY = POSITION_INVALIDE;

		for (int i = 0; i < N_CASES; ++i) {
			const Piece* p = plateau[i].get();
			if (p != nullptr && p->getCouleur() == couleur && p->getSymbole() == (couleur == Couleur::Blanc ? "♔" : "♚")) {
				roiX = p->getX();
				roiY = p->getY();
				break;
			}
		}

		if (roiX == POSITION_INVALIDE) {
			return false;
		}

		for (int i = 0; i < N_CASES; ++i) {
			const Piece* p = plateau[i].get();
			if (p != nullptr && p->getCouleur() != couleur) {
				if (p->estMouvementValide(roiX, roiY)) {
					if (p->sauteParDessus() || cheminLibre(p->getX(), p->getY(), roiX, roiY)) {
						return true;
					}
				}

			}
		}

		return false;
	}

	bool Jeu::roiEstEnEchecEtMat(Couleur couleur) {
		if (!roiEstEnEchec(couleur)) {
			return false;
		}

		for (int x = 0; x < TAILLE_PLATEAU; ++x) {
			for (int y = 0; y < TAILLE_PLATEAU; ++y) {
				const Piece* p = getPiece(x, y);
				if (p != nullptr && p->getCouleur() == couleur) {
					for (int newX = 0; newX < TAILLE_PLATEAU; ++newX) {
						for (int newY = 0; newY < TAILLE_PLATEAU; ++newY) {
							if (!p->estMouvementValide(newX, newY)) continue;
							if (!p->sauteParDessus() && !cheminLibre(x, y, newX, newY)) continue;
							const Piece* pieceArrivee = getPiece(newX, newY);
							if (pieceArrivee != nullptr && pieceArrivee->getCouleur() == couleur) continue;
							if (dynamic_cast<const Pion*>(p) != nullptr) {
								bool toutDroit = (x == newX);
								if (toutDroit) {
									if (pieceArrivee != nullptr) continue; 
								}
								else {
									if (pieceArrivee == nullptr) continue;
								}
							}
							{
								Deplacement simulation(getIndex(x, y), getIndex(newX, newY), plateau);

								if (!roiEstEnEchec(couleur)) {
									return false; 
								}
							}
						}
					}
				}
			}
		}

		return true;
	}

	bool Jeu::cheminLibre(int x1, int y1, int x2, int y2) const {
		int deltaX = x2 - x1;
		int deltaY = y2 - y1;

		int stepX = (deltaX > 0) ? 1 : ((deltaX < 0) ? -1 : 0);
		int stepY = (deltaY > 0) ? 1 : ((deltaY < 0) ? -1 : 0);

		int courantX = x1 + stepX;
		int courantY = y1 + stepY;

		while (courantX != x2 || courantY != y2) {
			if (getPiece(courantX, courantY) != nullptr) {
				return false;
			}
			courantX += stepX;
			courantY += stepY;
		}

		return true;
	}


	void Jeu::reinitialiser(PositionDepart position) {
		for (auto& p : plateau)
			p = nullptr;
		tourActuel = Couleur::Blanc;

		if (position == PositionDepart::PartieComplete) {
			// Plateau complet
			plateau[getIndex(4, 0)] = std::make_unique<Roi>(Couleur::Noir, 4, 0);
			plateau[getIndex(3, 0)] = std::make_unique<Reine>(Couleur::Noir, 3, 0);
			plateau[getIndex(2, 0)] = std::make_unique<Fou>(Couleur::Noir, 2, 0);
			plateau[getIndex(5, 0)] = std::make_unique<Fou>(Couleur::Noir, 5, 0);
			plateau[getIndex(0, 0)] = std::make_unique<Tour>(Couleur::Noir, 0, 0);
			plateau[getIndex(7, 0)] = std::make_unique<Tour>(Couleur::Noir, 7, 0);
			plateau[getIndex(1, 0)] = std::make_unique<Cavalier>(Couleur::Noir, 1, 0);
			plateau[getIndex(6, 0)] = std::make_unique<Cavalier>(Couleur::Noir, 6, 0);
			for (int i = 0; i < TAILLE_PLATEAU; ++i)
				plateau[getIndex(i, 1)] = std::make_unique<Pion>(Couleur::Noir, i, 1);

			plateau[getIndex(4, 7)] = std::make_unique<Roi>(Couleur::Blanc, 4, 7);
			plateau[getIndex(3, 7)] = std::make_unique<Reine>(Couleur::Blanc, 3, 7);
			plateau[getIndex(2, 7)] = std::make_unique<Fou>(Couleur::Blanc, 2, 7);
			plateau[getIndex(5, 7)] = std::make_unique<Fou>(Couleur::Blanc, 5, 7);
			plateau[getIndex(0, 7)] = std::make_unique<Tour>(Couleur::Blanc, 0, 7);
			plateau[getIndex(7, 7)] = std::make_unique<Tour>(Couleur::Blanc, 7, 7);
			plateau[getIndex(1, 7)] = std::make_unique<Cavalier>(Couleur::Blanc, 1, 7);
			plateau[getIndex(6, 7)] = std::make_unique<Cavalier>(Couleur::Blanc, 6, 7);
			for (int i = 0; i < TAILLE_PLATEAU; ++i)
				plateau[getIndex(i, 6)] = std::make_unique<Pion>(Couleur::Blanc, i, 6);
		}
		else {
			// Toujours 2 rois
			plateau[getIndex(4, 0)] = std::make_unique<Roi>(Couleur::Noir, 4, 0);
			plateau[getIndex(4, 7)] = std::make_unique<Roi>(Couleur::Blanc, 4, 7);

			if (position == PositionDepart::RoiEtTourVsRoi) {
				plateau[getIndex(0, 7)] = std::make_unique<Tour>(Couleur::Blanc, 0, 7);
			}
			else if (position == PositionDepart::RoiEtReineVsRoi) {
				plateau[getIndex(3, 7)] = std::make_unique<Reine>(Couleur::Blanc, 3, 7);
			}
			else {
				// FinPartieClassique : roi + tour + cavalier vs roi
				plateau[getIndex(0, 7)] = std::make_unique<Tour>(Couleur::Blanc, 0, 7);
				plateau[getIndex(1, 7)] = std::make_unique<Cavalier>(Couleur::Blanc, 1, 7);
			}
		}
	}
}
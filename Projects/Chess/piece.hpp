/*
* Fichier: piece.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: fichier d'en-tete d'une classe abstraite des pieces. Tout les pieces vont heriter.
*/

#pragma once
#include <QString>

inline constexpr int N_CASES = 64;
inline constexpr int TAILLE_PLATEAU = 8;
inline constexpr int TAILLE_CASE_PX = 80;
inline constexpr int N_ROIS_MAX = 2;
inline constexpr int N_COULEURS_CASES = 2;
inline constexpr int POSITION_INVALIDE = -1;

namespace logique {
	
	enum class Couleur {
		Blanc,
		Noir
	};

	class Piece {
	public:
		Piece(Couleur couleur, int x, int y) : couleur(couleur), x(x), y(y) {}

		virtual ~Piece() = default;

		virtual bool estMouvementValide(int newX, int newY) const = 0;
		virtual bool sauteParDessus() const { return false; }
		virtual void marquerJouee() {}
		virtual QString getSymbole() const = 0;

		Couleur getCouleur() const { return couleur; }
		int getX() const { return x; }
		int getY() const { return y; }
		virtual void setPosition(int newX, int newY) { x = newX; y = newY; }
	
	protected:
		Couleur couleur;
		int x;
		int y;
	};
}

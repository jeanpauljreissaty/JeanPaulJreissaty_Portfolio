/*
* Fichier: Echequier.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Fichier d'en tete de l'implementation de la creation et rafraichissement de l'interface graphique pour un jeu d'echec.
*/

#pragma once
#include <QWidget>
#include <QGridLayout>
#include <QPushButton>
#include <QComboBox>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>

#include "jeu.hpp"

namespace application {
	class Echiquier : public QWidget {
		Q_OBJECT
	

	public:
		Echiquier(QWidget* parent = nullptr);

	private slots:
		void caseCliquee(int x, int y);
		void nouvellePartie();

	private:
		QGridLayout* layoutGrille;
		QPushButton* casesBouton[8][8];
		QComboBox* comboPositions = nullptr;
		QPushButton* boutonNouvellePartie = nullptr;

		logique::Jeu jeu;

		bool pieceSelectionnee = false;
		int departX = POSITION_INVALIDE;
		int departY = POSITION_INVALIDE;

		void rafraichirTableau();

	};
}
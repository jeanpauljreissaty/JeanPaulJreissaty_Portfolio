/*
* Fichier: Echequier.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de la creation et rafraichissement de l'interface graphique pour un jeu d'echec.
*/

#include "roi.hpp"
#include "Echequier.hpp"
#include "roiException.hpp"
#include <QMessageBox>
#include <stdexcept>
#include <QString>


namespace application {
	Echiquier::Echiquier(QWidget* parent) : QWidget(parent) {
		layoutGrille = new QGridLayout();  
		layoutGrille->setSpacing(0);
		layoutGrille->setContentsMargins(0, 0, 0, 0);
		layoutGrille->setSizeConstraint(QLayout::SetFixedSize);

		for (int i = 0; i < TAILLE_PLATEAU; ++i) {
			for (int j = 0; j < TAILLE_PLATEAU; ++j) {
				casesBouton[i][j] = new QPushButton(this);
				casesBouton[i][j]->setFixedSize(TAILLE_CASE_PX, TAILLE_CASE_PX);
				connect(casesBouton[i][j], &QPushButton::clicked, this, [this, j, i]() {
					caseCliquee(j, i);
					});
				layoutGrille->addWidget(casesBouton[i][j], i, j);
			}
		}

		comboPositions = new QComboBox(this);
		comboPositions->addItem("Partie complete",
			static_cast<int>(logique::PositionDepart::PartieComplete));
		comboPositions->addItem("Roi+Tour+Cavalier vs Roi",
			static_cast<int>(logique::PositionDepart::FinPartieClassique));
		comboPositions->addItem("Roi+Tour vs Roi",
			static_cast<int>(logique::PositionDepart::RoiEtTourVsRoi));
		comboPositions->addItem("Roi+Reine vs Roi",
			static_cast<int>(logique::PositionDepart::RoiEtReineVsRoi));

		boutonNouvellePartie = new QPushButton("Nouvelle partie", this);
		connect(boutonNouvellePartie, &QPushButton::clicked, this, &Echiquier::nouvellePartie);

		auto layoutControles = new QHBoxLayout();
		layoutControles->addWidget(comboPositions, 1);
		layoutControles->addWidget(boutonNouvellePartie, 0);

		auto layoutPrincipal = new QVBoxLayout(this);
		layoutPrincipal->addLayout(layoutGrille);
		layoutPrincipal->addLayout(layoutControles);
		setLayout(layoutPrincipal);

		rafraichirTableau();  
	}

	void Echiquier::rafraichirTableau() {
		for (int i = 0; i < TAILLE_PLATEAU; ++i) {
			for (int j = 0; j < TAILLE_PLATEAU; ++j) {
				QString style = "border: none; font-size: 40px; font-weight: bold;";
				if ((i + j) % N_COULEURS_CASES == 0) {
					style += "background-color: #F0D9B5;";
				}
				else {
					style += "background-color: #B58863;";
				}

				if (pieceSelectionnee && departX == j && departY == i) {
					style += "background-color: #FFF000;";
				}

				casesBouton[i][j]->setStyleSheet(style);

				const logique::Piece* piece = jeu.getPiece(j, i);
				if (piece != nullptr) {
					casesBouton[i][j]->setText(piece->getSymbole());
				} else {
					casesBouton[i][j]->setText("");
				}
			}
		}
	}

	void Echiquier::caseCliquee(int x, int y) {
		if (!pieceSelectionnee) {
			const logique::Piece* piece = jeu.getPiece(x, y);
			if (piece != nullptr) {
				pieceSelectionnee = true;
				departX = x;
				departY = y;
			}
		} else {
			if (departX == x && departY == y) {
				pieceSelectionnee = false;
			} else {
				bool coupValide = jeu.jouerCoup(departX, departY, x, y);

				if (!coupValide) {
					QMessageBox::warning(this, "Coup invalide", "Ce coup n'est pas valide !");
				}
				else {
					rafraichirTableau();
					if (jeu.roiEstEnEchecEtMat(logique::Couleur::Blanc)) {
						QMessageBox::information(this, "Échec et mat", "Le roi blanc est en échec et mat. Les noirs gagnent !");
						nouvellePartie();
					}
					else if (jeu.roiEstEnEchecEtMat(logique::Couleur::Noir)) {
						QMessageBox::information(this, "Échec et mat", "Le roi noir est en échec et mat. Les blancs gagnent !");
						nouvellePartie();
					}
				}
				pieceSelectionnee = false;
			}
		}
		rafraichirTableau();
	}

	void Echiquier::nouvellePartie() {
		pieceSelectionnee = false;
		auto positionIndex = static_cast<logique::PositionDepart>(comboPositions->currentData().toInt());
		jeu.reinitialiser(positionIndex);
		rafraichirTableau();
	}
}
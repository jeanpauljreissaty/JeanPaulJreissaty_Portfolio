/*
* Fichier: main.cpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: fichier principal de l'application, qui lance l'interface graphique pour un jeu d'echec.
*/

#include <QApplication>
#include "Echequier.hpp"

int lancerTests();

int main(int argc, char* argv[]) {
	lancerTests();
    QApplication app(argc, argv);
	QCoreApplication::setApplicationName("Echiquier");
	application::Echiquier echiquier;
	echiquier.show();

	return app.exec();
}
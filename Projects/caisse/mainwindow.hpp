/*
* Fichier: mainwindow.hpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Gère l'interface graphique et la communication avec CaisseModele via les signaux Qt. La vue ne modifie jamais directement le modèle en dehors des méthodes dédiées.
*/



#pragma once

#include "modele.hpp"

#include <QCheckBox>
#include <QLabel>
#include <QLineEdit>
#include <QListWidget>
#include <QMainWindow>
#include <QPushButton>


class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);

private slots:
    void surAjout();
    void surRetrait();
    void surReinit();
    void surCommandeModifiee();

private:
    void configurerUI();
    void configurerConnexions();
    void mettreAJourTotaux();
    static QString formaterMontant(double montant);

    
    QLineEdit* ligneDescription_ = nullptr;
    QLineEdit* lignePrix_ = nullptr;
    QCheckBox* caseTaxable_ = nullptr;

    
    QPushButton* boutonAjouter_ = nullptr;
    QPushButton* boutonRetirer_ = nullptr;
    QPushButton* boutonReinit_ = nullptr;

    
    QListWidget* listeArticles_ = nullptr;

    
    QLabel* labelSousTotal_ = nullptr;
    QLabel* labelTaxes_ = nullptr;
    QLabel* labelTotal_ = nullptr;

    CaisseModele modele_;
};

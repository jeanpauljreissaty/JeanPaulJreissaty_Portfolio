/*
* Fichier: mainwindow.cpp
* Auteur: Giorgio Ghalbouni (2448189) et Jean-Paul Jreissaty (2462433)
* Description: Implémentation de la fenêtre principale.
*/



#include "mainwindow.hpp"

#include <QFormLayout>
#include <QGroupBox>
#include <QHBoxLayout>
#include <QMessageBox>
#include <QString>
#include <QVBoxLayout>
#include <QWidget>

MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
    , modele_(this)
{
    configurerUI();
    configurerConnexions();
    surCommandeModifiee(); 
}


void MainWindow::configurerUI() {
    auto* centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);
    setWindowTitle("Caisse Enregistreuse");
    resize(620, 520);

    
    ligneDescription_ = new QLineEdit(this);
    lignePrix_ = new QLineEdit(this);
    caseTaxable_ = new QCheckBox("Taxable", this);

    auto* groupeSaisie = new QGroupBox("Nouvel article", centralWidget);
    auto* formSaisie = new QFormLayout(groupeSaisie);
    formSaisie->addRow("Description article :", ligneDescription_);
    formSaisie->addRow("Prix article ($) :", lignePrix_);
    formSaisie->addRow("", caseTaxable_);

    
    boutonAjouter_ = new QPushButton("Ajouter", this);
    boutonRetirer_ = new QPushButton("Retirer sélection", this);
    boutonReinit_  = new QPushButton("Réinitialiser", this);

    auto* layoutBoutons = new QHBoxLayout();
    layoutBoutons->addWidget(boutonAjouter_);
    layoutBoutons->addWidget(boutonRetirer_);
    layoutBoutons->addWidget(boutonReinit_);

    
    listeArticles_ = new QListWidget(this);
    listeArticles_->setSelectionMode(QAbstractItemView::ExtendedSelection);

    
    labelSousTotal_ = new QLabel("0.00 $", this);
    labelTaxes_ = new QLabel("0.00 $", this);
    labelTotal_ = new QLabel("0.00 $", this);

    auto* groupeTotaux  = new QGroupBox("Totaux", centralWidget);
    auto* layoutTotaux  = new QFormLayout(groupeTotaux);
    layoutTotaux->addRow("Sous-total :", labelSousTotal_);
    layoutTotaux->addRow("Taxes (14,975%) :", labelTaxes_);
    layoutTotaux->addRow("Total à payer :", labelTotal_);

    
    auto* layoutPrincipal = new QVBoxLayout(centralWidget);
    layoutPrincipal->addWidget(groupeSaisie);
    layoutPrincipal->addLayout(layoutBoutons);
    layoutPrincipal->addWidget(listeArticles_);
    layoutPrincipal->addWidget(groupeTotaux);
}

void MainWindow::configurerConnexions() {
    connect(boutonAjouter_, &QPushButton::clicked, this, &MainWindow::surAjout);
    connect(boutonRetirer_, &QPushButton::clicked, this, &MainWindow::surRetrait);
    connect(boutonReinit_,  &QPushButton::clicked, this, &MainWindow::surReinit);

    
    connect(&modele_, &CaisseModele::commandeModifiee, this, &MainWindow::surCommandeModifiee);
}



void MainWindow::surAjout() {
    try {
        std::string description = ligneDescription_->text().toStdString();

        bool ok   = false;
        double prix = lignePrix_->text().toDouble(&ok);
        if (!ok)
            prix = 0.0; 

        bool taxable = caseTaxable_->isChecked();

        modele_.ajouterArticle(description, prix, taxable);

        ligneDescription_->clear();
        lignePrix_->clear();
        caseTaxable_->setChecked(false);
        ligneDescription_->setFocus();
    }
    catch (const std::invalid_argument& e) {
        QMessageBox::warning(this, "Erreur de saisie", QString::fromStdString(e.what()));
    }
}

void MainWindow::surRetrait() {
    auto itemsSelectionnes = listeArticles_ -> selectedItems();
    if (itemsSelectionnes.isEmpty())
        return;

    
    std::vector<Article> articlesARetirer;
    for (QListWidgetItem* item : itemsSelectionnes) {
        int row = listeArticles_->row(item);
        articlesARetirer.push_back( modele_.getArticles()[static_cast<size_t>(row)]);
    }

   
    modele_.retirerArticles(articlesARetirer);
}

void MainWindow::surReinit() {
    modele_.reinitialiser();
}



void MainWindow::surCommandeModifiee() {
   
    listeArticles_ -> blockSignals(true);
    listeArticles_ -> clear();

    for (const Article& article : modele_.getArticles()) {
        
        QString texte = QString::fromStdString(article.description) + "\t" + QString::number(article.prix, 'f', 2) + (article.taxable ? "\ttaxable" : "");
        listeArticles_ -> addItem(texte);
    }

    listeArticles_ -> blockSignals(false);

   
    boutonRetirer_ -> setEnabled(listeArticles_ -> count() != 0);

    mettreAJourTotaux();
}

void MainWindow::mettreAJourTotaux() {
    labelSousTotal_->setText(formaterMontant(modele_.calculerSousTotal()));
    labelTaxes_->setText(formaterMontant(modele_.calculerTaxes()));
    labelTotal_->setText(formaterMontant(modele_.calculerTotal()));
}



QString MainWindow::formaterMontant(double montant) {
    
    return QString::number(montant, 'f', 2) + " $";
}

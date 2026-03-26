
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <windows.h>

template <typename T>
class File {
private:
    struct Noeud {
        T donnee;
        Noeud* suivant;
        Noeud(T val) : donnee(val), suivant(nullptr) {}
    };
    Noeud* tete;
    Noeud* queue;
    int taille;

public:
    File() : tete(nullptr), queue(nullptr), taille(0) {}

    ~File() {
        while (!estVide()) defiler();
    }

    void enfiler(T val) {
        Noeud* nouveau = new Noeud(val);
        if (queue) queue->suivant = nouveau;
        queue = nouveau;
        if (!tete) tete = nouveau;
        taille++;
    }

    T defiler() {
        if (estVide()) throw std::runtime_error("File vide!");
        T val = tete->donnee;
        Noeud* temp = tete;
        tete = tete->suivant;
        if (!tete) queue = nullptr;
        delete temp;
        taille--;
        return val;
    }

    T premier() const {
        if (estVide()) throw std::runtime_error("File vide!");
        return tete->donnee;
    }

    bool estVide() const { return taille == 0; }
    int getTaille() const { return taille; }
};


class Passager {
protected:
    int    id;
    std::string nom;
    int    tickArrivee;
    int    tickDepart;
    bool   estPrioritaire;

public:
    Passager(int id, const std::string& nom, int tick, bool prioritaire = false)
        : id(id), nom(nom), tickArrivee(tick), tickDepart(-1), estPrioritaire(prioritaire) {}

    virtual ~Passager() {}

   
    virtual std::string typePassager() const = 0;
    virtual int         tempsTraitement() const = 0;  // ticks nécessaires au turniquet

    void setTickDepart(int t) { tickDepart = t; }

    int  getId()            const { return id; }
    std::string getNom()    const { return nom; }
    int  getTickArrivee()   const { return tickArrivee; }
    int  getTickDepart()    const { return tickDepart; }
    bool prioritaire()      const { return estPrioritaire; }

    int tempsAttente() const {
        return (tickDepart >= 0) ? (tickDepart - tickArrivee) : -1;
    }

    virtual std::string resume() const {
        return typePassager() + " #" + std::to_string(id) + " (" + nom + ")";
    }
};



class PassagerRegulier : public Passager {
public:
    PassagerRegulier(int id, const std::string& nom, int tick)
        : Passager(id, nom, tick, false) {}

    std::string typePassager() const override { return "Regulier "; }
    int tempsTraitement()      const override { return 1; }   // 1 tick
};



class PassagerHandicape : public Passager {
public:
    PassagerHandicape(int id, const std::string& nom, int tick)
        : Passager(id, nom, tick, true) {}

    std::string typePassager() const override { return "Prioritaire"; }
    int tempsTraitement()      const override { return 2; }   // 2 ticks
};



class Turniquet {
private:
    int         numero;
    File<Passager*> fileAttente;
    int         passagesTraites;
    int         ticksOccupe;       // ticks restants pour le passager courant
    Passager*   passagerCourant;

public:
    Turniquet(int num)
        : numero(num), passagesTraites(0), ticksOccupe(0), passagerCourant(nullptr) {}

    void ajouterPassager(Passager* p) {
        fileAttente.enfiler(p);
    }

    
    Passager* tick(int tickActuel) {
        Passager* fini = nullptr;

        
        if (passagerCourant && ticksOccupe > 0) {
            ticksOccupe--;
            if (ticksOccupe == 0) {
                passagerCourant->setTickDepart(tickActuel);
                fini = passagerCourant;
                passagerCourant = nullptr;
                passagesTraites++;
            }
        }

        
        if (!passagerCourant && !fileAttente.estVide()) {
            passagerCourant = fileAttente.defiler();
            ticksOccupe = passagerCourant->tempsTraitement();
        }

        return fini;
    }

    int  getNumero()          const { return numero; }
    int  getTailleFile()      const { return fileAttente.getTaille(); }
    int  getPassagesTraites() const { return passagesTraites; }
    bool estLibre()           const { return passagerCourant == nullptr && fileAttente.estVide(); }
    bool aPassagerCourant()   const { return passagerCourant != nullptr; }
};



class Station {
private:
    std::string         nom;
    std::vector<Turniquet*> turniquets;
    std::vector<Passager*>  tousPassagers;
    int                 prochainId;

   
    std::vector<std::string> prenoms = {
        "Alice", "Bob", "Carlos", "Diana", "Emile",
        "Fatima", "Gabriel", "Hannah", "Ivan", "Julia",
        "Kevin", "Laura", "Marc", "Nina", "Oscar"
    };

public:
    Station(const std::string& nom, int nbTurniquets)
        : nom(nom), prochainId(1) {
        for (int i = 0; i < nbTurniquets; i++)
            turniquets.push_back(new Turniquet(i + 1));
    }

    ~Station() {
        for (auto t : turniquets) delete t;
        for (auto p : tousPassagers) delete p;
    }

   
    void genererArrivees(int tick, int maxArrivees) {
        int nb = rand() % (maxArrivees + 1);
        for (int i = 0; i < nb; i++) {
            std::string prenom = prenoms[rand() % prenoms.size()];
            bool handicape = (rand() % 5 == 0);   // 20% de chance

            Passager* p;
            if (handicape)
                p = new PassagerHandicape(prochainId++, prenom, tick);
            else
                p = new PassagerRegulier(prochainId++, prenom, tick);

            tousPassagers.push_back(p);

       
            Turniquet* cible = turniquets[0];
            for (auto t : turniquets)
                if (t->getTailleFile() < cible->getTailleFile())
                    cible = t;

            cible->ajouterPassager(p);
        }
    }

    std::vector<Passager*> tick(int tickActuel) {
        std::vector<Passager*> finis;
        for (auto t : turniquets) {
            Passager* p = t->tick(tickActuel);
            if (p) finis.push_back(p);
        }
        return finis;
    }

    void afficherEtat(int tick) const {
        std::cout << "\n  Tick " << std::setw(3) << tick << " | ";
        for (auto t : turniquets) {
            std::cout << "[T" << t->getNumero()
                      << " file=" << t->getTailleFile()
                      << " traites=" << t->getPassagesTraites() << "] ";
        }
    }

    
    void afficherStatistiques(std::ofstream& log) const {
        int totalTraites = 0;
        double totalAttente = 0;
        int nbAvecDepart = 0;
        int nbHandicapes = 0;
        int nbReguliers = 0;

        for (auto p : tousPassagers) {
            if (p->getTickDepart() >= 0) {
                totalTraites++;
                totalAttente += p->tempsAttente();
                nbAvecDepart++;
            }
            if (p->prioritaire()) nbHandicapes++;
            else nbReguliers++;
        }

        double attenteMoyenne = (nbAvecDepart > 0)
            ? totalAttente / nbAvecDepart : 0.0;

       
        std::cout << "\n\n  ══════════════════════════════════════════\n";
        std::cout << "   STATISTIQUES FINALES — " << nom << "\n";
        std::cout << "  ══════════════════════════════════════════\n";
        std::cout << "   Passagers arrivés     : " << tousPassagers.size() << "\n";
        std::cout << "     → Réguliers         : " << nbReguliers << "\n";
        std::cout << "     → Prioritaires      : " << nbHandicapes << "\n";
        std::cout << "   Passagers traités     : " << totalTraites << "\n";
        std::cout << "   Temps d'attente moyen : " << std::fixed
                  << std::setprecision(2) << attenteMoyenne << " ticks\n";
        std::cout << "  ──────────────────────────────────────────\n";
        std::cout << "   Débit par turniquet :\n";
        for (auto t : turniquets)
            std::cout << "     Turniquet " << t->getNumero()
                      << " : " << t->getPassagesTraites() << " passagers\n";
        std::cout << "  ══════════════════════════════════════════\n\n";

        
        log << "STATISTIQUES — " << nom << "\n";
        log << "Passagers arrives     : " << tousPassagers.size() << "\n";
        log << "  Reguliers           : " << nbReguliers << "\n";
        log << "  Prioritaires        : " << nbHandicapes << "\n";
        log << "Passagers traites     : " << totalTraites << "\n";
        log << "Attente moyenne       : " << std::fixed
            << std::setprecision(2) << attenteMoyenne << " ticks\n";
        log << "\nDebit par turniquet :\n";
        for (auto t : turniquets)
            log << "  Turniquet " << t->getNumero()
                << " : " << t->getPassagesTraites() << " passagers\n";

        log << "\nDETAIL DES PASSAGERS :\n";
        log << std::left
            << std::setw(5)  << "ID"
            << std::setw(13) << "Type"
            << std::setw(12) << "Nom"
            << std::setw(10) << "Arrivee"
            << std::setw(10) << "Depart"
            << std::setw(10) << "Attente"
            << "\n";
        log << std::string(60, '-') << "\n";
        for (auto p : tousPassagers) {
            log << std::setw(5)  << p->getId()
                << std::setw(13) << p->typePassager()
                << std::setw(12) << p->getNom()
                << std::setw(10) << p->getTickArrivee()
                << std::setw(10) << (p->getTickDepart() >= 0 ? std::to_string(p->getTickDepart()) : "en cours")
                << std::setw(10) << (p->tempsAttente() >= 0 ? std::to_string(p->tempsAttente()) : "-")
                << "\n";
        }
    }

    std::string getNom() const { return nom; }
};



int main() {
    SetConsoleOutputCP(65001);

    srand(static_cast<unsigned>(time(nullptr)));

    const int NB_TICKS      = 30;   // durée de la simulation
    const int NB_TURNIQUETS = 3;    // nombre de turniquets
    const int MAX_ARRIVEES  = 4;    // max passagers par tick

    std::string nomStation;
    std::cout << "\n  ╔══════════════════════════════════════════╗\n";
    std::cout << "  ║   SIMULATEUR DE FILE D'ATTENTE — STM     ║\n";
    std::cout << "  ╚══════════════════════════════════════════╝\n\n";
    std::cout << "  Nom de la station : ";
    std::getline(std::cin, nomStation);
    if (nomStation.empty()) nomStation = "Berri-UQAM";

    Station station(nomStation, NB_TURNIQUETS);

    
    std::ofstream log("simulation_stm.txt");
    log << "SIMULATION STM — Station : " << nomStation << "\n";
    log << "Ticks: " << NB_TICKS << " | Turniquets: " << NB_TURNIQUETS << "\n\n";

    std::cout << "\n  Simulation de " << NB_TICKS << " ticks — Station : " << nomStation << "\n";
    std::cout << "  ──────────────────────────────────────────\n";

   
    for (int tick = 1; tick <= NB_TICKS; tick++) {
        station.genererArrivees(tick, MAX_ARRIVEES);
        std::vector<Passager*> finis = station.tick(tick);
        station.afficherEtat(tick);
        for (auto p : finis) {
            log << "Tick " << std::setw(3) << tick << " | "
                << p->resume()
                << " | attente: " << p->tempsAttente() << " tick(s)\n";
        }
    }

    station.afficherStatistiques(log);

    log.close();
    std::cout << "  Log sauvegardé dans : simulation_stm.txt\n\n";

    return 0;
}

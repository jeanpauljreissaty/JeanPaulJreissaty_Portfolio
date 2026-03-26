# 🏦 Banque Grasséenne — Simulation bancaire

Application bancaire complète avec interface graphique développée en Python.  
Permet la gestion de comptes clients, les transactions, et inclut un mode administrateur sécurisé.

---

## Fonctionnalités

- Création de comptes avec connexion sécurisée (validation mot de passe)
- Dépôts, retraits et virements entre clients
- Historique des transactions en temps réel
- **Mode administrateur** : visualiser, modifier et supprimer des comptes
- Persistance des données via base de données **SQLite**
- Mise à jour en temps réel des soldes lors des transactions
- Validation des entrées et gestion des accès

---

## Installation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/banque-grasseenne.git
cd banque-grasseenne

# 2. Aucune dépendance externe requise (Tkinter et SQLite inclus avec Python)

# 3. Lancer l'application
python banque.py
```
---

*Projet réalisé dans le cadre du cours — Collège André-Grasset, 2024*

# 🚇 Simulateur de file d'attente STM — C++

Simulation d'une station de métro en C++.  
Des passagers arrivent aléatoirement et sont acheminés vers des turniquets selon un algorithme de répartition de charge.

---

# Fonctionnalités

- Génération aléatoire de passagers (réguliers et prioritaires) à chaque tick
- **Répartition automatique** vers le turniquet le moins occupé
- **File générique**  implémentée from scratch 
- Passagers **prioritaires** (temps de traitement plus long, signalés visuellement)
- Simulation configurable : nombre de ticks, turniquets, taux d'arrivée
- **Statistiques finales** : passagers traités, temps d'attente moyen, débit par turniquet
- **Log complet** exporté dans `simulation_stm.txt`

---


## Compilation & lancement

```bash
# 1. Cloner le repo
git clone https://github.com/jp-jreissaty/stm-file-attente.git
cd stm-file-attente

# 2. Compiler
g++ -std=c++17 -o stm_simulation stm_simulation.cpp

# 3. Lancer
./stm_simulation
```

## Structure du projet

```
stm-file-attente/
├── stm_simulation.cpp    # Code source complet
└── simulation_stm.txt    # Log généré après exécution (exemple)
```


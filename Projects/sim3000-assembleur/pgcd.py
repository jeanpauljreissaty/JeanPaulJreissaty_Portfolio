READ 0
LOAD MEM 
READ 1
SUB MEM 
JNEG 6
JUMP 15
READ 0              #Permet de mettre le chiffre le plus grand 
LOAD MEM            # dans RAM[0] et le plus petit dans RAM[1]
STORE 3
READ 1 
LOAD MEM 
STORE 0
READ 3
LOAD MEM 
STORE 1
################################################
READ 0
LOAD MEM 
READ 1 
SUB MEM             #Soustrait RAM[0] avec RAM[1]
JZERO 24            #Si = 0, alors JUMP
JNEG 23             #Si = -, alors JUMP
STORE 0             #Sinon remplace la valeur dans RAM[0]
JUMP 17             #Continue pour savoir si on a soustrait jusqu'au plus petit chiffre
JUMP 0              # Puisque RAM[0] < RAM[1], alors on l'inverse 
READ 1              
LOAD MEM            #Met le PGCD dans RAM[2]
STORE 2
JUMP 27


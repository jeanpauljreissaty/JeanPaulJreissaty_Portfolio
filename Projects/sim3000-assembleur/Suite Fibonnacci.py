READ 11
LOAD 1
STORE 11    #Commence avec 0 et 1
READ 9
LOAD 12
STORE 9     #Pour savoir quel RAM[] il faudra STORE
READ 2
LOAD 1      
STORE 2
################################################
READ 0
LOAD MEM 
SUB 2           #Enleve 2 pour obtenir le bon K, puisqu'on commence deja
STORE 0         # avec 0 et 1
################################################
READ 0 
LOAD MEM 
JZERO 38    
SUB 1           #Soustrait 1 au K a chaque repetition, si k = 0 alors termine
STORE 0 
################################################
READ 1
LOAD MEM        # Additione RAM[1] + RAM[2] et le met dans RAM[3]
READ 2
ADD MEM    
STORE 3
################################################
READ 2 
LOAD MEM        # Le chiffre dans RAM[2] va dans RAM [1] et 
STORE 1         # le chiffre dans RAM[3] va dans RAM [2]
READ 3 
LOAD MEM 
STORE 2
################################################
READ 3
LOAD MEM        #Le chiffre dans RAM[3] va dans la case associer de RAM[10] et +
READ 9
STORE MEM   
READ 9 
LOAD MEM
ADD 1           # Additione 1 a RAM[9] pour permettre de mettre le prochain 
STORE 9         #chiffre dans le RAM[+1] prochain
JUMP 13
JUMP 38




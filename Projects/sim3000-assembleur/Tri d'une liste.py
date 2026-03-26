LOAD 10
STORE 0         #Pour permettre de commencer a RAM[10]
LOAD 10         #Pour permettre d'alterner de RAM[10] et +
STORE 3
################################################
READ 3
READ MEM        #Soustrait la case situee dans RAM[3] 
LOAD MEM        # avec la case dans RAM[0]
READ 0
READ MEM 
JZERO 31        #Si le dernier chiffre est 0 = JUMP
SUB MEM 
JNEG 13         #Si c'est negatif on veut inverser les chiffres 
JUMP 26         
################################################
READ 0
READ MEM 
LOAD MEM 
STORE 4         #STORE le chiffre de RAM[10] dans RAM[4]
READ 3
READ MEM 
LOAD MEM            
READ 0 
STORE MEM       #STORE le chiffre le plus petit dans la premiere position
READ 4
LOAD MEM        #Prend le chiffre de RAM[4] et le STORE dans la position
READ 3          #du chiffre precedent 
STORE MEM   
READ 3
LOAD MEM        #Additione 1 a RAM[3] pour alterner les chiffres dans la liste
ADD 1 
STORE 3
JUMP 4
################################################
READ 0      
READ MEM 
LOAD MEM        #Verifie si le chiffre soustrait est un zero = fin de la liste
JZERO 43
READ 0      
LOAD MEM 
ADD 1           #Adittione 1 a RAM[0] pour passer au deuxieme chiffre de la liste
STORE 0
READ 0 
LOAD MEM        #Permet de commencer le RAM[3] avec le RAM[0] a la meme position
STORE 3
JUMP 4          #Re-boucle
JUMP 43


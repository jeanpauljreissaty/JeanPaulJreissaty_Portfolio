####PREMIÈRE ÉTAPE###

layout = ([
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ])

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAZE_WIDTH = 25
MAZE_HEIGHT = 22
CELL_WIDTH = SCREEN_WIDTH / MAZE_WIDTH
CELL_HEIGHT = SCREEN_HEIGHT / MAZE_HEIGHT
    
coordonees = []

for row_index, row in enumerate(layout):
    for col_index, col in enumerate(row):
        if col == 0:
            x = col_index * int(CELL_WIDTH)
            y = row_index * int(CELL_HEIGHT)
            coordonees.append((x, y))
print(coordonees)


coordonees = [(32, 27), (64, 27), (96, 27), (128, 27), (160, 27), (192, 27), (224, 27), (256, 27), 
(288, 27), (320, 27), (352, 27), (416, 27), (448, 27), (480, 27), (512, 27), (544, 27), (576, 27), 
(608, 27), (640, 27), (672, 27), (704, 27), (736, 27), (32, 54), (160, 54), (352, 54), (416, 54), 
(608, 54), (736, 54), (32, 81), (64, 81), (96, 81), (128, 81), (160, 81), (192, 81), (224, 81), 
(256, 81), (288, 81), (320, 81), (352, 81), (384, 81), (416, 81), (448, 81), (480, 81), (512, 81), 
(544, 81), (576, 81), (608, 81), (640, 81), (672, 81), (704, 81), (736, 81), (32, 108), (160, 108), 
(224, 108), (544, 108), (608, 108), (736, 108), (32, 135), (64, 135), (96, 135), (128, 135), (160, 135), 
(224, 135), (256, 135), (288, 135), (320, 135), (352, 135), (416, 135), (448, 135), (480, 135), 
(512, 135), (544, 135), (608, 135), (640, 135), (672, 135), (704, 135), (736, 135), (32, 162), 
(160, 162), (352, 162), (416, 162), (608, 162), (736, 162), (32, 189), (160, 189), (224, 189), 
(256, 189), (288, 189), (320, 189), (352, 189), (384, 189), (416, 189), (448, 189), (480, 189), 
(512, 189), (544, 189), (608, 189), (736, 189), (32, 216), (160, 216), (224, 216), (320, 216), 
(352, 216), (384, 216), (416, 216), (448, 216), (544, 216), (608, 216), (736, 216), (32, 243), 
(64, 243), (96, 243), (128, 243), (160, 243), (192, 243), (224, 243), (288, 243), (320, 243), 
(352, 243), (384, 243), (416, 243), (448, 243), (480, 243), (544, 243), (576, 243), (608, 243), 
(640, 243), (672, 243), (704, 243), (736, 243), (32, 270), (160, 270), (224, 270), (288, 270), 
(320, 270), (352, 270), (384, 270), (416, 270), (448, 270), (480, 270), (544, 270), (608, 270), 
(736, 270), (32, 297), (160, 297), (224, 297), (544, 297), (608, 297), (736, 297), (32, 324), 
(160, 324), (224, 324), (256, 324), (288, 324), (320, 324), (352, 324), (384, 324), (416, 324), 
(448, 324), (480, 324), (512, 324), (544, 324), (608, 324), (736, 324), (32, 351), (160, 351), 
(352, 351), (416, 351), (608, 351), (736, 351), (32, 378), (64, 378), (96, 378), (128, 378), 
(160, 378), (192, 378), (224, 378), (256, 378), (288, 378), (320, 378), (352, 378), (416, 378), 
(448, 378), (480, 378), (512, 378), (544, 378), (576, 378), (608, 378), (640, 378), (672, 378), 
(704, 378), (736, 378), (32, 405), (160, 405), (352, 405), (416, 405), (608, 405), (736, 405), 
(32, 432), (64, 432), (96, 432), (160, 432), (192, 432), (224, 432), (256, 432), (288, 432), 
(320, 432), (352, 432), (384, 432), (416, 432), (448, 432), (480, 432), (512, 432), (544, 432), 
(576, 432), (608, 432), (672, 432), (704, 432), (736, 432), (96, 459), (160, 459), (224, 459), 
(544, 459), (608, 459), (672, 459), (32, 486), (64, 486), (96, 486), (128, 486), (160, 486), 
(224, 486), (256, 486), (288, 486), (320, 486), (352, 486), (416, 486), (448, 486), (480, 486), 
(512, 486), (544, 486), (608, 486), (640, 486), (672, 486), (704, 486), (736, 486), (32, 513), 
(352, 513), (416, 513), (736, 513), (32, 540), (64, 540), (96, 540), (128, 540), (160, 540), 
(192, 540), (224, 540), (256, 540), (288, 540), (320, 540), (352, 540), (384, 540), (416, 540), 
(448, 540), (480, 540), (512, 540), (544, 540), (576, 540), (608, 540), (640, 540), (672, 540), (704, 540), (736, 540)]



Dans la première étape, mon objectif est d'obtenir une liste des coordonnées contenant tous les espaces vides du labyrinthe dans la liste LAYOUT oû "1" est un mur et "0" un espace vide.  En parcourant chaque ligne et chaque colonne de cette liste, j'ai écrit un programme qui détecte les cellules contenant un zéro. Pour chacune d’elles, je calcule la position avec les dimensions des cellules sur l’écran en multipliant l’indice de colonne par la largeur d’une cellule, et l’indice de ligne par la hauteur d’une cellule. Ces coordonnées sont ensuite ajoutées à une liste que je peux utiliser pour placer les portails aléatoires sur l'écran. 

#########################################################################################################################

###DEUXIÈME ÉTAPE   game.py###

choix_orange_portal = random.choice(coordonees)
choix_bleu_portal = random.choice(coordonees)

orange_portal = pygame.Rect(choix_orange_portal[0] , choix_orange_portal[1] + 3 , CELL_WIDTH, CELL_HEIGHT)
blue_portal   = pygame.Rect(choix_bleu_portal[0] , choix_bleu_portal[1] + 3 , CELL_WIDTH, CELL_HEIGHT)

def portal(self):
    
    pygame.draw.circle(self.screen, ORANGE, orange_portal.center, 10)

    pygame.draw.circle(self.screen, (0, 100, 255), blue_portal.center, 10)

def draw_game(self):
    self.portal()



Pour la deuxième partie, à l'aide de RANDOM.CHOICE je séléctionne 2 coordonnées de la liste COORDONEES crée précédament, pour positioner aléatoirement les deux portaux sur l'écran. Ensuite, je crée deux PYGAME.RECT des portaux orange et bleu pour l'utiliser comme un hitbox. Ce code est mit à l'extérieure de la Class Game pour qu'ils génerent une seule fois les coordonnées. 

Pour la fonction PORTAL(SELF), je l'ai positioné dans la Class Game puis ensuite je l'appelle dans la fonction DRAW_GAME(SELF) pour être capable d'afficher les portaux sur l'écran, en utilisant PYGAME.DRAW.CIRCLE. 

#########################################################################################################################

###TROISIÈME ÉTAPE  pacman.py###

def __init__(self, x, y):

        self.teleport_pac_orange = True
        self.teleport_pac_blue = True

def update(self, maze, orange_portal, blue_portal):
         
         ###CODE PRÉCEDENT###

        teleported = False

        if orange_portal.colliderect(hitbox) and  self.teleport_pac_orange  == True: 
            self.x = (blue_portal.centerx - self.width//2 )
            self.y = (blue_portal.centery -self.height//2) 
            self.teleport_pac_blue = False
            teleported = True
        
        elif blue_portal.colliderect(hitbox) and  self.teleport_pac_blue == True: 
            self.x = orange_portal.centerx - self.width//2
            self.y = orange_portal.centery - self.height//2
            self.teleport_pac_orange = False 
            teleported  = True

        current_rect = self.get_rect()
        if not orange_portal.colliderect(current_rect):
            self.teleport_pac_orange = True 

        if not blue_portal.colliderect(current_rect):
            self.teleport_pac_blue = True

        if not teleported:
            ###CODE SUIVANT###

    
Pour la troisième partie, il faut gérer correctement la téléportation de Pacman entre les deux portails, j’ai dû commencer par initialiser deux variables dans le constructeur : self.teleport_pac_orange et self.teleport_pac_blue. Ces variables servent à contrôler si Pacman a le droit de traverser un portail. Elles sont importantes pour éviter l’effet ping-pong, c’est-à-dire une téléportation immédiate dans l’autre sens juste après être arrivé. 

Dans la fonction update, j’ai ensuite géré la détection de collision entre Pacman et les portails. Si Pacman entre en contact avec le portail orange et que self.teleport_pac_orange est activé, il est automatiquement déplacé vers la position du portail bleu. Après la téléportation, j’interdis immédiatement le passage inverse en mettant self.teleport_pac_blue à False. Le même principe s’applique dans l’autre direction. 

J’utilise aussi la variable teleported pour indiquer si une téléportation vient d’avoir lieu. Cela me permet d’empêcher le reste du code de la fonction update de s’exécuter pendant une téleportation. Enfin, lorsque Pacman s’éloigne d’un portail, je réactive l’autorisation de téléportation en remettant self.teleport_pac_orange ou self.teleport_pac_blue à True. Cela garantit que Pacman pourra repasser plus tard sans problème, mais seulement après avoir quitté la zone de collision.

#########################################################################################################################

###QUATRIÈME ÉTAPE  ghost.py###

 def __init__(self, x, y, color):

        self.teleport_orange = True
        self.teleport_blue = True

 def update(self, maze, pacman, orange_portal, blue_portal):
        """Update ghost position and state"""
      
      ###CODE PRÉCEDENT###
        
        # Move ghost
        self.move(maze, pacman, orange_portal, blue_portal)
        
 def move(self, maze, pacman, orange_portal, blue_portal):
        """Basic ghost movement (random direction on collision)"""
        
        new_x, new_y, hitbox = self.get_next_position()
        
        teleported = False

        if orange_portal.colliderect(hitbox) and self.teleport_orange == True: 
            self.x = blue_portal.centerx - self.width // 2
            self.y = blue_portal.centery - self.height // 2
            self.teleport_blue = False
            teleported = True
        
        
        elif blue_portal.colliderect(hitbox) and self.teleport_blue == True: 
            self.x = orange_portal.centerx - self.width // 2
            self.y = orange_portal.centery - self.height // 2
            self.teleport_orange = False 
            teleported = True
        
        current_rect = self.get_rect()
        if not orange_portal.colliderect(current_rect):
            self.teleport_orange = True
            
        if not blue_portal.colliderect(current_rect):
            self.teleport_blue = True

        if not teleported:
            ###CODE SUIVANT###

Pour les fantômes, j’ai appliqué la même logique de téléportation que pour Pacman. J’ai ajouté deux variables : self.teleport_orange et self.teleport_blue. Elles fonctionnent comme des interrupteurs permettant de contrôler si un fantôme peut traverser un portail. Comme pour Pacman, ces variables sont essentielles pour éviter l’effet de ping-pong, où un fantôme serait téléporté en boucle entre les deux portails. 

J’ai modifié l’appel à la fonction move afin qu’elle reçoive également les objets orange_portal et blue_portal. Cela permet à chaque fantôme de vérifier lui-même s’il entre en collision avec un portail pendant son déplacement. À l’intérieur de la fonction move, je commence par calculer la prochaine position du fantôme. Si cette position entre en contact avec le portail orange et que self.teleport_orange est encore active, le fantôme est immédiatement téléporté au centre du portail bleu. Juste après, je désactive self.teleport_blue pour empêcher un retour instantané. Le même principe est appliqué dans l’autre sens pour les collisions avec le portail bleu. 

La fonction update a aussi du etre modifier pour prendre en argument orange_portal et blue_portal, car elle appelle move, donc nécessairement si move prend comme argument orange_portal et blue_portal, alors update le doit aussi. 

Une variable teleported me permet ensuite de savoir si une téléportation vient d’avoir lieu. Tant que cette variable est vraie, le code responsable du déplacement normal du fantôme n’est pas exécuté, ce qui évite que le fantome rentre en collision avec un mur, suite à une téleportation. Enfin, dès que le fantôme s’éloigne de la zone du portail, self.teleport_orange ou self.teleport_blue sont réactivés, ce qui lui permet de réutiliser les portails plus tard, mais seulement après les avoir quittés.

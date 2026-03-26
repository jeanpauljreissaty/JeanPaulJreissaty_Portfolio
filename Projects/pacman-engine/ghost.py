import pygame
import random
from game_object import GameObject
from constants import *



class Ghost(GameObject):
    """Base Ghost class"""
    
    def __init__(self, x, y, color):
        super().__init__(x, y, int(CELL_WIDTH//2), int(CELL_HEIGHT//1.2), color)
        self.start_x = x
        self.start_y = y
        self.direction = random.randint(0, 3)
        self.speed = GHOST_SPEED
        self.vulnerable = False
        self.vulnerable_timer = 0
        self.vulnerable_duration = 300  # frames
        self.step = "left"
        self.step_timer = 0
        self.last_RL_direction = 0
        self.x = x - self.width // 2
        self.y = y - self.height // 2

        self.teleport_orange = True
        self.teleport_blue = True

    def update(self, maze, pacman, orange_portal, blue_portal):
        """Update ghost position and state"""
        # Update vulnerable state
        if self.vulnerable:
            self.vulnerable_timer += 1
            if self.vulnerable_timer >= self.vulnerable_duration:
                self.vulnerable = False
                self.vulnerable_timer = 0
        
        # Update ghost animation
        self.step_timer += 1
        if self.step_timer >= 10:
            self.step = "right" if self.step == "left" else "left"
            self.step_timer = 0
        
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
            # Check for collision with walls
            if maze.is_wall_collision(hitbox):
                # Change direction randomly
                
                self.direction = random.randint(0, 3)
            else:
                self.x = new_x
                self.y = new_y
            
        
            
    def get_next_position(self):
        """Get next position based on current direction"""
        new_x, new_y = self.x, self.y
        hitbox = None

        if self.direction in [0, 2]:  # Right or Left
            self.last_RL_direction = self.direction
            
        # TODO: Écrire votre code ici
        if self.direction == 0:
            new_x += self.speed
          
            
        elif self.direction == 1:
            new_y += self.speed
         
            
        elif self.direction == 2:
            new_x -= self.speed
         
            
        elif self.direction == 3:
            new_y -= self.speed
        
        

        hitbox = pygame.Rect(new_x, new_y, self.width, self.height)
        return new_x, new_y, hitbox
            
    def draw(self, screen):
        """Load ghost image"""
        # TODO: Écrire votre code ici

        if self.vulnerable == False:
            image = pygame.image.load(self.color + "_ghost.png")
        else: 
            image = pygame.image.load("weak_ghost.png")
        
        scaled_image = pygame.transform.scale(image, (self.width, self.height))


        if self.step == "right":
              scaled_image = pygame.transform.rotate(scaled_image, 10)
        elif self.step == "left":
             scaled_image = pygame.transform.rotate(scaled_image, -10)
        
        if self.last_RL_direction == 0:
            scaled_image = pygame.transform.flip(scaled_image, True, False)

                
        rect = scaled_image.get_rect(center=(self.x, self.y))
        screen.blit(scaled_image, rect)



    
    def make_vulnerable(self):
        """Make the ghost vulnerable to being eaten"""
        self.vulnerable = True
        self.vulnerable_timer = 0
    
    def reset_position(self):
        """Reset ghost to starting position"""
        self.x = self.start_x - self.width // 2
        self.y = self.start_y - self.height // 2
        self.vulnerable = False
        self.vulnerable_timer = 0

class RedGhost(Ghost):
    """Red ghost - aggressive, chases Pacman directly"""
    
    def __init__(self, x, y, color="red"):
        super().__init__(x, y, color)

    def move(self, maze, pacman, orange_portal, blue_portal):
        """Aggressive movement - chase Pacman directly"""
        
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
            if self.vulnerable:
                # Run away from Pacman when vulnerable
                self.flee_from_pacman(maze, pacman, orange_portal, blue_portal)
                
            else:
                # Chase Pacman
                self.chase_pacman(maze, pacman, orange_portal, blue_portal)
                
    
    def chase_pacman(self, maze, pacman, orange_portal, blue_portal):
        """Move towards Pacman"""
        pacman_x, pacman_y = pacman.get_position()

        # TODO: Écrire votre code ici
        distance_x = pacman_x - self.x 
        distance_y = pacman_y - self.y 
        self.ancienne_direction = self.direction
        
    
        if abs(distance_x) >= abs(distance_y):  
            if distance_x > 0:
                self.direction = 0
            else: 
                self.direction = 2
        else: 

            if distance_y > 0:
                self.direction = 1
            else:
                self.direction = 3

       
        new_x, new_y, hitbox = self.get_next_position()
     
        if maze.is_wall_collision(hitbox):
            self.direction = self.ancienne_direction
            super().move(maze, pacman, orange_portal, blue_portal )
            
        else:
            self.x = new_x
            self.y = new_y

    def flee_from_pacman(self, maze, pacman, orange_portal, blue_portal):
        """Run away from Pacman when vulnerable"""
        pacman_x, pacman_y = pacman.get_position()
        
        # TODO: Écrire votre code ici
        distance_x = int(pacman_x - self.x)
        distance_y = int(pacman_y - self.y)
        self.ancienne_direction = self.direction

        if abs(distance_x) >= abs(distance_y):  
            if distance_x > 0:
                self.direction = 2
            else:   
                self.direction = 0
        else:     
            if distance_y > 0:
                self.direction = 3
            else:
                self.direction = 1

        new_x, new_y, hitbox = self.get_next_position()
     
        if maze.is_wall_collision(hitbox):
            self.direction = self.ancienne_direction
            super().move(maze, pacman, orange_portal, blue_portal)
        else:
            self.x = new_x
            self.y = new_y

       

class PinkGhost(Ghost):
    """Pink ghost - tries to ambush Pacman"""

    def __init__(self, x, y, color="pink"):
        super().__init__(x, y, color)

    def move(self, maze, pacman, orange_portal, blue_portal):
        """Ambush movement - try to get ahead of Pacman"""

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
            if self.vulnerable:
                super().move(maze, pacman, orange_portal, blue_portal)  # Random movement when vulnerable
            else:
                self.ambush_pacman(maze, pacman, orange_portal, blue_portal)

    def ambush_pacman(self, maze, pacman, orange_portal, blue_portal):
        """Try to position ahead of Pacman"""
        # Try to position ahead of Pacman
        pacman_x, pacman_y = pacman.get_position()
        
        # TODO: Écrire votre code ici
        distance_x = pacman_x - self.x 
        distance_y = pacman_y - self.y
        x = pacman_x + (distance_x//2)
        y = pacman_y + (distance_y//2)
        self.ancienne_direction = self.direction

        if abs(x - self.x) >= abs(y - self.y):  
            if  x > self.x:
                self.direction = 0
            else:   
                self.direction = 2
        else:     
            if y > self.y:
                self.direction = 1
            else:
                self.direction = 3


        new_x, new_y, hitbox = self.get_next_position()
     
        if maze.is_wall_collision(hitbox):
            self.direction = self.ancienne_direction
            super().move(maze, pacman, orange_portal, blue_portal)
        else:
            self.x = new_x
            self.y = new_y


class BlueGhost(Ghost):
    """Blue ghost - patrol behavior"""

    def __init__(self, x, y, color="blue"):
        super().__init__(x, y, color)
        self.patrol_timer = 0
        self.patrol_duration = 120
    
    def move(self, maze, pacman, orange_portal, blue_portal):
        """Patrol movement - changes direction periodically"""

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
            self.patrol_timer += 1
            
            # TODO: Écrire votre code 
            new_x, new_y, hitbox = self.get_next_position()

            if self.patrol_timer >= self.patrol_duration:
                self.direction = random.randint(0, 3)
                self.patrol_timer = 0

            if maze.is_wall_collision(hitbox):
                self.direction = random.randint(0, 3)
            else:
                self.x = new_x
                self.y = new_y

class OrangeGhost(RedGhost):
    """Orange ghost - mixed behavior"""

    def __init__(self, x, y, color="orange"):
        super().__init__(x, y, color)
        self.behavior_timer = 0
        self.chase_mode = True
        self.behavior_duration = 180  # frames
    
    def move(self, maze, pacman, orange_portal, blue_portal):
        """Mixed behavior - alternates between chasing and fleeing"""
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
            self.behavior_timer += 1

            
            # TODO: Écrire votre code ici

            if self.vulnerable == True:
                self.flee_from_pacman(maze, pacman, orange_portal, blue_portal)
                return

            if self.behavior_timer >= self.behavior_duration:
                self.chase_mode = not self.chase_mode
                self.behavior_timer = 0

            if self.chase_mode == True:
                super().chase_pacman(maze, pacman, orange_portal, blue_portal)
                return

            new_x, new_y, hitbox = self.get_next_position()
            if maze.is_wall_collision(hitbox):
                self.direction = random.randint(0, 3)
            else:
                self.x = new_x
                self.y = new_y
        
ghosts_dict = {
            "red": RedGhost,
             "pink": PinkGhost,
            "blue": BlueGhost,
             "orange": OrangeGhost
        }
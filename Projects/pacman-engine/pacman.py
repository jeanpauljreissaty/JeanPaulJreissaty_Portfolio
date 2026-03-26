import pygame
import math
from game_object import GameObject
from constants import *
import random

class Pacman(GameObject):
    """Pacman player class"""
    
    def __init__(self, x, y):
        super().__init__(x, y, CELL_WIDTH//1.8, CELL_HEIGHT//1.8, YELLOW)
        self.start_x = x
        self.start_y = y
        self.direction = 0  # 0=right, 1=down, 2=left, 3=up
        self.next_direction = 0
        self.speed = PACMAN_SPEED
        self.mouth_open = True
        self.mouth_timer = 0
        self.x = x - self.width // 2
        self.y = y - self.height // 2

        self.teleport_pac_orange = True
        self.teleport_pac_blue = True
 
       

    def handle_input(self, key):
        """Handle keyboard input for movement"""
        # TODO: Écrire votre code ici
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.next_direction = 2
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.next_direction = 0
        elif key == pygame.K_UP or key == pygame.K_w:
            self.next_direction = 3
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.next_direction = 1

    def update(self, maze, orange_portal, blue_portal):
        """Update Pacman's position and state"""
        # Update mouth animation
        self.mouth_timer += 1
        if self.mouth_timer >= 10:
            self.mouth_open = not self.mouth_open
            self.mouth_timer = 0
        
        # Get next position based on next_direction
        new_x, new_y, hitbox = self.get_next_position()

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
            # Check if there is collision with a wall
            if not maze.is_wall_collision(hitbox):
                self.direction = self.next_direction
                self.x = new_x
                self.y = new_y

    def get_next_position(self):
        """
        Get the next position based on direction

        The hitbox will be used to detect collisions before moving.
        Returns new_x, new_y, hitbox
        """
        new_x, new_y = self.x, self.y
        # TODO:Écrire votre code ici
        if self.next_direction == 0:
            new_x += self.speed
        elif self.next_direction == 1:
            new_y += self.speed
        elif self.next_direction == 2:
            new_x -= self.speed
        elif self.next_direction == 3:
            new_y -= self.speed
        
        hitbox = pygame.Rect(new_x, new_y, self.width, self.height)
        
        return new_x, new_y, hitbox
    
    def draw(self, screen):
        """Draw Pacman with mouth animation"""
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        radius = self.width // 2

        # TODO: Écrire votre code ici
        # Draw Pacman body
        if self.mouth_open == False:
            pygame.draw.circle(screen, YELLOW, (center_x, center_y ),radius)
        
        if self.mouth_open == True:
            direction_face = 0
            angle_bouche = 30

            if self.direction == 0:   # 0=right, 1=down, 2=left, 3=up
                direction_face = 0
            elif self.direction == 1: 
                direction_face = 90
            elif self.direction == 2: 
                direction_face = 180
            elif self.direction == 3: 
                direction_face = 270


            angle_debut = direction_face + angle_bouche
            angle_fin = direction_face + 360 - angle_bouche

            liste_points = [(center_x, center_y)]  

            for i in range(angle_debut, angle_fin + 1, 5):  
                rad = math.radians(i)
                x = center_x + math.cos(rad) * radius
                y = center_y + math.sin(rad) * radius 
                liste_points.append((x, y))

            pygame.draw.polygon(screen, YELLOW, liste_points)

    
        # Draw Pacman eye
        if self.direction == 0:         # 0=right, 1=down, 2=left, 3=up
           pygame.draw.circle(screen, BLACK,(center_x + 0.5, center_y - 2),  2)
        elif self.direction == 1:
            pygame.draw.circle(screen, BLACK,(center_x + 2, center_y  -2),  2)
        elif self.direction == 2:
            pygame.draw.circle(screen, BLACK,(center_x + 0.5, center_y -2),  2)
        elif self.direction == 3:
            pygame.draw.circle(screen, BLACK,(center_x + 2, center_y + 2),  2)

    
    def reset_position(self):
        """Reset Pacman to starting position"""
        self.x = self.start_x - self.width // 2
        self.y = self.start_y - self.height // 2
        self.direction = 0
        self.next_direction = 0


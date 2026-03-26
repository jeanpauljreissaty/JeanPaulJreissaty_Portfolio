import pygame
from config import LOG_SIZES

# ======================== PARTIE 3.1 ===========================
# 
# TODO : Définir un dictionnaire pour les bûches en bois avec trois tailles différentes : petite, moyenne et longue
# 
# Étapes à suivre : 
# - Créer un dictionnaire nommé `logs_dict` avec les trois clés suivantes : 
#      - short
#      - medium
#      - long 
#
# - Utilisez "pygame.image.load()" pour charger l'image "log.png" (à partir du dossier "images/")
#   trois fois, c'est-à-dire une fois pour chaque taille.
# - Redimensionnez (avec "pygame.transform.scale") chaque image en utilisant les clés du dictionnaire LOG_SIZES. 


image_log = pygame.image.load(f"images/log.png")

image_log_short = pygame.transform.scale(image_log, LOG_SIZES["short"] )
image_log_medium = pygame.transform.scale(image_log, LOG_SIZES["medium"] )
image_log_long = pygame.transform.scale(image_log, LOG_SIZES["long"] )

logs_dict = {"short": image_log_short, "medium": image_log_medium, "long":image_log_long }

# ===============================================================
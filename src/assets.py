# assets.py

# imports
import pygame

# load all game assets
def load_assets():
    player_image = pygame.image.load("assets/player.png")
    enemy_image = pygame.image.load("assets/enemy.png")
    background_music = pygame.mixer.Sound("assets/music.mp3")

    return {
        'player_image': player_image,
        'enemy_image': enemy_image,
        'background_music': background_music,
    }
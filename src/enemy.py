import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, player_size):
        """
        Initialize an enemy character.

        Loads the enemy image, sets its size, and positions it randomly
        within the screen. Also defines the enemy's movement speed.

        Args:
            screen_width (int): Width of game screen.
            screen_height (int): Height of game screen.
            player_size (tuple): Size of the player (to scale enemy to same size).
        """
        # Load the enemy image and resize it
        self.image = pygame.image.load('../assets/images/dynamics/enemy.png')
        self.image = pygame.transform.scale(self.image, player_size)  # Same size as player

        # Get the rect (for positioning and collisions)
        self.rect = self.image.get_rect()

        # Random initial position
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint((screen_height // 2), screen_height - self.rect.height)

        # Movement speed (constant speed)
        self.speed_x = random.choice([-3, 3])  # Random speed in x direction
        self.speed_y = random.choice([-3, 3])  # Random speed in y direction

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        """
        Update the enemy's position.
        """
        # Move the enemy
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the screen edges
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1  # Reverse horizontal direction
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1  # Reverse vertical direction

    def draw(self, screen):
        """
        Draw enemy on screen.

        Args:
            screen (Surface): The surface to draw the enemy on.
        """
        screen.blit(self.image, self.rect)
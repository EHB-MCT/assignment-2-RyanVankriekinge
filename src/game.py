from player import Player
from enemy import Enemy
import pygame


class Game:
    def __init__(self, screen):
        """
        Initialise the game with player and enemies.

        Args:
            screen (Surface): The Pygame surface to draw the game on.
        """
        self.screen = screen
        self.player = Player()

        # Create a list of enemies
        self.enemies = []
        self.create_enemies(3) #number of enemies

        # Flag for game over or collision
        self.game_over = False

    def create_enemies(self, number_of_enemies):
        """
        Create enemies and add them to the game.

        Args:
            number_of_enemies (int): The amount of enemies.
        """
        # Get player size from player image rect
        player_size = (self.player.rect.width, self.player.rect.height)

        # Add enemies to the list
        for _ in range(number_of_enemies):
            enemy = Enemy(self.screen.get_width(), self.screen.get_height(), player_size)
            self.enemies.append(enemy)

    def check_collision(self):
        """
        Check for collisions between the player and enemies.

        Sets the game_over attribute to True if a collision is detected.
        """
        # Iterate through all enemies and check if they hit the player
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                print("Collision detected!")
                self.game_over = True
                return  # Stop when collision is detected

    def update(self):
        """
        Update the game state, player position and enemy position.

        Checks for collisions and updates the game status.
        """
        if not self.game_over:
            # Update player position
            self.player.update()

            # Update each enemy position
            for enemy in self.enemies:
                enemy.update()

            # Check for collisions
            self.check_collision()

    def draw(self):
        """
        Draw game elements on screen.

        Fills background, draws the player and enemies,
        displays "Game Over".
        """
        # Fill screen with a black background
        self.screen.fill((0, 0, 0))

        # Draw player
        self.player.draw(self.screen)

        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Display "Game Over" message if game is over
        if self.game_over:
            font = pygame.font.SysFont(None, 55)
            text = font.render('Game Over', True, (255, 0, 0))
            self.screen.blit(text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 30))
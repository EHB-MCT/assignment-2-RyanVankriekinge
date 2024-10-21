import pygame


class Player:
    def __init__(self):
        """
        Initialise the player.

        Loads and resizes the player image, sets the initial position,
        speed, and movement attributes.
        """
        # Load the player image
        self.image = pygame.image.load('assets/images/dynamics/player.png')

        # Resize the player image (reduce size)
        original_width, original_height = self.image.get_size()
        new_width = int(original_width * 0.2)  # 20% of the original width
        new_height = int(original_height * 0.2)  # 20% of the original height
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        # Set player rectangle (used for positioning and collisions)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 5

        # Movement attributes (boolean) declaration
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def handle_event(self, event):
        """
        Handle events for player movement.

        Updates movement attributes based on keyboard input.

        Args:
            event (Event): The pygame event to handle.
        """
        # Set movement attributes to True when key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moving_left = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moving_right = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moving_up = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moving_down = True

        # Set movement attributes back to False when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moving_left = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moving_right = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moving_up = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moving_down = False

    def update(self):
        """
        Update player's position.
        """
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_right:
            self.rect.x += self.speed
        if self.moving_up:
            self.rect.y -= self.speed
        if self.moving_down:
            self.rect.y += self.speed

    def draw(self, screen):
        """
        Draw the player on screen.

        Args:
            screen (Surface): The surface to draw the player on.
        """
        screen.blit(self.image, self.rect)
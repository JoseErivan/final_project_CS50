import pygame
import random

# Creating the enemy class.
class Enemy:
    def __init__(self, x, y, screen) -> None:
        self.size = 100
        self.x = x
        self.y = y
        self.velocity = random.randint(5, 20)
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, 64, self.size) # This rect is utilized to check the colllision.
        self.image = pygame.image.load("images/enemy.png")

    # Function to move the enemies.
    def move(self):
        self.y += self.velocity
        self.rect.y = self.y

    # Function to remove the enemies when out from screen.
    def out(self):
        if self.y > 700:
            return True

    # Function to draw enemy.
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, self.size, self.size))
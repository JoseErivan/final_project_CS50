import pygame

# Creating the player class.
class Player:
    def __init__(self, screen):
        self.size = 100
        self.x = 225
        self.y = 600
        self.velocity = 10
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size) # This rect is utilized to check the colllision.
    
    # Function to move the player.
    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.velocity
            self.rect.x = self.x
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.velocity
            self.rect.x = self.x

    # Function to verify the colision with map.
    def out(self):
        if self.x <= 50:
            self.x = 50
        if self.x >= 350:
            self.x = 350

    # Function to draw player.
    def draw(self):
        pygame.draw.rect(self.screen, (0,0,255), (self.x, self.y, self.size, self.size))
import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("assets/grass.png").convert()
        self.player = Player(400, 300)
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
    
    def draw(self):
        # Tile the background
        for y in range(0, self.screen.get_height(), self.background.get_height()):
            for x in range(0, self.screen.get_width(), self.background.get_width()):
                self.screen.blit(self.background, (x, y))
        
        self.player.draw(self.screen)

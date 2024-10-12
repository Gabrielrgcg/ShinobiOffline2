import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sprite_width = 64
        self.sprite_height = 64
        self.rows = 36
        self.columns = 4

    def get_sprite(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise ValueError(f"Invalid sprite position. Row must be 0-{self.rows-1}, Column must be 0-{self.columns-1}")

        x = col * self.sprite_width
        y = row * self.sprite_height

        sprite = pygame.Surface((self.sprite_width, self.sprite_height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, self.sprite_width, self.sprite_height))
        return sprite

    def get_animation_frames(self, start_row, num_frames):
        frames = []
        for i in range(num_frames):
            row = (start_row + i) % self.rows
            col = (start_row + i) // self.rows
            frames.append(self.get_sprite(row, col))
        return frames

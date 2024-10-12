import pygame
from sprite_sheet import SpriteSheet

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_walk = 3
        self.speed_run = 6
        self.direction = "down"
        self.state = "idle"
        
        sprite_sheet = SpriteSheet("assets/player_sprite_sheet.png")
        self.sprites = {
            "idle": {
                "down": sprite_sheet.get_animation_frames(0, 4),
                "left": sprite_sheet.get_animation_frames(4, 4),
                "right": sprite_sheet.get_animation_frames(8, 4),
                "up": sprite_sheet.get_animation_frames(12, 4)
            },
            "walk": {
                "down": sprite_sheet.get_animation_frames(1, 8),
                "left": sprite_sheet.get_animation_frames(5, 8),
                "right": sprite_sheet.get_animation_frames(9, 8),
                "up": sprite_sheet.get_animation_frames(13, 8)
            },
            "run": {
                "down": sprite_sheet.get_animation_frames(2, 8),
                "left": sprite_sheet.get_animation_frames(6, 8),
                "right": sprite_sheet.get_animation_frames(10, 8),
                "up": sprite_sheet.get_animation_frames(14, 8)
            }
        }
        
        self.animation_index = 0
        self.animation_speed = 0.2
        self.image = self.sprites["idle"]["down"][0]
    
    def update(self, keys):
        moved = False
        running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        speed = self.speed_run if running else self.speed_walk

        if keys[pygame.K_w]:
            self.y -= speed
            self.direction = "up"
            moved = True
        if keys[pygame.K_s]:
            self.y += speed
            self.direction = "down"
            moved = True
        if keys[pygame.K_a]:
            self.x -= speed
            self.direction = "left"
            moved = True
        if keys[pygame.K_d]:
            self.x += speed
            self.direction = "right"
            moved = True
        
        if moved:
            self.state = "run" if running else "walk"
            self.animation_index = (self.animation_index + self.animation_speed) % len(self.sprites[self.state][self.direction])
            self.image = self.sprites[self.state][self.direction][int(self.animation_index)]
        else:
            self.state = "idle"
            self.animation_index = (self.animation_index + self.animation_speed * 0.5) % len(self.sprites[self.state][self.direction])
            self.image = self.sprites[self.state][self.direction][int(self.animation_index)]
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

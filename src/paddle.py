import pygame

class Paddle(object):
    def __init__(self):
        self.rectangle = pygame.Rect((64, 54, 16, 16))
    def handle_move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rectangle.move_ip(-1,0)
        if key[pygame.K_RIGHT]:
            self.rectangle.move_ip(1,0)
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,128), self.rectangle)
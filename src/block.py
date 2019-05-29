import pygame

from pygame.math import Vector2
from pygame import Rect

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False


    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class GameBlock(KineticBlock):
    def __init__(self, position, width, height, color, hitPoints):
        super().__init__( position, width, height, color)
        self.hitPoints = hitPoints
        self.startHitPoints = hitPoints
    
    def draw(self, screen, pygame):
        if self.hitPoints > 0:
            pygame.draw.rect(screen, self.color, self.rectangle)
    
    def hit(self):
        self.hitPoints -= 1
        # reduce color
        for i, colorNum in enumerate(self.color):
            self.color[i] = colorNum*self.hitPoints/self.startHitPoints  
        if(self.hitPoints <= 0):
            # move off screen
            self.position.x = -1000
            
class Paddle(KineticBlock):
    pass
    def handle_move(self, is_left, is_right):
        speed = 8
        if is_left:
            self.rectangle.move_ip(-1 * speed,0)
            self.position.x -= speed
            print(self.rectangle)

        if is_right:
            self.rectangle.move_ip(speed,0)
            self.position.x += speed
            print(self.rectangle)
       
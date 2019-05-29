import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

import math

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2( 175, 700),
                                    Vector2(10*random.random() - 2, 10*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)
    # make all the game blocks
    numBlocksRow= 10
    numRows= 4
    for i in range(1, numBlocksRow * numRows +1):
        margin = 5
        blockHeight = 50
        blockWidth = (SCREEN_SIZE[0] - numBlocksRow*margin)/numBlocksRow
        row =  math.ceil(i/numBlocksRow)
        xPos = ( (blockWidth + margin) * i) - (blockWidth + margin)/2 - (row -1)*SCREEN_SIZE[0]
        yPos = row*blockHeight +margin*row 
        gameBlock = GameBlock(Vector2(xPos,yPos),blockWidth, blockHeight, [0, 200, 200], 3)
        object_list.append(gameBlock)

    paddle = Paddle(Vector2(200, 750), 100, 50, [0, 0, 255])
    object_list.append(paddle)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
    
    gameDone = True
    while gameDone: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        
        # see if all the game blocks are gone
        # changes to true if a block is still here 
        stillPlaying = False

        for object in object_list:
            handle_move = getattr(object, "handle_move", None)
            if callable(handle_move):
                handle_move(left, right)
            object.update()
            object.check_collision()
            if getattr(object, 'isAlive', None):
                if object.isAlive():
                    stillPlaying = True
            

                    
        # check if any game blocks left
        if stillPlaying == False:
            print('YOU WON')
            gameDone = False
        
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            # check if ball is dead
            if getattr(ball, 'dead', None) and ball.dead == True:
                print('You Lose')
                gameDone = False
            ball.draw(screen, pygame)
        for paddle in object_list:
            paddle.draw(screen, pygame)
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()

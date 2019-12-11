# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:38:36 2019

@author: AdamChen
"""
import pygame
import sys
import time
import random
from pygame.locals import *

# define color
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(150,150,150)
lightColor = pygame.Color(220,220,220)


# define game over
def gameOver(playSurface, score):
    # show game over info
    gameOverFont = pygame.font.SysFont('comicsansms', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 125)
    playSurface.blit(gameOverSurf, gameOverRect)
    
    # show score
    scoreFont = pygame.font.SysFont('comicsansms', 48)
    scoreSurf = scoreFont.render('Score: ' + str(score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (320, 225)
    playSurface.blit(scoreSurf, scoreRect)
    
    # render display
    pygame.display.flip()
    
    # sleep 5 sec and than power off
    time.sleep(5)
    pygame.quit()
    sys.exit()
    
def main():
    
    # init pygame
    pygame.init()
    fpsClock = pygame.time.Clock()

    # create pygame display
    playSurface = pygame.display.set_mode((640, 480))

    # define title
    pygame.display.set_caption('Snack go!!!')

    # load pic
    # image = pygame.image.load('teddy_balloon.ico')

    # set icon
    # pygame.display.set_icon(image)
    
    # initial data
    snakePosition = [100, 100]
    snakeSegments = [[100, 100], [100, 100], [100, 100]]
    rasebarryPositioin = [300, 300]
    rasebarrySpawned = 1
    direction = 'right'
    changeDirection = direction
    score = 0
    
    while True:
    
        # key event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        
        # check direction
        if changeDirection == 'right' and not changeDirection == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not changeDirection == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not changeDirection == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not changeDirection == 'up':
            direction = changeDirection

        # snake position
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
            
        snakeSegments.insert(0, list(snakePosition))

        # check eat
        if snakePosition[0] == rasebarryPositioin[0] and \
            snakePosition[1] == rasebarryPositioin[1]:
                rasebarrySpawned = 0
        else:
            snakeSegments.pop()
            
        # regenerate barry tree
        if rasebarrySpawned == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            rasebarryPositioin = [int(x*20), int(y*20)]
            rasebarrySpawned = 1
            score += 1

        # refleash display
        playSurface.fill(blackColor)
        for position in snakeSegments[1:]:
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))

        pygame.draw.rect(playSurface, lightColor, Rect(snakePosition[0], snakePosition[1], 20, 20))
        pygame.draw.rect(playSurface, redColor, Rect(rasebarryPositioin[0], rasebarryPositioin[1], 20, 20))
        # refleash display
        pygame.display.flip()

        # check death
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface, score)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver(playSurface, score)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface, score)

        # control game speed
        if len(snakeSegments) < 40:
            speed = 6 + len(snakeSegments)//4
        else:
            speed = 16
        fpsClock.tick(speed)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

import pygame
import sys
import math

def Main():
    pygame.init()
    
    size = width, height = 800, 800
    font = pygame.font.SysFont("freesansbold.ttf", 50)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    black = 0, 0, 0
    red = 255, 0, 0
    white = 255, 255, 255
    alpha = 1
    n = 3
    line = []
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    n +=1
                elif event.key == pygame.K_DOWN:
                    if n > 1:
                        n -=1

        screen.fill(black)
        xc = 250
        yc = 400
        for i in range(n):
            

            xi = i * 2 + 1
            alpha = (alpha + (1/(5*n) * clock.get_rawtime())) % 360
            a = math.radians(alpha)

            raggio = 100 * 4 / (math.pi * xi) 
            x = xc + int(raggio  * math.cos(a * xi))
            y = yc + int(raggio  * math.sin(a * xi))

            txt = "n:" + str(n) + " freccia su n+1, freccia giù n -1"
            text = font.render(txt, False, white)
            screen.blit(text,(10,10))
            pygame.draw.circle(screen, white, (xc, yc), int(raggio), 1)
            pygame.draw.line(screen, red, (xc, yc), (x, y))
            xc = int(x)
            yc = int(y)
        
        pygame.draw.line(screen, white, (x, y), (500, y))
        line.append((500,y))
        xb = 500
        yb = y
        for i in range(len(line) - 2, 0, -1):
            xp, yp = line[i]
            xp +=1
            line[i] = xp, yp
            pygame.draw.line(screen, white, (xb, yb), (xp, yp))
            xb = xp
            yb = yp
            
        pygame.display.flip()
        clock.tick()


if __name__=="__main__":
    Main()
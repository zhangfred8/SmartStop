import pygame
from time import sleep
from pygame.locals import*

WIDTH = 800
HEIGHT = 480
pygame.init()
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
##rect = pygame.Rect(0,0, WIDTH, HEIGHT)
flash = pygame.Color(255,0,0)
noFlash = pygame.Color(0,0,0)

##flash0 = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/flash0.png')
##flash1 = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/flash1.png')
##noFlash = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/noFlash.png')


flashing = 0

# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    global flashing
##    pygame.draw.rect(windowSurface, flash, rect)
    if (num == 0 and flashing == 0):
        #windowSurface.blit(flash0, (0,0))
        windowSurface.fill(flash)
        flashing = 1
    elif (num == 0 and flashing == 1):
##        windowSurface.blit(flash1, (0,0))
        windowSurface.fill(noFlash)
        flashing = 0
    elif (num == 1):
##        windowSurface.blit(noFlash, (0,0))
        windowSurface.fill(noFlash)
        flashing = 0

    sleep(0.5)
    pygame.display.update()

test = [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]
for x in test:
    chooseIm(x)

import os
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("background.jpg")
screen.blit(pygame.transform.scale(pic, (900, 800)), (0, 0))
pygame.display.flip()
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()



clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
import pygame
import random
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
pygame.init()
class lag_stuff(pygame.sprite.Sprite):
    def __init__(self):
        super(lag_stuff, self).__init__()
        self.image = pygame.image.load("./assets/explosion.png")
    def update(self, screen):
        screen.blit(self.image, (100, 100))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
laggy_stuff = []
while True:
    laggy_stuff.append(lag_stuff())
    for lag in laggy_stuff:
        lag.update(screen)
pygame.display.flip()
clock.tick(1)
pygame.display.set_caption("FPS: " + str(clock.get_fps()))
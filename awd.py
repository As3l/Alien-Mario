import pygame

# initialize the pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("FUGITIVE")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# logo of the game
logo = pygame.image.load("runer-silhouette-running-fast (1).png")
pygame.display.set_icon(logo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



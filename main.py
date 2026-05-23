import pygame

# initialize the pygame
pygame.init()

# fps
frames = pygame.time.Clock()

# screen
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("ALIEN Mario")

# logo of the game
logo = pygame.image.load("runer-silhouette-running-fast (1).png")
pygame.display.set_icon(logo)

# surface, background
backgroundImage = pygame.image.load("background.png")
BACKGROUND = pygame.transform.scale(backgroundImage, (1000, 600))

# gravity and movement properties
gravity = -10
vel = 9
jumping = False

# properties of the alien
Xaxis, Yaxis = 250, 500
alien_change = 0
alien = pygame.image.load("alien (1).png")
alien_rect = alien.get_rect()
alien2 = pygame.image.load("alien (1).png")#second alien
alien_rect2 = alien2.get_rect()

#obstacle properties
soldier1 = pygame.image.load("soldier.png")
soldier_rect = soldier1.get_rect()
soldier2 = pygame.image.load("soldier.png")#second obstacle
soldier_rect2 = soldier2.get_rect()
soldier3 = pygame.image.load("soldier.png")#third obstacle
soldier_rect3 = soldier3.get_rect()
soldier4 = pygame.image.load('soldier.png')#fourth obstacle
soldier_rect4 = soldier4.get_rect()
racket = pygame.image.load("rocket-launch.png")#destination
racket_rect = racket.get_rect()
obs_Xaxis = 160
obs_Yaxis = 500


def player(x, y):
    screen.blit(BACKGROUND, (0, 0))#draw the background
    screen.blit(alien,(Xaxis,Yaxis)) #draw the character
    screen.blit(alien2, (x -250,y))

def OBSTACLE(x,y):
    screen.blit(soldier1, (x, y))
    screen.blit(soldier2, (x +190, y))
    screen.blit(soldier3, (x +220,y))
    screen.blit(soldier4, (x +420,y))
    screen.blit(racket, (x +780,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # JUMPING CODE
    if keys[pygame.K_SPACE] and not jumping:
        gravity = -23
        jumping = True
    #movement code
    if keys[pygame.K_d]:
        Xaxis += vel
    if keys[pygame.K_a]:
        Xaxis -= vel

    #apply gravity
    gravity += 1.5
    Yaxis += gravity

    # Floor collision so that it won't go down
    if Yaxis >= 500:
        Yaxis = 500
        gravity = 0
        jumping = False

    #update the position
    alien_rect.topleft = (Xaxis, Yaxis)
    alien_rect2.topleft = (Xaxis -250 , Yaxis)
    soldier_rect.topleft = (obs_Xaxis, obs_Yaxis)
    soldier_rect2.topleft = (obs_Xaxis +190, obs_Yaxis)
    soldier_rect3.topleft = (obs_Xaxis +220, obs_Yaxis)
    soldier_rect4.topleft = (obs_Xaxis +420, obs_Yaxis)
    racket_rect.topleft = (obs_Xaxis +780, obs_Yaxis)

    # collision between alien and soldiers
    if (alien_rect.colliderect(soldier_rect) or alien_rect.colliderect(soldier_rect2) or alien_rect.colliderect(soldier_rect3) or alien_rect.colliderect(soldier_rect4) or alien_rect2.colliderect(soldier_rect) or alien_rect2.colliderect(soldier_rect2) or alien_rect2.colliderect(soldier_rect3) or alien_rect2.colliderect(soldier_rect4)):
        print("GAME OVER")
        running = False
    if alien_rect2.colliderect(racket_rect):
        print("VICTORY")
        running = False     

    player(Xaxis, Yaxis)
    OBSTACLE(obs_Xaxis, obs_Yaxis)
    pygame.display.update()
    frames.tick(60)

pygame.quit()

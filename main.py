import pygame
import math
import random

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((800,600))
# Icon for window
eagleIcon = pygame.image.load('eagle.png')
pygame.display.set_icon(eagleIcon)
# Window Name
pygame.display.set_caption("Eagle Glide - pygame project")

# Window Background
cloudsBack = pygame.image.load('26302.jpg')


# Playable Character
eagleR = pygame.image.load('eagle.png')
eagleX = 10
eagleY = 500
eagleC = 0.5
def eagle (x,y):
    window.blit(eagleR, (eagleX, eagleY))
# Tree (Obstacles)
"""
treeO = pygame.image.load('tall-tree (1).png')
treeX = 400
treeY = 471
treeNum = 10
count = 420
treeC = 0.7
"""


# Multiple Trees Code
treeO = []
treeX = []
treeY = []
treeNum = 50
treeC = []
changeX = 420

for tM in range(treeNum):
    treeO.append(pygame.image.load('tall-tree (1).png'))
    # if tM == 0:
    #     treeX.append()
    # else:
    treeX.append(changeX)
    changeX += random.randint(300,500)
    treeY.append(471)
    treeC.append(0.7)

def tree(x, y, z):
    window.blit(treeO[z], (x, y))



# Check collision
def collision(eX, eY, tX, tY):
    distance = math.sqrt(math.pow((eX-tX), 2) + math.pow((eY - tY), 2))
    return distance
    # print("The distance is: ", distance)

overImage = pygame.image.load('game-over-art.jpg')


score = 0
game = True
condition = True
# Infinited While loop
while condition:

    window.fill((255, 255, 255))
    window.blit(cloudsBack, (0,0))
    for event in pygame.event.get():

        # When the window is closed condition
        if event.type == pygame.QUIT:
            print("Window is closed")
            condition = False
        # Space Clicked (Jump)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                eagleC -= 1
                print("FLY")
        if event.type == pygame.KEYUP:
                eagleC += 1
                print("DOWN")

    eagleY += eagleC

    # Eagle Boundaries
    if eagleY <= 300:
        eagleY = 300
    if eagleY >= 500:
        eagleY = 500

    # Tree Movement
    score = 0
    for i in range(treeNum):
        treeX[i] -= treeC[i]
        d = collision(eagleX, eagleY, treeX[i], treeY[i])
        rD = round(d)
        # Game Over
        if 50 > rD > 45:
            game = False
            break
        if eagleY == treeY[i] and eagleX == treeX[i]:
            score += 1
            print(score)
        tree(treeX[i], treeY[i], i)



    eagle(eagleX, eagleY)
    if game is False:
        window.blit(overImage, (0, 0))
    pygame.display.update()


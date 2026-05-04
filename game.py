BlockingIOError
import pygame
import random
import time

pygame.init()

windowWidth = 1650
windowHeight = 900
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("UFO")
gameover = False
gameoverImage = pygame.image.load("gameover.png")
gameoverImage = pygame.transform.scale(gameoverImage, (windowWidth, windowHeight))
level1 = pygame.image.load("levelone.png")
level2 = pygame.image.load("leveltwo.png")
level3 = pygame.image.load("finallevel.png")


backgroundImage = pygame.image.load("space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))
meteors = []
spawntimer = 0
leveltimer = 0


class Player:
    def __init__(self, x, y, image, up, left, right, width, height):
        self.position = pygame.Rect(x, y, width, height)
       # self.image = pygame.image.load(image)
       # self.image = pygame.transform.scale(self.image, (width, height))
        self.speedX = 0
        self.speedY = 0 
        self.up = up
        self.left = left
        self.right = right

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.right]:
            self.speedX = 15
        elif keys[self.left]:
            self.speedX = -15
        else:
            self.speedX = 0

        self.position.x += self.speedX
        self.position.y += self.speedY

        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > windowWidth - self.position.width:
            self.position.x = windowWidth - self.position.width
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y > windowHeight - self.position.height:
            self.position.y = windowHeight - self.position.height

    def __str__(self):
        return f"{self.position.x} {self.position.y} {self.position.width} {self.position.height}"

class Meteor:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
    def __str__(self):
        return f"{self.position.x} {self.position.y} {self.position.width} {self.position.height}"


    

    

ufo = Player(1000, 900, "ufo.png", pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 200, 200)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(meteors)):
        meteors[i].position.y += 5 

    window.blit(backgroundImage, (0, 0))
    ufo.move()

    spawntimer += 1
    leveltimer += 1


    if 0 < leveltimer < 1000:
        if spawntimer > 50:  
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 100, 100))
                spawntimer = 0 
                window.blit(level1, (0, 0))
    elif 1000 < leveltimer < 2500:
         if spawntimer > 30:  
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 100, 100))
                spawntimer = 0
                window.blit(level2, (0, 0))
    elif 2500 < leveltimer:
        if spawntimer > 10:  
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 100, 100))
                spawntimer = 0
                window.blit(level3, (0, 0))
  
    
    #window.blit(ufo.image, ufo.position)
    window.fill("#fc0303", ufo)


    for i in range(len(meteors)):
        window.blit(meteors[i].image, meteors[i].position)

    for j in range(len(meteors)):
        if ufo.position.colliderect(meteors[j].position):
            gameover = True
            print(meteors[j], ufo)

    if gameover == True:
        window.blit(gameoverImage, (0, 0))
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
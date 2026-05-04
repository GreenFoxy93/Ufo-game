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
meteor_speed = 5

font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 100)

backgroundImage = pygame.image.load("space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))
meteors = []
levels = ["Level 1", "Level 2", "Final level"]
facts = [
    "It would take nine years to walk to the moon.",
    "A day on Venus is longer than a year.",
    "There are more stars than grains of sand.",
    "Black holes can bend time.",
    ]

spawntimer = 0
leveltimer = 0
current_fact = random.choice(facts)



class Player:
    def __init__(self, x, y, image, up, left, right, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
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

class Meteor:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

ufo = Player(1000, 900, "ufo.png", pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 100, 100)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(meteors)):
        meteors[i].position.y += meteor_speed

    window.blit(backgroundImage, (0, 0))
    ufo.move()

    spawntimer += 1
    leveltimer += 1
    meteor_speed += 0.002 

    if 0 < leveltimer < 1000:
        level = font2.render(levels[0], True, (255, 144, 144))
        window.blit(level, (10, 10))
        if spawntimer > 15:  
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 50, 50))
                spawntimer = 0 

    elif 1000 < leveltimer < 2500:
         level = font2.render(levels[1], True, (255, 82, 82))
         window.blit(level, (10, 10)) 
         if spawntimer > 5: 
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 50, 50))
                spawntimer = 0
    elif 2500 < leveltimer:
        level = font2.render(levels[2], True, (255, 16, 16))
        window.blit(level, (10, 10))
        if spawntimer > 2:  
                meteors.append(Meteor(random.randint(0, 1650), 0, "meteor.png", 50, 50))
                spawntimer = 0
                

  
    
    window.blit(ufo.image, ufo.position)


    for i in range(len(meteors)):
        window.blit(meteors[i].image, meteors[i].position)

    for j in range(len(meteors)):
        if ufo.position.colliderect(meteors[j].position):
            gameover = True
            print(meteors[j], ufo)

    if gameover == True:
        window.blit(gameoverImage, (0, 0))
        randomfact = font.render(current_fact, True, (255, 255, 255))
        window.blit(randomfact, (10, 10))

    
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
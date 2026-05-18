BlockingIOError
import pygame
import random

pygame.init()

# all the window settings. do not touch
windowWidth = 1650
windowHeight = 900
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("UFO")

#fonts
font = pygame.font.SysFont(None, 50) #facts 
font2 = pygame.font.SysFont(None, 100) #level
font3 = pygame.font.SysFont(None, 90) #score
font4 = pygame.font.SysFont('arial', 150) #start

#loading images
gameoverImage = pygame.image.load("gameover.png")
gameoverImage = pygame.transform.scale(gameoverImage, (windowWidth, windowHeight))
backgroundImage = pygame.image.load("space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))
startImage = pygame.image.load("startbackground.png")
startImage = pygame.transform.scale(startImage, (windowWidth, windowHeight))

images = ["meteor.png", "meteor2.png", "meteor4.png", "ufo.png"]
meteors = []
flashes = []
shields = []
startscreen = []
levels = ["Level 1", "Level 2", "Final level"]
facts = [
    "It would take nine years to walk to the moon.",
    "A day on Venus is longer than a year.",
    "There are more stars than grains of sand.",
    "Black holes can bend time.",
    "One million Earths could fit inside the Sun.",
    "One year on Mercury is only 88 Earth days.",
    "Saturn could float in water because it is mostly gas.",
    "The International Space Station orbits Earth every ~90 minutes."
    ]


start = False
gameover = False

meteor_speed = 5
spawntimer = 0
forfun = 0
leveltimer = 0
flashtimer = 0
protectiontimer = 500
speedtimer = 600
current_fact = random.choice(facts)
#facts.remove(current_fact)
highscore = 0
score = 0
factnumber = 1
pressr = "Press 'r' to restart"
game = "THE UFO GAME"
pressenter = "Press 'space' to start"
speed = False


beginning = font.render(game, True, (255, 255, 255))
enter = font.render(pressenter, True, (255, 255, 255))
endofgame = font3.render(pressr, True, (150, 255, 255))
theufogame = font4.render(game, True, (200, 200, 255))
enterpress = font3.render(pressenter, True, (0, 200, 255))

class Player:
    def __init__(self, x, y, image, up, left, right, width, height, speed):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed = speed
        self.speedX = 0
        self.speedY = 0
        self.up = up
        self.left = left
        self.right = right

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.right]:
            self.speedX = self.speed
        elif keys[self.left]:
            self.speedX = (self.speed - 2*self.speed)
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

class Powerup:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

class Justforfun:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(-3, 3)
        if self.speedx == 0:
            self.speedx = random.randint(-3, 3)
        if self.speedy == 0:
            self.speedy = random.randint(-3, 3)

    def startmoving(self):
        
        self.position.x += self.speedx
        self.position.y += self.speedy

        if self.position.x < 0:
            self.speedx *= -1
        if self.position.x > windowWidth - self.position.width:
            self.speedx *= -1
        if self.position.y < 0:
            self.speedy *= -1
        if self.position.y > windowHeight - self.position.height:
            self.speedy *= -1


ufo = Player(500, 900, "ufo.png", pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 100, 100, 15)

#glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka#
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    menu = True
    window.blit(startImage, (0, 0))

    forfun += 1
    if forfun == 20:
        if len(startscreen) <= 50:
            startscreen.append(Justforfun(random.randint(0, (windowWidth - 100)), random.randint(0, (windowHeight - 100)), random.choice(images), 100, 100))
        forfun = 0


    for i in range(len(startscreen)):
        window.blit(startscreen[i].image, startscreen[i].position)
        startscreen[i].startmoving()

    window.blit(theufogame, (10, 600))
    window.blit(enterpress, (20, 800))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True
    
    if start == True:

        #window.blit(backgroundImage, (0, 0))
        window.blit(beginning, (500, 500))
        window.blit(enter, (500, 600))

        spawntimer += 1
        leveltimer += 1
        flashtimer += 1
        meteor_speed += 0.004
        score += 1
        speedtimerforscreen = f"Speed time left: {speedtimer}"
        factsunlocked = f"Facts unlocked: {factnumber}/8"
        scoreboard = f"Score: {score}"
        highscoreboard = f"Highscore: {highscore}"
        randomfact = font.render(current_fact, True, (255, 155, 155))
        size = random.randint(30, 150)
        size2 = random.randint(100, 200)
        size3 = random.randint(25, 70)
        randomnumber = random.randint(1, 3)

        def spawnmeteors():
            if randomnumber == 1:
                meteors.append(Meteor(random.randint(-20, 1350), -100, "meteor.png", size2, size2))
            elif randomnumber == 2:
                meteors.append(Meteor(random.randint(-20, 1350), -100, "meteor4.png", size2, size2))
            elif randomnumber == 3:
                meteors.append(Meteor(random.randint(-20, 1350), -100, "meteor2.png", size2, size2))
            
        

        for i in range(len(meteors)):
            meteors[i].position.y += meteor_speed

        for i in range(len(flashes)):
            flashes[i].position.y += meteor_speed

        window.blit(backgroundImage, (0, 0))
        ufo.move()
        window.blit(ufo.image, ufo.position)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
                current_fact = random.choice(facts)

        for i in range(len(meteors)):
            window.blit(meteors[i].image, meteors[i].position)

        if 0 < leveltimer < 1000:
            level = font2.render(levels[0], True, (255, 144, 144))
            window.blit(level, (10, 10))
            if spawntimer > 18:   #20 18 is best
                    spawnmeteors()
                    spawntimer = 0 
        elif 1000 < leveltimer < 2500:
            level = font2.render(levels[1], True, (255, 82, 82))
            window.blit(level, (10, 10)) 
            if spawntimer > 8:  #7 8 is good
                    spawnmeteors()
                    spawntimer = 0
        elif 2500 < leveltimer:
            level = font2.render(levels[2], True, (255, 16, 16))
            window.blit(level, (10, 10))
            if spawntimer > 5:  #2 5 is good
                    spawnmeteors()
                    spawntimer = 0

        

        scr = font.render(scoreboard, True, (255, 255, 255))
        window.blit(scr, (1300, 10))
        highscr = font.render(highscoreboard, True, (255, 255, 255))
        window.blit(highscr, (1300, 50))
        unlocked = font.render(factsunlocked, True, (255, 255, 255))
        speedtimeronscreen = font.render(speedtimerforscreen, True, (150, 255, 100))

        # flashes settings, shield settings

        if random.randint(300, 1000) < flashtimer:
            flashes.append(Powerup(random.randint(-20, 1350), -100, "flash.png", 100, 100))
            flashtimer = 0

        if ufo.speed > 15:
            window.blit(speedtimeronscreen, (1300, 90))
            speedtimer -= 1
    

        for flash in flashes[:]:
            if ufo.position.colliderect(flash.position):
                ufo.speed = 35
                speedtimer = 500
                flashes.remove(flash)

        if speedtimer == 0:
            ufo.speed = 15
            speedtimer = 500
                    
        for i in range(len(flashes)):
            window.blit(flashes[i].image, flashes[i].position)
            
        for j in range(len(meteors)):
            if ufo.position.colliderect(meteors[j].position):
                gameover = True
            
        if gameover == True:
            if score > highscore:
                highscore = score
            window.blit(gameoverImage, (0, 0))
            #window.blit(unlocked, (10, 500))
            window.blit(endofgame, (530, 770))
            window.blit(randomfact, (10, 10))
            window.blit(scr, (10, 70))
            window.blit(highscr, (10, 110))

            
            score -= 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                meteors = []
                flashes = []
                ufo.speed = 15
                gameover = False
                spawntimer = 0
                leveltimer = 0
                meteor_speed = 5
                ufo.position.x = 1000
                ufo.position.y = 900
                score = 0
                score += 1
                ufo.speed = 15
                speedtimer = 500
                
                #if factnumber < 8:
                    #facts.remove(current_fact)

                #if factnumber > 8:
                    #factsunlocked == "You unlocked all facts!"
                #factnumber += 1
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()

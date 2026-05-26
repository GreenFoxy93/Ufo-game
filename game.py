BlockingIOError
import pygame
import random

pygame.init()

# all the window settings. do not touch
windowWidth = 1350
windowHeight = 750
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("UFO")

#fonts
font = pygame.font.SysFont(None, 50) #facts 
font2 = pygame.font.SysFont(None, 100) #level, controls
font3 = pygame.font.SysFont(None, 90) #score
font4 = pygame.font.SysFont('arial', 150) #start
font5 = pygame.font.SysFont(None, 60) #start


#loading images
gameoverImage = pygame.image.load("gameover.png")
gameoverImage = pygame.transform.scale(gameoverImage, (windowWidth, windowHeight))
backgroundImage = pygame.image.load("space.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))
startImage = pygame.image.load("startbackground.png")
startImage = pygame.transform.scale(startImage, (windowWidth, windowHeight))
meteor_img = pygame.image.load("meteor.png")
meteor2_img = pygame.image.load("meteor2.png")
meteor4_img = pygame.image.load("meteor4.png")
ufo_img = pygame.image.load("ufo.png")
oldufo_img = pygame.image.load("oldufo.png")
flash_img = pygame.image.load("flash.png")
shield_img = pygame.image.load("shield.png")
controlsrect = pygame.Rect(1090, 10, 200, 60)


images = ["meteor.png", "meteor2.png", "meteor4.png", "oldufo.png"]
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

state = "menu"

meteor_speed = 5
spawntimer = 0
forfun = 0
leveltimer = 0
shieldtimer = 0
flashtimer = 0
protectiontimer = 0
speedtimer = 600
current_fact = random.choice(facts)
score = 0
factnumber = 1
pressr = "Press 'r' to restart"
gametitle = "THE UFO GAME"
pressenter = "Press 'space' to start"
controls = "Controls"
speed = False
try:
    with open("highscore.txt", "r") as file:
        highscore = int(file.read())
except:
    highscore = 0

beginning = font.render(gametitle, True, (255, 255, 255))
enter = font.render(pressenter, True, (255, 255, 255))
endofgame = font3.render(pressr, True, (150, 255, 255))
theufogame = font4.render(gametitle, True, (200, 200, 255))
enterpress = font3.render(pressenter, True, (0, 200, 255))
controlsbutton = font5.render(controls, True, (255, 255, 255))


class Player:
    def __init__(self, x, y, image, up, left, right, width, height, speed):
        self.position = pygame.Rect(x, y, width, height)
        self.image = image
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
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
class Powerup:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
class Justforfun:
    def __init__(self, x, y, image, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(-3, 3)
        if self.speedx == 0:
            self.speedx = random.uniform(-3, 3)
        if self.speedy == 0:
            self.speedy = random.uniform(-3, 3)

    def startmoving(self):
        self.realspeedx = int(self.speedx)
        self.realspeedy = int(self.speedy)

        self.position.x += self.realspeedx
        self.position.y += self.realspeedy

        if self.position.x < 0:
            self.speedx *= -1
        if self.position.x > windowWidth - self.position.width:
            self.speedx *= -1
        if self.position.y < 0:
            self.speedy *= -1
        if self.position.y > windowHeight - self.position.height:
            self.speedy *= -1

ufo = Player(650, 670, ufo_img, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 85, 45, 15)

def spawnmeteors():
            randomnumber = random.randint(1, 3)
            if randomnumber == 1:
                meteors.append(Meteor(random.randint(-20, 1350), -100, meteor_img, size2, size2))
            elif randomnumber == 2:
                meteors.append(Meteor(random.randint(-20, 1350), -100, meteor2_img, size2, size2))
            elif randomnumber == 3:
                meteors.append(Meteor(random.randint(-20, 1350), -100, meteor4_img, size2, size2))

#glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka##glavna zanka#
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if controlsrect.collidepoint(event.pos):
                state = "controls"

        if event.type == pygame.KEYDOWN:
            if state == "menu" and event.key == pygame.K_SPACE:
                state = "game"

            if event.key == pygame.K_ESCAPE:
                state = "menu"
                meteors.clear()
                flashes.clear()

                spawntimer = 0
                leveltimer = 0
                flashtimer = 0

                ufo.speed = 15
                meteor_speed = 5 
                score = 0
                protectiontimer = 0

                
            if state == "gameover" and event.key == pygame.K_r:
                state = "game"
                meteors = []
                flashes = []
                shields = []
                ufo.speed = 15
                spawntimer = 0
                leveltimer = 0
                meteor_speed = 5
                ufo.position.x = 650
                ufo.position.y = 670
                score = 0
                speedtimer = 500
                protectiontimer = 0

    if state == "controls":
        window.blit(startImage, (0, 0))
        y = 20

        controls =["Move: Left / Right arrows", "Avoid meteors", "Pick up flash = speed","Pick up shield = protection", "ESC = back"]
        for control in controls:
            text = font3.render(control, True, (100, 240, 240))
            y += 100
            window.blit(text, (100, y))

        escape = "To go to the menu, press ESC"
        backtomenu = font.render(escape, True, (255, 255, 255))
        window.blit(backtomenu, (800, 700))

    if state == "menu":
        window.blit(startImage, (0, 0))
        forfun += 1
        if forfun == 20:
            if len(startscreen) <= 50:
                sizehere = random.randint(50, 200)
                startscreen.append(Justforfun(random.randint(0, (windowWidth - (sizehere + 10))), random.randint(0, (windowHeight - (sizehere + 10))), random.choice(images), sizehere, sizehere))
            forfun = 0

        for i in range(len(startscreen)):
            window.blit(startscreen[i].image, startscreen[i].position)
            startscreen[i].startmoving()

        window.blit(theufogame, (10, 400)) 
        window.blit(enterpress, (20, 600)) 
        pygame.draw.rect(window, (100, 180, 180), controlsrect)
        window.blit(controlsbutton, (1100, 15))
        
    
    if state == "game":
        spawntimer += 1
        leveltimer += 1
        flashtimer += 1
        shieldtimer += 1
        meteor_speed += 0.004
        score += 1
        randomcolor1 = random.randint(70, 255)
        randomcolor2 = random.randint(70, 255)
        randomcolor3 = random.randint(70, 255)
        randomfact = font.render(current_fact, True, (randomcolor1, randomcolor2, randomcolor3))
        speedtimerforscreen = f"Speed time left: {speedtimer}"
        protectiontimerforscreen = f"Protection time left: {protectiontimer}"
        if factnumber >= 8:
            factsunlocked = "You unlocked all facts!"
        else:
            factsunlocked = f"Facts unlocked: {factnumber}/8"
        scoreboard = f"Score: {score}"
        highscoreboard = f"Highscore: {highscore}"
        size = random.randint(30, 150)
        size2 = random.randint(100, 200)
        size3 = random.randint(25, 70)
        
            
        for meteor in meteors:
            meteor.position.y += meteor_speed

        for flash in flashes:
            flash.position.y += meteor_speed

        for shield in shields:
            shield.position.y += meteor_speed

        window.blit(backgroundImage, (0, 0))
        ufo.move()
        window.blit(ufo.image, ufo.position)

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_r]:
                current_fact = random.choice(facts)

        for meteor in meteors:
            window.blit(meteor.image, meteor.position)

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
        window.blit(scr, (1000, 10))
        highscr = font.render(highscoreboard, True, (255, 255, 255))
        window.blit(highscr, (1000, 50))
        unlocked = font.render(factsunlocked, True, (255, 150, 255))
        speedtimeronscreen = font.render(speedtimerforscreen, True, (250, 250, 150))
        protectiontimeronscreen = font.render(protectiontimerforscreen, True, (150, 250, 250))

        # flash settings
        if random.randint(300, 1000) < flashtimer:
            flashes.append(Powerup(random.randint(-20, 1350), -100, flash_img, 60, 90))
            flashtimer = 0

        if random.randint(700, 7000) < shieldtimer:
            shields.append(Powerup(random.randint(-20, 1350), -100, shield_img, 70, 80))
            shieldtimer = 0

        if ufo.speed > 15:
            window.blit(speedtimeronscreen, (10, 90))
            speedtimer -= 1
    
        for flash in flashes[:]:
            if ufo.position.colliderect(flash.position):
                ufo.speed = 35
                speedtimer = 500
                flashes.remove(flash)

        for shield in shields[:]:
            if ufo.position.colliderect(shield.position):
                protectiontimer = 300
                shields.remove(shield)

        if protectiontimer > 0:
            protectiontimer -= 1
            if ufo.speed > 15:
                window.blit(protectiontimeronscreen, (10, 150))
            else:
                window.blit(protectiontimeronscreen, (10, 90))
        
        if protectiontimer <= 0:
            ufo.protection = False

        if speedtimer == 0:
            ufo.speed = 15
            speedtimer = 500
                    
        for flash in flashes:
            window.blit(flash.image, flash.position)

        for shield in shields:
            window.blit(shield.image, shield.position)
            
        for meteor in meteors:
            if ufo.position.colliderect(meteor.position):
                if protectiontimer > 0:
                    pass
                else:
                    state = "gameover"

        if state == "gameover": 
            window.blit(gameoverImage, (0, 0))
            if score > highscore:
                highscore = score
            with open("highscore.txt", "w") as file:
                file.write(str(highscore))
            window.blit(endofgame, (370, 600))
            if factnumber == 8:
                window.blit(scr, (10, 70))#10
                window.blit(highscr, (10, 100))#50
                window.blit(unlocked, (10, 10))#90
            else:
                window.blit(scr, (10, 130)) #70
                window.blit(highscr, (10, 170))#110
                window.blit(unlocked, (10, 70)) #150

            if factnumber < 8:
                window.blit(randomfact, (10, 10))

            if factnumber < 8:
                facts.remove(current_fact)
                factnumber += 1

            
            

                
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
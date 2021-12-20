import pygame
from random import randint

width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
pygame.display.set_caption("Kill the Monsters !!!!")

class Monster:
    def __init__(self):
        self.monster = pygame.image.load("monster.png")
        self.x = randint(0,width - self.monster.get_width())
        self.y = randint(-60,-40)
        self.hitmo = 0
        self.prev = -1
        
    def draw(self):
        screen.blit(self.monster, (self.x, self.y))
        
    def hit(self, hits):
        if hits != self.prev:
            self.hitmo += 1
            self.prev = hits
    
    def monspos(self):
        return (self.x, self.y)
        
    def falldown(self):
        self.y += 1
        
    def inground(self):
        if self.y + self.monster.get_height() < height:
            return True
        return False
        
    def dead(self):
        if self.hitmo == 3:
            return True
        return False
        
    def change(self):
        self.x = randint(0,width - self.monster.get_width())
        self.y = randint(-60,-40)
        self.hitmo = 0
        self.prev = -1

class Coin:
    def __init__(self):
        self.coin = coin = pygame.image.load("coin.png")
        self.x = randint(0,width - self.coin.get_width())
        self.y = 0
        
    def draw(self):
        screen.blit(self.coin, (self.x, self.y))
        
    def inground(self):
        if self.y + self.coin.get_height() < height:
            return True
        self.x = randint(0,width - self.coin.get_width())
        self.y = 0
        return False
        
    def coindown(self):
        self.y += 2
        
    def position(self):
        return (self.x, self.y)
        
    def nposition(self, x, y):
        self.x = x
        self.y = y

class Bullet:
    def __init__(self):
        self.x1 = 540
        self.y1 = height - robot.get_height()
            
    def goup(self):
        self.y1 -= 7
        pygame.draw.rect(screen, (255,51,51), (self.x1, self.y1, 10,10))
        if self.y1 < 0:
            self.y1 = height - robot.get_height()
        
    def bullpos(self):
        return (self.x1, self.y1)
        
    def roboaxis(self, robox):
        self.x1 = robox + 20
        
    def change(self):
        self.x1 = 540
        self.y1 = height - robot.get_height()
        
    def yaxis(self):
        return self.y1
Bestscore = 0
def main():
    pygame.init()
    font = pygame.font.SysFont("Arial",24)
    robot = pygame.image.load("robot.png")
    door = pygame.image.load("door.png")
    monster = pygame.image.load("monster.png")
    
    def Bestscorefun(points):
        if points*10> Bestscore:
            return True
        return False
    
    number  = 25
    robox = width//2
    roboy = height - robot.get_height()
    left = False
    Right = False
    up = False
    live = 3
    monsters = []
    coins = []
    bullets = []
    for i in range(number):
        monsters.append(Monster())
    for i in range(number):
        coins.append(Coin())  
    x = 540
    y = 700
    clock = pygame.time.Clock()
    index = 3

    for i in range(10):
        bullets.append(Bullet())

    bullnum = 30
    reloaded = False
    points  = 0

    k = 0
    c = 1080
    c1 = 540
    c2 = 0

    def level(points):
        if points%15 == 0:
            lev = points//15
        if points%16 == 0:
            lev = points//16
        return 3 + lev

    bullincrement = 10

    while True:
        screen.fill((102, 178, 255))
        pygame.draw.circle(screen, (255,128,0),(100, 50), 100)
        pygame.draw.ellipse(screen, (255, 255, 255), (-195+ c, 60, 150, 50))
        pygame.draw.ellipse(screen, (255, 255, 255), (-335+ c, 50, 225, 70))
        pygame.draw.ellipse(screen, (255, 255, 255), (-445 + c, 60, 150, 50))
        pygame.draw.ellipse(screen, (255, 255, 255), (-555+ c1, 80, 150, 50))
        pygame.draw.ellipse(screen, (255, 255, 255), (-655+ c1, 70, 225, 70))
        pygame.draw.ellipse(screen, (255, 255, 255), (-700 + c1, 80, 150, 50))
        pygame.draw.ellipse(screen, (192,192,192), (-1450+ c2, 60, 150, 50))
        pygame.draw.ellipse(screen, (192,192,192), (-1550+ c2, 50, 225, 70))
        pygame.draw.ellipse(screen, (192,192,192), (-1650 + c2, 60, 150, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and bullnum > 0:
                    bullets[k].roboaxis(robox)
                    bullnum -= 1
                    bullets[k].goup()
                    k += 1
                    if k == 10:
                        k = 0
                    up = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    Right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    Right = False
        
        if Right:
            if robox + robot.get_width() < 1076:
                robox += 8
        if left:
            if robox > 4:
                robox -= 8

        for bullet in bullets:
            if bullet.yaxis() < height - robot.get_height():
                bullet.goup()

        for i in range(index):
            if monsters[i].inground():
                monsters[i].falldown()
            if not monsters[i].inground():
                monsters[i].change()
                live -= 1
                if live <= 0:
                    game = True
                    while game:
                        pygame.draw.rect(screen, (102,0,204), (340, 200, 400,300))
                        fontexit = pygame.font.SysFont("freesansbold.ttf",60)
                        screen.blit(fontexit.render(" Final Score "+ str(points*10),True,(153,0,0)), (380,260))
                        screen.blit(fontexit.render("Press R to Continue",True,(0,0,0)), (340,320))
                        screen.blit(fontexit.render("Press X to Exit",True,(0,0,0)), (390,380))
                        global Bestscore
                        Bestscore = points*10 if Bestscorefun(points) else Bestscore
                        screen.blit(fontexit.render("Best Score "+ str(Bestscore),True,(0,0,0)), (390,440))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    game = False
                                if event.key == pygame.K_x:
                                    exit()

                    main()
            
        for c in range(index-2):
            if coins[c].inground():
                coins[c].coindown()
        
        for j in range(index-2):
            coins[j].draw()
        
        for b in range(index):
            pos = coins[b].position()
            if pos[0] in range(robox-robot.get_width(), robox+robot.get_width()) and pos[1] in range(height-100,height - robot.get_height()):
                coins[b].nposition(randint(0,1040), 0)
                points += 1
        
        for h in range(index):
            req = monsters[h].monspos()
            for a in range(10):
                bureq = bullets[a].bullpos()
                if bureq[0] in range(req[0], req[0] + monster.get_width()):
                    if bureq[1] in range(req[1]- monster.get_height(), req[1] + monster.get_height()):
                        monsters[h].hit(a)
                        bullets[a].change()
                        if monsters[h].dead():
                            points += 2
                            monsters[h].change()

        pygame.draw.rect(screen, (255,51,51), (955,35, 12,12))
        pygame.draw.circle(screen, (255,255,0),(960, 15), 12)
        bullleft = "Bullets " + str(bullnum)
        point = "1   Score " + str(points*10)
        leftlives = "$   Lives "
        livesym = "$ "*live
        text = font.render(point,True,(255,0,0))
        livesym = font.render(livesym,True,(0,102,0))
        bulltext = font.render(bullleft, True, (255,0,0))
        livetext = font.render(leftlives, True, (255,0,0))
        screen.blit(bulltext, (980,25))
        screen.blit(text,(955,0))
        screen.blit(livetext,(955,50))
        screen.blit(livesym, (1035,50))
        
        if bullnum > 27 and points == 0:
            screen.blit(font.render("Press ↑ to shoot and ← → to move",True,(0,0,102)), (400,35))
        for i in range(index):
            monsters[i].draw()
        
        if (points >= bullincrement and points <= bullincrement + 30) and points != 0 and not reloaded:
            bullnum = 30
            bullincrement += 10
            reloaded = True
        
        if (points%15 == 0 or points%16 == 0):
            reloaded = False
            index = level(points)

        screen.blit(robot,(robox, roboy))
        c += 1
        if c > 1500:
            c = 0
        c1 += 1
        if c1 > 1800:
            c1 = 0
        c2 += 1
        if c2 > 3000:
            c2 = 0
        y -= 7
        
        pygame.display.flip()
        clock.tick(60)

main()










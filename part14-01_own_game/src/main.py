#This games theme is to fight Monsters with a Robot and Collecting coins
#Sorry in advance for the long code as I tried to include many features and levels in the game 
#Sorry again
#The Pygame Module is imported
 
import pygame
from random import randint
 
#The height and width of the screen are initialized you can change it if you want
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
pygame.display.set_caption("Kill the Monsters !!!!")
 
#Moster Class
class Monster:
    #Initializing moster in a random position
    def __init__(self):
        self.monster = pygame.image.load("monster.png")
        self.x = randint(0,width - self.monster.get_width())
        self.y = randint(-60,-40)
        self.hitmo = 0
        self.prev = -1
 
    #Drawing monster in the screen   
    def draw(self):
        screen.blit(self.monster, (self.x, self.y))
 
    #It requires Three Bullets to kill a monster here we keep the count of bullet hits    
    def hit(self, hits):
        if hits != self.prev:
            self.hitmo += 1
            self.prev = hits
    
    #It returns monster position to compare with bullet position
    def monspos(self):
        return (self.x, self.y)
    
    #It makes the monster To fall down
    def falldown(self):
        self.y += 1
    
    #It checks if the monster touches the ground if yes player loses a life
    def inground(self):
        if self.y + self.monster.get_height() == height:
            return False
        return True
    
    #To check a monster is dead or not
    def dead(self):
        if self.hitmo == 3:
            return True
        return False
 
    #Change monster position to a random place if it is dead or touches ground   
    def change(self):
        self.x = randint(0,width - self.monster.get_width())
        self.y = randint(-60,-40)
        self.hitmo = 0
        self.prev = -1
 
#Coin class
class Coin:
    #initializing coin at random position
    def __init__(self):
        self.coin = coin = pygame.image.load("coin.png")
        self.x = randint(0,width - self.coin.get_width())
        self.y = 0
 
    #Drawing the coin in screen 
    def draw(self):
        screen.blit(self.coin, (self.x, self.y))
 
    #Checking if the coin has reached the ground if yes initialize a new position   
    def inground(self):
        if self.y + self.coin.get_height() < height:
            return True
        self.x = randint(0,width - self.coin.get_width())
        self.y = 0
        return False
 
    #Making the coin to fall down    
    def coindown(self):
        self.y += 2
    
    #Returns position of coin to compare with robot
    def position(self):
        return (self.x, self.y)
    
    #Initialize a new position
    def nposition(self, x, y):
        self.x = x
        self.y = y
 
#Bullet Class
class Bullet:
    #Initialize a bullet at the top of a robot
    def __init__(self):
        self.x1 = 540
        self.y1 = height - robot.get_height()
 
    #Makes the bullet to go up        
    def goup(self):
        self.y1 -= 7
        pygame.draw.rect(screen, (255,51,51), (self.x1, self.y1, 10,10))
        if self.y1 < 0:
            self.y1 = height - robot.get_height()
 
    #return Bullet position to compare with monster position    
    def bullpos(self):
        return (self.x1, self.y1)
    
    #returns the bullet at the top of robot
    def roboaxis(self, robox):
        self.x1 = robox + 20
    #reuse of bullet   
    def change(self):
        self.x1 = 540
        self.y1 = height - robot.get_height()
        
    def yaxis(self):
        return self.y1
 
#Class Raindrop for Rain
class Raindrop:
    #Initialize Raindrop at random position
    def __init__(self):
        self.x = randint(0,1080)
        self.y = randint(0,720)
    
    #Makes the rain to fall
    def getrain(self):
        self.y += 1
        pygame.draw.line(screen,(255,255,255),(self.x,self.y),(self.x,self.y+3),2)
        if self.y == 720:
            self.y = 0
                
#Keeps record of Best score since no File is used score gets reseted after the exit of application
Bestscore = 0
 
#Main function to Re initialize if game is over
def main():
    pygame.init()
    #Game images and font
    font = pygame.font.SysFont("Arial",24)
    robot = pygame.image.load("robot.png")
    monster = pygame.image.load("monster.png")
    
    #Return True if new Best score is greater than Old
    def Bestscorefun(points):
        if points*10> Bestscore:
            return True
        return False
    
    #necessary initialixation of variables and list of Monster, Coin, Bullet and Raindrop
    number  = 25
    robox = width//2
    roboy = height - robot.get_height()
    left = False
    Right = False
    live = 3
    monsters = []
    coins = []
    bullets = []
    rain = []
    for i in range(number):
        monsters.append(Monster())
    for i in range(number):
        coins.append(Coin()) 
    for r in range(1500):
        rain.append(Raindrop())
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
    rc = -500
 
    #After a certain score is reached this method is called and returns a new level
    def level(points):
        if points%20 == 0:
            lev = points//20
        if points%21 == 0:
            lev = points//21
        return 3 + lev
 
    bullincrement = 10
    helpreload = 4
 
    #Game loop !!
    while True:
        screen.fill((102, 178, 255))
        #Sun and Cloud
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
 
        #Event monitoring for exit, pause, Escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                axis = event.pos
                if axis[0] in range(9,30) and axis[1] in range(8,30):
                    pause = True
                    while pause:
                        pygame.draw.rect(screen, (102,0,204), (340, 200, 400,300))
                        fontpause = pygame.font.SysFont("freesansbold.ttf",60)
                        screen.blit(fontpause.render("  Game Paused ",True,(153,0,0)), (380,260))
                        screen.blit(fontpause.render("Press C to Continue",True,(0,0,0)), (340,320))
                        screen.blit(fontpause.render("Press X to Exit",True,(0,0,0)), (390,380))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    pause = False
                                if event.key == pygame.K_x:
                                    exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape = True
                    while escape:
                        pygame.draw.rect(screen, (102,0,204), (330, 200, 430,300))
                        pygame.draw.rect(screen, (255,0,0), (400, 400, 70,45))
                        pygame.draw.rect(screen, (0,255,0), (600, 400, 70,45))
                        fontpause = pygame.font.SysFont("freesansbold.ttf",60)
                        screen.blit(fontpause.render("Do you want to Exit ?",True,(153,0,0)), (330,260))
                        screen.blit(fontpause.render("Yes",True,(0,0,0)), (400,400))
                        screen.blit(fontpause.render(" No",True,(0,0,0)), (600,400))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.K_c:
                                    escape = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                axis = event.pos
                                if axis[0] in range(400,470) and axis[1] in range(400,445):
                                    exit()
                                if axis[0] in range(600,670) and axis[1] in range(400,470):
                                    escape = False
                    
            
            #Using Bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and bullnum > 0:
                    bullets[k].roboaxis(robox)
                    bullnum -= 1
                    bullets[k].goup()
                    k += 1
                    if k == 10:
                        k = 0
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    Right = True
 
            if event.type == pygame.KEYUP:
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
        
        #If point is greater than 40 it Rains in some random intervals
        if points >= 40:
            if rc == 550:
                screen.fill((0,128, 255))
            pygame.draw.ellipse(screen, (224,224,224), (130+rc, 4, 450, 150))
            pygame.draw.ellipse(screen, (224,224,224), (-200+rc, 5, 600, 160))
            pygame.draw.ellipse(screen, (224,224,224), (-800+rc, 0, 850, 150))
            pygame.draw.ellipse(screen, (192,192,192), (90+rc, -50, 450, 150))
            pygame.draw.ellipse(screen, (192,192,192), (-300+rc, -30, 650, 160))
            pygame.draw.ellipse(screen, (192,192,192), (-600+rc, -50, 850, 150))
            if rc < 550:
                rc += 1
            else:
                if points< 100:
                    for r in rain:
                        r.getrain()
                else:
                    rc += 1
                    if rc == 18000:
                        rc = -500
 
        #Making coins, monsters, bullets to work as required
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
                    #Game ends Here press P to play again
                    while game:
                        pygame.draw.rect(screen, (102,0,204), (340, 200, 420,300))
                        fontexit = pygame.font.SysFont("freesansbold.ttf",60)
                        screen.blit(fontexit.render(" Final Score "+ str(points*10),True,(153,0,0)), (380,260))
                        screen.blit(fontexit.render("Press P to Play again",True,(0,0,0)), (340,320))
                        screen.blit(fontexit.render(" Press X to Exit",True,(0,0,0)), (390,380))
                        global Bestscore
                        Bestscore = points*10 if Bestscorefun(points) else Bestscore
                        screen.blit(fontexit.render(" Best Score "+ str(Bestscore),True,(0,0,0)), (390,440))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    game = False
                                if event.key == pygame.K_x:
                                    exit()
                    #If player wants to continue main is called to reinitialize
                    main()
            
        for c in range(index-2):
            if coins[c].inground():
                coins[c].coindown()
        
        for j in range(index-2):
            coins[j].draw()
        
        #Counting points
        for b in range(index):
            pos = coins[b].position()
            if pos[0] in range(robox-robot.get_width(), robox+robot.get_width()) and pos[1] in range(height-100,height - robot.get_height()):
                coins[b].nposition(randint(0,1040), 0)
                points += 1
        
        #If monster is killed user gets twice the points
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
 
        #Commands to display Lives, Score, Bullets left
        pygame.draw.rect(screen, (255,51,51), (955,35, 12,12))
        pygame.draw.rect(screen, (0,0,0), (10,10, 10,22))
        pygame.draw.rect(screen, (0,0,0), (22,10, 10,22))
        pygame.draw.circle(screen, (255,255,0),(960, 15), 12)
        bullleft = "Bullets " + str(bullnum)
        point = "1   Score " + str(points*10)
        leftlives = "♥  Lives"
        livesym = "♥"*live
        text = font.render(point,True,(255,0,0))
        livesym = font.render(livesym,True,(0,102,0))
        bulltext = font.render(bullleft, True, (255,0,0))
        livetext = font.render(leftlives, True, (255,0,0))
        screen.blit(bulltext, (980,25))
        screen.blit(text,(955,0))
        screen.blit(livetext,(955,50))
        screen.blit(livesym, (1035,50))
        
        #Message for new User
        if bullnum > 27 and points == 0:
            screen.blit(font.render("Press ↑ to shoot and ← → to move or click Pause Button to pause",True,(0,0,102)), (220,35))
        for i in range(index):
            monsters[i].draw()
        
        #Reload bullet if the user get more than 100 points and incremented for every other 100 landmark
        if (points >= bullincrement  and points <= bullincrement + 3) and points != 0 and not reloaded:
            bullnum = 30
            bullincrement += 10
            helpreload += 10
            reloaded = True
 
        if points >= helpreload and points <= helpreload + 4:
            reloaded = False
 
        #Level Up in here Be carefull
        if (points%20 == 0 or points%21 == 0):
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
        
        #Displaying all
        pygame.display.flip()
        clock.tick(60)
 
main()
 
#The End
#If you reached here Thumbs Up and Thank you For Reviewing my game ♥♥♥ :-)
#I beleived you like my game Thank You Once again
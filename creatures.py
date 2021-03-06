import random
import sys
import time
import pygame

WINDOWWIDTH = 896
WINDOWHEIGHT = 504
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
pygame.init()
font = pygame.font.SysFont('centaur', 22)
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
TEXT = 450

def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    #print textrect
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#working on adding
class zombie:
    def __init__(self):
        self.name = 'zombie'
        self.health = 800
        self.stamina = 80
        self.damage = 0
        self.miss = 20
        self.last = -1
        self.mod = 1
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 175
    def f_ability0(self):
        ability = random.randrange(0,2)
        if ability == 0:
            damage = random.randrange(70,100)
            self.last = 0
            dam = str(damage)
            drawText('The cyclops smashes you with his fist',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The cyclops smashes you with his fist"
        elif ability == 1:
            damage = 0
            self.last = 1
            self.damage = 0
            dam = str(damage)
            drawText('The cyclops is disoriented.',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The cyclops is disoriented and just looks at you funny"
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss and ability != 1:
            self.damage = 0
            drawText('The cyclops MISSES you completely!',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The cyclops MISSES you completely!"
        elif crit >=9 and ability != 1:
            crit = damage*2
            self.damage = crit
            dam = str(crit)
            drawText('The cyclops CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The cyclops CRITS you for {0} damage".format(self.damage)
        else:
            if ability != 1:
                self.damage = damage
                dam = str(self.damage)
                drawText('The cyclops hits you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The cyclops {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
                
class cyclops:
    def __init__(self):
        self.name = 'cyclops'
        self.health = 700
        self.stamina = 70
        self.damage = 0
        self.miss = 10
        self.last = -1
        self.mod = 1
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 175
    def f_ability0(self):
        ability = random.randrange(0,2)
        if ability == 0:
            damage = random.randrange(70,100)*self.mod
            self.last = 0
            dam = str(damage)
            drawText('The cyclops smashes you with his fist',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The cyclops smashes you with his fist"
        elif ability == 1:
            damage = 0
            self.last = 1
            self.damage = 0
            dam = str(damage)
            drawText('The cyclops is disoriented.',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The cyclops is disoriented and just looks at you funny"
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss and ability != 1:
            self.damage = 0
            drawText('The cyclops MISSES you completely!',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The cyclops MISSES you completely!"
        elif crit >=9 and ability != 1:
            crit = damage*2
            self.damage = crit
            dam = str(crit)
            drawText('The cyclops CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The cyclops CRITS you for {0} damage".format(self.damage)
        else:
            if ability != 1:
                self.damage = damage
                dam = str(self.damage)
                drawText('The cyclops hits you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The cyclops {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The cyclops has {0} health remaining".format(self.health)
    def f_display(self):
        print """
              You enter a room filled with a foul stench.
              A cyclops smells your flesh...
              'ME HUNGRY ME EAT YOU NOW'
              Prepare yourself for a fight!"""
        time.sleep(2)
        print '''
            _......._
        .-'.'.'.'.'.'.`-.
      .'.'.'.'.'.'.'.'.'.`.
     /.'.'               '.\
    
     |     _..- .-. -.._   |
  .-.'    `.   ((@))  .'   '.-.
 ( ^ \      `--.   .-'     / ^ )
  \  /         .   .       \  /
  /          .'     '.  .-    \

  `-' \   ' .--.          / `-'
      |  / /|_| `-._.'\   |
      |   |       |_| |   /-.._
  _..-\   `.--.______.'  |
       \       .....     |
        `.  .'      `.  /
          \           .'
           `-..___..-`
                '''
        
class ogre:
    def __init__(self):
        self.name = 'ogre'
        self.health = 300
        self.stamina = 30
        self.damage = 0
        self.miss = 10
        self.last = -1
        self.mod = 1
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 75
    def f_ability0(self):
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        ability = random.randrange(0,2)
        if ability == 0 or self.last == 1:
            if self.last == 1:
                damage = (random.randrange(17,30)*3)*self.mod
                miss = self.miss + 1
                self.last = 0
                drawText('The ogre smashes you to the ground ',font,windowSurface,TEXT,0,TEXTCOLOR)
                print "The Ogre smashes you to the ground with full force!"
            else:
                damage = random.randrange(17,30)*self.mod
                drawText('The ogre stakes a swing with his club!',font,windowSurface,TEXT,0,TEXTCOLOR)
                print "The Ogre takes a swing with his club!"
                self.last = 0
        elif ability == 1 and self.last !=1:
            damage = 0
            self.last = 1
            self.damage = 0
            drawText('The ogre picks you up!',font,windowSurface,450,0,TEXTCOLOR)
            print "The ogre picks you up and prepares to slam you to the ground"
        else:
            damage = random.randrange(17,30)*self.mod
            dam = str(damage)
            drawText('The ogre takes a swing with his club',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Ogre takes a swing with his club!"
        if miss <= self.miss and self.last == 0:
            self.damage = 0
            drawText('The ogre MISSES you completey!',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The ogre MISSES you completely!"
        elif crit ==10 and self.last == 0:
            crit = damage*2
            self.damage = crit
            dam = str(crit)
            drawText('The ogre CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The ogre CRITS you for {0} damage".format(self.damage)
        else:
            if self.last == 0:
                self.damage = damage
                dam = str(self.damage)
                drawText('The ogre hits you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The ogre {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The ogre has {0} health remaining".format(self.health)
    def f_display(self):
        print """
              An ogre is sleeping in the next room.
              He appears to be surrounded by bones from those
              who have attempted to kill him before."""
        time.sleep(2)
        print '''
                      |\  ,,,,,  /|
                      | \/_   _\/ |
               /\     (_    "    _)
               \ \      (  ,--, )
               / /    ,,,\__-__/,,,
               \ \   ,,,,""""""",,,,  ,,,,
               /_/   |  |"""""""(  ) ,(  )
              [!!!]-'  / """"""" \  \ / /
               |!|----' """"""""" `,___/
                        ;;;;;;;;;
                        """""""""
                        """" """"
                        """   """
                       _"",   ,""_
                      (___)   (___)

                '''
        
class gargoyle:
    def __init__(self):
        self.name = 'gargoyle'
        self.health = 450
        self.stamina = 45
        self.damage = 0
        self.miss = 10
        self.last = -1
        self.mod = 1
        self.dict = ['DECIMATES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 150
    def f_ability0(self):
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        ability = random.randrange(0,2)
        if ability == 0:
            damage = random.randrange(30,45)*self.mod
            dam = str(damage)
            drawText('The Gargoyle swipes you with his fierce claws!',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Gargoyle swipes you with his fierce claws!"
            self.last = 0
        elif ability == 1:
            damage = 0
            self.last = 1
            self.stamina += 5
            self.health += 50
            self.damage = 0
            drawText('The Gargoyle turns to stone, increasing health by 50',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The gargoyle turns to stone, increasing his health by 50"
        else:
            damage = random.randrange(30,45)*self.mod
            print "The Gargoyle swipes you with his fierce claws!"
        if miss <= self.miss and ability != 1:
            self.damage = 0
            drawText('The Gargoyle MISSES you completely!',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The Gargoyle MISSES you completely!"
        elif crit ==10 and ability != 1:
            crit = damage*1.5
            self.damage = crit
            dam = str(crit)
            drawText('The Gargoyle CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The Gargoyle CRITS you for {0} damage".format(self.damage)
        else:
            if ability != 1:
                self.damage = damage
                dam = str(self.damage)
                drawText('The Gargoyle hits you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The Gargoyle {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The Gargoyle has {0} health remaining".format(self.health)
    def f_display(self):
        print """
              You enter the next room and a
              Gargoyle guards a tomb.  I wonder whats inside?"""
        time.sleep(2)
        print """
               /|    /(_)\    |\                
             /' `\   \`,'/   /' `\              
           /' / | `\_/\~/\_/' | \ `\          
          O  |   \/'   V   `\/   |  O        
         O   |,-,|   ,_;_,   |,-,|   O       
        oO    \  \\ '\ I /` //  /    Oo     
        oO     \ \`\  \ /  /'/ /     Oo     
         O    /~\ \,\  |  /,/ /~\    O       
    ______O  /__/ /__| I |__\ \__\  O____    
    |      \|  '''  ''' ```  ```  |/     
        """

class dragon:
    def __init__(self):
        self.name = 'dragon'
        self.health = 1000
        self.stamina = 100
        self.damage = 0
        self.miss = 10
        self.last = -1
        self.mod = 1
        self.dict = ['HITS','BITES','BURNS','DEVOURES','BREATHES FIRE','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 1000
    def f_ability0(self):
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        ability = random.randrange(0,2)
        if ability == 0:
            if self.last == 1:
                damage = (random.randrange(10,80)*2)*self.mod
                drawText('The tar ignites and you are engulfed in flames!',font,windowSurface,TEXT,0,TEXTCOLOR)
                print "The tar ignites and you are engulfed in flames!"
            else:
                damage = random.randrange(10,80)*self.mod
                drawText('The Dragon attacks you!',font,windowSurface,TEXT,0,TEXTCOLOR)
                print "The Dragon attacks you!"
            self.last = 0
        elif ability == 1 and self.last !=1:
            damage = 0
            self.last = 1
            self.damage = 0
            drawText('The Dragon spews tar all over your body...un oh',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Dragon spews tar all over your body...un oh"
        else:
            damage = random.randrange(10,80)*self.mod
            drawText('The Dragon attacks you for '+str(damage),font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Dragon attacks you!"
        if miss <= self.miss and ability != 1:
            self.damage = 0
            drawText('The Dragon MISSES you completely!',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The Dragon MISSES you completely!"
        elif crit ==10 and ability != 1:
            crit = damage*2.5
            self.damage = crit
            dam = str(crit)
            drawText('The Dragon CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR) 
            print "The Dragon CRITS you for {0}".format(self.damage)
        else:
            if ability != 1:
                self.damage = damage
                dam = str(self.damage)
                drawText('The Dragon hits you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The Dragon {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The Dragon has {0} health remaining".format(self.health)
    def f_display(self):
        print """
              You happen upon a dragon's lair.
              The gold and spoils he is guarding are beyond
              your wildest dreams.  If you can manage to defeat him..."""
        time.sleep(2)
        print """
                                             ..
                                     ,o""'o
                                  ,o$"     o
                               ,o$$$                                 
                             ,o$$$'
                           ,o$"o$'
                         ,o$$"$"'   
                      ,o$"$o"$"'    
                   ,oo$"$"$"$"$$`                      ,oooo$$$$$$$$oooooo.  
                ,o$$$"$"$"$"$"$"o$`..             ,$o$"$$"$"'            `oo.o
             ,oo$$$o"$"$"$"$  $"$$$"$`o        ,o$$"o$$$o$'                 `o
          ,o$"$"$o$"$"$"$  $"$$o$$o $$o`o   ,$$$$$o$"$$o'                    $
        ,o"$$"'  `$"$o$" o$o$o"  $$$o$o$oo"$$$o$"$$"$o"'                     $
     ,o$"'        `"$ "$$o$$" $"$o$o$$"$o$$o$o$o"$"$"`""o                   ' 
   ,o$'          o$ `"$"$o "$o$$o$$$"$$$o"$o$$o"$$$    `$$  
  ,o'           (     `" o$"$o"$o$$$"$o$"$"$o$"$$"$ooo|  `` 
 $"$             `    (   `"o$$"$o$o$$ "o$o"   $o$o"$"$    )
(  `                   `    `o$"$$o$" "o$$     "o /|"$o"
 `                           `$o$$$$"" o$      "o$\|"$o'
                              `$o"$"$ $ "       `"$"$o$
                               "$$"$$ "oo         ,$""$ 
                               $"$o$$""o"          ,o$"$
                               $$"$$"$ "o           `,",
                     ,oo$oo$$$$$$"$o$$$ ""o           
                  ,o$$"o"o$o$$o$$$"$o$$oo"oo
                ,$"oo"$$$$o$$$$"$$$o"o$o"o"$o o
               ,$$$""$$o$,      `$$$$"$$$o""$o $o               
               $o$o$"$,          `$o$"$o$o"$$o$ $$o             
              $$$o"o$$           ,$$$$o$$o"$"$$ $o$$oo      ,   
              "$o$$$ $`.        ,"$$o$"o$""$$$$ `"$o$$oo    `o
              `$o$o$"$o$o`.  ,.$$"$o$$"$$"o$$$$   `$o$$ooo    $$ooooooo
                `$o$"$o"$"$$"$$"$"$$o$$o"$$o"        `"$o$o            `"o
                   `$$"$"$o$$o$"$$"$ $$$  $ "           `$"$o            `o
                      `$$"o$o"$o"$o$ "  o $$$o            `$$"o          ,$
                         (" ""$""'     o"" "o$o             `$$ooo     ,o$$
                              $$'""o   (   "$o$$$"o            `$o$$$o$"$'
                                ) ) )           )  ) )            ` "'
        """
class giant_snake:
    def __init__(self):
        self.name = 'snake'
        self.health = 250
        self.stamina = 25
        self.damage = 0
        self.miss = 10
        self.last = -1
        self.counter = 2
        self.mod = 1
        self.dict = ['HITS','BITES','KNICKS','DEVOURES','POISONS','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 65
    def f_ability0(self):
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        ability = random.randrange(0,2)
        if ability == 0 or self.last == 1:
            if self.counter > 1:
                damage = (random.randrange(17,30) + 10)*self.mod
                drawText('The Giant Snake attacks! His poison does an additional 10 damage.',font,windowSurface,300,0,TEXTCOLOR)
                print "The Giant Snake attacks! His poison does an additional 10 damage."
                self.counter -= 1
                if self.counter == 0:
                    self.counter = 2
            else:
                damage = random.randrange(17,30)*self.mod
                drawText('The Giant Snake attacks!',font,windowSurface,TEXT,0,TEXTCOLOR)
                print "The Giant Snake attacks!"
            self.last = 0
        elif ability == 1 and self.last !=1 and self.counter == 2:
            damage = 0
            self.last = 1
            self.damage = 0
            drawText('The Giant Snake injects you with poison.',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Giant Snake injects you with poison"
        else:
            damage = random.randrange(17,30)*self.mod
            drawText('The Giant Snake attacks!',font,windowSurface,TEXT,0,TEXTCOLOR)
            print "The Giant Snake attacks!"
        if miss <= self.miss and self.last == 0:
            self.damage = 0
            drawText('The Giant Snake MISSES you completely',font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The giant snake MISSES you completely!"
        elif crit ==10 and self.last == 0:
            crit = damage*2.5
            self.damage = crit
            dam = str(crit)
            drawText('The Giant Snake CRITS you for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
            print "The giant snake CRITS you for {0}".format(self.damage)
        else:
            if self.last == 0:
                self.damage = damage
                dam = str(self.damage)
                drawText('The Giant Snake hits for '+dam,font,windowSurface,TEXT,25,TEXTCOLOR)
                print "The giant snake {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The giant snake has {0} health remaining".format(self.health)
    def f_display(self):
        print """
              You enter the next room and startle
              a Giant Snake.  He attacks!"""
        time.sleep(1.5)
        print '''
           ---_ ...... _/_ -    
          /  .      ./ .'*\ \    
          : '         /__-'   \. 
         /                      )
       _/                  >   .' 
     /   .   .       _.-" /  .'   
     \           __/"     /.'/|   
       \ '--  .-" /     //' |\|  
        \|  \ | /     //_ _ |/|
         `.  \:     //|_ _ _|\|
         | \/.    //  | _ _ |/| 
          \_ | \/ /    \ _ _ \\\ 
              \__/      \ _ _ \|\
        '''

from gamelib import *

game = Game(1000,400,"Tiny Quest")

######################################################

bk = Image("games//bk.png",game)
bk.resizeTo(1000,400)

runF = Animation("for//RunningBackwards.png",8,game,864/8,140,10)
runB = Animation("for//Running Forward.png",8,game,864/8,140,10)

stand = Animation("for//StandRE.png",7,game,180/3,207/3,10)
stand.resizeBy(100)
stand.y += 100

Punch = Animation("for//Punch.png",6,game,158/2,192/3,5)
Punch.resizeBy(100)
Punch.y += 100

Punch2 = Animation("for//Imported piskel.png",6,game,158/2,192/3,5)
Punch2.resizeBy(100)
Punch2.y += 100

Power = Animation("for//HUD_LevOutroAnim_Sprites02.png",4,game,1600/2,1600/2,3)
Power.resizeBy(-90)

#######################################################

PunchFX = Sound("for//Jab-SoundBible.com-1806727891.wav",1)
GameOver = Sound("for//game over.wav",2)
Win = Sound("for//Victory Sound Effect.wav",3)
game.setMusic("for//GameMusic.wav")

######################################################

player = {"x":stand.x,"y":stand.y}

Energy = 750

stand.health = 255

#game.score = 999

######################################################
Alien = []

for times in range(35):
    Alien.append(Animation("for//Sprite.png",5,game,1000/2,1125/3,10))
for a in Alien:
    a.resizeBy(-60)
    


Alien2 = []
for times in range(25):
    Alien2.append(Animation("for//Imported piskel (1).png",5,game,1000/2,1125/3,10))
for a in Alien2:
    a.resizeBy(-60)
    x = game.width  + randint(-15000,-100)
    s = randint(3,6)
    a.moveTo(x,300)
    a.setSpeed(s,-90)



######################################################
while not game.over:
    game.processInput()
    bk.draw()
    Punch.draw()
    for a in Alien:
        a.draw()
        a.moveTo(Punch.x + 80,Punch.y)
    game.drawText("Tiny Quest",game.width/4,game.height/4,Font(cyan,90,cyan))
    game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(cyan,40,cyan))
    game.drawText("For controls look at bottom of code",5,5,Font(yellow,30,white))
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(60)

######################################################
game.over = False
game.playMusic()
for a in Alien:
    x = game.width  + randint(100,15000)
    s = randint(3,6)
    a.moveTo(x,300)
    a.setSpeed(s,90)

x = randint(100,1000)
y = -randint(500,1000)
s = randint(3,6)
Power.moveTo(x,y)
Power.setSpeed(s,90)

while not game.over:
    game.processInput()
    bk.draw()
    Power.draw()
    Power.y += 5
    #WinScreen.draw()
  
    if keys.Pressed[K_RIGHT]:
        runF.moveTo(player["x"],player["y"])
        runF.draw()
        player["x"] += 5
    elif keys.Pressed[K_LEFT]:
        runB.moveTo(player["x"],player["y"])
        runB.draw()
        player["x"] -= 5
    elif keys.Pressed[K_e] and Energy > 0:
        stand.moveTo(999,999)
        Energy -= 1
        Punch.moveTo(player["x"],player["y"])
        Punch.draw()
    elif keys.Pressed[K_q] and Energy > 0:
        stand.moveTo(999,999)
        Energy -= 1
        Punch2.moveTo(player["x"],player["y"])
        Punch2.draw()
        
    else:
        Punch.moveTo(999,999)
        Punch2.moveTo(999,999)
        stand.moveTo(player["x"],player["y"])
        stand.draw()

    for a in Alien:
        a.move()
        if keys.Pressed[K_e] and a.collidedWith(Punch):
            a.makeVisible(False)
            PunchFX.play()
            game.score += 20
        if a.collidedWith(stand,"rectangle"):
            stand.health -= 1

    for a in Alien2:
        a.move()
        if keys.Pressed[K_q] and a.collidedWith(Punch2):
            a.makeVisible(False)
            PunchFX.play()
            game.score += 20
        if a.collidedWith(stand,"rectangle"):
            stand.health -= 1
            

        if Power.collidedWith(stand):
            Energy += 10
            #Power.makeVisible = False
            x = randint(100,1000)
            y = -randint(500,1000)
            s = randint(3,6)
            Power.moveTo(x,y)
            Power.setSpeed(s,90)
        if Power.collidedWith(runF):
            Energy += 10
            #Power.makeVisible = False
            x = randint(100,1000)
            y = -randint(500,1000)
            s = randint(3,6)
            Power.moveTo(x,y)
            Power.setSpeed(s,90)
        if Power.collidedWith(runB):
            Energy += 10
            #Power.makeVisible = False
            x = randint(100,1000)
            y = -randint(500,1000)
            s = randint(3,6)
            Power.moveTo(x,y)
            Power.setSpeed(s,90)
        if Power.isOffScreen("bottom"):
            x = randint(100,1000)
            y = -randint(500,1000)
            s = randint(3,6)
            Power.moveTo(x,y)
            Power.setSpeed(s,90)
           #Power.makeVisible = True


#



    if game.score >= 1000:
        game.over = True
        game.drawText("You Win",game.width/4,game.height/4,Font(cyan,90,cyan))
        game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(cyan,40,cyan))
        Win.play()
        game.stopMusic()
        game.update()

    if stand.health < 0:
        game.over = True
        game.drawText("Game Over",game.width/4,game.height/4,Font(cyan,90,cyan))
        game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(cyan,40,cyan))
        game.stopMusic()
        GameOver.play()
        game.update()
        


    game.drawText("Score: " + str(game.score),5,5)
    game.drawText("Energy: " + str(Energy),5,20)
    game.drawText("Health: " + str(stand.health),5,35)
    
    game.update(160)

game.wait(K_ESCAPE)
game.quit()

#Controls
'''
e:Punch Right
q:Punch Left
Arrow Left: Move Left
Arrow Right: Move Right

Goal:
Score of 1000

Gems:
Give Energy

'''


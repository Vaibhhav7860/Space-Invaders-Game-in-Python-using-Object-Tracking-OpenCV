# Importing necessary modules
import turtle
import math
import winsound
import playsound




ms = turtle.Screen()                      # Making the main screen as the turtle object
ms.bgcolor("black")                     # Setting the color of main screen to black
ms.title("Space Invaders")              # Setting the title of the main screen
ms.setup(height=650)                    # Setting the custom height of main screen

ms.bgpic("C:/Users/ACER/Desktop/space_invader_background.gif")      # Loading a background pic on the main screen
ms.tracer(0)                    # Setting delay for updating drawings to 0


# Registering the shapes of Spaceship, enemies and bullet

ms.register_shape('C:/Users/ACER/Desktop/spaceship.gif')
ms.register_shape('C:/Users/ACER/Desktop/Invaders-unscreen.gif')
ms.register_shape('C:/Users/ACER/Desktop/Bullet-unscreen.gif')

# Creating a rectangular border on the main screen

border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-283,-292)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(575)
    border_pen.lt(90)
border_pen.hideturtle()

# Adding scores

# Initializing score to 0

SCORE = 0

# Drawing the score on the game screen

Score_Pen=turtle.Turtle()
Score_Pen.speed(0)
Score_Pen.color("white")
Score_Pen.penup()
Score_Pen.setposition(-275,260)
scorestring="Score : {}".format(SCORE)
Score_Pen.write(scorestring,False,align="left",font=("Arial",10,"normal"))
Score_Pen.hideturtle()


# Creating Player Turtle and setting its attributes

player=turtle.Turtle()
player.color("blue")
player.shape("C:/Users/ACER/Desktop/spaceship.gif")
player.penup()
player.speed(0)
player.setposition(-10,-270)
player.setheading(90)
player.speed=0

# Moving the player left and right


# Deciding number of enemies
Number_of_enemies=30
# Creating an empty list of enemies

enemies=[]                      # empty list for appending enemies as turtle object in it
# Adding enemies to list

for i in range(Number_of_enemies):
    # Creating the Enemy
    enemies.append(turtle.Turtle())

# Setting the starting positions of enemies

enemy_start_x=-200
enemy_start_y=250

# enemy_number variable is used for bringing the enemies in a set of 10.

enemy_number=0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("C:/Users/ACER/Desktop/Invaders-unscreen.gif")
    enemy.penup()
    enemy.speed(0)
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x,y)
    # Updating the enemy number
    enemy_number+=1
    if enemy_number==10:
        enemy_start_y-=50
        enemy_number=0

# Setting the enemy speed
enemyspeed=0.3

c = 0

# Creating Player's Bullet

bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("C:/Users/ACER/Desktop/Bullet-unscreen.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.goto(0,-350)

bulletspeed=3.3

# Defining Bullet Speed
# ready  -  ready to fire
# fire   -   bullet is firing

bulletstate = "ready"

# Displaying Game Over when game gets over

game_over_pen=turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.setposition(0,0)
game_over_pen.hideturtle()

#   Displaying Victory when the player wins.
victory_pen = turtle.Turtle()
victory_pen.speed(0)
victory_pen.color("green")
victory_pen.penup()
victory_pen.setposition(0,0)
victory_pen.hideturtle()

# CREATING REQUIRED FUNCTIONS


def start_game():
    global game_state
    game_state = 'game'

def move_left():
    player.speed=-1


def move_right():
    player.speed=1

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -283:                    # Condition for blocking the player in the boundary
        x = -283
    if x>292:                      # Condition for blocking the player in the boundary
        x=292
    player.setx(x)


def fire_bullet():
    # Declare bulletstate as a global variable
    global bulletstate
    if bulletstate=="ready":
        play_sound("C:/Users/ACER/Desktop/bullet fire.wav")
        bulletstate="fire"
    # Moving the bullet just above the player
        x=player.xcor()
        y=player.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <15:
        return True
    else:
        return False

def play_sound(sound_file,time=0):
    winsound.PlaySound(sound_file,winsound.SND_ASYNC)

    # repeating the sound
    if time>0:
        turtle.ontimer(lambda: play_sound(sound_file,time),t=int(time*1000))
# Creating keyboard Bindings

ms.listen()

# Required game boundings

ms.onkeypress(start_game, "s")
ms.onkeypress(move_left, "Left")
ms.onkeypress(move_right,"Right")
ms.onkeypress(fire_bullet, "space")
ms.onkeypress(fire_bullet, "a")

# Playing Background music

playsound.playsound('C:/Users/ACER/Desktop/aibm.wav', False)


game_state="Splash"

# main game loop


c = 0
while True:
    ms.update()

    if game_state == 'Splash':
        ms.bgpic("C:/Users/ACER/Desktop/Space Invaders splash screen.gif")
        border_pen.hideturtle()
        for enemy in enemies:
            enemy.hideturtle()
        player.hideturtle()

    elif game_state == 'game':
        ms.bgpic("C:/Users/ACER/Desktop/space_invader_background.gif")

        move_player()
        player.showturtle()

        for enemy in enemies:
            enemy.showturtle()
            #      Moving the enemy
            x=enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)

            # Moving the enemy back and down
            if enemy.xcor()>290:
                # Moving all the enemies down
                for e in enemies:
                    y=e.ycor()
                    y-=20
                    e.sety(y)
                # Changing enemies direction
                enemyspeed *= -1

            elif enemy.xcor()<-280:
                # Moving all the enemies down
                for e in enemies:
                    y=e.ycor()
                    y-=20
                    e.sety(y)
                # Changing enemies direction
                enemyspeed *= -1
                # Checking for a collision between bullet and enemy

            if isCollision(bullet, enemy):
                play_sound("C:/Users/ACER/Desktop/explosion.wav")
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # Reset the enemy
                enemy.setposition(0, 10000)
                c += 1
                print(c)
                # Updating the score

                SCORE+=10
                scorestring = "Score : {}".format(SCORE)
                Score_Pen.clear()
                Score_Pen.write(scorestring, False, align="left", font=("Arial", 10, "normal"))
                Score_Pen.hideturtle()

                # If all 30 players are destroyed then showing the victory message on the screen

                if c == 30:
                    victory_pen.write(" YOU WON !!! ", move=False, align='center', font=("Arial", 60, "normal"))
                    victory_pen.hideturtle()
                    break


            # Collision of enemy with player

            if isCollision(player, enemy):
                play_sound("C:/Users/ACER/Desktop/Gameover.wav")
                player.hideturtle()
                enemy.hideturtle()
                game_over_pen.write(" GAME OVER !!! ",move=False,align='center',font=("Arial",60,"normal"))
                game_over_pen.hideturtle()
                break

        #if all(enemy.xcor() > 290 or enemy.xcor() < -280 for enemy in enemies):
         #   game_over_pen.write(" GAME OVER !!! ", move=False, align='center', font=("Arial", 60, "normal"))
          #  game_over_pen.hideturtle()
           # break

        # Moving the bullet
        if bulletstate=="fire":
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

        # Checking to see whether the bullet has gone to the top or not
        if bullet.ycor()>275:
            bullet.hideturtle()
            bulletstate = "ready"


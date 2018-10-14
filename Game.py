import turtle
import math
import winsound
import time

turtle.tracer(2)
wn = turtle.Screen()
wn.bgpic("Space-Invaders.png")
turtle.register_shape("laser.gif")
turtle.register_shape("Space-Invaders-Alien.gif")
turtle.register_shape("alien.gif")
speed = 1
bulletSpeed = 2
alienSpeed = 1
player = turtle.Turtle()
player.penup()
player.hideturtle()
player.setposition(0, -300)
player.showturtle()
turtle.register_shape("ship.gif")
player.shape("ship.gif")
canfire = True
bullet = turtle.Turtle()
bullet.penup()
bullet.hideturtle()
aliensHit = 0
aliens = []
for i in range(5):
    alien = turtle.Turtle()
    alien.penup()
    
    alien.shape("alien.gif")
    alien.setposition(-300 + (i * 150), 200)
    
    aliens.append(alien)

def left():
    player.left(180)

def right():
    player.right(180)

def fire():
    global bullet, canfire
    if canfire == True:
        winsound.PlaySound("Sci-Fi Laser Gun Shot Sound Effect", winsound.SND_ASYNC)
        bullet = turtle.Turtle()
        bullet.penup()
        bullet.hideturtle()
        bullet.left(90)
        bullet.shape("laser.gif")
        bullet.setposition(player.xcor(), player.ycor())
        bullet.showturtle()
        canfire = False

def collision (e1, e2):
    d = math.sqrt(math.pow(e1.xcor() - e2.xcor(), 2) + math.pow(e1.ycor() - e2.ycor(), 2))
    if d < 30:
        return True
    return False

turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(fire, "space")
gameOver = False
while gameOver == False:
    player.forward(speed)
    bullet.forward(bulletSpeed)

    if len(aliens) == 0:
        turtle.hideturtle()
        winsound.PlaySound("You Win", winsound.SND_ASYNC)
        turtle.color("green")
        turtle.penup()
        turtle.write("You Win!", False, align="center",font=("script", 75, "bold"))
        gameOver = True
        break
    
    for i in range(len(aliens)):
        aliens[i].forward(alienSpeed)
        if aliens[i].xcor() > 350 or aliens[i].xcor() < -350:
            aliens[i].setposition(aliens[i].xcor(), aliens[i].ycor() - 60)
            aliens[i].right(180)

    for i in range(len(aliens)):
        if collision(bullet, aliens[i]):
            winsound.PlaySound("Alien Hit", winsound.SND_ASYNC)
            aliens[i].hideturtle()
            bullet.hideturtle()
            aliensHit += 5
            aliens.remove(aliens[i])
            speed -= 0.1
            break
        
        
    for i in range(len(aliens)):
        if aliens[i].ycor() <= -300:
            turtle.hideturtle()
            winsound.PlaySound("You Lost", winsound.SND_ASYNC)
            turtle.color("red")
            turtle.penup()
            turtle.write("Game Over", False, align="center",font=("script", 75, "bold"))
            gameOver = True
            break
        
    if player.xcor() > 350 or player.xcor() < -350:
        player.right(180)

    if bullet.ycor() > 400:
        canfire = True
 
    if aliensHit == 1:
        turtle.color("green")
        turtle.penup()
        turtle.hideturtle()
        turtle.write("You Win!", False, align="center",font=("script", 75, "bold"))
        gameOver = True
        break
    
time.sleep(3)
turtle.bye()
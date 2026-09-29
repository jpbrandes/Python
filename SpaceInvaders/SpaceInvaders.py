import turtle
import os
import math
import random
import platform


if platform.system() == "Windows":
	try:
		import winsound
	except:
		print( "WinSound not available")
	

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders - A&P 2026")
#wn.bgpic("space_invaders_background.gif")
wn.tracer( 10 )

#wn.register_shape("invader.gif")
#wn.register_shape("player.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

message_pen = turtle.Turtle()
message_pen.speed(0)
message_pen.color("yellow")
message_pen.penup()
message_pen.setposition(-50, 0)
message_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
#player.shape("player.gif")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 1

number_of_enemies = 30
enemies = []

for i in range(number_of_enemies ):
	#Create the enemy
	enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
	enemy.color("green")
#	enemy.shape("invader.gif")
	enemy.shape("square")
	enemy.penup()
	enemy.speed(0)
	x = enemy_start_x + (50 * enemy_number)
	y = enemy_start_y
	enemy.setposition(x, y)
	enemy_number += 1
	if enemy_number == 10:
		enemy_start_y -= 50
		enemy_number = 0
	
enemyspeed = 0.1

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 3

bulletstate = "ready"

def move_left():
	player.speed = -1
	
def move_right():
	player.speed = 1

def move_player():
	x = player.xcor()
	x += player.speed
	if x < -280:
		x = - 280
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
#		play_sound( "laser.wav" )
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

def play_sound( sound_file, time = 0 ):
	if platform.system() == "Windows":
		winsound.PlaySound( sound_file, winsound.SND_ASYNC )
	elif platform.system() == "Linux":
		os.system("aplay {} &".format( sound_file ))
	else:
		os.system( "afplay {} &".format(sound_file))

def sair():
	turtle.bye()

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress( sair, "Escape" )

gameover = False
turtle._Speed = 0
while not gameover:
	wn.update()
	move_player()
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
			
		if isCollision(bullet, enemy):
			play_sound( "explosion.wav" )
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			enemy.setposition( 0, 10000)
			score += 10
			scorestring = "Score: {}".format( score )
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
			number_of_enemies -= 1
			if number_of_enemies == 0:
				message_pen.write("Victory", False, align="left", font=("Arial", 18, "normal"))
				gameover = True
				break
		
		if isCollision(player, enemy) or enemy.ycor() < -250 :
			player.hideturtle()
			enemy.hideturtle()
			message_pen.write("Game Over", False, align="left", font=("Arial", 18, "normal"))
			play_sound( "explosion.wav" )
			gameover = True
			break

	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

delay = input("Press enter to finsh.")

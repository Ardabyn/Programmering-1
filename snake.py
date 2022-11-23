# Assigning directions
import turtle
import random
import time

player_score = 0
highest_score = 0
delay_time = 0.1

# window screen created
wind = turtle.Screen()
wind.title("Snake Maze🐍")
wind.bgcolor("red")

# The screen size
wind.setup(width=700, height=700)


# creating the snake 
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# creating the food
snake_food = turtle.Turtle()
shapes = random.choice(['triangle','circle', 'square'])
snake_food.shape(shapes)
snake_food.color("blue")
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your_score: 0 Highest_Score : 0", align="center", 
font=("Arial", 24, "normal"))


def moveleft():
    if snake.direction != "right":
        snake.direction = "left"

def moveright():
    if snake.direction != "left":
        snake.direction = "right"

def moveup():
    if snake.direction != "down":
        snake.direction = "up"

def movedown():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    speed = 5
    print(snake.direction)
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y+speed)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y-speed)

    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x+speed)

    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x-speed)

wind.listen()
wind.onkeypress(moveleft, 'Left')
wind.onkeypress(moveright, 'Right')
wind.onkeypress(moveup, 'Up')
wind.onkeypress(movedown, 'Down')

while True:
    wind.update()
    move()
    time.sleep(0.05)


'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle


class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        ''' initializes a paddle with a position '''

        self.turt = make_turtle("square", "white", 5, 1, x_position, y_position)

    def up(self):
        y = self.turt.ycor()
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        self.turt.sety(y)    #move the paddle to the new y position
        self.y_position = y

    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()


class Ball:
    # implements a Pong game ball

    def __init__(self):
        ''' intializes a ball with default direction and position '''

        self.turt = make_turtle("square", "white", 1, 1, 0, 0)
        self.ball_dx = 0.0925 #speed in x direction
        self.ball_dy = 0.0925 #speed in y direction
    
    def check_TopBottom_boundary(self):

        if self.turt.ycor() > 290:
            self.turt.sety(290)
            self.ball_dy *= -1

        elif self.turt.ycor() < -290:
            self.turt.sety(-290)
            self.ball_dy *= -1
    
    def move(self):
        ''' moves the ball in x and y directions '''

        # Move the ball
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)
        self.check_TopBottom_boundary()
        
    
    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()

    # TODO: what's the difference between goto and set?

    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)

# TODO: Methods outside of class: A bigger class named PongGame
class PongGame: 

    def __init__(self):

        self.window = None
        self.pen = None
        self.ball = None
        self.paddle_1 = None
        self.paddle_2 = None
        self.score_player1 = 0
        self.score_player2 = 0


    def make_window(self, window_title, bgcolor, width, height):
        '''this function creates a screen object and returns it'''

        self.window = turtle.getscreen() #Set the window size
        self.window.title(window_title)
        self.window.bgcolor(bgcolor)
        self.window.setup(width, height)
        self.window.tracer(0) #turns off screen updates for the window Speeds up the game

    def make_pen(self):

        self.pen = make_turtle("square", "white", 1, 1, 0, 260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
        self.pen.hideturtle()

    def keyboard_bindings(self):

        self.window.listen() #Listen for keyboard input
        self.window.onkeypress(self.paddle_1.up, "w") #when you press w run paddle_a_up
        self.window.onkeypress(self.paddle_1.down, "s")
        self.window.onkeypress(self.paddle_2.up, "Up")
        self.window.onkeypress(self.paddle_2.down, "Down")
    
    def check_win(self):

        if self.ball.xcor() > 350:
            self.score_player1 += 1
            self.pen.clear()
            self.pen.write("Player A: "+ str(self.score_player1) + "  Player B: "+ str(self.score_player2), align="center", font=("Courier", 24, "normal"))
            self.ball.goto(0, 0)
            self.ball.ball_dx *= -1

        elif self.ball.xcor() < -350:
            self.score_player2 += 1
            self.pen.clear()
            self.pen.write("Player A: "+ str(self.score_player1) + "  Player B: "+ str(self.score_player2), align="center", font=("Courier", 24, "normal"))
            self.ball.goto(0, 0)
            self.ball.ball_dx *= -1
    
    def check_paddle_ball_collision(self):

        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and self.ball.ycor() < self.paddle_1.ycor() + 50 and self.ball.ycor() > self.paddle_1.ycor() - 50:
            self.ball.goto(-340,self.ball.ycor())
            self.ball.ball_dx *= -1.5
        
        elif self.ball.xcor() > 340 and self.ball.xcor() < 350 and self.ball.ycor() < self.paddle_2.ycor() + 50 and self.ball.ycor() > self.paddle_2.ycor() - 50:
            self.ball.goto(340,self.ball.ycor())
            self.ball.ball_dx *= -1.5
        

    def game_play(self):

        self.make_window("Pong - A CS151 Reproduction!", "black", 800, 600)
        self.score_player1 = 0
        self.score_player2 = 0
        self.paddle_1 = Paddle(-350, 0)
        self.paddle_2 = Paddle(350, 0)
        self.ball = Ball()
        self.make_pen()
        self.keyboard_bindings()

        # Main game loop
        while True:
            self.window.update() #This is the update to offset the wn.tracer(0)

            self.ball.move()

            # Border checking    
            self.check_win()

            # Paddle and ball collisions
            self.check_paddle_ball_collision()

def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0) # Speeed of animation, 0 is max
    turt.shape(shape) # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) #Start position
    return turt

def main():
    ''' the main function where the game events take place '''

    game = PongGame()
    game.game_play()

if __name__ == "__main__":
	main()
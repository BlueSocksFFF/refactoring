'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

import turtle

class Connect4:
    
    def __init__(self):
        self.window = self.make_window("Connect 4", "light sky blue", 800, 600)
        self.grid = []
        for rows in range(5):
            self.grid.append([0]*7)
        self.turtle = self.make_turtle('classic', "white", 1, 1, 0, 0 )
        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50
        self.turn = 1
        self.window.onscreenclick(self.play)
        self.window.listen()

    def make_window(self, window_title, bgcolor, width, height):
        ''' this function creates a screen object and returns it '''

        window = turtle.getscreen() # Set the window size
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(width, height)
        window.tracer(0) #turns off screen updates for the window Speeds up the game
        return window

    def make_turtle(self, shape, color, stretch_width, stretch_length, x_pos, y_pos):
        ''' creates a turtle and sets initial position '''

        turt = turtle.Turtle()
        turt.speed(0)    # Speed of animation, 0 is max
        turt.shape(shape)
        turt.color(color)
        turt.shapesize(stretch_width, stretch_length) 
        turt.penup()
        turt.goto(x_pos, y_pos) # Start position
        return turt


    def draw_grid(self):
        ''' draws a grid at x, y with a specific tile_size '''

        self.turtle.up()
        self.turtle.goto(self.x_offset, self.y_offset)
        self.turtle.down()

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                
                self.turtle.up()
                self.turtle.goto(self.x_offset + col * self.tile_size, self.y_offset -row * self.tile_size)
                self.turtle.down()
                self.draw_each_cell(row, col)

    def draw_each_cell(self, row, col):
        if self.grid[row][col] == 1:
            self.turtle.dot(self.tile_size-5, "red")
                
        elif self.grid[row][col] == 2:
            self.turtle.dot(self.tile_size-5, "yellow")
        
        else:
            self.turtle.dot(self.tile_size-5, "white")


    def check_win(self, player):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''
        
        # check rows
        row_win = self.check_win_rows(player)
        if row_win:
            return True
        
        # check columns
        col_win = self.check_win_cols(player)
        if col_win:
            return True

        # check diagonal
        diag_win = self.check_win_diagonal(player)
        if diag_win:
            return True
        
                    
    def check_win_rows(self, player):
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True
        return False
    
    
    def check_win_cols(self, player):
        for col in range(len(self.grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == player:
                    count += 1
                    
                    if count == 4:
                        return True
        return False
    
    def check_win_diagonal(self, player):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if row + 3 < len(self.grid) and col + 3 < len(self.grid[row]):
                    if self.grid[row][col] == 1\
                    and self.grid[row+1][col+1] == 1\
                    and self.grid[row+2][col+2] == 1\
                    and self.grid[row+3][col+3] == 1:
                        return True
        return False

    def play(self, x_pos, y_pos):
        ''' '''
        row = int(abs((y_pos - self.y_offset - 25) // (50) + 1))
        col = int(abs((x_pos - self.x_offset - 25) // (50) + 1))
        print(row, col)
        self.grid[row][col] = self.turn
        self.draw_grid(self.grid, self.turtle, self.x_offset, self.y_offset, self.tile_size)
        self.window.update()

        if self.check_win(self.grid, 1):
            print("player 1 won")

        elif self.check_win(self.grid, 2):
            print("player 2 won")

        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

def main():
    ''' the main function where the game events take place '''
    
    connect4_game = Connect4()
    connect4_game.draw_grid()

    while True:

        # grid[1][0] = 1
        # grid[2][1] = 1
        # grid[3][2] = 1
        # grid[4][3] = 1

        selected_row = int(input("enter row, player "+ str(turn) +": "))
        selected_col = int(input("enter col, player "+ str(turn) +": "))

        if grid[selected_row][selected_col] == 0:

            if turn == 1:
                grid[selected_row][selected_col] = 1
            else:
                grid[selected_row][selected_col] = 2

        draw_grid(grid, my_turtle, -150, 200, 50)
        window.update()

        if check_win(grid, 1):
            print("player 1 won")

        elif check_win(grid, 2):
            print("player 2 won")

        if turn == 1:
            turn = 2
        else:
            turn = 1


    # window.exitonclick()

if __name__ == "__main__":
	main()


import turtle
import time
from playsound import playsound
from multiprocessing import Process


class Search_maze:
    
    color_dict = {
        'X': ('grey', "black"),
        'S': ('grey', "yellow"),
        'E': ('grey', "red"),
        'P': ('grey', "royalblue"),
        'T': ('grey', "light blue"),
        'D': ('gainsboro', "gray")
    }
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.window = turtle.getscreen()
        self.window.bgcolor('slate gray')
        self.turtle.hideturtle()
        self.turtle.shape('square')
        self.turtle.shapesize(2.5, 2.5)

        # set offsets and tile size for drawing the grid
        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50

        # create an int variable for counting steps
        self.steps = 0
        
        self.grid = None
        

    def draw_grid(self):
        ''' draws a grid at x_pos, y_pos with a specific tile_size '''

        # turn off tracer for fast drawing
        self.window.tracer(False)
        
        # move turtle to initial drawing position
        self.turtle.up()
        self.turtle.goto(self.x_offset, self.y_offset)
        self.turtle.down()

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                
                # move turtle to the position of the cell in the grid
                self.turtle.up()
                self.turtle.goto(self.x_offset + col * self.tile_size, self.y_offset -row * self.tile_size)
                self.turtle.down()

                # if the cell is an obstacle (X) draw a black dot
                if self.grid[row][col] == 'X':
                    #self.turtle.dot(tile_size-5, "Black")
                    self.turtle.color('grey', "black")
                    self.turtle.stamp()
                
                # if the cell is the start drawing position (S) draw a yellow dot
                elif self.grid[row][col] == 'S':
                    #self.turtle.dot(tile_size-5, "yellow")
                    self.turtle.color('grey', "yellow")
                    self.turtle.stamp()
                
                # if the cell is the End position (E) draw a Red dot
                elif self.grid[row][col] == 'E':
                    #self.turtle.dot(tile_size-5, "red")
                    self.turtle.color('grey', "red")
                    self.turtle.stamp()

                # if the cell is part of a path (P) draw a royalblue dot
                elif self.grid[row][col] == 'P':
                    #self.turtle.dot(tile_size-5, "royalblue")
                    self.turtle.color('grey', "royalblue")
                    self.turtle.stamp()

                # if the cell has been tried before (T) draw a light blue dot
                elif self.grid[row][col] == 'T':
                    #self.turtle.dot(tile_size-5, "light blue")
                    self.turtle.color('grey', "light blue")
                    self.turtle.stamp()

                # if the cell is part of a deadend (D) draw a gray dot
                elif self.grid[row][col] == 'D':
                    #self.turtle.dot(tile_size-5, "gray")
                    self.turtle.color('gainsboro', "gray")
                    self.turtle.stamp()
                
                # else draw a white dot
                else:
                    #self.turtle.dot(tile_size-5, "white")
                    self.turtle.color( 'grey', "white")
                    self.turtle.stamp()
        
        # turn tracer back on
        self.window.tracer(True)
        
    # Helper method
    def draw_each_cell(self, row, col):
        


    def find_start(self):
        ''' finds the start position (S) in the grid
        returns a tuple of start row and col
        '''

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                # cell at row, col is 'S' return row and col as a tuple
                if self.grid[row][col] == 'S':
                    return (row, col)



    def read_grid(self, file_name):
        ''' reads a maze file and initializes a gird with its contents '''

        # create an empty grid (an empty list called grid)
        self.grid = []

        # open the text file
        file = open(file_name)

        # read a line from the file
        line = file.readline()

        # replace \n with nothing
        line = line.replace('\n', '')

        while line:
            # split the line into tokens
            tokens = line.split(',')

            # add the tokens to the grid as a single row
            self.grid.append(tokens)

            line = file.readline()
            
            # replace \n with nothing
            line = line.replace('\n', '')

    def search_from(self, row, col):
        ''' recursive function to search the grid for the end (E) '''

        self.steps += 1

        # make sure row and col are valid points on the grid
        if row < 0 or col < 0 or row == len(self.grid) or col == len(self.grid[0]):
            # return False if not valid
            return False

        # check that the grid cell at row and col is not obstacle, tried, or deadend
        if self.grid[row][col] == 'X' or self.grid[row][col] == 'T' or self.grid[row][col] == 'D':
            # return False if obstacle, tried, or deadend
            return False

        # If end is found at row, col return True
        if self.grid[row][col] == 'E':
            return True
        
        # If the cell at row, col is not the start cell, mark the cell as tried (T)
        if self.grid[row][col] != 'S':
            self.grid[row][col] = 'T'

        # draw the grid
        self.draw_grid()

        # pause the program for a short duration, try 0.5 and 0.01 seconds
        time.sleep(0.25)

        # recursively search differnt directions adjacent to current row, col (up, down, left, right)
        found = (self.search_from(row-1, col)
                or self.search_from(row+1, col)
                or self.search_from(row, col-1)
                or self.search_from(row, col+1)
                )

        # if any of the 4 directions returns True, mark the cel at row, col as part of the path and return True
        if found and self.grid[row][col] != 'S':
            self.grid[row][col] = 'P'
            return True
        # else, if the cell at row, col is not the start cell (S), mark it as a deadend
        elif self.grid[row][col] != 'S':
            self.grid[row][col] = 'D'
    
    def get_path(self):
        path = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'P':
                    path.append((row, col))
        return path
    
    def get_steps(self):   
        return self.steps
    
def background_music():
    ''' plays tetris music in the background '''

    playsound('Tetris.mp3')

def main():
    ''' reads a maze file and sets the search parameters '''

    game = Search_maze()

    # read maze file and create playground grid
    game.read_grid("maze2.txt")

    # find start position
    row, col = game.find_start()

    # call the search function, it takes the grid, row, column, and steps
    game.search_from(row, col)

    # create a list of tuples representing the path
    
    # print path length
    print('path length:', len(game.get_path()))

    # draw the final grid
    game.draw_grid()
    
    # pause the grid drawing for 4 seconds
    time.sleep(4)

    # print the number of steps taken to find the path
    print("number of steps taken to reach answer:", game.get_steps())
    
# create a turtle and a window for drawing
if __name__ == "__main__":

    p = Process(target=background_music, args=())
    p.start()
    main()
    p.terminate()


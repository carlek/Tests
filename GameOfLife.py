# randomness for intialization
from random import randint

# simple Tk graphics
import turtle

Alive = True
Dead = False

class Universe:
    """ constructor for Universe """
    # grid: a list of cells with (x,y), state, and tick (update count)
    # M and N: dimensions of Universe
    # count: total count of all
    # live_cells: a hashtable of live cells indexed by (x,y)
    # modified: boolean if universe was modified
    # myrtle: turtle object for drawing
    def __init__(self, M, N, random=False, title='Game of Life', speed='slow', dotsize=10, dimension=(800,800)):
        self.M = M
        self.N = N
        self.count = 0
        self.grid = []
        self.live_cells = {}
        self.modified = False
        self.myrtle = MyTurtle(title=title, speed=speed, dimension=dimension, dotsize=dotsize)
        for i in range(M):
            self.grid.append([])
            for j in range(N):
                self.grid[i].append({})
                if not random:
                    state = Alive
                else:
                    state = (randint(1, 10) % 2) == 0
                self.grid[i][j]['state'] = state
                self.grid[i][j]['tick'] = 0
                if state == Alive:
                    self.live_cells[(i, j)] = Alive

    def dump(self):
        """ dump the grid """
        print(self.grid)
        print(self.live_cells)
        for i in range(self.M):
            for j in range(self.N):
                print(i, j, self.grid[i][j])

    def get_state(self, x, y):
        return self.grid[x][y]['state']

    def set_state(self, x, y, state):
        """ change cell at x,y to state """
        self.grid[x][y]['state'] = state
        # maintain the live_cell hashtable
        if state == Alive: # add to livecell and draw black dot
            if (x, y) not in self.live_cells.keys():
                self.live_cells[(x, y)] = True
                self.myrtle.draw_dot(x, y, colour='black')
        else: # remove from livecells and draw white dot
            try:
                self.live_cells.pop((x, y))
                self.myrtle.draw_dot(x, y, colour='white')
            except KeyError as e:
                print('Error in death of cell')

    def up_tick(self, x, y):
        """ increase count for a cell (not used) """
        self.grid[x][y]['tick'] += 1
        self.count += 1

    def run_simulation(self):
        """ run one simulation, keep track if universe was modified."""
        self.modified = False
        for i in range(self.M):
            for j in range(self.N):
                r = self.process_cell(i, j)
                if r and self.modified == False:
                    self.modified = True

    # process a cell based on the rules.
    # if a cell state is changed, return true, else false
    def process_cell(self, x, y):
        self.up_tick(x, y)
        # count # of live neighbours
        num_live = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not i and not j:
                    continue
                # don't go beyond boundaries
                if x + i > 0 and y + j > 0 and x + i < self.M and y + j < self.N:
                    state = self.get_state(x + i, y + j)
                    if state == Alive:
                        num_live += 1

        # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        # Any live cell with two or three live neighbours lives on to the next generation.
        # Any live cell with more than three live neighbours dies, as if by over-population.
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        if self.get_state(x, y) == Alive:
            if num_live < 2 or num_live > 3:
                self.set_state(x, y, Dead)
                return True
        if self.get_state(x, y) == Dead:
            if num_live == 3:
                self.set_state(x, y, Alive)
                return True
        return False

    def draw(self):
        """ draw the universe """
        self.myrtle.draw(self.live_cells)

    def pause(self):
        """ pause simulation """
        self.myrtle.pause()


class MyTurtle(turtle.Turtle):
    """ Turtle class to handle simple graphics """
    def __init__(self, title="Game of Life", dimension=(1200,800), speed='slow', dotsize=10):
        """  initialze the turtle object  """
        self.dotsize = dotsize
        w, h = dimension
        turtle.setup(w, h, 0,0)
        turtle.title(title)
        turtle.speed(speed)
        turtle.shape('blank')
        turtle.Turtle.__init__(self)

    def draw_cell(self, x, y, width=10):
        """ draw an individual square cell (not used)"""
        self.penup()
        self.setpos(y * width, x * width)
        self.pendown()
        for i in range(4):
            self.forward(width)
            self.right(90)

    def draw_dot(self, x, y, colour='black'):
        """ draw a dot at x,y """
        width = self.dotsize
        self.setpos(y * width, x * width)
        self.dot(width, colour)

    def draw(self, live_cells):
        """ draw entire universe from live_cell hash table """
        self.clear()
        self.penup()
        for x, y in live_cells.keys():
            # self.draw_cell(x, y)
            self.draw_dot(x, y)

    def pause(self):
        """ pause graphics until key press """
        turtle.exitonclick()


LIMIT = 100000
U = Universe(10, 10, random=True, title='Game of Life', speed='slow', dimension=(500,500))

# U.dump()

U.draw()

# run the simulation LIMIT times, if not modified, leave
for t in range(LIMIT):
    U.run_simulation()
    # if the simulation didn't change anything, we are done.
    if not U.modified:
        break

# pause.  click will finish
U.pause()

import sys
from queue import PriorityQueue
from math import sqrt


class Cell:
    """
    Represents a position in map.

    A cell has X Y coordinates, its parent cell and some function's values.
    The coordinates of the top-left one is (0, 0).

    Attributes:
    x: The cell's x position.
    y: The cell's y position.
    g: The cost to move from the start cell to this cell.
    h: Heuristic - a function that estimates how close a cell is to the goal
    (use Euclidean distance).
    f: The cost to move from the start cell to this cell &
    the estimated cost to move from this cell to the goal (f = g+h).
    parent: Its parent cell - from that it's expanded.
    """
    def __init__(self, x=0, y=0, g=0.0, h=0.0, f=float('inf'), parent=None):
        """
        Initialize a new cell with the given arguments.
        The new cell will automatically be assigned as above,
        with a f attribute of positive infinity float.
        """
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent

    def set_parent(self, parent):
        """Set parent for this cell."""
        self.parent = parent

    def compute_h_f(self, goal):
        """Compute h & f function, use Euclidean distance."""
        self.h = sqrt((goal.x-self.x)**2+(goal.y-self.y)**2)
        self.f = self.g+self.h

    def __lt__(self, other):
        """A cell with less f is  prioritized."""
        return self.f < other.f


def is_in_bounds(row, col, N):
    """Check if a successor is in bounds."""
    return (row >= 0) and (row < N) and (col >= 0) and (col < N)


def is_goal(row, col, goal):
    """Check if a cell is goal."""
    return row == goal.x and col == goal.y


def a_star_search(outfile, grid, N, start, goal):
    """
    Implement A* search algorithm.

    At each step it picks the neighbour cell having the lowest f,
    and process that cell.
    
    Arguments:
    outfile: The file to write result in.
    grid: A 2D matrix includes the status of each cell
    (it is free or obstacle).
    N: The number of row/col in grid (row = col).
    start: The start cell.
    goal: The goal cell.
    """
    # Check if start, goal are in bounds and not obstacles.
    if (not is_in_bounds(start.x, start.y, N)) or (not is_in_bounds(goal.x, goal.y, N)) or (grid[start.x][start.y] == 1) or (grid[goal.x][goal.y] == 1):
        outfile.write('-1')
        return

    # Create a closed list and initialize it to false
    # which means that no cell has been included yet
    closed_list = [[False for x in range(N)] for y in range(N)]
    open_list = PriorityQueue()
    open_list.put(start)
    found_goal = False

    while not open_list.empty():
        q = open_list.get()
        closed_list[q.x][q.y] = True

        if (q.x == goal.x) and (q.y == goal.y):
            found_goal = True
            road = []
            road.append((goal.x, goal.y))
            maps = [['-' for x in range(N)]for y in range(N)]

            for i in range(N):
                for j in range(N):
                    if (grid[i][j] == 1):
                        maps[i][j] = 'o'

            # Trace back to find the road from start to goal
            while (q.x != start.x or q.y != start.y):
                q = q.parent
                road.append((q.x, q.y))

            outfile.write('%d\n' % len(road))

            for i in range(len(road)):
                (x, y) = road.pop()
                maps[x][y] = 'x'
                outfile.write('(%d, %d) ' % (x, y))

            maps[start.x][start.y] = 'S'
            maps[goal.x][goal.y] = 'G'

            for i in range(N):
                outfile.write('\n')
                for j in range(N):
                    outfile.write('%c ' % maps[i][j])

            return

        # Coordinates of 8-successors of a cell
        successors = [(q.x-1, q.y-1), (q.x-1, q.y), (q.x-1, q.y+1), (q.x, q.y+1),
                      (q.x+1, q.y+1), (q.x+1, q.y), (q.x-1, q.y-1), (q.x, q.y)]

        for successor in successors:
            # Check if this successor is in bounds
            if is_in_bounds(successor[0], successor[1], N) == True:
                temp = Cell(successor[0], successor[1])
                # Case the successor is not in Close List & not an obstacle
                if (closed_list[temp.x][temp.y] == False) and (grid[temp.x][temp.y] == 0):
                    temp.g = q.g+1.0
                    temp.compute_h_f(goal)
                    # If `temp.parent` did not set, set parent for it
                    # or `temp.parent.f` is larger than `temp.f`, update new parent
                    # with less value of f
                    if (temp.parent == None) or (temp.parent.f > temp.f):
                        temp.set_parent(q)
                        temp.parent.f = temp.f
                        open_list.put(temp)

    if found_goal == False:
        outfile.write('-1')


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        N = int(next(f))
        start_x, start_y = map(int, next(f).split())
        goal_x, goal_y = map(int, next(f).split())
        grid = [[int(x)for x in line.split()]for line in f]
        f.close()

    start = Cell(start_x, start_y)
    goal = Cell(goal_x, goal_y)

    outfile = open(sys.argv[2], 'w')

    a_star_search(outfile, grid, N, start, goal)

    outfile.close()

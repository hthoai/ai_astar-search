from queue import PriorityQueue
from math import sqrt


class Cell:
    def __init__(self, x=0, y=0, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g+h

    def set_parent(self, parent):
        self.parent = parent

    def compute_h_f(self, goal):
        self.h = sqrt((goal.x-self.x)**2+(goal.y-self.y)**2)
        self.f = self.g+self.h

    def __lt__(self, other):
        return self.f > other.f


grid = [[None for x in range(N)] for x in range(N)]
start = Cell(0, 0)
goal = Cell(6, 6)


def is_in_bounds(row, col):
    return (row >= 0) & (row < N) & (col >= 0) & (col < N)


def is_unblocked(grid, row, col):
    return grid[row][col] == 1


def is_destination(row, col, goal):
    return row == goal.x & col == goal.y


def a_star_search(grid, start, goal):
    # Create a closed list and initialise it to false
    # which means that no cell has been included yet
    ClosedList = [[False for x in range(N)] for x in range(N)]
    OpenList = PriorityQueue()
    OpenList.put(start)
    found_goal = False

    while not OpenList.empty():
        q = OpenList.get()
        ClosedList[q.x][q.y] = True

        sx = [-1, 0, 1, 1, 1, 0, -1, -1]
        sy = [1, 1, 1, 0, -1, -1, -1, 0]

        successors = []

        for i in range(8):
            temp = Cell(q.x+sx[i], q.y+sy[i])
            if is_in_bounds(temp.x, temp.y) == True:
                if is_destination(temp.x, temp.y, goal) == True:
                    temp.set_parent(q)
                    print("Found")
                    found_goal = True
                    return
                elif (ClosedList[temp.x][temp.y] == False) & is_unblocked(gird, temp.x, temp.y) == True:
                    temp.g += 1
                    temp.compute_h_f(goal)

                successors.append(temp)

        for s in successors:
            # Check if this successor is goal
            if (s.x == goal.x & s.y == goal.y):
                return
        else:
            # Compute g (distance between successor and q)
            s.g += 1
            # Compute h (distance from goal to successor) and f
            s.compute_h_f(goal)
        elif:

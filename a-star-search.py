from queue import PriorityQueue
from math import sqrt


class Cell:
    def __init__(self, x=0, y=0, g=0.0, h=0.0, f=0.0, parent=None, parent_f=float('inf')):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent
        self.parent_f = parent_f

    def set_parent(self, parent):
        self.parent = parent

    def compute_h_f(self, goal):
        self.h = sqrt((goal.x-self.x)**2+(goal.y-self.y)**2)
        self.f = self.g+self.h

    def __lt__(self, other):
        return self.f < other.f


N = 7
grid = [[0 for x in range(N)] for y in range(N)]

grid[0][6] = grid[1][5] = grid[1][6] = 1
grid[2][0] = grid[2][1] = grid[2][6] = 1
grid[3][1] = grid[3][2] = grid[4][1] = grid[4][2] = 1
grid[4][5] = grid[5][1] = grid[5][5] = grid[6][5] = 1

start = Cell(0, 0)
goal = Cell(6, 6)


def is_in_bounds(row, col):
    return (row >= 0) & (row < N) & (col >= 0) & (col < N)


def is_blocked(row, col, grid):
    return grid[row][col] == 1


def is_destination(row, col, goal):
    return row == goal.x & col == goal.y


def a_star_search(grid, start, goal):
    # Create a closed list and initialise it to false
    # which means that no cell has been included yet
    ClosedList = [[False for x in range(N)] for y in range(N)]
    OpenList = PriorityQueue()
    OpenList.put(start)
    found_goal = False

    while not OpenList.empty():
        q = OpenList.get()
        ClosedList[q.x][q.y] = True

        sx = [-1, -1, -1, 0, 1, 1, 1, 0]
        sy = [-1, 0, 1, 1, 1, 0, -1, -1]

        for i in range(8):
            # Check if this successor is in bounds
            if is_in_bounds(q.x+sx[i], q.y+sy[i]) == True:
                temp = Cell(q.x+sx[i], q.y+sy[i])

                # Check if this successor is destination
                if is_destination(temp.x, temp.y, goal) == True:
                    temp.set_parent(q)
                    found_goal = True

                    u = goal.x
                    v = goal.y
                    road = []
                    maps = [['-' for x in range(N)]for y in range(N)]

                    for i in range(N):
                        for j in range(N):
                            if (grid[i][j] == 1):
                                maps[i][j] = 'o'

                    while (u != start.x or v != start.y):
                        t = (u, v)
                        temp = temp.parent
                        road.append(t)
                        u = temp.x
                        v = temp.y

                    for i in range(len(road)):
                        temp = road.pop()
                        maps[temp[0]][temp[1]] = 'x'

                    maps[start.x][start.y] = 'S'
                    maps[goal.x][goal.y] = 'G'

                    for i in range(N):
                        for j in range(N):
                            print(maps[i][j], end='')
                        print()

                    return

                elif (ClosedList[temp.x][temp.y] == False) and (grid[temp.x][temp.y] == 0):
                    temp.g = q.g+1
                    temp.compute_h_f(goal)

                    if temp.parent_f == float('inf') or temp.parent_f > temp.f:
                        temp.parent_f = temp.f
                        temp.set_parent(q)
                        OpenList.put(temp)

    if found_goal == False:
        print('-1')


a_star_search(grid, start, goal)

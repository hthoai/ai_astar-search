import sys
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


def is_in_bounds(row, col, N):
    return (row >= 0) & (row < N) & (col >= 0) & (col < N)


def is_destination(row, col, goal):
    return row == goal.x & col == goal.y


def a_star_search(outfile, grid, N, start, goal):
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
            if is_in_bounds(q.x+sx[i], q.y+sy[i], N) == True:
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
                    t = (start.x, start.y)
                    road.append(t)

                    outfile.write('%d\n' % len(road))

                    for i in range(len(road)):
                        temp = road.pop()
                        maps[temp[0]][temp[1]] = 'x'
                        outfile.write('(%d, %d) ' % (temp[0], temp[1])

                    maps[start.x][start.y]='S'
                    maps[goal.x][goal.y]='G'

                    for i in range(N):
                        for j in range(N):
                            outfile.write('%c ' % maps[i][j])
                        outfile.write('\n')

                    return

                elif (ClosedList[temp.x][temp.y] == False) and (grid[temp.x][temp.y] == 0):
                    temp.g=q.g+1
                    temp.compute_h_f(goal)

                    if temp.parent_f == float('inf') or temp.parent_f > temp.f:
                        temp.parent_f=temp.f
                        temp.set_parent(q)
                        OpenList.put(temp)

    if found_goal == False:
        outfile.write('-1')

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        N=int(next(f))
        start_x, start_y=[int(x)for x in next(f).split()]
        goal_x, goal_y=[int(x)for x in next(f).split()]
        grid=[[int(x)for x in line.split()]for line in f]

    start=Cell(start_x, start_y)
    goal=Cell(goal_x, goal_y)

    outfile=open(sys.argv[2], 'w')

    a_star_search(outfile, grid, N, start, goal)

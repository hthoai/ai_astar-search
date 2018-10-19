import sys
from queue import PriorityQueue
from math import sqrt
import time

class cell:
    def __init__(self, x=0, y=0,f=float('inf'), g=0.0, h=0.0):
        self.x , self.y, self.f, self.g, self.h = x, y, f, g, h
    def __lt__(self, other):
        return (self.f < other.f)
    def __ge__(self, other):
        return (self.f >= other.f)
def inBounds(n, x, y):
    return (x >= 0) and (x < n) and (y >= 0) and (y < n)

def h(x, y, g):
    return sqrt((x - g.x)**2 + (y - g.y)**2) 

def A_Star_Search(fOut, grid, n, s, g):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    if (not inBounds(n,s.x,s.y)) or (not inBounds(n, g.x,g.y)) or (grid[s.x][s.y] == 1) or (grid[g.x][g.y] == 1):
        fOut.write("-1")
        return
    
    ClosedList = [[False for x in range(n)] for y in range(n)]
    OpenList = PriorityQueue()
    Check = False
    Pa = [[(0, 0 , float('inf')) for x in range(n)] for y in range(n)]
    Pa[s.x][s.y] = -1, -1, float('inf')
    
    OpenList.put(s)

    while not OpenList.empty():
        q = OpenList.get()
        ClosedList[q.x][q.y] = True
        if (q.x == g.x) and (q.y == g.y):
            Check = True
            stack = []
            stack.append((g.x, g.y))
            u, v = g.x, g.y
            map = [['-' for x in range(n)] for y in range(n)]
            for i in range(n):
                for j in range(n):
                    if (grid[i][j] == 1):
                        map[i][j] = 'o'
            while (u != s.x) or (v != s.y):
                temp = u
                u = Pa[u][v][0]
                v = Pa[temp][v][1]
                stack.append((u, v))
            fOut.write('%d\n' % len(stack))
        
            for i in range(len(stack)):
                (u, v) = stack.pop()
                fOut.write("(%d,%d) " % (u, v))
                map[u][v] = 'x'

            map[s.x][s.y], map[g.x][g.y] = 'S', 'G'
            for row in map:
                fOut.write('\n')
                for e in row:
                    fOut.write('%c ' % e)
            fOut.write("\n")
            # for i in range(n):
            #     for j in range(n):
            #         if (Pa[i][j][2] != float('inf')):
            #             fOut.write("%0.3f " % Pa[i][j][2])
            #         else:
            #             fOut.write("       ")
            #     fOut.write("\n")
            return
        for i in range(8):
            if (inBounds(n,q.x + dx[i],q.y + dy[i])):
                p = cell(q.x + dx[i], q.y+dy[i])
                p.h = h(p.x, p.y, g)
                if (ClosedList[p.x][p.y] == False) and (grid[p.x][p.y] == 0):
                    p.g = q.g + 1.0
                    p.f = p.g + p.h
                    if (Pa[p.x][p.y][2] == float('inf')) or (Pa[p.x][p.y][2] > p.f):
                        Pa[p.x][p.y] = q.x, q.y, p.f
                        OpenList.put(p)
    if (Check == False):
        fOut.write("-1")

f = open(sys.argv[1])
g = open(sys.argv[2],"w")
reader = f.readlines()
f.close()
n = int(reader[0])
sX, sY = (int(val) for val in reader[1].split())
gX, gY = (int(val) for val in reader[2].split())
star = cell(sX, sY)
goal = cell(gX, gY)

arr = [[int(val) for val in line.split()] for line in reader[3:]]
start_time = time.time()
A_Star_Search(g,arr,n,star,goal)
g.close()
end_time = time.time()
print('total run-time: %f ms' % ((end_time - start_time) * 1000))

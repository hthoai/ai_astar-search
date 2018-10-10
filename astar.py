from queue import Queue, PriorityQueue
from math import sqrt


class Cell:
    def __init__(self, x, y, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g+h

    def compute_h_f(self, goal):
        self.h = sqrt((goal.x-self.x)**2+(goal.y-self.y)**2)
        self.f = self.g+self.h

    def __lt__(self, other):
        return self.f > other.f


start = Cell(0, 0)
goal = Cell(6, 6)
N = 7

OpenList = PriorityQueue()
ClosedList = PriorityQueue()

OpenList.put(start)

while not OpenList.empty():
    sx = [-1, 0, 1, 1, 1, 0, -1, -1]
    sy = [1, 1, 1, 0, -1, -1, -1, 0]
    q = OpenList.get()
    successors = []

    for i in range(8):
        temp = Cell(q.x+sx, q.y+sy)
        if temp.x >= 0 & temp.x < N & temp.y >= 0 & temp.y < N:
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

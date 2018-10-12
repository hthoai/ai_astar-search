# from queue import PriorityQueue
# from math import sqrt


# class Cell:
#     def __init__(self, x=0, y=0, g=0.0, h=0.0, f=0.0, parent=None, parent_f=float('inf')):
#         self.x = x
#         self.y = y
#         self.g = g
#         self.h = h
#         self.f = f
#         self.parent = parent
#         self.parent_f = parent_f

#     def set_parent(self, parent):
#         self.parent = parent

#     def compute_h_f(self, goal):
#         self.h = sqrt((goal.x-self.x)**2+(goal.y-self.y)**2)
#         self.f = self.g+self.h

#     def __lt__(self, other):
#         return self.f < other.f


# a = Cell(f=5)
# b = Cell(f=2)
# c = Cell(f=9)

# OL = PriorityQueue()
# OL.put(a)
# OL.put(b)
# OL.put(c)

# while not OL.empty():
#     t = OL.get()
#     print(t.f)

road = []
a = (4, 6)
road.append(a)
pri
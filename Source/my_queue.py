class PriorityQueue:
    def __init__(self):
        self.Q = []
        self.size = 0

    def put(self, item):
        self.Q.append(item)
        id = len(self.Q) - 1

        while (id > 0) and (self.Q[int(id)] < self.Q[int((id - 1)/2)]):
            temp = self.Q[id]
            self.Q[id] = self.Q[int((id - 1)/2)]
            self.Q[int((id - 1)/2)] = temp
            id = int((id - 1)/2)

        self.size = len(self.Q)

    def __getitem__(self, id):
        return self.Q[id]

    def get(self):
        val = self.Q[0]
        if (len(self.Q) > 1):
            self.Q[0] = self.Q[self.size - 1]
            self.Q.pop()
            n, id = len(self.Q) - 1, 0

            while True:
                left, right, temp = id * 2 + 1, id * 2 + 2, self.Q[id]
                if (left <= n and temp < self.Q[left]) and (right <= n and self.Q[right] > temp):
                    break
                if (left <= n):
                    if (right <= n) and (self.Q[right] < self.Q[left]):
                        self.Q[id] = self.Q[right]
                        self.Q[right] = temp
                        id = right
                    else:
                        self.Q[int(id)] = self.Q[int(left)]
                        self.Q[left] = temp
                        id = left
                else:
                    break
        else:
            self.Q.pop()
        self.size = len(self.Q)

        return val

    def empty(self):
        return (len(self.Q) == 0)
        
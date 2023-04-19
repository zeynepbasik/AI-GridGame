

class PriorityQueue:

    queue: list  # List of objects

    def __init__(self):
        self.queue = []

    def enqueue(self, obj: object, val: float):
      
        self.queue.append([obj, val])

        for i in range(len(self.queue) - 2, -1, -1):
            if self.queue[i][1] < self.queue[i + 1][1]:
                self.queue[i], self.queue[i + 1] = self.queue[i + 1], self.queue[i]

    def dequeue(self):
       
        return self.queue.pop(0)[0]

    def is_empty(self) -> bool:

        return len(self) == 0

    def __len__(self):
       
        return len(self.queue)

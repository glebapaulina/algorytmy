class NaiveMinPriorityQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)
        self.data.sort()

    def dequeue(self):
        x = self.data[-1]
        self.data = self.data[:-1]
        return x

    def __len__(self):
        return len(self.data)


q = NaiveMinPriorityQueue()
q.enqueue(10)
q.enqueue(1)
q.enqueue(13)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
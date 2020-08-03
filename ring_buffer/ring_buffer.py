class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for x in range(capacity)]
        self.oldest = 0;

    def append(self, item):
        if self.oldest >= self.capacity:
            self.oldest = 0
        self.storage[self.oldest] = item
        self.oldest += 1

    def get(self):
        return [x for x in self.storage if x is not None]

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
      # Check if current is less than storage
        if self.current < len(self.storage):
            self.storage[self.current] = item
            self.current += 1
        else:
          # Reset the current count to 0
            self.current -= self.capacity
            self.storage[self.current] = item
            self.current += 1
        return self.storage

    def get(self):
      # Print all numbers if it isn't None
        return [x for x in self.storage if x is not None]

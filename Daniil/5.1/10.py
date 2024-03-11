from queue import LifoQueue as Q


class Stack(Q):
    def push(self, item):
        self.put(item)

    def pop(self):
        return self.get()

    def is_empty(self):
        return self.empty()

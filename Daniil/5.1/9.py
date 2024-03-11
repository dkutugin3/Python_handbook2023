from queue import Queue as Q


class Queue(Q):
    def push(self, item):
        self.put(item)

    def pop(self):
        return self.get()

    def is_empty(self):
        return self.empty()

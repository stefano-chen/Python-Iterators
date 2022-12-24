class Even:

    def __init__(self, low, high):
        self.a = low
        self.b = high

    def __iter__(self):
        self.current = self.a
        return self

    def __next__(self):
        if self.current > self.b:
            raise StopIteration
        x = self.current
        self.current += 1
        if x % 2 == 0:
            return x
        else:
            return next(self)
    
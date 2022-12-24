class Prime:

    def __init__(self, low, high):
        if not isinstance(low, int) or not isinstance(high, int):
            raise TypeError("Invalid Type")
        if low <= 0 or low > high:
            raise ValueError("Invalid Interval")
        self.a = low
        self.b = high

    def __iter__(self):
        self.current = self.a
        return self

    def __next__(self):
        if self.current > self.b:
            raise StopIteration
        if self.current > 1:
            for i in range(2, self.current):
                if self.current % i == 0:
                    self.current += 1
                    return next(self)
        self.current += 1
        return self.current - 1

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        if self.current % 2 !=0:
            self.current += 1
        self.current += 2
        return self.current - 2


counter = Counter(0, 10)
for item in counter:
    print(item)


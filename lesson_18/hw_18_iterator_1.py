class ListReversOrder:
    def __init__(self, list_rev):
        self.list = list_rev
        self.len = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.len == 0:
            raise StopIteration
        self.len -= 1
        return self.list[self.len]


list_to_revers = ListReversOrder([1, 5, "t"])
for item in list_to_revers:
    print(item)


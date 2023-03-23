class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj

        if self.top is None:
            self.top = obj

    def pop_back(self):
        temp = self.top

        if self.top is None:
            return

        while temp and temp.next != self.last:
            temp = temp.next

        temp_last = self.last
        self.last = temp_last

        if temp_last is None:
            self.top = None

        return temp_last

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        [self.push_back(StackObj(x)) for x in other]
        return self

    def __imul__(self, other):
        return self.__mul__(other)

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
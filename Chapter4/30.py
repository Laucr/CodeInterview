class StackWithMin:
    def __init__(self):
        self._data_ = []
        self._stack_ = []

    def push(self, x):
        self._data_.append(x)
        if not self._stack_:
            self._stack_.append(x)
        else:
            if x < self._stack_[-1]:
                self._stack_.append(x)
            else:
                self._stack_.append(self._stack_[-1])

    def pop(self):
        if not self._data_:
            return None
        self._stack_.pop()
        return self._data_.pop()

    def get_min(self):
        if self._stack_:
            return self._stack_[-1]
        else:
            return None


s = StackWithMin()
s.push(7)
s.push(3)
s.push(5)
s.push(4)
s.push(2)
s.push(6)
s.push(1)

s.pop()
print(s.get_min())

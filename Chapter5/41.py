class Heap:
    """
    _type_ == 0 Min
    _type_ == 1 Max
    """
    def __init__(self, _type_=0):
        self.data = [0]
        self._type_ = _type_

    def compare(self, a, b):
        if self._type_ == 0:
            if a > b:
                return True
            else:
                return False
        else:
            if a < b:
                return True
            else:
                return False

    def insert(self, x):
        self.data.append(x)
        father = int(len(self.data) / 2)
        pos = len(self.data) - 1
        while pos > 0 and father > 0 and self.compare(self.data[father], x):
            self.up(father, pos)
            pos = father
            father = int(father / 2)

    def up(self, father, pos):
        tmp = self.data[pos]
        self.data[pos] = self.data[father]
        self.data[father] = tmp

    def get_all(self):
        print(self.data)


h = Heap()
s = []
# for i in range(10, 0, -1):
for i in range(1, 10):
    s.append(i)
    h.insert(i)
print(s)
h.get_all()

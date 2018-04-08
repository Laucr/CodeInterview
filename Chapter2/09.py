class Queue:
    def __init__(self):
        self._a_stack_ = []
        self._b_stack_ = []

    def append_tail(self, p):
        self._a_stack_.append(p)

    def delete_head(self):
        if len(self._a_stack_) == 0 and len(self._b_stack_) == 0:
            return None
        if len(self._b_stack_) != 0:
            return self._b_stack_.pop()
        else:
            while len(self._a_stack_) != 0:
                self._b_stack_.append(self._a_stack_.pop())
            return self._b_stack_.pop()


q = Queue()
a = [1, 2, 3, 4, 5]
for i in a:
    q.append_tail(i)
print(q.delete_head())
print(q.delete_head())
print(q.delete_head())
q.append_tail(6)
print(q.delete_head())
print(q.delete_head())
print(q.delete_head())

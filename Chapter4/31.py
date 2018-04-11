def is_pop_order(push_, pop_):
    if not push_ and not pop_:
        return True
    aux = [push_[0]]
    i, j = 1, 0
    while j < len(pop_) and i < len(push_):
        if pop_[j] != aux[-1]:
            while push_[i] != pop_[j]:
                aux.append(push_[i])
                i += 1
            aux.append(push_[i])
        else:
            j += 1
            aux.pop()
            i += 1
    while len(aux) != 0 and j < len(pop_) and pop_[j] == aux[-1]:
        aux.pop()
        j += 1
    if j == len(pop_):
        return True
    else:
        return False



"""
push = [1, 2, 3, 4, 5]
 pop = [4, 5, 3, 2, 1]
 
push = [1, 2, 3, 4, 5]
 pop = [4, 3, 5, 1, 2]
"""
print(is_pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

from random import random, randint
dim = 3
largo = 10
pos = [0]*dim
lista = []
def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos

for t in range(largo):
    pos = paso(pos, dim)
    print(pos)

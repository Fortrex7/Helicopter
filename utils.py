from random import randint as rand

def randbool(r, mxr): # проверка сгенерированного числа на наличие в диапазоне (генерация леса)
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h): # генерация рандомных клеток начала рек
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

# 0 - наверхб 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y): # генерация следующих клеток рек
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)

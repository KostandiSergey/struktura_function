import math 

PI = math.pi # const PI

def radius():
    n = float(input("Диаметр цилиндра в см: "))
    n /= 2
    return n 

def height():
    m = float(input("Высота цилиндра в см: "))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2 # ** в квадрате
    v = s*h
    return v

print("Обьем цилинда", volume(), " см3")    

def mass(g):
    n = float(input("Удельный вес г/см3: "))
    return g*n/1000

print("Вес цилиндра в кг: ", mass(volume()))
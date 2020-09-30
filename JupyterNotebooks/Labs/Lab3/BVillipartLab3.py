import math
#part one
sample_string = "HeY thERe HowS iT GoING"
print(sample_string.swapcase())

#part two
sample_string = "Hey There"
print(sample_string.center((len(sample_string)+8), '-'))

#part three
sample_string = "abcdefg.hijklmnop"
print(sample_string.partition("."))

#part four 
def powerRaise(x, y):
    print(x ** y)

#part five
def numCounter(num):
    arr = []
    count = 0
    for x in len(arr):
        if arr[x] == num:
            count += 1
    print(count)

#part six
def division(x, y):
    return x / y

def subtraction(x, y):
    return x - y

def slope(x1, y1, x2, y2):
    xDif = subtraction(x2 - x1)
    yDif = subtraction(y2 - y1)
    return division(yDif, xDif)

#part seven
def function(x1, x2, y1, y2):
    return((subtraction(x2 - x1) ** 2) + (subtraction(y2 - y1) ** 2))
            

'''
The reduce() function applies a function of two arguments cumulatively on a list of objects
in succession from left to right to reduce it to one value.
'''
from functools import reduce
from fractions import Fraction

def product(fracs):
    t = reduce(lambda x,y: x*y,fracs)
    return t.numerator, t.denominator

if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
#region Task
'''
•Input s is the start point, and t is the endpoint. The
tree is to left of the house, and the orange tree is to its right.

•Assume trees are located on a single point, where the apple tree
is is at point "a", and the orange tree is at point "b".

•When fruit falls from its tree, it lands "d" units of
distance from its tree of origin along the x-axis.

•A negative value of d means the fruit fell 
d units to the tree's left.

• Given the value of d for "m" apples
and "n" oranges.

Determine how many apples and oranges will fall
on Sam's house?
-----------------------------------
→ Example:
Sam's house located between "s = 7" and "t = 10"
The apple tree is located "a = 4" and the orange at "b = 12"
There are "m=3" apples and "n = 3" oranges.

→Apples are thrown "apples = [2, 3, -4]" and
"oranges = [3, -2 -4]".

→ Landing positions are 
    appleLanding = [2+4, 3+4, -4+4] → [6, 7, 0]
    orangeLanding = [3+12, -2+12, -4+12] → [15, 10, 8]
    → 1 apple and 2 oranges land in the [7, 10] range thus:
    #Output: 1
             2
---------------------------------------
Input Format:
    •The 1st line two space-separated integers donating "s" and "t"
    •The 2nd line two space-separated integers donating "a" and "b"
    •The 3rd line two space-separated integers donating "m" and "n"
    •The 4th line m space-separated integers donating appleLandings
    •The 5th line n space-separated integers donating orangeLandings

'''
#endregion

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesLanding = [num+a for num in apples]
    orangesLanding = [num+b for num in oranges]
    print(sum(pos in range(s,t+1) for pos in applesLanding), sum(pos in range(s,t+1) for pos in orangesLanding), sep="\n")

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

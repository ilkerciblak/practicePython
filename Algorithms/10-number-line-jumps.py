#region Task
'''
    Given two kangaroos on a number line read to jump in the
positive direction

•The first kangaroo starts @ location "x1" and moves 
at a rate of "v1" meters per jump

•The second kangaroo starts at location "x2" and moves
at a rate of "v2" meters per jump

→You have yo figure out a way to get both kangaroos at
same location at same time as part of the show. If it is possible
return "YES", otherwise return "NO".
--------------------------------------------
→Example:
x1, v1, x2, v2 = 2, 1, 1, 2
    •After one jump, they both at x = 3 thus
    #Output: YES

---------------------------------------------
    →Input Format:
A single line f four space-separated integers denoting the respective
values of x1, v1, x2, v2.

Constraints:
0 <= x1 < x2 <= 10k
1 <= v1 <= 10k
1 <= v2 <= 10k

'''

#endregion

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        if (x2-x1)%(v1-v2)==0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    '''

    x1, v1, x2, v2 = map(int, input().split())
    result = kangaroo(x1, v1, x2, v2)
    print(result)
#region Task
'''
The birthday cake will have one(1) candle for each year 
of their otal age. They will only be able to blow out
the tallest of the candles. Count how many candles are 
tallest.
------------------
Example:
candles = [4, 4, 1, 3]
    •The maximum height candles are 4 units high.
    •There are 2 of them, so return 2.
'''
#endregion


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#region solver_function w/o counter
def birthdayCakeCandles(candles):
    counter = 0
    for num in candles:
        if num == max(candles):
            counter += 1
    return counter
#endregion

#region solver_function w/ counter
def birthdayCakeCandles_counter(candles):
    return Counter(candles)[max(candles)]

    '''
    The solver w/o Counter() function requires more
    time to done the job!
    '''

    
#endregion


    

if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles_counter(candles)

    print(result)

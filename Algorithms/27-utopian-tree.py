#region Task
'''
→ Explanation:
    The Utopian Tree goes through 2 cycles of growth every year. Each 
    spring, it doubles in height. Each summer, its height increases 
    by 1 meter.

    How tall it be after n growth cycles ?
----------------------

→ Example:

    3 → Number of Test Cases
    0 → Initially height = 1m
    1 →  1*2 (Spring growth) = 2m
    4 →  (2 +1)*2 + 1 ([Last height+SummerGrowth]*SpringGrowth + SummerGrowth) = 7m

    # Output: 1
              2
              7

-----------------------
→ Input Format:
    •The first line contains an integer, t, the number of test cases.
    •"t" subsequent lines each contain an integer, "n", the number of
    cycles for that test case

→ Returns:
    •int: the height of the tree after the each given cycles

------------------------
'''
#endregion



def utopianTree(n):
    #region reminder
    '''
    If cycle number is an evenNumber than it's a summerGrowth (+1) 
    expect the number 0.
    But if the cycle number is an oddNumber than it's a springGrowth 
    (heigh*2).
    '''
    #endregion

    utopianTreeHeight = 1 #m
    cycle = 1
    while cycle <= n:
        if cycle % 2 == 1: #springGrowth
            utopianTreeHeight *= 2
        else: #summerGrowth
            utopianTreeHeight += 1
        cycle += 1
    return utopianTreeHeight


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        print(result)
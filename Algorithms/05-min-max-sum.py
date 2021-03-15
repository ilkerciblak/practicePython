#region Task
'''
Given five(5) positive integers, find the minimum and
maximum values that can be calculated by summing exactly
four(4) of the five(5) integers. Then print the respective
minimum and maximum values as a single line of two space
separated long integers
------
Example: arr = list( range(1, 10, 2))

The minimum sum is 1+3+5+7 = 16
The maximum sum is 3+5+7+9 = 24

#Output:16 24
'''
#endregion


def miniMaxSum(arr):
    _min = sorted(arr, reverse= False)[:4]
    _max = sorted(arr, reverse= True)[:4]

    print(sum(_min), sum(_max), sep=" ")


if __name__ == "__main__":
    arr = list( map(int, input().rstrip().split()))
    miniMaxSum(arr)



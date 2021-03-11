#region Task
'''
Given an array of integers, calculate the ratios of its 
elements that are positive, negative, and zero. Print 
the decimal value of each fraction on a new line
with 6 places after the decimal.
'''
#endregion

def solve(arr, n):
    posNum, negNum, zeroNum = 0, 0, 0
    for num in arr:
        if num > 0:
            posNum += 1/n
        elif num < 0:
            negNum += 1/n
        elif num == 0:
            zeroNum += 1/n

    return [f"{posNum:0.6f}",f"{negNum:0.6f}",f"{zeroNum:0.6f}"]

if __name__ == "__main__":
    n, arr = int(input()), map(int, input().split())
    print(*solve(arr,n), sep="\n")
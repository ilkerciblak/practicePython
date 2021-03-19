#region Task
'''
Given an array of integers and a positive integer "k", determine the
number of (i, j) pairs where i< j and arr[i]+ arr[j] is divisible by "k".

---------------------------
→Example:
    arr = [1, 2, 3 ,4 ,5 6]
    k = 5
    Three pairs meet the criteria: [1, 4], [2, 3] and [4, 6]
    #OUTPUT: 3

----------------------------
→ Input Format:
    •The 1st line contains 2 space-separated int., "n" and "k".
    •The 2nd line contains "n" space-separated int., each a value of arr[i].

→ Returns:
    •int: the number of pairs

'''
#endregion

def divisibleSumPairs(n, k, ar):
    return sum(sum())

if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().split()))
    res = divisibleSumPairs(n, k, arr)
    print(str(res))


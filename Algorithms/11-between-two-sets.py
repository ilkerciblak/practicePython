#region Task
'''
    There will be two arrays of integers. Determine all integers that 
satisfy the following two conditions:
    •The elements of the first array all factors of the int. being
considered.
    •The integer being considered is a factor of all elements 
of the second array

    Determine how many such number exists.
---------------------------------------------------
→Example:
a = [2, 6]
b = [24, 36]

There are two numbers between the array [6, 24] which 
    • num % a[i] == 0 and
    • b[i] % num == 0

Thus, #OUTPUT : 2
----------------------------------------------------
→Input Format:
    •The First line contains two space-separated integers, "n" and "m", the number
of elements in the arrays "a" and "b".
    •The second line contains n distinct space-separated integers a[i]
    •The third line contains n distinct space-separated integers b[i]

→Constraints :
    • 1 <= n,m <= 10
    • 1 <= a[i] <= 100
    • 1 <= b[j] <= 100   
'''
#endregion

def getTotalX(a, b):
    res = 0
    for num in range(a[-1], b[-1]+1):
        if any(list(map(lambda x:num%x, a))) and any(list(map(lambda x: x%num, b))):
            pass
        elif not any(list(map(lambda x:num%x, a))) and not any(list(map(lambda x: x%num, b))):
            res += 1

    return res


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    arr = [int(num) for num in input().split()]
    brr = list(map(int, input().split()))
    res = getTotalX(arr, brr)
    print(res)
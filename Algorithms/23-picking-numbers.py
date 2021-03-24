#region Task
'''
→ Explanation:
    Given an array of integers, find the longest subarray where the absolute
    difference between any two elements is less than or equal to "1".

-------------------------------------
→ Example:
    a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
    
    There are two subarrays meeting the criterion : 
    [1, 1, 2, 2] and [4, 4, 5, 5, 5].
    The maximum lentgh of subarrays is 5 thus return 5.
-------------------------------------
→ Input Format:
    •The 1st line contains a single integer "n", the size of the array a.
    •The 2nd line contains n space-separated integers, each an a[i].

→ Constraints:
    •2 <= n <= 100
    •0 < a[i] < 100
    •The answer will be >= 2

→ Returns:
    •int: the length of the longest subarray that meets the criterion

'''
#endregion


def pickingNumbers(a):
    subArraysLentgh = []
    for num in a:
        singleSubArray = [num1 for num1 in a if 0 <= num-num1 <= 1]
        subArraysLentgh.append(len(singleSubArray))
    return max(subArraysLentgh)

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    res = pickingNumbers(a)
    print(res)
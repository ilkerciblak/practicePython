#region Task
'''
Two children, Lily and Ron, want to share a chocolate bar. Each of the
squares has an integer on it. Lily decides to share a contiguous segment
of the bar selected such that:

•The length of the segment matches Ron's birth month and
•The sum of the integers on the squares is equal to his birth day.
-----------------------------------
→Example:
    s = [2, 2, 1, 3, 2]
    d = 4 #Birth Day
    m = 2 #Birth Month

    [2, 2] and [1, 3] segments meeting the criteria thus
    #OUTPUT: 2
------------------------------------
→ Input Format:
    •The 1st line contains an int "n", the number of squares.
    •The 2nd line contains n space-sep. integers on the chocolate bar.
    •The 3rd line contains two space-sep. integers "d" and "m" for birth
    day and birth month.

→ Returns:
    •int: the number of ways the bar can be divided.

→ Constraints:
    •1 <= n <= 100
    •1 <= s[i] <= 5 where 0 <= i < n
    •1 <= d <= 31 and 1 <= m <= 12

'''
#endregion

def birthday(s, d, m):
    return sum(sum(s[i:i+m])==d for i in range(len(s)))
if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d, m = map(int, input().split())
    res = birthday(s, d, m)
    print(res, end="\n")
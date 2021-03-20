#region Task
'''
Given an array of bird sightings where every element represents a bird 
type id, determine the id of the most frequently sighted type. If more
than 1 type has been spotted that maximum amount, return the smalles of
their ids.
------------------------------
→Example:
    arr = [1, 1, 2, 2, 3]
    There are two each of types "1" and "2", and one sighting of type "3".
    Pick the lower of the two types seen twice:
    #OUTPUT: 1 #type 1
-------------------------------
→ Input Format:
    •The 1st line contains an integer, "n", the size of arr.
    •The 2nd line describes arr as n space-separated ints., each
    a type number of the bird sighted.

→ Returns:
    •int: the lowest type id of the most frequently sighted birds.

→ Constraints:
    •5 <= n <= 2e+05
    •It is guaranteed that each type is 1,2,3,4 or 5.

--------------------------------
'''
#endregion

from collections import Counter

def migratoryBirds(arr):
    cnt = Counter(arr)
    '''
    arr = sorted(arr)
    for num in arr:
        if cnt[num] == max(cnt.values()):
            return num
    '''
    return min([num for num in sorted(arr) if cnt[num] == max(cnt.values())])
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = migratoryBirds(arr)
    print(res)
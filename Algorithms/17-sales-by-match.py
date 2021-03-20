#region Task
'''
There is a large pile of socks that must be paired by color. Given an array of 
integers representing the color of each sock, determine how many 
pairs of socks with matching colors there are.
------------------
→Example:
    n = 7
    arr = [1, 2, 1, 2, 1, 3 ,2]
    There is one pair of color "1" and one of color "2". There are three
    odd socks left. The number of paris is "2".
-------------------
→ Input Format:
    •The 1st line contains an int "n", the # of socks represented in arr.
    •The 2nd line contains n space-separated ints, ar[i].

→ Returns
    int: the number of pairs

'''
#endregion

def sockMerchant(n, ar):
    matchCount = 0 # Initilization
    for i in range(len(ar[:-1])): #In order to not to run last item, last item cannot be the firstColor to match
        for j in range(i+1, len(ar)): 
            if ar[i] == None:
                break
            elif ar[i] == ar[j]:
                matchCount += 1
                ar[j] = None
                break
                
    return matchCount




if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = sockMerchant(n, arr)
    print(res)

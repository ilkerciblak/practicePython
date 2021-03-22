#region Task
'''
Given the sequence of up and down steps during a hike, find
and print the number of valleys walked through.
--------------------
→Example:
    steps = [UDDDUDUU]
    #OUTPUT = 1

--------------------
→ Input Format:
    •The 1st line contains an int "steps", number of steps in the hike.
    •The 2nd line contains the characteristics of steps = U or D

→ Returns:
    •int:the number of valleys traversed

---------------------
'''
#endregion

def countingValleys(steps, path):
    hikerLevel = 0
    countValley = 0
    for i in range(steps):
        if path[i] == "U":
            hikerLevel += 1
            if hikerLevel == 0:
                countValley += 1
        elif path[i] == "D":
            hikerLevel -= 1
        
        
    return countValley

if __name__ == "__main__":
    from itertools import permutations
    n = int(input()) # number of steps
    path = input()
    print(countingValleys(n, path))
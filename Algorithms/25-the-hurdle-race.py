#region Task
'''
→ Explanation:
    A video player plays a game in which the character competes in a hurdle
    race. Hurdles are of varying heights, and the characters have a maximum
    height they can jump. There is a magic potion they can take that will 
    increase their maximum jump height by "1" unit for each dose. How many
    doses of the potion must the character take to be able to jump all of 
    all of the hyrdles. If the character can already clear all of the hurdles
    return 0.

----------------------------------
→ Example:
    height = [1, 2, 3, 3, 2]
    k = 1

    The character can jump 1 unit high initially and must take 
    3 - 1 = 2 doses of potion to be able to jump all of the hurdles.


------------------------------------
'''
#endregion



def hurdleRace(k, height):
    return [abs(max(height) - k) if max(height) > k else 0][0]
    
if __name__ == "__main__":
    n, k = map(int, input().strip().split())

    height = list(map(int, input().strip().split()))
    res = hurdleRace(k, height)
    print(res)

#region Task
'''
→Given the scores for a season, determine the number of times Maria breaks
her records for most and least points scored during the season.
----------------------
→Example:
    scores = [10, 5, 20, 20, 4, 5 ,2, 25, 1]
    #Output (max, min): 2 4

----------------------
→Input Format:
    •The first line contains an integer "n", the number of games in a season.

    •The second line contains "n" space-separated integers describing the
    scores.

→Returns:
     An array with the numbers of times she broke her records. Index 0
    is for breaking most points, the index 1 is for breaking least points.
-----------------------
'''
#endregion

def breakingRecords(scores):
    recordMost, recordLeast = scores[0], scores[0]
    breakMost, breakLeast = 0, 0
    for num in scores:
        if num>recordMost:
            recordMost = num
            breakMost += 1
        elif num<recordLeast:
            recordLeast = num
            breakLeast += 1
    return [breakMost, breakLeast]

if __name__ == "__main__":
    n = int(input()) # Number of games
    scores = list(map(int, input().rstrip().split())) # list of scores
    result = breakingRecords(scores)
    print(" ".join(map(str, result)))
#region Task
'''
→ Explanation:
    A magic square to be an "n by n" matrix of distinc positive ints
    from 1 to n**2 where the sum of any row, column, or diagonal
    or lenthg "n" is always equal to the same number: the magic constant.


-------------
→ Example:
    givenMatrix = 5 3 4    →Magic Square:8 3 4 
                  1 5 8                  1 5 9
                  6 4 2                  6 7 2

    replacements : 5→8, 8→9, 4→7 
    Thus cost is abs(5-8)+abs(8-9)+abs(4-7) = 7

---------------
→ Input Format:
    •Each of the 3 lines contains three space-separated integers
    of row s[i].

→ Constraints:
    1 <= s[i][j] <= 9 

→ Returns:
    •int: the minimal total cost of converting the input square to
    a magic square.
------
'''
#endregion


def formingMagicSquare(s):
    
    magicMatrixList = [
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
    
    costs = []
    for singleMagicMatrix in magicMatrixList:
        cost = 0
        for singleMagicMatrixRow, sRow in zip(singleMagicMatrix, s):
            for num1, num2 in zip(singleMagicMatrixRow, sRow):
                if num1 != num2:
                    cost += abs(num1-num2)
        costs.append(cost)
    return min(costs)
    
   
if __name__ == "__main__":
    s = list()
    for _ in range(3):
        s.append(list(map(int, input().split())))
    res = formingMagicSquare(s)
    print(res)
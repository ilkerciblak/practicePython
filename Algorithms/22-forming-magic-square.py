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
    
    sTranspose = list()
    for i in range(3):
        elm = []
        for j in range(3):
            elm.append(s[j][i])
        sTranspose.append([elm])
  

if __name__ == "__main__":
    s = list()
    for _ in range(3):
        s.append(list(map(int, input().split())))
    res = formingMagicSquare(s)
    print(res)
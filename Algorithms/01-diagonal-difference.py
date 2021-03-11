#region Task
'''
Given a square matrix, calculate the abs difference
between the sums of its diagonals.
'''

#endregion

if __name__ == "__main__":
    n = int(input())
    arr = [input().split() for _ in range(n)]
    firstDiagonalNum, secondDiagonalNum = 0,0
    for i in range(len(arr)):
        firstDiagonalNum += int(arr[i][i])
        secondDiagonalNum += int(arr[i][n-i-1])
    
    print(abs(firstDiagonalNum-secondDiagonalNum))
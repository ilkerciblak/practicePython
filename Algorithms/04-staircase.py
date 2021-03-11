#region Task
'''
For a int input, like n=4 print an # staircase
   #
  ##
 ###
#### → n=4

'''
#endregion


def solve(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)

if __name__ == "__main__":
    n = int(input())
    solve(n)

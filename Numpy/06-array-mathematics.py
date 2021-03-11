#region Explanation
'''
► Basic mathematical functions operate →element-wise← on arrays.
They are avaliable both as operator overloads and as functions
► For the arrays A, B:
    • A+B = np.add(A, B)
    • A-B = np.subtract(A, B)
    • A*B = np.multiply(A, B)
    • A/B = np.divide(A, B)
    • A%B = np.mod(A, B)
    • A**B = np.power(A, B) 
Both methods can be used!
'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    ► For given arrays A and B of dim NxM perform following operations:
    •Addition
    •Subtract
    •Multiply
    •Division
    •Mod
    •Power
    '''
    #endregion
    import numpy as np
    n, m = map(int, input().split())
    arr_A = np.array([[int(num) for num in input().split()]  for _ in range(n)])
    arr_B = np.array([[int(num) for num in input().split()]  for _ in range(n)])
    print(*[eval("arr_A"+opr+"arr_B") for opr in ["+", "-", "*", "//", "%", "**"]], sep="\n")

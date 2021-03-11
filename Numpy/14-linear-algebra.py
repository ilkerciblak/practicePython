#region Explanation
'''
from numpy import linalg

► The linalg.det(list_array) computes the determinant of an array.
    •print(linalg.det([[1, 2], [2, 1]]))  #Output: -3.0 → Default Type of Elements is Float!

► The linalg.inv(list_array) computes the multiplicative inverse of a matrix.
    •print(linalg.det([[1, 2], [2, 1]]))  #Output: [[-.333.., .666..],
                                                    [0.66.., -0.333]]

► The linalg.eig(list_array) eigenvalues and right eigenvectors of a square array.
    •vals, vecs = linalg.eig([[1, 2], [2, 1]])
    print(vals, vecs, sep="\n")           # Output:[3. -1.]
                                                   [[0.707, -0.707],
                                                    [0.707,  0.707]]

► Other routines can be found from http://docs.scipy.org/doc/numpy/reference/routines.linalg.html
'''
#endregion

if __name__ == "__main__":
    from numpy import linalg
    #region Task
    '''
    Given matrix A with dims NxN (user imput), task is to find
    determinant. Note: round the answer to 2 places after the 
    decimal.
    '''
    #endregion

    n = int(input("Enter the number of rows:    ")) #Number of rows
    arr_A = [[float(num) for num in input("Enter row of numbers:  ").split()] for _ in range(n)]
    print(round(linalg.det(arr_A), 2))
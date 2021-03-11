#region Explanation
'''
The tools np.inner(A, B), np.outer(A, B) returns 
the inner and outer product of two arrays.
'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    Given two arrays A and B, task is to compute inner and outer products.
    '''
    #endregion

    import numpy as np
    arr1, arr2 = np.array([input("Enter a row of numbers:   ").split()], dtype= int), np.array([input("Enter a row of numbers:   ").split()], dtype= int)
    print(*np.inner(arr1, arr2)[0], np.outer(arr1, arr2), sep="\n")
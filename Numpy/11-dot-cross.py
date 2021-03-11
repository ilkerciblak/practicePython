#region Explanation
'''
The np.dot(arr1, arr2) and np.cross(arr1, arr2) returns the dot and cross
products of given arrays, respectively.

A, B = np.array([1,2]), np.array([3,4])

→np.dot(A, B) #Output: 11
→np.cross(A, B) #Output: -2

'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    Given two arrays A, B w/ dims NxN (user input)
    Task is to compute matrix product.
    '''
    #endregion

    import numpy as np
    n = int(input())
    arr1, arr2 = np.array([input("Enter a row of numbers:    ").split() for _ in range(n)], dtype = int), np.array([input("Enter a row of numbers:    ").split() for _ in range(n)], dtype = int)
    print(np.dot(arr1, arr2))
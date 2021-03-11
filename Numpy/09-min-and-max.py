#region Explanation
'''
The tools np.min(my_array, axis= int) and np.max(my_array, axis =int)
returns the minimum and maximum value along the given axis, respecively.

For arr = np.array([[2, 5], [3, 7], [1, 3], [4, 0]]])
        max:                  min:
axis  --------              -------
 0     [4, 7]                [1, 0]
 1   [5, 7, 3 ,4]         [2, 3, 1, 0]
None      7                     0
'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    For a given 2-D array w/ dims NxM (user input)
    perform the min function over axis 1 and then find the max of that.
    '''
    #endregion
    import numpy as np
    n, m = map(int, input("Please give the row and column numbers:    ").split())
    arr = np.array([input().split() for _ in range(n)], dtype = int)
    print(np.max(np.min(arr, axis = 1)))

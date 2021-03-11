#region Explanation
'''
The np.mean(my_array, axis= int), np.var(my_array, axis= int) and
np.std(my_array, axis= int) returns the arithmetic mean, variance and standard
deviation along the specified axis, respectively

‼ The Default type of output elements is FLOAT ‼

For arr = np.array([[1, 2], [3, 4]])
        mean:                 var:           std:
axis  --------              -------        -------
 0     [2., 3.]             [1., 1.]        [1., 1.]
 1    [1.5, 3.5]           [0.25, 0.25]    [0.5, 0.5]
None     2.5                  1.25           1.11803..
'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    For a given 2-D array of size NxM(user input)
    Find:
    1. Mean, axis=1
    2. Var, axis = 0
    3. std, axis = None
    '''
    #endregion

    import numpy as np
    np.printoptions
    n, m = map(int, input("Please enter the row and column numbers:     ").split())
    arr = np.array([input("Enter a row of numbers      ").split() for _ in range(n)], dtype= float)
    print(np.mean(arr, axis=1), np.var(arr, axis = 0), round(np.std(arr, axis= None), 11), sep = "\n")
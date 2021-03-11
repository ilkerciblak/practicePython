#region Explanation
'''
► The np.sum(my_array, axis = int) returns sum of array elements over a given axis

my_array = np.array([[1, 2], [3, 4]])
•np.sum(my_array, axis = 0) #Output : [4, 6]
•np.sum(my_array, axis = 1) #Output : [3, 7]
•np.sum(my_array, axis = None) #Output : 10
•np.sum(my_array) #Output : 10


► The np.prod(my_array, axis= int) returns the product of array elements over a given axis
my_array = np.array([[1, 2], [3, 4]])
•np.prod(my_array, axis = 0) #Output : [3, 8]
•np.prod(my_array, axis = 1) #Output : [2, 12]
•np.prod(my_array, axis = None) #Output : 24
•np.prod(my_array) #Output : 24

'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    A given 2-D array with dim NxM perform the sum over axis 0
    and then find the product of that result.
    '''
    #endregion

    import numpy as np
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], dtype= int)
    print(np.prod(np.sum(arr, axis = 0), axis = None))
    
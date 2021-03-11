#region Explanation
'''
► The np.floor(my_array) returns the floor of the input ‼element-wise‼
The default element type is FLOAT!

► The np.ceil(my_array) returns the ceil of the input ‼element-wise‼
The default element type is FLOAT!

► The np.rint(my_array) rounds tot he nearest integer of input ‼element-wise‼
The default element type is FLOAT!

'''
#endregion

if __name__ == "__main__":
    #region Task
    '''
    Given 1D array,A. Task is to print floor, 
    ceil and rint of all elements in A
    '''
    import numpy as np
    np.set_printoptions(legacy = "1.13")
    arr_A = np.array([*input().split()], dtype = float)
    print(np.floor(arr_A), np.ceil(arr_A), np.rint(arr_A), sep="\n")
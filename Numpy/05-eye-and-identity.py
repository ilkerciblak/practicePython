#region Explanation
'''
♦ The identity(integer) returns an identity array with dimensions
integerXinteger. An identity array is a square matrix w/ all the
main diagonal elements are "1" and the rest as "0".

np.identity(3) → [[1. 0. 0.] 
                  [0. 1. 0.] → Default type of elements is Float!
                  [0. 0. 1.]]

♦ The np.eye(int, int, k= int) return a 2-D array with "1"'s as the 
assigned diagonal(k=var) "0"'s elsewhere. A positive "k" refers upper diagonal
a negative k refers to the lowers. (k = 0 is for the main diagonal)

np.eye(4,3, k = -1) →[[0. 0. 0.]
                      [1. 0. 0.] → Default type of elements is Float!
                      [0. 1. 0.]
                      [0. 0. 1.]] 

'''
#endregion
if __name__ == "__main__":
    #region Task
    '''
    Task is to print an array of size NxM (user inputs) with its
    main diagonal elements as 1's and 0's elsewhere.
    '''
    #endregion
    import numpy as np
    np.set_printoptions(legacy = '1.13')
    n, m = map(int, input().split())
    print(np.eye(n, m, k= 0))

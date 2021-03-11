if __name__ == "__main__":
#region    
    '''
    import numpy as np
    arr1 = np.array([[1,2,3], [0,0,1]])
    arr2 = np.array([[0,0,2], [4,5,6]])
    print(np.concatenate((arr1,arr2), axis = 1))

    print("-"*20)

    arr1 = np.array([[1,2,3], [0,0,1]])
    arr2 = np.array([[0,0,2], [4,5,6]])
    print(np.concatenate((arr1,arr2), axis = 0))
    '''
#endregion
import numpy as np
n, m, k = map(int, input().split())
arr1 = np.array([[int(num) for num in input().split()] for _ in range(n)])
arr2 = np.array([[int(num) for num in input().split()] for _ in range(m)])
print(np.concatenate((arr1,arr2), axis=0))

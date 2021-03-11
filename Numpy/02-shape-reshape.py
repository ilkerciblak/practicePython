if __name__ == "__main__":
    import numpy as np

    arr = np.array([int(num) for num in input().split()])
    #print(arr)
    print(np.reshape(arr, (3,3)))
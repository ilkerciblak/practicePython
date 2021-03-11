if __name__ == "__main__":
    import numpy as np
    n, m = map(int, input().split())
    arr = np.array([[int(num) for num in input().split()] for _ in range(n)])
    print(np.transpose(arr), arr.flatten(), sep="\n")
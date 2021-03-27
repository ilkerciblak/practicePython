#region Task
'''
→ Explanation:
    An angry professor decides to cancel class if fewer than thresholded
    number of students are present when the class starts. Determine whether
    she/ he cancels the class or NOT.

-------------------
→ Example:
    n, threshold = 5, 3
    arrivalTimes = [-2, -1, 0, 1, 2]

    Arrivial on time or early indicated with the (-∞, 0]
    Arrival late indicated with the interval (0, ∞)

    Thus arrivalLate = 2 < threshold thus class GOES ON !

---------------------
→ Input Format:
    •The 1st line of input contains t, the number of test cases.
    • Each test case consists of two lines,
    The 1st line has two space-separated integers, n and k, the number of
    students and the cancellation threshold.
    The 2nd line contains "n" space-separated integers that describe the
    arrival time for each student.

→ Returns:
    •string: either YES or NO. It must return YES if class is cancelled!

'''
#endregion

import time

def angryProfessor(k, a):
    '''
    attendance = studentID =  0
    while studentID < len(a):
        if a[studentID] <= 0:
            attendance += 1
            if attendance == k:
                return "NO"
        studentID += 1
    return "YES"
    '''
    return ["YES" if sum([1 if i else 0 for i in map(lambda x:x<=0, sorted(a))]) < k  else "NO"][0]

if __name__ == "__main__":
    t = int(input()) # number of testCases
    start = time.time()
    for t_itr in range(t):
        n, k = map(int,input().strip().split())  # number of students and calcellationThreshold
        a = list(map(int, input().strip().split())) # list of arrivalTime of each student
        print(angryProfessor(k, a))
    end = time.time()
    print(f"Elapsed Time = \t{end-start}")
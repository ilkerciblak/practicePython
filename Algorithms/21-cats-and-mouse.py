#region Task
'''
→ Explanation:
    Two cats and a mouse are at various position on a line. You will
    be given their starting position. Your task is to determine which
    reach the mouse first, assuming the mouse does not move and the
    cats travek at equal speed. 
    If the cats arrive at the same time, the mouse will be allowed
    to move and escape.
------------------------
→ Example:
    x, y, z = 2, 5, 4
    The cats are at pos 2, 5 and the mouse at pos 4. Cat B will
    arrive first since it is only "1" unit away while the other
    is "2" units away. Return "Cat B".
------------------------
→ Input Format:
    •The 1st line contains a single int, "q" denoting the number 
    of queries.
    Each of the q subsequent lines contains three space-sep. int
    describing the respective values of catA_Loci, catB_Loci, 
    mouse_Loci

→ Return:
    •string: Either "Cat A", "Cat B", "Mouse C"

'''
#endregion

def catAndMouse(x, y, z):
    chickenDinner = ["Cat A" if abs(x-z) < abs(y-z) else "Cat B" if abs(x-z) > abs(y-z) else "Mouse C"]
    return chickenDinner[0]

if __name__ == "__main__":
    q = int(input())
    for i in range(q):    
        x, y, z = map(int, input().rstrip().split())
        result = catAndMouse(x, y, z)
        print(result)
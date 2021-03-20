#region Task
'''
Two friends Anna nad Brian trying to split the bill. You must
determine if his calculation is correct.
-------------------------------------
→ Example:
    bill = [2, 4, 6]
    Anna declines to eat the item k = bill[2] which costs 6.
    Correct calculation of billAnna = sum[:k] = (2+4)/2 = 3
--------------------------------------
→ Input Format:
    •The 1st line contains 2 space-separated integers "n" and "k",
    the number of items ordered and 0-based index of the item that
    Anna did not eat.
    •The 2nd line contains n space-separated ints bill[i] where
    0<= i < n.
    •The 3rd line contains an int, "b" the Brian's calculation for
    billAnna.

→ Returns:
    • If billAnna is correct, return "Bon Appetit" on a new line.
    • Otherwise, return the difference that Brian has to refund to Anna

----------------------------------------
'''
#endregion

def bonAppetit(bill, k, b):
    print(*[int(b - sum(bill[:k]+bill[k+1:])/2) if b != sum(bill[:k]+bill[k+1:])/2 else "Bon Appetit"])
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    bill = list(map(int, input().split()))
    b = int(input())
    bonAppetit(bill, k, b)
#region Task
'''
→ Explantation:
    A person wants to determine the most expensive computer keyboard 
    and USB drive that can be purchased with a give budget. Given
    price lists for keyboards and USB drives and a budget, find the
    cost to buy them. If it is not possible to buy both items
    return "-1".

-----------------------
→ Example:
    b = 60
    keyboards = [40, 50, 60]
    usbDrives = [5, 8, 12]

    The person can buy:
    40 keyboard + 12 UsbDrive = 52 or
    50 keyboard + 8 UsbDrive = 58.

    Choose the expensive option and return 58.
--------------------------
→ Input Format:
    •The 1st line contains three space-separated ints "b, n, and m".
    The budget, the # of keyboard and usbDrive models.
    •The 2nd line contains "n" space-separated ints which refer to
    keyboardCoast of each model.
    •The 3rd line contains "m" space-separated ints which refer to
    usbDriveCoast of each model.

→ Returns:
    •int: the maximum that can be spent, or "-1" if it is not possible
    to buy both items.

-----------------------------
'''
#endregion


def getMoneySpent(keyboards, drives, b):
    from itertools import product
    res = [sum(nums) if sum(nums) <= b else -1 for nums in product(keyboards,drives)]
    return max(res)
    


if __name__ == "__main__":
    b, n, m = map(int, input().rstrip().split())
    keyboards = [int(num) for num in input().split()]
    drives = [int(num) for num in input().split()]
    res = getMoneySpent(keyboards, drives, b)
    print(res)
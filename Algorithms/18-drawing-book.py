#region Task
'''
This is too long to write soo...
-------------
→ Input Format:
    •The 1st line contains an int "n" the number of
    pages in the book.
    •The 2nd line contains an int, "p" the page 
    to turn to.
→ Returns:
    •int: the minimum number of pages turn
--------------
→ Example:
    n, p = 6, 2
    #OUTPUT: 1

    If the std. starts turning from page "1",
    they only need to turn 1 page.

'''
#endregion

def pageCount(n, p):
    pages = [[page, page+1] for page in range(0,n+1,2)]
    turns =[*[i for i, nums in enumerate(pages) if p in nums], *[i for i, nums in enumerate(pages[::-1]) if p in nums]]
    return min(turns)
if __name__ == "__main__":

    n = int(input())
    p = int(input())
    res = pageCount(n, p)
    print(res)
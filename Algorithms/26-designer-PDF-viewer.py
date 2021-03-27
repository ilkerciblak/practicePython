#region Task
'''
→ Explanation:
    With 0th order indexing, Using the letter heights given, determine the
    determine the are of the rectangle heighlight in mm**2 assuming all letters
    are 1mm wide.

----------------------------------
→ Example:
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 
    5, 5, 5, 5, 5, 5]
    word = 'torn'

    The heights are t=2, o = r = n = 1. The tallest letter is "2" heigh and
    there are 4 letters. Area = 2* 4= 8 mm**2

    Return 8

-----------------------------------
→ Input Format:
    •The 1st line contain h[26]: the heights of each letter
    •The second line contains a single word consisting of lowercase
    English alphabetic letters

→ Returns:
    •int: the size of the highlighted area

-----------------------------------------

'''
#endregion



def designerPdfViewer(h, word):
    import string
    maxHeight = 0
    for letter in word:
        if h[string.ascii_lowercase.index(letter)] > maxHeight:
            maxHeight = h[string.ascii_lowercase.index(letter)]
    return maxHeight*len(word)
    
if __name__ == "__main__":
    h = list(map(int, input().strip().split()))

    word = input()
    print(designerPdfViewer(h, word))
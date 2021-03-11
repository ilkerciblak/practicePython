'''
http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
'''

def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun


if __name__ == "__main__":

    #region Task
    '''
    The given mobile numbers may have +91, 91, 0 written
    before the actual 10 digit number. Standardize them as
    +91 xxxxx(5) xxxxx(5) format and sort them in ascending order
    '''
    #endregion
    
    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep="\n")


    l = [input() for _ in range(int(input()))]
    sort_phone(l)

#region Explanation
'''
► The np.poly(my_array) returns the coeff. of a polynomial
with the given sequence of roots.
    •print(np.poly([-1 1 1 10])) #Output: [1 -11 9 11 -10]

► The np.roots(my_array) returns the roots of a polynomial
with the given sequence of coefficients.
    •print(np.roots([1 0 -1])) #Output: [-1. 1.] → Default type of elements FLOAT!

► The np.polyint(my_array) returns an antiderivative(indefinite integral)
of a polynomial
    •print(np.polyint([1 1 1])) #Output: [0.3333 0.5 1. 0.] → Default type of elements is FLOAT!

► The np.polyder(my_array) returns the derivative 
of the specified order of a polynomial.
    •print(np.polyder([1 1 1 1])) #Output: [3 2 1]

► The np.polyval(my_array, x) evaluates the polynomial at specified value.
    •print(np.polyval([1 -2 0 2], 4)) #Output: 34

► The np.polyfit(my_array) fits a polynomial of a specified 
order to a set of data using a ‼least-squares‼ approach.
    •print(np.polyfit([0 1 -1 2 -2], [0 1 1 4 4], 2)) #Output: [1.00e+00 0.00e+00 -3.9720..e-16]

► Also the are functions polyadd, polysub, polymul, and polydiv to handle
proper operations respectively.

https://numpy.org/doc/stable/reference/routines.polynomials.html

'''
#endregion

if __name__ == "__main__":
    import numpy as np
    #region Task
    '''
    Given coefficients of a poly P(user input), task is to find
    the value of P at point x(user input).
    '''
    #endregion

    poly_eqn = list(map(float, input("Enter the coefficients:").split()))
    x = float(input("Enter the point:             "))
    print(np.polyval(poly_eqn, x))

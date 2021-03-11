#region Task
'''
For this challenge, you are given two complex numbers, 
and you have to print the result of their addition, subtraction, multiplication, 
division and modulus operations.

The real and imaginary precision part should be 
correct up to two decimal places.
'''
#endregion
import math
#region Class Complex
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __add__(self, other):
        return Complex((self.real+ other.real), (self.img+ other.img))
    
    def __sub__(self, other):
        return Complex((self.real- other.real), (self.img- other.img))

    def __mul__(self, other):
        return Complex((self.real* other.real- self.img* other.img),
                        (self.real* other.img + self.img* other.real))
    
    def __truediv__(self, other):
        try:
            return self.__mul__(Complex(other.real, -1 * other.img)).__mul__(Complex(1.0/(other.mod().real)**2, 0))
        except BaseException as e:
            print("Error Code: ", e)
            return None
    def mod(self):
        return Complex(pow(self.real**2+self.img**2, 0.5), 0)
    def __str__(self):
        if self.img == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % (self.img)
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img > 0:
            result = "%.2f+%.2fi" % (self.real, self.img)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img))
        return result
#endregion
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

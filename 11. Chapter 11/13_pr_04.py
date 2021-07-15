# (a+bi)(c+di) = (ac−bd) + (ad+bc)i   #complex number operations

class Complex:
    def __init__(self, r, i):          #r=real, i=imaginary part of 1st complex number
        self.real = r 
        self.imaginary = i

    def __add__(self, c):              # c represents the 2nd complex number
        return Complex(self.real + c.real, self.imaginary + c.imaginary) # add() returns objects of the same class  #2 complex numbers added, real added to real parts and img to img parts
    
    def __mul__(self, c):
        mulReal =  self.real*c.real - self.imaginary*c.imaginary
        mulImg =  self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)


    # def __str__(self):
    #     return f"{self.real} + {self.imaginary}i"     # you can write like also or like below
    
    
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(1, -4)
c2 = Complex(331, -37)
print(c1 + c2)         # to print this in a format we use __str__ dunder method
print(c1 * c2)
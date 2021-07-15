#single inheritence

class C2dVec:                        #base class
    def __init__(self, i, j):       # use constructor -used for instantiating an object. assign values to the data members of the class when an object of class is created.
        self.icap = i
        self.jcap = j
 
    def __str__(self):                         # this dunder method used to show o/p in a prticular format.
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):              # child class
    def __init__(self, i, j, k):
        super().__init__(i, j)     # super method used to access methods of a super class in the derived class. i,j base class will be accessed in child class
        self.kcap = k              # istead of wrting like this for i,j we used super()
     
    def __str__(self):             # this dunder method used to show o/p in a prticular format.
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)        #objects created for base class 
v3d = C3dVec(1, 9, 7)     #objects created for child class 
print(v2d)
print(v3d)

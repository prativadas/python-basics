#operotor overloading of sum and dot product

class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):       #prints the o/p in a readable format
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):                    # '+' operator will append the elemnts of  one list to the 2nd list; so we use for loop for adding(sum) the elemnts foe both list index wise.
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self, vec2):              # for dot product. scalar quantity
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1+v2)              # add 1+1,4+6,6+9
print(v1*v2)
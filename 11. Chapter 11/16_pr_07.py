#find length of vector in previous method 

class Vector:
    def __init__(self, vec):          #vector 1
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):       #vector 2
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
            # if len(self.vec) != len(vec2.vec):
            #      print('addition failed as length is not same') #debug ????when len of 2 vectors are not same print msg that sum and dot product failed
            # else:                                      
            #      print('addition sucessful') 
        return Vector(newList)
    
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):                #can we use exception handle when dot prod of 2 different dimension vector
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    # def __len__(self):               #prints lenth of a vector
    #     return len(self.vec)

    # def __len__(self, vec2):                      #prints length of a vector
    #     if len(self.vec) != len(vec2.vec):                           # ????when len of 2 vectors are not same print msg that sum and dot product failed
    #         print('addition failed as length is not same')
    #     else:
    #         return len(self.vec)
        
    
            
v1 = Vector([1, 4, 6, 6])
v2 = Vector([1, 6, 9])
# print(len(v1))
# print(len(v2))

print(v1+v2)              # add 1+1,4+6,6+9
print(v1*v2)
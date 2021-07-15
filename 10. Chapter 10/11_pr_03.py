class Sample:
    a = "Harry"      # class atrr

obj = Sample()       # object of class sample
obj.a = "Vikky"     # instance atrr with same same name 'a'.
# obj.a = "Vikky"    #if we comment ou this, then print(obj.a)  returns harry by default value.
# Sample.a = "Vikky"  #this way we can change the value of class attr

print(Sample.a)      # doesnt change its value.
print(obj.a)         # instance attributes takes preferenace over class attribute during assignmnet and retrieval.
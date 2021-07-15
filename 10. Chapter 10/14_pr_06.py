class Sample: 
    def __init__(slf, name):         #instead of using self parameter we can name it anything, it will still work. but we usually dont do it.
        slf.name = name

obj = Sample("Harry") 
print(obj.name) 
 
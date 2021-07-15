class Programmer:
    company = 'Microsoft'              #class attr

    def __init__(self, id,name, salary):      #why do we need constructor? as it initializes the objects #info about programmer. objects of class is instantiated
        self.id=id                            # these arguements are passed as arguements of class while object is created below.
        self.name=name                        ## object instantiated.
        self.salary=salary

    # def getInfo(self):
    #     print(f'id of programmer is:{self.id}')
    #     print(f'name of programmer is:{self.name}')
    #     print(f'salary of programmer is:{self.salary}')
    
    # def getInfo(self,id,name, salary):   # doesnt work this way
    def getInfo(self):             
        print(f'id of programmer is:{self.id} name is:{self.name} salary is:{self.salary} ')

    

programmer1 = Programmer('20','liva', '2lac')   # objects of class.# always type out of the class scope #instance attr
programmer2 = Programmer('9','liza', '3lac') 
programmer3 = Programmer('12','rinku', '2lac') 


programmer1.getInfo()
programmer2.getInfo()

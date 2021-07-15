
class RailwayForm:
    formType = "RailwayForm"               # class attributes
    def printData(self):
        print(f"Name is {self.name}")      # self refers to the instance of class. automatically passed with a function call from an object.
        print(f"Train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"                #instance attributes
harrysApplication.train = "Rajdhani Express"
harrysApplication.printData()
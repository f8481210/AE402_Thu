class Human():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        
    def bmi(self):
        return self.weight/ ((self.height/100)**2)
'''    
a = Human('NN',60,165)
print("name",a.name)
print("weight",a.weight)
print("height",a.height)
print("bmi",a.bmi())
'''   
'''
class Woman(Human):
    def __init__(self, name, weight, height, bust, waist, hip):
        super().__init__(name, weight, height)
        self.bust=bust
        self.waist=waist
        self.hip=hip
    
    def printBWH(self):
        print(" bust={}, waist={}, hip={}".format(self.bust, self.waist, self.hip))
'''
class Student(Human):
    def __init__(self, name, weight, height, study):
        super().__init__(name, weight, height)
        self.study = study
    
    def description(self):
        if self.study:
            print(self.name , "is a student")
        else:
            print(self.name , "is not a student")

        
    
    

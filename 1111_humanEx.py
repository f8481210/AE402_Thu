'''
class Human():
    pass


a = Human()
a.name = "Zi yi"
a.learn = "Python"

b = Human()
b.name = "Maurice"
b.learn = "Pygame"

c = Human()
c.name = "Yu"
c.learn = "English"
'''
#class有幾個？
#Object 有幾個？ > 都是從Human創造出來的

class Human():
    def __init__(self,name,learn):
        self.name = name
        self.learn = learn
        
a = Human("Zi yi", "Python")
b = Human("Maurice", "Pygame")
c = Human("Yu", "English")


class A:
    def __init__(self):
        super().__init__()
        self.title = "Implementing A"
        self.name = "Class A"
        self.price = 10

class B:
    def __init__(self):
        super().__init__()
        self.title = "Implementing B"
        self.name = "Class B"
        self.type = "hardprint"

class C(A,B):
    def __init__(self):
        super().__init__()
        pass

    def display(self):
        print(self.title)
        print(self.name)
        print(self.type)
        print(self.price)

c1 = C()
c1.display()
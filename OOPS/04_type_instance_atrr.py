
class publication:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class book(publication):
    def __init__(self,title,author):
        super().__init__(title,author) 

    def display(self):
        if(hasattr(self,"author")):
           print(self.title+" "+ self.author)


b1 = book("The secret","Murphy")

b1.display()

print(isinstance(b1,book))

print(type(b1))

varInt = 11
varFloat = 1.22
varString = "this is a string"
print(type(varInt))
print(type(varFloat))
print(type(varString))
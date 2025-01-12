from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,50))


@dataclass()
class Book:
    title : str = "No title"
    author : str = "No Author"
    price : float = field(default_factory=price_func)

    def __post_init__(self):
        self.description = f"{self.title} by {self.author} with price=${self.price}"

@dataclass(frozen=True)
class ImmutableClass:
    value1 : str
    value2 : int = 0

b0 = Book()
b1 = Book("RichDad PoorDad", "Robert", 200.0)
b2 = Book("Atomic Habits", "James", 300.0)

print(b0.description)
print(b1.description)
print(b2.description)

Im = ImmutableClass("val 1", 88.0)
print(Im)
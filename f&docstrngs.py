name="Umme Kulsum"
city="Hyderabad"
print(f"My name is {name} and I am from {city}")


price = 89.0354
print(f"The price of the box is: ${price:.2f}")

name="python" 
print(f"|{name:<10}|")
print(f"|{name:^10}|")
print(f"|{name:>10}|")

#DOC STRINGS
def add(a, b):
    """This function returns the sum of two numbers a and b."""
    return a + b

result = add(5, 3)
print("Sum:", result)
print("Docstring:", add.__doc__)


def even_odd(num):
    """
    Checks whether a number is even or odd."""
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)
print(even_odd.__doc__)

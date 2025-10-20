
def greet():
    print("Hello , hope you're doing well")
greet()

def add(a,b):
    return a+b
result=add(55,99)
print("The result is:",result)

def square(num):
    return num*num
result=square(5)
print("The suqare is:",result)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print("The factorial is:",factorial(7))

#POSITIONAL ARGUEMENTS
def average(a=1,b=5):
    print("The average is:",(a+b)/2)
average(2,5)

def add(a,b):
    print("The sum is:",a+b)
add(9,7)
    
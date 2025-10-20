# '''print the above line
# and dont print the above line
# and also print the line'''
# print("Hello World")
# print("hello",1,2, sep='-',end="202\n")
# print ("AM GOOD")
# #HEY THERE#
# #PYTHON IS BAD
# list={"John",100,1.1,True} 
# print(list) 
# tuple=(True,"Mandroves",1988)
# print(tuple)

# a=1990
# b=2000
# print("The value of",a,"+",b,"is:",a+b)
# print("The value of",a,"-",b,"is:",a-b)
# print("The value of",a,"*",b,"is:",a*b)
# print("The value of",a,"/",b,"is:",a/b)
# print("The value of",a,"//",b,"is:",a//b)
# print("The value of",a,"%",b,"is:",a%b)
# #print("The value of",a,"**",b,"is:",a**b)

# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# print(x+y)

# name="Afifa Princess"
# print(name[:7])
# print(name[::-1])
# print(name[:-3])
# print(len(name))
# print(name[-14:-9])

name="umme kulsum!"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.count("m"))
print(name.find("k"))
print(name.endswith("k"))
print(name.startswith("u"))
print(name.center(60))
print(name.replace("kulsum","siddiqua"))
print(name.rstrip("!"))
print(name.isalpha())
print(name.isalnum())
print(name.swapcase())
print(name.title())
print(name.islower())
print(name.isupper())
print(name.isprintable())
print(name.isspace())
print(name.istitle())

import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
hour=int(time.strftime("%H"))
t=int(input("Enter your time:"))
if hour>=0 and hour<=12:
    print("Good Morning Princess")
elif hour>12 and hour<=17:
    print("Good Afternoon Princess")
if hour>17 and hour<0:
    print("Good Night Princess")




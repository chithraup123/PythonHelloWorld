splitString = "Hello\nworld"
print(splitString)

tabbedString = "1\t2\t3\t4"
print(tabbedString)
splittedString = """This String
has splitted
in several lines"""
print(splittedString)

print("The pycharm is one of the \"IDEs\" for python based prgramming")
print(r'm\npqrs\tuvw')

age = 24
price = 424.50
print(type(tabbedString))
print(type(age))
print(type(price))
# print('The Price is ' + price + 'Rupees') #--->this type of concatenation is not allowed like in C/Java,
# so we can call python as strongly typed language

a = 12
b = 3
print("Arithmetic operations")
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # gets 4.0
print(a // b)  # gets 4 here division operation gives integer value
print(a % b)

# python is strongly typed
print('Python is a Strictly typed language')

# for i in range(1, a/b): # error gets like 'float' object cannot be interpreted as an integer
#     print(i)

for i in range(1, a // b):  # error resolved
    print(i)

print("Hello " * 5)
print("Hello " * (4 + 5))
print("Hello " * 5 + "4")

today = "Friday"
print("day" in today)  # displays true
print("Fri" in today)  # displays true
print("Thur" in today)  # displays false
print("Wed" in "Wednesday")  # displays true

# How to concatenate string and number/float variables
###################################################
age = 24
print("The age of Michael is " + str(age) + " years")
price = 12.52
print("The price is " + str(price))
#  Python 3 provides replacement field with formatting with period for concatenation of string with other type
########################################################
print("The age is {0} years".format(age))
print("There are {0} days in {1}, {2}".format(31, "Jan", "Mar"))
###################################################################
#  Python 3.6 provides an easier way for concatenation than the above one
################################################################
print(f"The age is {age} years")  # using f for formatted string

pi = 22 / 7
print(f"Pi is approximately {pi}")

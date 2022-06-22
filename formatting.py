for i in range(1, 13):
    print("No. {0} squared is {1} cubed is {2}".format(i, i ** 2, i ** 3))

#  Formatting can be done as follows
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} cubed is {2:4}".format(i, i ** 2, i ** 3))
    #  2 spaces, 3 spaces and 4 spaces are getting added here

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} cubed is {2:<4}".format(i, i ** 2, i ** 3))
    # cubed value has been left aligned ny using < symbol
    # can be right aligned using > symbol
    # center alignment can be done with ^ symbol

#  Formatting with decimal values
#####################################
print("Pi is approximately {0:12}".format(22 / 7))
# 12 space width has been given
# and python gives 15 precisions by default


# indexing
#######################################################
parrot = "Norwegian Blue"
# print(parrot[3])
print(parrot[0] + parrot[1] + parrot[2] + parrot[3] + parrot[4] + parrot[5] + parrot[6]
      + parrot[7] + parrot[8] + " " + parrot[10] + parrot[11] + parrot[12] + parrot[13])
print('w\ne\n\nw\ni\nn')
print()

# negative indexing always starts from -1, not from 0 which gives last character from the sequence
print(parrot[-14])  # gives e

# Slicing
#########################################################
print(parrot[0:6])  # prints 0 to up to but not including 6 th char
print(parrot[:6])  # same as above result
print(parrot[0:])  # till the end it will consider
print(parrot[:])  # prints full string

print(parrot[0:6:2])  # prints Nre
# Slicing
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

#  Slicing backwards
####################################################################
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[25:0:-1])  # 25th char to 1st character step by 1 to the backwards direction

#  25th char to starting char step by 1 to the backwards direction
print("Reversed String is " + letters[::-1])
# print(letters[16:13:-1])
# print(letters[4::-1])
# print(letters[25:17:-1])
# or
print(letters[:-9:-1])  # prints last 8 chars in reverse order
print(letters[:5:1])  # prints first 5 chars
print(letters[:4])  # prints first 4 chars
print(letters[-4:])  # prints last 4 chars

chars = ""
print(chars[:1])

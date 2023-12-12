#problem
# You have the price of a product stored as a string, "25.99"
# Convert it to a floating-point number so that you can perform calculations with it.

#problem
# You've collected a user's age as input, which is stored as a string, "28".
# Convert it to an integer so that you can use it for comparison in your program

#datatype
#Integer

variable_int = 125
print(variable_int)
variable_float = 125.25
print(variable_float)

#type()
print(type(variable_float)) # datatype of your variable
#
var_str = 'string datatype'
print(var_str)

var_bool = True
print(var_bool)

#input()
#


var_random = input("Enter a value")
print("The value of my variable is:"+var_random)
print(var_random)

int_var = 5 #integer
float_var = 5.5 #float
print(type(int_var + float_var))

var_str = input("Enter a value")
var_str = int(var_str)
print(var_str)







#Ctrl + /







#Float

#String

#Boolean

# Type conversion
# Implicit type conversion - int -----> float


# intNum = 5 # integer
# floatNum = 5.0#float

ans = intNum + floatNum
print(ans)
print(type(ans))

#Explicit type conversion

num1 = int(input("Enter the value1"))
num2 = float(input("Enter the value2"))

# Explicit type conversion int(), float(), str(), bool()

# str ---> int

print(int(num1) + int(num2))

# 0 ---> False 1 is True

print(bool(" "))
print(bool(263571))
print(bool(''))
print(bool(0))
print(bool(0.0))

# + ---> addition

print(12 % 5)  # returns the remainder value
#
print(189 // 5)  # floor division rounding off
#
print(3 ** 2) # exponentiation operator

#problems
#problems to be solved
#Area of a rectangle #input from te user
#Area of a square
# Area of a circle pi * r*r
#Area of a triangle

#homework problem
#Get the following details of a student 1. Enter the name of the student 2.Enter the year of birth
# 3. Enter the class 4.Enter his place 5.Enter his favourite subject.
# You have to calculate the age of the student and display all his details in the following manner
# The student's name is '_____________.
# He was born in '_____________'
# His age is '______________'
# He lives in '__________' and his favourite subject is '__________'

#problem
# Enter the marks in five subjects from a student
# Add the five subjects and give the total
# Find the average (sum of all subjects / no of subjects) --> using division first then with floor division
# convert the answer to int() and display the output
# The average of all five subjects is '_____________'


# assignment operator

# var = 10 # --- 10
# # print(var)
#
# # var += 3 # var = var + 3
#
# print(var + 3)
#
# var +=3 # added and stored ----> 13
#
# print(var)
#
# var -= 3 # var = var -3 ---> var = 13 -3 = 10
#
# print(var)
#
# var +=4
#
# print(var)
#
# var *= 4 # var = var * 4
#
# print(var)
#
# var /= 3 # var = var / 3
# print(var)
#
# var1 = 3
#
# var1 **= 2 # var = var** 2
# print(var1)
#
# var //= 4
# print(var)
#
# var %= 3
#
# print(var)

# comparison operator

# LHS is compared WITH rhs

# var1 = 10
# var2 = 10
#
# print(var1 == var2) # returns a boolean value --> True or False
# print(var1 != var2)  # Not equals
# print(var1 < var2) # lesser than
# print(var1 > var2) # greater than
# print(var1 <= var2) # lesser than or equal to
# print(var1 >= var2) # greater than or equal to


# var1 = 20
# var2 = 20

# print(var1 == var2  and  var1 <= var2)
# True and True ---> True
# True and False ---> False
# False and False ---? False

# print((var1 == var2 and var1 > var2) or (var1 > var2))
# True or False ---> True
# True or True ---> True
# False or False --> False

# #not
# # False or True ---> True
# print(not(not(var1 == var2) or (var1 == var2)))
#
# dec_num = 100
#
# print(bin(dec_num))

# num1 = 2
# num2 = 6
#
# print(num1 & num2)

# bitwise and &


#bitwise operator

#bitwise operators
# dec_no = 789
# bin_no = bin(dec_no)
# print(bin_no)
# #
# int_num1 = 6
# int_num2 = 3
# print(int_num1 & int_num2)
#
# print(int_num1 | int_num2)

# Quiz Form : https://forms.gle/7nLXQJt9acYQE4cN6



# #Bitwise AND----->  &
#
# """
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
#
# 1 & 0 ---> True & False ----> False ---> 0
# 1 & 1 ---> True & True ---> True ---> 1
# 1 & 0 ----> False ---> 0

# 010 ----> 2^1 ---> 2

# 6 = 110
# 3 = 011
# --------------------
# 2 = 010  --->
# ====================
# """
#
# #Bitwise OR ---> |
#
# """
# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
#
# 0 or 1 ---> False or True ---> True ---> 1
# 1 or 1 ---> True or True ---> True ---> 1
# 1 or 0 ---> True or False ---> True --> 1

# 6 = 110
# 3 = 011
# --------------------
# 7 = 111 ---> 2^0 + 2^1 + 2^2 = 1 + 2 + 4 = 7
# ====================
# """
#
# #Bitwise XOR ----> ^
#
# """
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
#
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 5 = 0000000000000101
# ====================
# """
#
# #Bitwisr NOT ----> ~
#
# """
# The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
#
# Inverted 3 becomes -4:
#  3 = 0000000000000011
# -4 = 1111111111111100
# """
#
# # Bitwise Leftshift ----> <<
# print(500 >> 10)
# print(bin(500))
# print(bin(500 << 10))
# print(bin(2000))
#
# """
# The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
#
# If you push 00 in from the left:
#  3 = 0000000000000011 ---> 000110 ---> 1100
# becomes
# 12 = 0000000000001100
# """
#
# # Bitwise right shift ----> >>
#
# """
# The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
#
# If you move each bit 2 times to the right, 8 becomes 2:
#  8 = 0000000000001000
# becomes
#  2 = 0000000000000010
#  """









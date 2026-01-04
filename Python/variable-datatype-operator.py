
# this is a commented line


a = "hello Bishwa"
print(a)
print(type(a))
print(type(a) == int)
print( isinstance(a, str))

age = float(2)
print(isinstance(age, int))


age2 = int("20")
print(isinstance(age2, int))





# operators 


print("\n### Operators ###")

add = 1 + 1
print(add)

minus = 2 - 1
print(minus)

multiply = 2 * 2
print(multiply)

divide = 4 / 2  # this will return 2.0, so use class constructor -> int(4 / 2) to get int
print(divide)

remainder = 4 % 3
print(remainder)

power = 4 ** 3  # this means 4^3
print(power)

floordivide = 5 // 2    # 5 / 2 = 2.5, so floor = 2
print(floordivide)





# below are assignment and comparision operators

print("\n### assignment and comparision operators ###")


a = 1
b = 2

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)




# boolean operators

print("\n### Boolean Operators ###")

condition1 = True
condition2 = False

print(not condition1)
print(condition1 and condition2)
print(condition1 or condition2)

# Note - or used in an expression returns the value of the first opperand that is not a false value otherwise it returns the last value

print("**Note - or used in an expression returns the value of the first opperand that is not a false value otherwise it returns the last value")


print(1 or 0)
print(False or "hey")
print("hello" or "hi")
print([] or False)
print(False or [])

# Note - and returns 1st value if it is false, if the 1st value is true then it checks 2nd value and returns it

print("**Note - and returns 1st value if it is false, if the 1st value is true then it checks 2nd value and returns it")

print(1 and 0)
print(0 and 1)
print(False and "hey")
print("hey" and False)
print("hi" and "hello")
print([] and False)
print(False and [])





# bitwise operators 

print("\n### Bitwise Operators ###")


# & performs binary AND
# | performs binary OR
# ^ performs binary XOR
# ~ performs binary NOT
# << performs left shift operation
# >> performs Right shift operation





# is & in Operator
print("\n### is & in Operators ###")
# is -> (Identity operator) Its used to comapre two objects and returns true if both are the same object. (more about it on objects section)
# in -> (Membership operator) It is used to tell if a value is contained in a list or another sequence,etc. (more about it on lists)


# Ternary Operator
print("\n### Ternary Operator ###")

def validAge(age):
    return True if age>=18 else False
    
print(validAge(20))
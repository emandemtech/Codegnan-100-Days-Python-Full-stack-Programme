"""num = int(input("enter any number:"))
def check_factor(number):
    if number % 3 ==0 and number %5 ==0:
        return f"{number} is a factor of both 3 and 5"
    elif number % 3 ==0:
        return f"{number} is factor of 3 only"
    elif number % 5 ==0:
        return f"{number} is a factor of 5 only"
    else:
        return f"{number} is neither a factor of 3 and 5"
print(check_factor(num))"""



"""num = (int(input("enter any number:")))
if num % 5 == 0:
       print(f"{num} is a factor of 5")
else:
       print(f"{num} is a factor of 5")
print("end of the loop")"""


"""num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
num3 = int(input("enter number 3:"))
if num1 > num2 and num1 > num3:
           print(f"{num1} is greater than 3")
elif num2 > num1 and num2 > num3:
           print(f"{num2} is greater than the 3")
else:
    print(f"{num3} is greater than the 3")

print("end of the program")"""

"""n = int(input("enter any number:"))
if n == 0:
    print(f"{n} is zero")
elif n < 0:
    print(f"{n} is negative")
elif n > 0:
    print(f"{n} is positive")
else:
    print(f"{n} is not an integer")
print("end of the program")"""

num = int(input("enter a number:"))
if num == 0:
    print("The number is zero (even)")
elif num > 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    else:
        print(f"{num} is positive and odd")
elif num < 0:
    if num % 2 == 0:
        print(f"{num} is negative and even")
    else:
        print(f"{num} is negative and odd")
else:
    print("done")



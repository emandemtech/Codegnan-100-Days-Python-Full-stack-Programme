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


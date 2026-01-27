"""def table_of_three():
    for i in range (1,13):
        print(f"{3*i}" , end = " ")
table_of_three()"""

n = int(input("Enter how many times to print: "))
count = 0
while count < n:
    i = 1
    while i <= 6:
        print(i, end="")
        i += 1
    print()
    count += 1


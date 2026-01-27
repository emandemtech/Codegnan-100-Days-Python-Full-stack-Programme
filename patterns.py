"""n = int(input("enter number of rows:"))
m = int(input("enter number of columns:"))
for rows in range(1 , n+1):
    if rows % 2 == 0:
        print("+ " * m)
    else:
        print("- " * m)"""
        
"""n = int(input("enter number of rows:"))
m = int(input("enter number of columns:"))
for i in range (n):
    for j in range (m):
      if (i+j)% 2 == 0:
          print("0" , end = " ")
      else:
          print("1", end = " ")
    print()"""

"""n = 6
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i == n-1 or j == n-1:
            print("*", end = " ")
        else:
            print("+", end = " ")
    print()"""

n = 6
for i in range(n):
    for j in range(n):
        if i == n-1 or j == 0 or i == j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> rows = int(input("enter number of rows:"))
enter number of rows:4
>>> columns = int(input("enter number of columns:"))
enter number of columns:4
>>> num = 1
>>> for i in range(rows):
...     for j in range(columns):
...         print(num, end = " ")
...         num+=1
...     print()
... 
...     
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 
>>> 

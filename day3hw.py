Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=30
print(a+b)
50
print(a-b)
-10
print(a*b)
600
print(a/b)
0.6666666666666666
print(a//b)
0
print(a%b)
20
print(a^b)
10
print(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
print(a)
20
print(a+=5)
SyntaxError: invalid syntax
print(a += 5)
SyntaxError: invalid syntax
a+=20
print(a)
40
print(a==b)
False
print(a>b and b>a)
False
print(a>b or b>a)
True
>>> print(not(a>b and b<a))
False
>>> print(9 & 10)
8
>>> print(15 | 3)
15
>>> print(2 ~ 5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(~2)
-3
>>> print(6^3)
5
>>> print(3<<2)
12
>>> print(6>>12)
0
>>> c = a
>>> print(c is a)
True
>>> print (c is b)
False
>>> print(c = b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(c = b)
TypeError: print() got an unexpected keyword argument 'c'
>>> print(c == b)
False
>>> print(c is not a)
False
>>> print(20 in a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(20 in a)
TypeError: argument of type 'int' is not a container or iterable
>>> x = ["banana","apple"]
>>> print("banana" in x)
True
>>> print("pineapple" not in x]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> print("pineapple" not in x)
True

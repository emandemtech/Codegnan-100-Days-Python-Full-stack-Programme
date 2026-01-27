"""def mul(a,b,c=0,d=0):
    return a*b*c*d
print(mul(1,2))
print(mul(1,2,3))
print(mul(1,2,3,4))"""

"""lst = [1,2,3]
lst.append(100)
print(lst)"""

"""l1 = []
l2 = list()
print(type(l2))
print(len(l1), len(l2))"""

"""l1 = []   
l2 = []  
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        l1.append(num)
    else:
        l2.append(num)
print("Even list:", l1)
print("Odd list:", l2)"""

passed = []
failed = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 35:
        passed.append((name, marks))
    else:
        failed.append((name, marks))

print("\nStudents who passed:")
for student in passed:
    print(student[0], "-", student[1])

print("\nStudents who failed:")
for student in failed:
    print(student[0], "-", student[1])

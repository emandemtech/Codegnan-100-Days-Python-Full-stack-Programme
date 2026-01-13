n = int(input("enter number of students:"))
present_count = 0
absent_count = 0
rollno = 1
for rollno in range(1,n+1):
    print("enter roll no", rollno," is present or absent and select following option 1 or 2 \n 1. Present \n 2. Absent:")
    status = input()
    if status == '1':
        present_count += 1
    elif status == '2':
        absent_count += 1
    else:
        print("Please select either 1 or 2 options")
print("total stude3nt in the class:",n)
print("number of students present:", present_count)
print("number of students absent:", absent_count)
percentage = (present_count/n * 100)
print(f"attendance report is {percentage} percent")
print("done")

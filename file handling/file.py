#write mode
# f = open('sample.txt','w')
# string = """python programming"""
# f.write(string)
# f.close()
# print("Content added successfully")

#append
# f = open('sample.txt','a')
# string = """java programming"""
# f.write(string)
# f.close()
# print("Content added successfully")

#w+ mode
f = open('sample.txt','w+')
# string = """java programming"""
# f.write(string)
content=f.read()
print(content)
f.close()
print("content added successfully")
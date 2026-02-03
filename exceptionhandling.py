# try:
#     a = [10, 20, 30]
#     c = a[10]
#     print(c)
# except ZeroDivisionError:
#     print("Zero division error it is")
# except TypeError:
#     print("not possible")
# except Exception as e:
#     print(e)
# except:
#     print("denominator cant be zero")
# else:
#     print("valuated")
# finally:
#     print("done")

# a = 10
# print(a[0])

# t = (1,2,3,4)
# t[0] = 100
# print(t)

# if 1 == 1:
# print(1)

# s = "python"
# print(s+1)
try:
    with open('file.txt','r') as f:
        print(f.read())
except Exception as e:
    print(e)
    

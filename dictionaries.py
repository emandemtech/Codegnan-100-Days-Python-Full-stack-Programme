# empty:
"""d1 = {}
d2 = dict()"""
# print:
"""details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON"}
print(type(details))
print(details)
print(details["name"])"""

"""# updating:
details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON"}
details["name"] = "Madhulika"
print(details)"""

# assigning:
'obj_name["item_key"]'

# functions:
"""get(key, def_value)
details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON"}
marks = {"PYTHON": 90 , "SOFTSKILLS": 95, "APTITUDE": 70}"""

#print(details)
"""print(details.get("Percentage"))   # prints none
print(details.get("Percentage", 90))   
details.update(marks)
print(details)
print(marks)
details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON" , "Percentage" : 85 , "Percentage" : 90}
print(details.keys())
print(details.values())
print(details.items())
print(type(details.keys()))
print(type(details.values()))
print(type(details.items()))
print(list(details.keys()))"""

#deleting: pop(key, def_value)
"""details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON" , "Percentage" : 85 , "Percentage" : 90}
popped_value = details["age"]
print(popped_value)
popped_value = details.pop('age')
print(details)"""
# if given item = details.popitem then it will remove the last positioned key value pair

# built in works only for length()returns number of items
"""details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON" , "Percentage" : 85 , "Percentage" : 90}
print(len(details))
for item in details.items(): # for key, value in details.items()
    print(f"{item[0]}:{item[1]}")"""

# membership 
"""details = {"name": "madhu" , "age": 24 , "batch": 47 , "course": "PYTHON" , "Percentage" : 85 , "Percentage" : 90}
if "name" in details:
    print("present")
else:
    print("absent")"""

#contacts:
ph_bk = {}
def add_contact(name:str,number:int):
    if name not in ph_bk:
        ph_bk[name] = number
        print("contact saved")
    else:
        print("contact is exisitng")
def update_number(name:str, number:int):
       if name not in ph_bk:
        ph_bk.update({name:number) #updating number
        print("add contact")
    else:
        print("updated")
def delete_number(name:str):
    if name in ph_bk:
        ph_bk.pop(name)  
        print("contact deleted")
    else:
         print("contact not found")
def get_number(name:str):
    if name in ph_bk:
        number = ph_bk.get(name, 'Name Not Found')
def all_contacts():
    for name,number in ph_bk.items():
        print(f"{name}:{number}")
        if not ph_bk:
            print("no contact found")
        return

#main
    if_name_ == '__main__':
        print("welcome to the contact book")





























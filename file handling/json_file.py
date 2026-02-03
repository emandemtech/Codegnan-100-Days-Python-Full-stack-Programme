import json
try:
    with open('contact.josn', 'r')as file:
        data = json.load(file)
        print(data)
except Exception as e:
    print(e)
import csv


try: 
    with open('contacts.csv', 'r') as f:
        data = csv.reader(f)
        print(list(data))
except Exception as e:
    print(e)
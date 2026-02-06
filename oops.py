class User:
    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password
    def details(self):
        return " name is, {}  mail is, {} password is, {}".format(self.name, self.mail, self.password)
    
class Admin:
    def __init__(self, name, mail, password, total_income, total_user_count):
        self.name = name
        self.mail = mail
        self.password = password
        self.total_income = total_income
        self.total_users = total_user_count
    def details(self):
        return " name is, {} mail is, {} password is, {} total_income is {}, total_users{}".format(self.name, self.mail, self.password, self.total_income, self.total_users)
    
u = User("Ravi", "ravi@gmail.com", "1234")
a = Admin("Admin1", "admin@gmail.com", "admin123", 50000, 120)

print(u.details())
print(a.details())

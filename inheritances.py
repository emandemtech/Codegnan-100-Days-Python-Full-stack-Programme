# Base class (used everywhere)
class Person:
    def show_person(self):
        print("I am a person")


# ---------- 1. SINGLE INHERITANCE ----------
class Student(Person):
    def show_student(self):
        print("I am a student")


# ---------- 2. MULTI-LEVEL INHERITANCE ----------
class CollegeStudent(Student):
    def show_college_student(self):
        print("I am a college student")


# ---------- 3. HIERARCHICAL INHERITANCE ----------
class Teacher(Person):
    def show_teacher(self):
        print("I am a teacher")


# ---------- 4. MULTIPLE INHERITANCE ----------
class Sports:
    def show_sports(self):
        print("I play sports")


class Athlete(Student, Sports):
    def show_athlete(self):
        print("I am an athlete")


# ---------- 5. HYBRID INHERITANCE ----------
class ResearchScholar(CollegeStudent, Teacher):
    def show_research_scholar(self):
        print("I am a research scholar")


# ---------- Object Creation ----------
print("---- Single Inheritance ----")
s = Student()
s.show_person()
s.show_student()

print("\n---- Multi-level Inheritance ----")
cs = CollegeStudent()
cs.show_person()
cs.show_student()
cs.show_college_student()

print("\n---- Hierarchical Inheritance ----")
t = Teacher()
t.show_person()
t.show_teacher()

print("\n---- Multiple Inheritance ----")
a = Athlete()
a.show_person()
a.show_student()
a.show_sports()
a.show_athlete()

print("\n---- Hybrid Inheritance ----")
r = ResearchScholar()
r.show_person()
r.show_student()
r.show_college_student()
r.show_teacher()
r.show_research_scholar()

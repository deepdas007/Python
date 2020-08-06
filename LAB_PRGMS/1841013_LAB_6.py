import calendar
import datetime

BCA_code = 40300
all_sub = ["Python", "Computer Networks", "Mobile Applications",
           "Graphic Designing", "Cyber Security", "Multimedia"]
core_subject_list = ["Python", "Computer Networks"]
op1_subject = ["Mobile Applications", "Graphic Designing"]
op2_subject = ["Cyber Security", "Multimedia"]


class Student:
    Name = ""
    Reg_no = ""
    Subject = dict()
    stud_sub = []

    def __init__(self, name):
        self.Name = name

    def reg_no(self, reg):
        self.Reg_no = reg

    def __str__(self):
        return "{} {} ".format(self.Reg_no, self.Name)

    def sub_value(self):
        return self.stud_sub

    def sub(self, subjects):
        self.stud_sub.append(subjects)
        self.Subject[subjects] = {}
        self.Subject[subjects]['Date'] = []
        self.Subject[subjects]['Attendence'] = []

    def attendence(self, sub, date, mark):
        self.Subject[sub]['Date'].append(date)
        self.Subject[sub]['Attendence'].append(mark)

    def result_attendence(self, subject):
        print("{} Attendence".format(subject))
        print("Date\tPresent/Absent")
        for j in range(len(self.Subject[subject]['Date'])):
            for i in self.Subject[subject].values():
                print(i[j], end="\t")
            print(end="\n")

# Form The Student list


Student_list = []
name = ''
reg = 1

while True:
    try:
        Number_of_students = int(input("Enter No. of Students: "))
        if(Number_of_students > 0):
            break
        else:
            print("Value must be grater than 0")

    except Exception:
        print("Enter only integer value ")


for i in range(Number_of_students):
    # Taking Student Name
    while True:
        try:
            name = input("Enter Student {} Name: ".format(i+1))
            name = name.upper()
            if name.isalpha():
                break
            else:
                print("Student Name must contain only alphabets...")
                print("Enter name again.....\n")
        except Exception:
            print("Error Occured")

    # Creating Student Object
    Student_list.append(Student(name))

# Sorting the Students with respect to their Names
Student_list.sort(key=lambda x: x.Name)

# Assigning Register No. to Students
for i in Student_list:
    i.reg_no(BCA_code + reg)
    reg = reg + 1

# Assign Optional subjects to Students
op1 = 0
op2 = 0
print("Choose optional Subject for Students.(Enter 1/2 only)\n")
for i in Student_list:
    print("---------------------")
    print(i)
    print("---------------------")
    i.stud_sub = []
    while True:
        try:
            op1 = int(
                input("Subject 1:\n\t1) Mobile Applications\n\t2) Graphic Designing\nEnter: "))
            if(op1 == 1 or op1 == 2):
                break
            else:
                print("Wrong Input...enter agin")
        except Exception:
            print("Error Occured...enter again")
    while True:
        try:
            op2 = int(
                input("Subject 2:\n\t1) Cyber Security\n\t2) Multimedia\nEnter: "))
            if(op2 == 1 or op2 == 2):
                break
            else:
                print("Wrong Input...enter agin")
        except Exception:
            print("Error Occured...enter again")
    for j in core_subject_list:
        i.sub(j)

    i.sub(op1_subject[op1-1])
    i.sub(op2_subject[op2-1])

# Recording Attendence
temp = 1
print("----------------------------")
print("    Student Attendence ")
print("----------------------------")

while True:
    print("Choose Subject :")
    for i in all_sub:
        print("{}) {}".format(temp, i))
        temp = temp + 1
    try:
        sub_attend = int(input("Enter :"))
        if sub_attend > 0 and sub_attend <= 7:
            break
        else:
            print("wrong input")
    except Exception:
        print("Error Input")

while True:
    print("\nEnter Date:")
    try:
        date = int(input("DD: "))
        month = int(input("MM: "))
        year = int(input("YY: "))
        sub_date = datetime.date(year, month, date)
        break
    except Exception as e:
        print(e)

print("Enter Attendence (Input only: 0=Absent or 1=Present): ")

for i in Student_list:
    if all_sub[sub_attend-1] in i.stud_sub:
        while True:
            try:
                mark = int(input("{} : ".format(i)))
                if mark == 0 or mark == 1:
                    break
            except Exception:
                print("Wrong Input")

        i.attendence(all_sub[sub_attend-1], sub_date, mark)

a = datetime.date(2012, 2, 29)
print(a)
for i in Student_list[0].Subject['Python'].values():
    print(i, i[0])

for i in Student_list:
    i.result_attendence(all_sub[sub_attend-1])

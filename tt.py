from area import Student

students = []

def CreatNewStudent():
    # name=input("Enter your name: ")
    # roll=int(input("Enter your roll: "))
    # gender=input("Enter your gender: ")
    # marks=int(input("Enter your marks: "))
    name= ("alon ")
    roll=int("2")
    gender=("M")
    marks=int(("100"))

    s = Student(name,gender,roll,marks)
    fuckkkkkk =s.Display()
    students.append(fuckkkkkk)
    print(fuckkkkkk)

def totalStudents():
    for student in students:
        print(student.name,student.gender,student.roll,student.marks)
    return(len(students))
    


def males():
    for s in students:
        if s.gender == "M" :
            s.Display()

def female():
    for s in students:
        if s.gender == "F" :
            s.Display()

while True:
    print(
            """
            #1. Enter student\n
            #2. Total Students\n
            #3. Male\n
            #4. Female\n
            #5. Exit\n
            """
        )
    c = int(input("Enter your choose: "))
    if c == 1:
        CreatNewStudent()
    elif c== 2:
        print(totalStudents())
    elif c== 3:
        print(males())

    elif c== 4:
        print(female())
    else:
        print("Exit")

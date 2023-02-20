student_info = {}
course_info = {}
mark_info = {}

def get_student():
    number_student = int(input("Enter the number of students in the class: "))
    while number_student <= 0:
        number_student = int(input("Please enter a number bigger than 0: "))
    print("There are " + str(number_student) + " students in the class \n" )
    for i in range(1, number_student + 1):
        student_name = input("Enter student " + str(i) + "'s name: ")
        student_id = input("Enter student " + str(i) + "'s ID: ")
        student_DoB = input("Enter student " + str(i) + "'s DoB: ")
        print("\n")
        student = i
        student_info[student] = {"name": student_name, "ID": student_id, "DoB": student_DoB}

def list_student():
    for i in student_info:
        print("Student " + str(i) + "'s information: ")
        print(f" Name: {student_info[i]['name']} \n ID: {student_info[i]['ID']} \n DoB: {student_info[i]['DoB']} \n")

def get_course():
    number_course = int(input("Enter the number of courses: "))
    while number_course <= 0:
        number_course = int(input("Please enter a number bigger than 0: "))
    print("There are " + str(number_course) + " courses that students attend \n")
    for i in range(1, number_course + 1):
        course_name = input("Enter course " + str(i) + "'s name: ")
        course_id = input("Enter course " + str(i) + "'s ID: ")
        print("\n")
        course = i
        course_info[course] = {"name": course_name, "ID": course_id}

def list_course():
    for i in course_info:
        print("Course " + str(i) + "'s information: ")
        print(f" Name: {course_info[i]['name']} \n ID: {course_info[i]['ID']} \n")

def course_number():
    for i in course_info:
        print("Course number " + str(i) + ": " f"{course_info[i]['name']}")

def get_mark():
    course = int(input("Enter the course's number to choose: "))
    if course not in course_info:
        print("Please enter the right course number.")
        return
    for student in student_info:
            mark_student = float(input(f"Enter the mark for {student_info[student]['name']} ({student_info[student]['ID']}): "))
            if student not in mark_info:
                mark_info[student] = {}
            mark_info[student][course] = mark_student
    print("\n")

def display_mark():
    course = int(input("Enter the course's number to choose: "))
    if course not in course_info:
        print("Please enter the right course number.")
        return
    for student in student_info:
        if student in mark_info and course in mark_info[student]:
            print(f"{student_info[student]['name']}'s mark in the course {course_info[course]['name']} is: {mark_info[student][course]}")
        else:
            print(f"Students in {course_info[course]['name']} course haven't been graded.")
            break
    print("\n")    

get_student()
get_course()

while True:
    print("********************************************")
    print("Select an option: ")
    print("1/ List all students and their information.")
    print("2/ List all courses and their information.")
    print("3/ Input marks for a course")
    print("4/ Display student marks for a given course")
    print("5/ End task")
    print("********************************************\n") 
    option = input("Enter your choice: ")
    if option == "1":
        list_student()
    elif option == "2":
        list_course()
    elif option == "3":
        print("Choose one of the following courses to input marks: ")
        course_number()
        print("\n")
        get_mark()
    elif option == "4":
        print("Choose one of the following courses to view the marks: ")
        course_number()
        print("\n")
        display_mark()
    elif option == "5":
        break
    else:
        print("Choose only from option 1 to option 5. Please try again!")
        print("\n")
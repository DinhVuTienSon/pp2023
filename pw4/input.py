from domains.Uni import Students
from domains.Uni import Courses
from domains.Marks import Marks
import math

student_info = {}
course_info = {}
mark_info = {}
gpa_info = {}

def input_student():
    while True:
        try:
            number_student = int(input("Enter the number of students in the class: "))
            if number_student <= 0:
                print("Please enter a number bigger than 0.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")
    print("There are " + str(number_student) + " students in the class \n" )
    for i in range(1, number_student + 1):
        student_name = str(input("Enter student " + str(i) + "'s name: "))
        while student_name == "":
            student_name = str(input("Please enter student " + str(i) + "'s name: "))
        student_id = str(input("Enter student " + str(i) + "'s ID: "))
        while student_id == "":
            student_id = str(input("Please enter student " + str(i) + "'s ID: "))
        student_DoB = str(input("Enter student " + str(i) + "'s DoB: "))
        while student_DoB == "":
            student_DoB = str(input("Please enter student " + str(i) + "'s DoB: "))
        print("\n")          
        student = i
        student_info[student] = {"name": student_name, "ID": student_id, "DoB": student_DoB}

def input_course():
    while True:
        try:
            number_course = int(input("Enter the number of courses: "))
            if number_course <= 0:
                print("Please enter a number bigger than 0.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")
    print("There are " + str(number_course) + " courses that students attend \n")
    for i in range(1, number_course + 1):
        course_name = str(input("Enter course " + str(i) + "'s name: "))
        while course_name == "":
            course_name = str(input("Please enter course " + str(i) + "'s name: "))
        course_id = str(input("Enter course " + str(i) + "'s ID: "))
        while course_id == "":
            course_id = str(input("Please enter course " + str(i) + "'s ID: "))
        while True:
            try:
                course_credit = int(input("Enter course " + str(i) + "'s credit: "))
                if course_credit <= 0:
                    print("Please enter a number bigger than 0.")
                else:
                    break
            except ValueError:
                print("Please enter an integer.")
        print("\n")
        course = i
        course_info[course] = {"name": course_name, "ID": course_id, "credit": course_credit}
        
def input_mark():
    while True:
        try:
            course = int(input("Enter the course's number to choose: "))
            if course <= 0:
                print("Please enter a number bigger than 0.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")
    if course not in course_info:
        print("Please enter the right course number.")
        return
    for student in student_info:
            mark_student = math.floor(float(input(f"Enter the mark for {student_info[student]['name']} (id: {student_info[student]['ID']}): ")) * 10) / 10
            if student not in mark_info:
                mark_info[student] = {}
            mark_info[student][course] = {"mark": mark_student}
    print("\n")
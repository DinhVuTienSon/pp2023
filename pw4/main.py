import input as inp
import output as out

def course_number():
    for i in inp.course_info:
        print("Course number " + str(i) + ": " f"{inp.course_info[i]['name']}")

inp.input_student()
inp.input_course()

while True:
    print("********************************************")
    print("Select an option: ")
    print("1/ List all students and their information.")
    print("2/ List all courses and their information.")
    print("3/ Input marks for a course")
    print("4/ Display student marks for a given course")
    print("5/ Display student gpa")
    print("6/ Sort student list by GPA descending")
    print("7/ End task")
    print("********************************************\n") 
    option = input("Enter your choice: ")
    if option == "1":
        out.list_student()
    elif option == "2":
        out.list_course()
    elif option == "3":
        print("Choose one of the following courses to input marks: ")
        course_number()
        print("\n")
        inp.input_mark()
    elif option == "4":
        print("Choose one of the following courses to view the marks: ")
        course_number()
        print("\n")
        out.display_mark()
    elif option == "5":
        out.display_gpa()
        print("\n")
    elif option == "6":
        out.sort_gpa_descend()
    elif option == "7":
        break
    else:
        print("Choose only from option 1 to option 7. Please try again!")
        print("\n") 

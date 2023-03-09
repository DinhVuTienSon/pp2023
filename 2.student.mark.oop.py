# parent class Uni contain variables and functions 
class Uni:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__student_info = {}
        self.__course_info = {}
        self.__mark_info = {}

    def get_mark_info(self):
        return self.__mark_info

    def get_courses(self):
        return self.__course_info

    def get_students(self):
        return self.__student_info

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def input_student(self):
        number_student = int(input("Enter the number of students in the class: "))
        while number_student <= 0:
            number_student = int(input("Please enter a number bigger than 0: "))
        print("There are " + str(number_student) + " students in the class \n" )
        for i in range(1, number_student + 1):
            student_name = input("Enter student " + str(i) + "'u name: ")
            student_id = input("Enter student " + str(i) + "'u ID: ")
            student_DoB = input("Enter student " + str(i) + "'u DoB: ")
            print("\n")          
            student = i
            self.__student_info[student] = {"name": student_name, "ID": student_id, "DoB": student_DoB}

    def list_student(self):
        for i in self.__student_info:
            print("Student " + str(i) + "'u information: ")
            print(f" Name: {self.__student_info[i]['name']} \n ID: {self.__student_info[i]['ID']} \n DoB: {self.__student_info[i]['DoB']} \n")

    def input_course(self):
        number_course = int(input("Enter the number of courses: "))
        while number_course <= 0:
            number_course = int(input("Please enter a number bigger than 0: "))
        print("There are " + str(number_course) + " courses that students attend \n")
        for i in range(1, number_course + 1):
            course_name = input("Enter course " + str(i) + "'u name: ")
            course_id = input("Enter course " + str(i) + "'u ID: ")
            print("\n")
            course = i
            self.__course_info[course] = {"name": course_name, "ID": course_id}

    def list_course(self):
        for i in self.__course_info:
            print("Course " + str(i) + "'u information: ")
            print(f" Name: {self.__course_info[i]['name']} \n ID: {self.__course_info[i]['ID']} \n")

    # function display courses with their corresponding number 
    def course_number(self):
        for i in self.__course_info:
            print("Course number " + str(i) + ": " f"{self.__course_info[i]['name']}")

    def input_mark(self):
        course = int(input("Enter the course'u number to choose: "))
        if course not in self.__course_info:
            print("Please enter the right course number.")
            return
        for student in self.__student_info:
                mark_student = float(input(f"Enter the mark for {self.__student_info[student]['name']} ({self.__student_info[student]['ID']}): "))
                if student not in self.__mark_info:
                    self.__mark_info[student] = {}
                self.__mark_info[student][course] = mark_student
        print("\n")

    def display_mark(self):
        course = int(input("Enter the course'u number to choose: "))
        if course not in self.__course_info:
            print("Please enter the right course number.")
            return
        for student in self.__student_info:
            if student in self.__mark_info and course in self.__mark_info[student]:
                print(f"{self.__student_info[student]['name']}'u mark in the course {self.__course_info[course]['name']} is: {self.__mark_info[student][course]}")
            else:
                print(f"Students in {self.__course_info[course]['name']} course haven't been graded.")
                break
        print("\n")

# child class Students
class Students(Uni):
    def __init__(self, name, id, DoB):
        super().__init__(name, id)
        self.__DoB = DoB
        
    def get_DoB(self):
        return self.__DoB
    
# child class Courses    
class Courses(Uni):
    def __init__(self, name, id):
        super().__init__(name, id)

# class Marks        
class Marks():
    def __init__(self, marks):
        self.__marks = marks

    def get_mark(self):
        return self.__marks

# create a variable and some random parameters to call Uni class
u = Uni("name", "id")
u.input_student()
u.input_course()

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
        u.list_student()
    elif option == "2":
        u.list_course()
    elif option == "3":
        print("Choose one of the following courses to input marks: ")
        u.course_number()
        print("\n")
        u.input_mark()
    elif option == "4":
        print("Choose one of the following courses to view the marks: ")
        u.course_number()
        print("\n")
        u.display_mark()
    elif option == "5":
        break
    else:
        print("Choose only from option 1 to option 5. Please try again!")
        print("\n") 
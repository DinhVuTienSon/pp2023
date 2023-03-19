import curses
import math
import numpy as np

# parent class Uni contain variables and functions 
class Uni:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__student_info = {}
        self.__course_info = {}
        self.__mark_info = {}
        self.__gpa_info = {}

    def get_gpa_info(self):
        return self.__gpa_info

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
            self.__student_info[student] = {"name": student_name, "ID": student_id, "DoB": student_DoB}

    def list_student(self):
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)        
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)       
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        green = curses.color_pair(1)
        cyan = curses.color_pair(3)
        red = curses.color_pair(5)
        stdscr.clear()
        stdscr.addstr(2, 45, "[ List of students ]", curses.A_BOLD | green)
        line = 3
        for i in self.__student_info:
            stdscr.addstr(line + 1, 3, "--> Student " + str(i) + "'s information: ", cyan)
            stdscr.addstr(line + 2, 7, f"+) Name: {self.__student_info[i]['name']}")
            stdscr.addstr(line + 3, 7, f"+) ID: {self.__student_info[i]['ID']}")
            stdscr.addstr(line + 4, 7, f"+) DoB: {self.__student_info[i]['DoB']}")
            line = line + 5
        stdscr.refresh()
        stdscr.addstr(line + 1, 42, "Press any key to continue!", curses.A_BOLD | red)
        stdscr.getch()
        curses.endwin()

    def input_course(self):
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
            self.__course_info[course] = {"name": course_name, "ID": course_id, "credit": course_credit}

    def list_course(self):
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        green = curses.color_pair(1)
        cyan = curses.color_pair(3)
        red = curses.color_pair(5)
        stdscr.clear()
        stdscr.addstr(2, 45, "[ List of courses ]", curses.A_BOLD | green)
        line = 3
        for i in self.__course_info:
            stdscr.addstr(line + 1, 3, "--> Course " + str(i) + "'s information: ", cyan)
            stdscr.addstr(line + 2, 7, f"+) Name: {self.__course_info[i]['name']}")
            stdscr.addstr(line + 3, 7, f"+) ID: {self.__course_info[i]['ID']}")
            stdscr.addstr(line + 4, 7, f"+) Credit: {self.__course_info[i]['credit']}")
            line = line + 5
        stdscr.refresh()
        stdscr.addstr(line + 1, 42, "Press any key to continue!", curses.A_BOLD | red)
        stdscr.getch()
        curses.endwin()
        
    # function display courses with their corresponding number 
    def course_number(self):
        for i in self.__course_info:
            print("Course number " + str(i) + ": " f"{self.__course_info[i]['name']}")

    def input_mark(self):
        while True:
            try:
                course = int(input("Enter the course's number to choose: "))
                if course <= 0:
                    print("Please enter a number bigger than 0.")
                else:
                    break
            except ValueError:
                print("Please enter an integer.")
        if course not in self.__course_info:
            print("Please enter the right course number.")
            return
        for student in self.__student_info:
                mark_student = math.floor(float(input(f"Enter the mark for {self.__student_info[student]['name']} (id: {self.__student_info[student]['ID']}): ")) * 10) / 10
                if student not in self.__mark_info:
                    self.__mark_info[student] = {}
                self.__mark_info[student][course] = {"mark": mark_student}
        print("\n")

    def display_mark(self):
        while True:
            try:
                course = int(input("Enter the course's number to choose: "))
                if course <= 0:
                    print("Please enter a number bigger than 0.")
                else:
                    break
            except ValueError:
                print("Please enter an integer.")
        if course not in self.__course_info:
            print("Please enter the right course number.")
            return
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        green = curses.color_pair(1)
        red = curses.color_pair(5)
        stdscr.clear()
        stdscr.addstr(2, 45, "[ List of student's marks ]", curses.A_BOLD | green)
        line = 3
        for student in self.__student_info:
            if student in self.__mark_info and course in self.__mark_info[student]:
                stdscr.addstr(line + 1, 3, f"--> {self.__student_info[student]['name']}'s mark in the course {self.__course_info[course]['name']} is: {self.__mark_info[student][course]['mark']}")
                line = line + 2
            else:
                stdscr.addstr(line + 1, 3, f"Students in {self.__course_info[course]['name']} course haven't been graded.")
                line = line + 2
                break
        stdscr.refresh()
        stdscr.addstr(line + 1, 45, "Press any key to continue!", curses.A_BOLD | red)
        stdscr.getch()
        curses.endwin()

    def display_gpa(self):
        total_credit = 0
        total_quality_point = 0

        for student in self.__student_info:
            for course in self.__course_info:
                total_credit += self.__course_info[course]['credit']
            break
        
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        green = curses.color_pair(1)
        yellow = curses.color_pair(4)
        red = curses.color_pair(5)
        stdscr.clear()
        stdscr.addstr(2, 45, "[ List of student's GPA ]", curses.A_BOLD | green)
        line = 3

        for student in self.__student_info:
            for course in self.__course_info:
                while True:
                    i = 0   
                    try:
                        total_quality_point += self.__mark_info[student][course]['mark'] * self.__course_info[course]['credit']
                        i = 1
                    except:
                        stdscr.addstr(line + 1, 3, "Some courses may not have been graded yet.")
                        stdscr.addstr(line + 2, 3, "Please choose option 3 to grade all the courses and then try again.")
                        line = line + 3
                    break
            if i == 1:
                stdscr.addstr(line + 1, 3, "+)", yellow)
                stdscr.addstr(line + 2, 7, f"Total credit of the courses that {self.__student_info[student]['name']} attended: {total_credit} credits")
                stdscr.addstr(line + 3, 7,f"{self.__student_info[student]['name']}'s total quality points: {math.floor(total_quality_point * 10) / 10}")
                stdscr.addstr(line + 4, 7,f"{self.__student_info[student]['name']}'s gpa is: {math.floor(float(total_quality_point / total_credit) * 10) / 10}\n")
                self.__gpa_info[self.__student_info[student]['name']] = {'GPA': math.floor(float(total_quality_point / total_credit) * 10) / 10}
                total_quality_point = 0
                line = line + 5
            else:
                break
        stdscr.refresh()
        stdscr.addstr(line + 1, 45, "Press any key to continue!", curses.A_BOLD | red)
        stdscr.getch()
        curses.endwin() 
        
    def sort_gpa_descend(self):
        sort_gpa = sorted(self.__gpa_info.items(), key=lambda v:v[1]['GPA'], reverse= True)
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        green = curses.color_pair(1)
        red = curses.color_pair(5)
        stdscr.clear()
        stdscr.addstr(2, 45, "[ Student list sorted by GPA descending ]", curses.A_BOLD | green)
        line = 3
        for sort in sort_gpa:
            string = '\n'.join([str(value) for value in sort_gpa])
            stdscr.addstr(line + 1, 0, f"{string}")
        stdscr.refresh()
        stdscr.addstr(line + len(sort_gpa) + 2, 53, "Press any key to continue!", curses.A_BOLD | red)
        stdscr.getch()
        curses.endwin() 

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
    print("5/ Display student gpa")
    print("6/ Sort student list by GPA descending")
    print("7/ End task")
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
        u.display_gpa()
        print("\n")
    elif option == "6":
        u.sort_gpa_descend()
    elif option == "7":
        break
    else:
        print("Choose only from option 1 to option 7. Please try again!")
        print("\n") 


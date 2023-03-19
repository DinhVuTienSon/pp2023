import domains
import input as inp
import curses

def list_student():
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
    for i in inp.student_info:
        stdscr.addstr(line + 1, 3, "--> Student " + str(i) + "'s information: ", cyan)
        stdscr.addstr(line + 2, 7, f"+) Name: {inp.student_info[i]['name']}")
        stdscr.addstr(line + 3, 7, f"+) ID: {inp.student_info[i]['ID']}")
        stdscr.addstr(line + 4, 7, f"+) DoB: {inp.student_info[i]['DoB']}")
        line = line + 5
    stdscr.refresh()
    stdscr.addstr(line + 1, 42, "Press any key to continue!", curses.A_BOLD | red)
    stdscr.getch()
    curses.endwin()

def list_course():
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
    for i in inp.course_info:
        stdscr.addstr(line + 1, 3, "--> Course " + str(i) + "'s information: ", cyan)
        stdscr.addstr(line + 2, 7, f"+) Name: {inp.course_info[i]['name']}")
        stdscr.addstr(line + 3, 7, f"+) ID: {inp.course_info[i]['ID']}")
        stdscr.addstr(line + 4, 7, f"+) Credit: {inp.course_info[i]['credit']}")
        line = line + 5
    stdscr.refresh()
    stdscr.addstr(line + 1, 42, "Press any key to continue!", curses.A_BOLD | red)
    stdscr.getch()
    curses.endwin()

def display_mark():
    while True:
        try:
            course = int(input("Enter the course's number to choose: "))
            if course <= 0:
                print("Please enter a number bigger than 0.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")
    if course not in inp.course_info:
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
    for student in inp.student_info:
        if student in inp.mark_info and course in inp.mark_info[student]:
            stdscr.addstr(line + 1, 3, f"--> {inp.student_info[student]['name']}'s mark in the course {inp.course_info[course]['name']} is: {inp.mark_info[student][course]['mark']}")
            line = line + 2
        else:
            stdscr.addstr(line + 1, 3, f"Students in {inp.course_info[course]['name']} course haven't been graded.")
            line = line + 2
            break
    stdscr.refresh()
    stdscr.addstr(line + 1, 45, "Press any key to continue!", curses.A_BOLD | red)
    stdscr.getch()
    curses.endwin()

def display_gpa():
    total_credit = 0
    total_quality_point = 0

    for student in inp.student_info:
        for course in inp.course_info:
            total_credit += inp.course_info[course]['credit']
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

    for student in inp.student_info:
        for course in inp.course_info:
            while True:
                i = 0   
                try:
                    total_quality_point += inp.mark_info[student][course]['mark'] * inp.course_info[course]['credit']
                    i = 1
                except:
                    stdscr.addstr(line + 1, 3, "Some courses may not have been graded yet.")
                    stdscr.addstr(line + 2, 3, "Please choose option 3 to grade all the courses and then try again.")
                    line = line + 3
                break
        if i == 1:
            stdscr.addstr(line + 1, 3, "+)", yellow)
            stdscr.addstr(line + 2, 7, f"Total credit of the courses that {inp.student_info[student]['name']} attended: {total_credit} credits")
            stdscr.addstr(line + 3, 7,f"{inp.student_info[student]['name']}'s total quality points: {inp.math.floor(total_quality_point * 10) / 10}")
            stdscr.addstr(line + 4, 7,f"{inp.student_info[student]['name']}'s gpa is: {inp.math.floor(float(total_quality_point / total_credit) * 10) / 10}\n")
            inp.gpa_info[inp.student_info[student]['name']] = {'GPA': inp.math.floor(float(total_quality_point / total_credit) * 10) / 10}
            total_quality_point = 0
            line = line + 5
        else:
            break
    stdscr.refresh()
    stdscr.addstr(line + 1, 45, "Press any key to continue!", curses.A_BOLD | red)
    stdscr.getch()
    curses.endwin()

def sort_gpa_descend():
    sort_gpa = sorted(inp.gpa_info.items(), key=lambda v:v[1]['GPA'], reverse= True)
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
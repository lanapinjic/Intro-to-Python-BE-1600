def main_function():
    rooms = {'CS101' : 3004, 'CS102': 4501, 'CS103': 6755, 'NT110':1244, 'CM241': 1411}
    instruc = {'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich', 'NT110' : 'Burke', 'CM241' :'Lee'}
    time = {'CS101' : '8:00 a.m.', 'CS102' : '9:00 a.m.', 'CS103' : '10:00 a.m.', 'NT110' : '11:00 a.m.', 'CM241' :'1:00 p.m.'}
    course_num = input("Enter a course number: ")
    if course_num not in rooms:
        print(course_num, "is an invalid course nuber")
    else:
        print("The details for course", course_num, "are: ")
        print("Room: ", rooms[course_num])
        print("Instructor: ", instruc[course_num])
        print("Time: ", time[course_num])
main_function()


print()
print('Welcome to Course information system.')
print()
course_list =['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']

room_dict = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755', 'NET110': '1244', 'COM241': '1411'}
instructor_dict = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}
time_dict = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

course = ''

while course != 'q':

    course = input('Please enter your course # or \'q\' to quit: ')

    output = f'{course_list[course_list.index(course)]}: Room# {room_dict[course]}, Prof. {instructor_dict[course]}, @ {time_dict[course]}'

    print()
    print(output)
    print()

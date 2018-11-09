import student

studentName = raw_input('Enter your student name : ').strip()
student_id = raw_input('Enter your student ID : ')

testing = student.Student(studentName, student_id)
print testing.get_name_capitalize()
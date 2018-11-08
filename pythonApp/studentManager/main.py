import student
"""
An app that will collect : 
-> student basic information,
-> easy to expand,
-> from console to Web App. 
""" 

# the function that capatalise each of the student
def get_students_titlecase():
    student_titlecase = []
    for eachStudent in student.students:
        student_titlecase.append(eachStudent['name'].title())    #.title capitalises each word in a sentence. 
    return student_titlecase


# function prints the capitalised names 
def print_student_titleCase():
    student_titlecase = get_students_titlecase()
    print student_titlecase
    

# functions saved student names. 
def saveStudentName(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print error
        print ' File could not be saved.'


# functions read student files
def read_file():
    try:
        f = open('students.txt', 'r')
        for s in f.readlines():
            student.Student(s)
        f.close()
    except Exception as error:
        print error
        print 'Could not read the file. \n'


read_file()
print_student_titleCase()     

studentName = raw_input('Enter your student name : ').strip()
student_id = raw_input('Enter your student ID : ')

student.Student(studentName, student_id)
saveStudentName(studentName)







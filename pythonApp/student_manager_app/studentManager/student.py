# lists of student.
students = []

# class contains student name,id, and we can add more. 
class Student:

    school_name = 'Bhetey University'

    def __init__(self, name, last_name, student_ids=322):
        self.name = name
        self.last_name = last_name
        self.student_ids = student_ids
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name
    
    def get_name_capitalize(self):
        """Capitalise the first character of the string"""
        return self.name.capitalize()

    def get_school_name(self):
        """returns the school name"""
        return self.school_name 


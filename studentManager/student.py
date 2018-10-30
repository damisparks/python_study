# class contains student name,id, and we can add more. 
class AddStudent:
    def __init__(self, name, studentID=322):
        self.name = name
        self.studentID = studentID
        students.append(self)

class Student:
    """ 
    The class takes 
    ->  name of the student 
    -> studentID 
    -> append the variables to students list
    """
    def __init__(self, name, student_ids=322):
        self.name = name
        self.ids = student_ids
        students.append(self)

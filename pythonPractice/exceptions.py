student = {
    'name_of_student' : 'Damilola',
    'student_ID' : 48549,
    'feedback' : None
}
student['lastName'] = 'Omifare'

try:
    lastName = student['lastName']
    numbered_last_name = 3 + lastName
    #catches any KeyError
except KeyError:
    print 'Error find lastName'
    # catch the TypeError 
    ## as error is to get the actually error message 
except TypeError as error:
    print 'I can not add the two together.!!!'
    print(error)

print 'Code executed successfully!!!'

"""
- Problem 
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer  followed by the names and marks for students. 
You are required to save the record in a dictionary data type. 
The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

- Input Format
The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

- Constraints
_to be added._
- Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

"""
# Here is the started code. 

n = int(input('Input a number ? '))
student_marks = {}
for _ in range(n):
    name, *line = input('Write a name').split()
    scores = list(map(float, line))
    print (line)
    print (name)
    #average = scores / len(scores)
    print(len(scores))
    student_marks[name] = scores
    print (student_marks[name])
    print ('This is your score', scores)
    print (student_marks)
query_name = input('What name do you want to query ?: ')
if query_name in student_marks:
    print (sum(student_marks[query_name])/len(student_marks[query_name]))


#--To be continued later today.--#

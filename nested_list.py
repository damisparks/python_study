print " PROBLEM : \n \
Given the names and grades for each student in a Physics class of N students, \n \
store them in a nested list and print the name(s) of any student(s) having the second lowest grade. \
------------------------------------------------------------"
# create a nested list 
numberOfStudent = int(raw_input("Please, input a number : "))
studentNameWithScore = []
for a in range(numberOfStudent):
    student_name = raw_input("Please, write a name : ")
    student_score = float(raw_input("Please, Input a score : "))
    studentNameWithScore.append([student_name, student_score])

studentNameWithScore.sort(key=lambda person: (person[1], person[0]))
second_lowest_grade = [person[1] for person in studentNameWithScore if person[1] != studentNameWithScore[0][1]][0]
for b in [person for person in studentNameWithScore if person[1] == second_lowest_grade]:
    print b[0]

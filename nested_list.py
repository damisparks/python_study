print " PROBLEM : \n \
Given the names and grades for each student in a Physics class of N students, \n \
store them in a nested list and print the name(s) of any student(s) having the second lowest grade. \
------------------------------------------------------------"

# create a nested list 
name_score = []
for _ in range(int(raw_input("Please, input a number : "))):
    # write a name 
    name = raw_input("Please, write a name : ")
    # input a score. 
    score = float(raw_input("Please, Input a score : "))
    #add name and score to the list "name_score"
    name_score.append([name, score])
print name_score
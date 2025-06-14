'''
Suppose we need to assign different grades to students based on their scores.

If a student scores above 90, assign grade A
If a student scores above 75, assign grade B
If a student scores above 65, assign grade C

'''

def assign_grades():
     scores = float (input ("Input Score of Student: "))
     if scores > 90:
        print("Congratulations You Got Grade A")
        print("Wishing you all the best")
     elif scores > 75:
       print("Congratulations You Got Grade B")
       print("Wishing you all the best")
     elif scores > 65: 
       print("Congratulations You Got Grade C")
       print("Wishing you all the best")
     else:
       print("Soory You Not Got Grade ")
       print("Study Hard To Get Grade In Next Exam")
        
assign_grades()

'''
OutPut
1) 90
Input Score of Student: 90.71
Congratulations You Got Grade A
Wishing you all the best

Input Score of Student: 89.99
Congratulations You Got Grade B
Wishing you all the best

2) 65
Input Score of Student: 65
Soory You Not Got Grade 
Study Hard To Get Grade In Next Exam

Input Score of Student: 65.1
Congratulations You Got Grade C
Wishing you all the best



'''


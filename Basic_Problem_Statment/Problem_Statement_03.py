
'''
Write a function to check whether a student passed or failed his/her examination.

Assume the pass marks to be 50.
Return Passed if the student scored more than 50. Otherwise, return Failed.

'''

def pass_fail():
    score = int(input("Please enter your your Marks: "))
    if score > 50:
       print("Pass")
    else:
       print("Failed")

pass_fail()        
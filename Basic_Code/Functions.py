def add_number(num1, num2):
    sum = num1 + num2
    print('Sum is : ',sum)
    print ('---------------')
    
    multi = num1 * num2
    print('Multiplication is :',multi)
    
add_number(6,8)
print ('-------------End Of Code ---------')
'''
output

Sum is :  14
---------------
Multiplication is : 48

=== Code Execution Successful ===
'''

def function_call(s):
    result= s * s
    return result
print('------------Start of code----------')
sq = function_call(8)

print('Sq is: ',sq)

print ('-------------End Of Code ---------')
#///////////////////////////////////////////////////////

def defalt_value(a=5, b=7):
    sum = a + b
    print('sum: ',sum )
    
print('------------Function Argument with Default Values----------')    
defalt_value(9,5)

defalt_value(3)

defalt_value()

print ('-------------End Of Code ---------')

'''
------------Function Argument with Default Values----------
sum:  14
sum:  10
sum:  12
-------------End Of Code ---------
'''

'''
Write a function to split the restaurant bill among friends.

Take the subtotal of the bill and the number of friends as inputs.
Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
Return the amount each friend has to pay, rounded off to two decimal places.

'''

def bill_split():
        a = int(input('Total Bill : '))
        c = 20 / 100 * a                                    #tax
        b = int(input('Number of Friends: '))
        amount = a + c
        friends = int(amount / b)
        print('Each Friend has to pay :',friends)
    
bill_split()

'''
output:

Total Bill : 221
Number of Friends: 5
Each Friend has to pay : 53

=== Code Execution Successful ===

'''
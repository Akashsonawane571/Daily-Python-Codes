while True:
    user_input = input('Enter your name (Type end for exit) : ')

    if user_input == 'end':
        print(f'The loop is ended')
        break  

    print(f'Hi {user_input}')
    
    '''
    
    Output:

Enter your name (Type end for exit) : Akash
Hi Akash
Enter your name (Type end for exit) : Hello
Hi Hello
Enter your name (Type end for exit) : end
The loop is ended

=== Code Execution Successful ===
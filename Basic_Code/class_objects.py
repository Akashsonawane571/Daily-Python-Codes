class Room():
    length = 0.0
    width = 0.0
    
    def calculate_area(self):
        print('Area of Room: ', self.length * self.width)
        
        
study = Room()
study.length = float(input('Enter Length: '))
study.width = float(input('Enter width: '))

study.calculate_area()

'''
output

Enter Length: 55.5
Enter width: 87.5
Area of Room:  4856.25

=== Code Execution Successful ===

'''

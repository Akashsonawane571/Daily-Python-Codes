Sonawane = ['Akash', "Yash", "Tanu", "Aaru"]
Pagar = ["Sunita", "Nanu", "Shashikant", "Tau"]

for _ in range(0,4):
    print('Hi')
    for sonawane in Sonawane:
        if sonawane == "Tanu" :
           break
        for pagar in Pagar:
           if pagar == "Shashikant":
              continue
           print(sonawane, pagar)
    
    print('-----------------------')
  
    '''
    OUTPUT;
    
Hi
Akash Sunita
Akash Nanu
Akash Tau
Yash Sunita
Yash Nanu
Yash Tau
-----------------------
Hi
Akash Sunita
Akash Nanu
Akash Tau
Yash Sunita
Yash Nanu
Yash Tau
-----------------------
Hi
Akash Sunita
Akash Nanu
Akash Tau
Yash Sunita
Yash Nanu
Yash Tau
-----------------------
Hi
Akash Sunita
Akash Nanu
Akash Tau
Yash Sunita
Yash Nanu
Yash Tau
-----------------------

=== Code Execution Successful ===

'''
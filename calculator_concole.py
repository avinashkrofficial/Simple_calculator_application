def operation(choose,x,y):
    if choose == 1:
        print("\nAddition of two number is: ",x+y)
    elif choose == 2:
        print("\nSubtraction of two number is: ",x-y)
    elif choose == 3:
        print("\nMultiplication of two number is: ",x*y)
    elif choose == 4:
        print("\nDivision of two number is: ",x/y)
    else :
        print("\nPlease choose correct option")      
    
        


x =  int(input("Enter the first number: "))
y =  int(input("Enter the second number: "))

print("\n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division ")
choose = int(input("\nEnter any number 1 to 4: "))
operation(choose,x,y)
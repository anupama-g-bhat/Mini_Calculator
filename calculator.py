def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    try :
        return num1/num2
    except ZeroDivisionError:
         return "Division by zero is not allowed"
         
while True:     
    print("Welcome! Choose an option \n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n")
    
    try :
        choice =int(input("Enter your choice(1-4)"))
    except ValueError :
        print("Please enter a number")
        continue

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Try again!")
        continue
    
    try :
        a = float(input("Enter the first number"))
        b = float(input("Enter the second number"))
    except ValueError :
        print("Enter the numbers only")
        continue
    
    if choice == 1:
        print("Answer : ", add(a,b))
    elif choice == 2:
        print("Answer : ",subtract(a,b))
    elif choice == 3:
        print("Answer : ",multiply(a,b))
    elif choice == 4:
        print("Answer : ",divide(a, b))

    option =input("Do you want to calculate again? (Y/N)").strip().lower()
    if option != "y" :
        print("Good Bye!") 
        break
    
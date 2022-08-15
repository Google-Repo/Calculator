# Programmer for an simple calculator

#This function for adding two numbers
def add(x,y):
    return x+y

#This function for substracting two numbers

def substract(x,y):
   return x-y

#This  functions is for Multipling two numbers
def multiply(x,y):
    return x*y

#This functions is for dividing two numbers
def divide(x,y):
    return x/y

print("Type of Calculation")
print("1.addition")
print("2.substraction")
print("3.Multiplication")
print("4.Divition")

while True:
    #take input from the user
    Type = input("Enter your Type(1/2/3/4): ")
    
    #check if Type is one of the four options
    if Type in ('1','2','3','4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if Type  == '1':
            print(num1,"+", num2 ,"=", add(num1,num2))

        elif Type == '2':
            print(num1, '-', num2, '=', substract(num1,num2))

        elif Type == '3':
            print(num1,'*',num2,'=',multiply(num1,num2))

        elif Type == '4':
            print(num1,'/',num2,'=',divide(num1,num2))

        #check if user wants another calculation
        #break the while loop if answer is no
        next_calculation = input("let's do next calcution?(y/n): ")
        if next_calculation == 'n':
           break

    else:
        print("Invalid Input")
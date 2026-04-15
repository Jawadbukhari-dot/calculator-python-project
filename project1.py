#Calculator 


def addition (num1,num2):
    return (num1+num2)

def substraction (num1,num2):
    return (num1-num2)

def multiplication (num1,num2):
    return (num1*num2)

def division (num1,num2):
    return (num1/num2)

def average (num1,num2):
    return (num1+num2)/2


print ("Please select an operation \n"\
       "1.Addition \n"\
        "2.Substraction \n" \
        "3.Multiplication \n" \
        "4.Division \n" \
        "5.Average \n")

select= int(input("select an operation from 1,2,3,4,5:"))

number1 = int(input("Enter first number"))
number2 = int(input("Enter secound number"))

if select == 1:
    print(number1,"+", number2, "=", \
           addition(number1,number2))
elif select == 2:
    print(number1, "-",number2, "=", \
         substraction(number1,number2))
elif select ==3:
    print(number1, "*", number2,"=",\
          multiplication (number1,number2))
elif select == 4:
    print(number1, "/", number2, "=", \
          division(number1,number2))
elif select == 5:
    print (number1, "+", number2, "/2","=",\
           average (number1,number2))
else:
    print("you'r operation is invalid")
    
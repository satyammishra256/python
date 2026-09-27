email=input("enter the email :")
password=input("enter the password :")
if email=="satyam@gmail.com" and password=="1234":
    print("you are welcome")
elif email=="satyam@gmail.com" and password!="1234" :
    print("password is incorrect")
else :
    print("enter the correct details")


# minimum of three numbers program
a=int(input("enter a number1 :\n"))
b=int(input("enter the number2 :\n"))
c=int(input("enter the number3 :\n"))
if a>b and a>c :
    print("a:",a," is the greatest")
elif b>a and b>c :
    print("b:",b," is the greatest")
else :
    print("c:",c," is the greatest")


# Menu driven ATM
menu=input("""
    hey! how can i help you 
    1. enter 1 to change the pin
    2. enter 2 to check the balance
    3. enter 3 to withdraw the money
    4. enter 4 to exit \n""")
if menu=='1' :
    print("change the pin")
elif menu=='2' :
    print('your bank balance is 0')
elif menu=='3' :
    print('here is your money')
else :
    print('EXIT')


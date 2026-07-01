num1 = input("enter the first number\n")
num2 =input("enter the second number\n")
sum=int(num1)+int(num2)
print("sum of two numbers is"); 
print(sum)
print(type(num1)) #isme num ka type string aaraha kyonki type conversion original value par nhi kar rha balki ek naya integer object banake return kar rha

# BETTER WAY
fnum=int(input("enter the first number"))
snum=int(input("enter the second number"))
result=fnum+snum
print(result)
print(type(fnum)) # here the type of fnum will be int because we convert the value the value into string before storing it into fnum
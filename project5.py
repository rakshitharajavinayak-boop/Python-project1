f=int(input("enter first digit of the number:"))
s=int(input("enter second digit of the number:"))
t=int(input("enter third digit of the number:"))
num=int(input("enter the number:"))
if f*f*f+t*t*t+s*s*s==num:
    print ("the number is an armstrong number")
else:
    print ("the number is not an armstrong number")
    
i = input("Enter a number: ")
if i.isdigit():
    i = int(i)
if i % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")

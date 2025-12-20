e=int(input("enter the total no of working days:"))
f=int(input("enter the total no of days 100 for absent:"))
per=f/e*100
if(per<=50):
    print("eligible for exam")
else:
    print ("not eligible for exam")
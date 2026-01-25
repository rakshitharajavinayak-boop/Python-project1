def recur_fibo(n):
    if n <= 1:
       return n
    else:
       return (recur_fibo(n-1) + recur_fibo(n-2))
x = int(input("How many numbers are required? "))

if x <= 0:
   print("Please enter a positive integer.")
elif x!=int(x):
   print("Please enter an integer.")
else:
   print("Fibonacci series is generated below:")
   for i in range(x):
       print(recur_fibo(i))
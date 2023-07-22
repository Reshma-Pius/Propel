#Q2). Write a Python program to create the table (from 1 to 10) of a number getting input from the user

a = int(input("Enter a number: "))
n = int(input("Enter the limit: "))
print(f"Multiplication table of {a}: ")
for i in range(1,n+1):
    b=a*i

    print(f"{a}*{i}={b}")
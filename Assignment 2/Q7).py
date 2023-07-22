#Q7). Program to print all odd numbers from 1-50

odd_numbers=[]
for n in range(1,51):
    if n%2==0:
        continue
    else:
        odd_numbers.append(n)
print("Odd numbers are:    ")
print(odd_numbers)



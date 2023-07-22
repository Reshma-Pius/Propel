#Q5). Python program to print odd numbers & even numbers separately in a list of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1=[]
list2=[]
for i in list:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print("List of even numbers: ",list1)
print("List of odd numbers: ",list2)
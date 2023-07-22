#Q3). Sort the list in ascending order and print the first element

list=[]
n = input("Enter the elements in the list: ")
list=n.split()
print("Orginal list: ",list)
list.sort()
print("Ascending order: ",list)
print("The first element is: ",list[0])
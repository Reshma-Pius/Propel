#Q4). Python program to find second largest number in a list

list=[]
elements = input("Enter elements in the list: ")
list= elements.split()
print("Orginal list: ",list)
list.sort()
print("Ascending order: ",list)
list1=list[::-1]
print("Descending order: ",list1)
print("Second largest Element:", list1[1])


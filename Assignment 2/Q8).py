#Q8).	Program to count Even and odd numbers in a list

list1=[]
list2=[]
even_count=0
odd_count=0
a = input("Enter the elements: ")
list=a.split()
for i in range(len(list)+1):
    if i==0:
        continue
    elif (i%2==0):
        list1.append(i)
        even_count+=1
    else:
        list2.append(i)
        odd_count += 1

print("List1 of Even numbers: ", list1)
print("List2 of Odd numbers: ", list2)
print("Count of Even list: ",even_count)
print("Count of Odd list: ",odd_count)


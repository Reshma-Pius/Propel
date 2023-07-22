#Q6). Program for Reversing a list

list=[]
a = (input("Enter number of elements separeted by space: "))
list = a.split()
reversed_list = list[ : :-1]
print("Orginal list: ", list)
print("Reversed_list: ",reversed_list)

#or

list=[]
a = input("Enter numbers in the list: ")
list=a.split()
print("Orginal list: ", list)
list.reverse()
print("Reversed_list: ",list)
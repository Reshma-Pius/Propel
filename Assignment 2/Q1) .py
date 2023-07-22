#Q1). Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500

list=[]
for i in range(2000,2500):
    if i%5==0 and i%8==0:
        list.append(i)
print("Numbers divisible by 5 and multiple of 8 are: ")
print(list)
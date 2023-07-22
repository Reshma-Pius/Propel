#Q10). Write a Python program that matches a string that has an 'a' followed by anything, ending with 's'

string = input("Enter the string: ")
if string.startswith('a') and string.endswith('s'):
 print("Matches")
else:
      print("not matches")
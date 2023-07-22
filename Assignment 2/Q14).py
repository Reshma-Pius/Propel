#Q14) Write a program to accept percentage from the user and display the grade according to the following criteria:
'''
          Marks                                    Grade
	     > 90                                        A
         > 80 and <= 90                              B
         >= 60 and <= 80                             C
         below 60
'''

marks_percnt = int(input("Enter your Percentage: "))

if marks_percnt >90:
    print("Grade: A")
elif marks_percnt >80 and marks_percnt<=90:
    print("Grade: B")
elif marks_percnt >=60 and marks_percnt<=80:
    print("Grade: C")
else:
    print("Grade: D")



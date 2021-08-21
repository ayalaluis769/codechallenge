#Before 
"""
Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+


if 0 == 100:
    print("Passing")
else:
    print("Failing")
"""
"""
our Challenge:
You will be working on creating a grading system for the students at Nucamp! 
You will use what you have learned this week, to put student numeric grades into a system that you create, and have it tell you what the corresponding letter grades should be. 
In the cc_if.py file, you should see the beginning of this system, and a small table of students and grades. 
Right now it prints out Passing or Failing depending on what we put into the conditional statement. We will need to expand on that and make it show a letter grade (A+, A, B, C, D, F), depending on their numeric grade. 
Turn lines 1 through 10 into a multi-line comment using a pair of triple quotes. All that's left is an if/else statement that checks if 0 is equal to 100. 
Declare a variable on line 11, above the first conditional if statement. Name it gradeToTest and assign it the value of 0. 
Replace the number 0 on line 12 with gradeToTest.
If a student has a grade of 100, the program should print out "A+". Replace the "Passing" string in the print function on line 13 with "A+".
Underneath the first if statement, you will need to create several elif statements for the grades A, B, C, and D:
On line 14, create a new elif statement that checks to see if gradeToTest is greater than or equal to 90. If so, then on line 15 print "A".
On line 16, create another elif statement that checks to see if gradeToTest is greater than or equal to 80. If so, then on line 17 print "B".
On line 18, create another elif statement that checks to see if gradeToTest is greater than or equal to 70. If so, then on line 19 print out "C".
On line 20, create another elif statement that checks to see if gradeToTest is greater than or equal to 50. If so, then on line 21 print out "D".
For the else statement, replace the string "Failing" with "F". This will be the default case.
Finally, open the integrated terminal in Visual Studio Code. You can do this either by going to the View menu and selecting Terminal, or using the keyboard shortcut Ctrl/Control + ` <-- this character is a backtick character, not a single quote, and you can find it just below your Esc button at the top left of your keyboard. 
"""

#After

"""
Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""

gradeToTest = 100
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 60:
    print("D")              
else:
    print("F")
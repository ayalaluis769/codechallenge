#Before

"""
x = 0

while x != 10:
    x = x + 0.1
    if x > 1:
        break
    if x < 5:
        print(x)
    elif x == 6:
        break
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    else:
        print("x is bigger than 8. It is:", x)

"""


"""Your Challenge:
Change the value by which x is incremented to 1  instead of 0.1.
Delete the lines that cause the program to break out of the loop if x  is bigger than 1.
For the elif statement with the condition that x == 6, add a print(x) statement above the break statement, then change the break statement to a continue.
"""




#After

x = 0

while x != 10:
    x = x + 1
    if x < 5:
        print(x)
    elif x == 6:
        print(x)
        continue
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    else:
        print("x is bigger than 8. It is:", x)
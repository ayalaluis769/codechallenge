#Before

"""priceIsRight = 15

if priceIsRight:
    print("Price is too low!")
    if priceIsRight:
        print("Price is almost there!")
        if priceIsRight:
            print("Price is exactly that!")
        if priceIsRight:
            print("Price is too high!")"""
            

"""Your Challenge:
On line 3, update the condition to check if priceIsRight is lower than 5.
On line 5, update the condition to check if priceIsRight is greater than or equal to 5 and that priceIsRight is lower than or equal to 9.
On line 7, update the condition to check if the price is correct by evaluating if priceIsRight is equal to 10.
Un-indent line 5 and 7 and change the if statements to elif.
Un-indent line 9 and change that if statement to an else statement.
You should be able to test the code now with any variation of numbers for priceIsRight, and it should only print out one message for you."""



#After

priceIsRight = 15

if priceIsRight < 5:
    print("Price is too low!")
elif priceIsRight >= 5 and priceIsRight <= 9:
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")
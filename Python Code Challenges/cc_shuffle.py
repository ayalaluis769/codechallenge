"""Consider this: We can use a Python list to represent a part of a deck of playing cards, like so so:
["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
This defines a list containing 13 items, each of which represent a single card of the Diamonds suit: AD is Ace of Diamonds, 2D is 2 of Diamonds, and so on. 
We can also define an empty hand (no cards) with an empty list: []
Code Challenge
Begin by creating a new file with a .py extension and adding the following code to it:
import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
This last line that says "while diamonds:" will begin a while loop that will iterate as long as the diamonds list is not empty.
Your challenge begins inside the while loop:
Prompt the user to input either enter to pick a card, or Q plus enter to quit.
If the user input is "Q" then break out of the while loop.
Otherwise, think of a way to use a method from the random module such that a random card is selected from the diamonds list.
Use list methods to remove that card from the diamonds list, then add it to the hands list.
Print the contents of both decks. 
After the while loop ends, use an if statement to check the condition not diamonds like so:
if not diamonds:
This statement will evaluate as True if the diamonds list is empty. 
Inside this if statement's body, print the string "There are no more cards to pick."
"""

import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:

    choice = input("Press enter to pick a card, or Q then enter to quit: ")

    if choice == "yes":
        
        pick = random.choice(diamonds)

        index_of_pick = diamonds.index(pick)

        hand.append(pick)
        diamonds.pop(index_of_pick)
        print("Your hand: ", hand)
        print("Reamining cards: ", diamonds)
    if choice == ("Q" and "q"):
        quit()    

if not diamonds:
    print("There are no more cards to pick")
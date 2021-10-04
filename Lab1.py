##################################
#
#    File Name: Lab1_Group1.py
#    Date: Oct 4, 2021
#    Authors: Henry Peng, Irina Nazarova
#    Description: This application will take the card number,
#                         and using Luhn algorithm will determine if
#                         the card number is valid
#
##################################

# Declaration Section

# card_number variable will store the enetered value of card number
card_number = ""

# valid_card variable will indicate whether the card is valid or not
valid_card = false

# last_digit variable will store teh value of the last digit in entered value
last_digit = 0

# card_reversed variable will store the reversed sequence od characters
card_reversed = ""

# card_list is the list that contain card characters in reverse order
card_list = []

# sum_of_digits will store the sum of resulting digits
sum_of_digits = 0


# Input Section

# Promt the user to enter a card number and store the value in card_number
card_number = input("Please enter a card number: ")

# Processing Section

# Take the last character, turn in to int and store the result in last_digit
last_digit = int(card_number[len(card_number)  - 1])
# reverse the card_number and store the result in card_reversed
card_reversed = card_number[::-1]
# take all characters except for the last digit and update the value of card_number
card_number = card_number[0:-1]
# make a list out of carrd_number and turn all characters to int using function map
card_list = list(map(int, list(card_reversed)))
# set sum_of_digits to last_digit
sum_of_digits = last_digit
# go through each elements in a list
for i in range(len(card_list)):
    # if the index is even:
    if i % 2 == 0:
        # double the value of the element
        card_list[i] *= 2
        # if the element is greater than 9:
        if card_list[i] > 9:
            # decrease this number by 9
            card_list[i] -= 9
    # add the value of each element to sum_of_digits
    sum_of_digits += card_list[i]
# if the sum of digits is divisible by 10:
if sum_of_digits % 10 == 0:
    # set the value of valid_card to true
    valid_card = true

# Output Section

# if the card is valid:
if valid_card:
    # display the message of validity
    print("********The card is valid********")

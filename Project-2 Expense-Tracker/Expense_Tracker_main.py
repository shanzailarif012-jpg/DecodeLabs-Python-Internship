"""
Project 2: Expense Tracker
Author: Muhammad Shanzail
GitHub: dev_shanzail username: shanzailarif012-jpg
Batch: DecodeLabs 2026 - Python Programming Industrial Training

Description:
This script tracks user expenses using the Accumulator Pattern.
User continuously enters expense amounts, program adds them,
and displays the total on exit. Includes error handling for
invalid inputs.
"""

total = 0

while True:

    user = input("Enter Expense Amount or Quit: ")

    if user.lower() == "quit":
        break

    else:
        try:
            expense = int(user) # string ko int me Convert
            total = total + expense 
            print("Current Total:", total)
            
        except ValueError:
            print("Invalid input, please enter a valid number")

print("Final Total:" , total)

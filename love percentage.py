import random

def calculate_love_percentage(name1, name2):
    
    """
    This function calculates a random love percentage between two names.
    """
    love_percentage = random.randint(50, 100)  # Generates a random love percentage
    return f"Love percentage between {name1} and {name2} is {love_percentage}%"

# Taking input from user
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

# Calling function and displaying result
print(calculate_love_percentage(name1, name2))
import random
import sys

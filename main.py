# Create a program to simulate the game of EuroMillions. The user is the player and the computer generates the winning numbers. The computer must also calculate the probability of the user winning the jackpot. The regular rules for the EuroMillions apply. 

# Import the random module
import random

# Define the main function
def main():

    # Define the variables
    user_numbers = []
    winning_numbers = []
    star_numbers = []
    winning_star_numbers = []
    user_star_numbers = []
    jackpot = 0
    jackpot_probability = 0
    prize = 0
    prize_probability = 0
    winning_numbers_count = 0
    star_numbers_count = 0
    user_winning_numbers_count = 0
    user_star_numbers_count = 0
    

    # Generate the winning numbers
    for i in range(5):
        winning_numbers.append(random.randint(1,50))
    for i in range(2):
        star_numbers.append(random.randint(1,12))

    # Get the user numbers
    for i in range(5):
        user_numbers.append(int(input("Enter a number between 1 and 50: ")))
    for i in range(2):
        user_star_numbers.append(int(input("Enter a star number between 1 and 12: ")))

    # Check if the user numbers are valid
    for i in range(5):
        while user_numbers[i] < 1 or user_numbers[i] > 50:
            user_numbers[i] = int(input("Enter a number between 1 and 50: "))
    for i in range(2):
        while user_star_numbers[i] < 1 or user_star_numbers[i] > 12:
            user_star_numbers[i] = int(input("Enter a star number between 1 and 12: "))

    # Check if the user numbers are unique
    for i in range(5):
        while user_numbers[i] in user_numbers[i+1:]:
            user_numbers[i] = int(input("Enter a unique number between 1 and 50: "))
    for i in range(2):
        while user_star_numbers[i] in user_star_numbers[i+1:]:
            user_star_numbers[i] = int(input("Enter a unique star number between 1 and 12: "))

    # Check if the user numbers match the winning numbers
    for i in range(5):
        if user_numbers[i] in winning_numbers:
            winning_numbers_count += 1
    for i in range(2):
        if user_star_numbers[i] in star_numbers:
            star_numbers_count += 1

    # Calculate the prize
    if winning_numbers_count == 5 and star_numbers_count == 2:
        jackpot = 100000000
        jackpot_probability = 1/139838160
    elif winning_numbers_count == 5 and star_numbers_count == 1:
        prize = 1000000
        prize_probability = 1/622614630
    elif winning_numbers_count == 5 and star_numbers_count == 0:
        prize = 500000
        prize_probability = 1/3440075130
    elif winning_numbers_count == 4 and star_numbers_count == 2:
        prize = 10000
        prize_probability = 1/12871592
    elif winning_numbers_count == 4 and star_numbers_count == 1:
        prize = 500
        prize_probability = 1/6777225
    elif winning_numbers_count == 4 and star_numbers_count == 0:
        prize = 200
        prize_probability = 1/3819815
    elif winning_numbers_count == 3 and star_numbers_count == 2:
        prize = 100
        prize_probability = 1/188188
    elif winning_numbers_count == 2 and star_numbers_count == 2:
        prize = 20
        prize_probability = 1/9865
    elif winning_numbers_count == 3 and star_numbers_count == 1:
        prize = 10
        prize_probability = 1/7071
    elif winning_numbers_count == 3 and star_numbers_count == 0:
        prize = 8
        prize_probability = 1/3147
    elif winning_numbers_count == 1 and star_numbers_count == 2:
        prize = 5
        prize_probability = 1/1881
    elif winning_numbers_count == 2 and star_numbers_count == 1:
        prize = 4
        prize_probability = 1/50
    elif winning_numbers_count == 2 and star_numbers_count == 0:
        prize = 3
        prize_probability = 1/22
    elif winning_numbers_count == 0 and star_numbers_count == 2:
        prize = 2
        prize_probability = 1/17


    # Check if the user numbers match the winning numbers
    for i in range(5):
        if user_numbers[i] in winning_numbers:
            user_winning_numbers_count += 1
    for i in range(2):
        if user_star_numbers[i] in star_numbers:
            user_star_numbers_count += 1

    # Print the results
    print("The winning numbers are: ", winning_numbers)
    print("The star numbers are: ", star_numbers)
    print("Your numbers are: ", user_numbers)
    print("Your star numbers are: ", user_star_numbers)
    print("You matched ", user_winning_numbers_count, " winning numbers and ", user_star_numbers_count, " star numbers.")
    print("You won ", prize, " euros.")
    print("The probability of winning the jackpot is ", jackpot_probability, " and the probability of winning a prize is ", prize_probability, ".")

# Call the main function
main()

# End of program
print("End of program.")


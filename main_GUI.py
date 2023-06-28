import random
import tkinter as tk
from tkinter import messagebox

def check_numbers(user_numbers, user_star_numbers, winning_numbers, star_numbers):
    # variables
    winning_numbers_count = 0
    star_numbers_count = 0
    user_winning_numbers_count = 0
    user_star_numbers_count = 0

    # valid numbers checker
    for i in range(5):
        if user_numbers[i] < 1 or user_numbers[i] > 50:
            messagebox.showerror("Invalid Input", "Enter a number between 1 and 50.")
            return
    for i in range(2):
        if user_star_numbers[i] < 1 or user_star_numbers[i] > 12:
            messagebox.showerror("Invalid Input", "Enter a star number between 1 and 12.")
            return

    # unique numbers checker
    if len(set(user_numbers)) != 5:
        messagebox.showerror("Invalid Input", "Enter unique numbers.")
        return
    if len(set(user_star_numbers)) != 2:
        messagebox.showerror("Invalid Input", "Enter unique star numbers.")
        return

    # winning numbers checker
    for number in user_numbers:
        if number in winning_numbers:
            winning_numbers_count += 1
    for number in user_star_numbers:
        if number in star_numbers:
            star_numbers_count += 1

    # your numbers are winning numbers checker
    for number in user_numbers:
        if number in winning_numbers:
            user_winning_numbers_count += 1
    for number in user_star_numbers:
        if number in star_numbers:
            user_star_numbers_count += 1

    # Calculate prize and probability
    prize = 0
    prize_probability = 0

    if winning_numbers_count == 5 and star_numbers_count == 2:
        prize = 100000000
        prize_probability = 1 / 139838160
    elif winning_numbers_count == 5 and star_numbers_count == 1:
        prize = 1000000
        prize_probability = 1 / 622614630
    elif winning_numbers_count == 5 and star_numbers_count == 0:
        prize = 500000
        prize_probability = 1 / 3440075130
    elif winning_numbers_count == 4 and star_numbers_count == 2:
        prize = 10000
        prize_probability = 1 / 12871592
    elif winning_numbers_count == 4 and star_numbers_count == 1:
        prize = 500
        prize_probability = 1 / 6777225
    elif winning_numbers_count == 4 and star_numbers_count == 0:
        prize = 200
        prize_probability = 1 / 3819815
    elif winning_numbers_count == 3 and star_numbers_count == 2:
        prize = 100
        prize_probability = 1 / 188188
    elif winning_numbers_count == 2 and star_numbers_count == 2:
        prize = 20
        prize_probability = 1 / 9865
    elif winning_numbers_count == 3 and star_numbers_count == 1:
        prize = 10
        prize_probability = 1 / 7071
    elif winning_numbers_count == 3 and star_numbers_count == 0:
        prize = 8
        prize_probability = 1 / 3147
    elif winning_numbers_count == 1 and star_numbers_count == 2:
        prize = 5
        prize_probability = 1 / 1881
    elif winning_numbers_count == 2 and star_numbers_count == 1:
        prize = 4
        prize_probability = 1 / 50
    elif winning_numbers_count == 2 and star_numbers_count == 0:
        prize = 3
        prize_probability = 1 / 22
    elif winning_numbers_count == 0 and star_numbers_count == 2:
        prize = 2
        prize_probability = 1 / 17

    # Display the results
    messagebox.showinfo("EUROMILLIONS Results", f"You matched {user_winning_numbers_count} winning numbers and {user_star_numbers_count} star numbers.\nYou won {prize} euros.")

def generate_random_numbers():
    winning_numbers = random.sample(range(1, 51), 5)
    star_numbers = random.sample(range(1, 13), 2)
    
    return winning_numbers, star_numbers

def main():
    # Create the GUI
    window = tk.Tk()
    window.title("EUROMILLIONS")
    

    # Create and configure labels
    label1 = tk.Label(window, text="Click the buttons to select 5 unique numbers between 1 and 50:")
    label1.pack()

    # Create and configure number buttons
    number_buttons = []
    number_frame = tk.Frame(window)
    number_frame.pack()
    for number in range(1, 51):
        if number < 10:
            formatted_number = f"0{number}"
        else:
            formatted_number = str(number)
        button = tk.Button(number_frame, text=formatted_number, command=lambda num=number: select_number(num))
        button.pack(side=tk.LEFT)
        number_buttons.append(button)
        if number % 10 == 0:
            number_frame = tk.Frame(window)
            number_frame.pack()

    label2 = tk.Label(window, text="Click the buttons to select 2 unique star numbers between 1 and 12:")
    label2.pack()

    # Create and configure star number buttons
    star_number_buttons = []
    star_number_frame = tk.Frame(window)
    star_number_frame.pack()
    for number in range(1, 13):
        if number < 10:
            formatted_number = f"0{number}"
        else:
            formatted_number = str(number)
        button = tk.Button(star_number_frame, text=formatted_number, command=lambda num=number: select_star_number(num))
        button.pack(side=tk.LEFT)
        star_number_buttons.append(button)

    winning_numbers, star_numbers = generate_random_numbers()

    selected_numbers = []
    selected_star_numbers = []

    def select_number(number):
        if len(selected_numbers) < 5:
            selected_numbers.append(number)
            selected_numbers_label.config(text=str(selected_numbers))

    def select_star_number(number):
        if len(selected_star_numbers) < 2:
            selected_star_numbers.append(number)
            selected_star_numbers_label.config(text=str(selected_star_numbers))

    def delete_selected_number():
        if selected_numbers:
            selected_numbers.pop()
            selected_numbers_label.config(text=str(selected_numbers))

    def delete_selected_star_number():
        if selected_star_numbers:
            selected_star_numbers.pop()
            selected_star_numbers_label.config(text=str(selected_star_numbers))

    def handle_check_numbers():
        if len(selected_numbers) == 5 and len(selected_star_numbers) == 2:
            check_numbers(selected_numbers, selected_star_numbers, winning_numbers, star_numbers)
            winning_numbers_label.config(text=f"Winning Numbers: {winning_numbers}")
            winning_stars_label.config(text=f"Winning Stars: {star_numbers}")
        else:
            messagebox.showerror("Invalid Selection", "Select 5 numbers and 2 star numbers.")

    # Create and configure buttons
    button = tk.Button(window, text="Check Numbers", command=handle_check_numbers)
    button.pack()

    # Create and configure selected numbers label
    selected_numbers_label = tk.Label(window, text="")
    selected_numbers_label.pack()

    # Create and configure selected star numbers label
    selected_star_numbers_label = tk.Label(window, text="")
    selected_star_numbers_label.pack()

    # Create and configure delete buttons
    delete_button = tk.Button(window, text="Delete Last Number", command=delete_selected_number)
    delete_button.pack()

    delete_star_button = tk.Button(window, text="Delete Last Star Number", command=delete_selected_star_number)
    delete_star_button.pack()

    # Create and configure winning numbers label
    winning_numbers_label = tk.Label(window, text="")
    winning_numbers_label.pack()

    winning_stars_label = tk.Label(window, text="")
    winning_stars_label.pack()

    # Start the GUI event loop
    window.mainloop()

# Call the main function to run the program
if __name__ == "__main__":
    main()
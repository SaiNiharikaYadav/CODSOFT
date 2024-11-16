import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score, rounds_played

    if user_choice == computer_choice:
        result.set("It's a Tie! 🎉")
        rounds_played += 1
        update_scores()
        return

    # Determine winning conditions
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Scissors" and computer_choice == "Paper") or \
       (user_choice == "Paper" and computer_choice == "Rock"):
        result.set(f"You Win! 🎉 {user_choice} beats {computer_choice} 🏆")
        user_score += 1
    else:
        result.set(f"You Lose! 😞 {computer_choice} beats {user_choice} 😞")
        computer_score += 1

    rounds_played += 1
    update_scores()

    if rounds_played >= 10:
        if user_score > computer_score:
            result.set(f"YOU WIN THE GAME! 🏆 Final Score: {user_score}-{computer_score} 🏆")
        elif user_score < computer_score:
            result.set(f"YOU LOSE THE GAME! 😞 Final Score: {user_score}-{computer_score} 😞")
        else:
            result.set(f"IT'S A TIE GAME! 🎉 Final Score: {user_score}-{computer_score} 🎉")
        disable_buttons()

# Function to handle the user's choice
def play(user_choice):
    if rounds_played >= 10:
        return  # Prevent further play after 10 rounds

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    computer_choice_label.set(f"Computer chose: {computer_choice}")

    determine_winner(user_choice, computer_choice)

# Function to update the score display
def update_scores():
    score_label.set(f"User: {user_score} | Computer: {computer_score} | Rounds Played: {rounds_played}/10")

# Function to reset the game
def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0
    result.set("")
    computer_choice_label.set("Computer chose: ")
    update_scores()

    # Enable buttons for playing again
    enable_buttons()

# Function to stop the game
def stop_game():
    if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
        root.destroy()

# Function to disable buttons after 10 rounds
def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

# Function to enable buttons after reset
def enable_buttons():
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x600")
root.configure(bg="#f0f8ff")  # Alice Blue background color

# Global variables
user_score = 0
computer_score = 0
rounds_played = 0

# Labels and instructions
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#ff4500").pack(pady=10)
tk.Label(root, text="Choose your move:", font=("Helvetica", 16), bg="#f0f8ff", fg="#00008b").pack()

# Result and computer choice variables
result = tk.StringVar()
result.set("")
computer_choice_label = tk.StringVar()
computer_choice_label.set("Computer chose: ")

# Buttons for user input
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

# Custom button colors
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14), bg="#ff4500", fg="white",
                        command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=15)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14), bg="#32cd32", fg="white",
                         command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=15)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), bg="#1e90ff", fg="white",
                            command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=15)

# Labels to display the computer's choice and the result
tk.Label(root, textvariable=computer_choice_label, font=("Helvetica", 14), bg="#f0f8ff", fg="#000").pack(pady=10)
tk.Label(root, textvariable=result, font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#ff6347").pack(pady=20)

# Scoreboard
score_label = tk.StringVar()
score_label.set(f"User: {user_score} | Computer: {computer_score} | Rounds Played: {rounds_played}/10")
tk.Label(root, textvariable=score_label, font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#008b8b").pack(pady=10)

# Frame for Restart and Stop buttons
control_frame = tk.Frame(root, bg="#f0f8ff")
control_frame.pack(pady=10)

# Restart button
restart_button = tk.Button(control_frame, text="Restart Game", font=("Helvetica", 12), bg="#ff8c00", fg="white", command=reset_game)
restart_button.grid(row=0, column=0, padx=10)

# Stop button
stop_button = tk.Button(control_frame, text="Stop Game", font=("Helvetica", 12), bg="#4682b4", fg="white", command=stop_game)
stop_button.grid(row=0, column=1, padx=10)

# Run the Tkinter event loop
root.mainloop()

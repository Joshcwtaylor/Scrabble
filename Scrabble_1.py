# Scrabble 1.0
import random 
import time

words = ["Dorothy", "Blanche", "Rose", "Sophia", "Stan", "Miles", 
    "Salvadore", "Gloria", "Angelo", "Clayton", "Phil", "Rebecca", 
    "Michael", "Kirsten", "David", "Renee", "Charley", "Edgar", 
    "Big Daddy", "George"]

#Function to display the current hint with guessed letters
def display_hint(hint):
    print(" ".join(hint))

#Function to display the correct answer when game ends
def display_answer(answer):
    print(" ".join(answer))

#Function to update the hint array based on the guessed letter
def update_hint(answer, hint, guessed_letter):
    for i in range(len(answer)):
        if answer[i] == guessed_letter:
            hint[i] = guessed_letter

#Function to display the menu
def display_menu():
    print("  *******Welcome to Scrabble********")
    print("Guess a Series of words in 60 seconds!")
    print("1) Start Game")
    print("2) Exit the program")
    choice = input("Enter 1 or 2 ")
    return choice

def main():
    choice = display_menu()
    if choice == "2":
        print("Exiting the Program. See ya!")
        return
    
    correct_guesses = 0
    words_to_guess = 5
    time_limit = 60 #seconds
    available_words = words.copy()

    start_time =time.time()
   
    while correct_guesses < words_to_guess and available_words:
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            print("\nTime's up. You ran out of time.")
            break
        
        answer = random.choice(available_words)
        hint = ["_"] * len(answer)
        word_guessed = False
    
        while not word_guessed:
            random_letter_1 = random.choice(answer)
            random_letter_2 = random.choice(answer)

            print("\nMake a Selection:")
            print("┌───────┬───────┬─────────────┐")
            print("│   1   │   2   │      3      │")
            print("├───────┼───────┼─────────────┤")
            print(f"│   {random_letter_1}   │   {random_letter_2}   │  Guess Word │")
            print("└───────┴───────┴─────────────┘")
            display_hint(hint)
            selected_number = input("Pick Letter 1 or 2, or Select 3 to guess the word ")

            if selected_number == "1":
                update_hint(answer, hint, random_letter_1)
            elif selected_number == "2":
                update_hint(answer, hint, random_letter_2)
            elif selected_number == "3":
                guess = input("What is your guess? ")
                if guess == answer:
                    print("Yes, thats the dish!")
                    display_answer(answer)
                    correct_guesses += 1
                    word_guessed = True
                else:
                    print("Incorrect guess")
            else:
                print("Invalid input, please select, 1, 2, or 3. ")

            if "_" not in hint:
                print("Youve revealed the entire word")
                display_answer(answer)
                correct_guesses += 1
                word_guessed = True
        
        # Remove guessed word from available words
        available_words.remove(answer)

        #time calculation 
        elapsed_time =time.time() - start_time
        remaining_time = time_limit - elapsed_time
        if remaining_time > 0 and correct_guesses != words_to_guess:
            print(f"\nYou have", int(remaining_time), "seconds left")    
        
        if correct_guesses == words_to_guess:
            print(f"\nCongratulations! You've guessed", words_to_guess, "words correctly!")
            print(f"With only", int(remaining_time), "remaining!")
            

if __name__ == "__main__":
    main()

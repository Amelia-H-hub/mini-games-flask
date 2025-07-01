import random
import string

class Hangman:
    def __init__(self):
        self.words = [
            "airport", "luggage", "passport", "hotel", "reservation",
            "ticket", "boarding", "flight", "itinerary", "tourist",
            "destination", "map", "souvenir", "guidebook", "hostel",
            "visa", "checkin", "checkout", "departure", "arrival",
            "customs", "travel", "explore", "journey", "backpack",
            "restaurant", "menu", "breakfast", "lunch", "dinner",
            "dessert", "chocolate", "cheese cake", "appetizer", "main",
            "beverage", "coffee", "bubble tea", "water", "soup",
            "salad", "pizza", "burger", "noodles", "rice",
            "chicken", "beef", "seafood", "vegetable", "fruit"
        ]
        self.difficulties = {'easy': 0, 'medium': 1, 'hard': 2}
        self.chosen_difficulty = 0
        self.guess_times = 0
        self.result = ""
        self.result_underline = []
        self.letters = ""
    
    def get_context(self):
        return {
            "words": self.words,
            "difficulties": self.difficulties,
            "chosen_difficulty": self.chosen_difficulty,
            "guess_times": self.guess_times 
        }
    
    def set_guess_times(self, level):
        print(level)
        if level == 0:
            self.guess_times = 7
        elif level == 1:
            self.guess_times = 6
        else:
            self.guess_times = 5

        return self.guess_times
    
    def start_guess(self):
        self.result = random.choice(self.words).upper()
        self.result_underline = [" " if ch == " " else "_" for ch in self.result]
        self.letters = string.ascii_uppercase

        return {
            "result": self.result,
            "question": self.result_underline,
            "letters": self.letters
        }

    def guess_letter(self, letter):
        is_correct = False
        status = False
        for i in range(len(self.result)):
            if self.result[i] == letter:
                  self.result_underline[i] = letter
                  is_correct = True
                  message = f"Nice catch! You found {letter}!"

        if not is_correct:
            self.guess_times -= 1
            if self.guess_times == 0:
                status = True
                message = f"You've used up all your guesses. The answer is '{self.result}'.\n"
            else:
                message = f"{letter} is not in the mystery word."

        self.letters = self.letters.replace(letter, " ")

        if list(self.result) == self.result_underline:
            message += "\nBingo! You guessed the mystery word!"
            status = True
        
        return {
            "question": self.result_underline,
            "letters": self.letters,
            "message": message,
            "guessTimes": self.guess_times,
            "status": status
        }


  # Game starts
#   print("Welcome to the Hangman Game!")


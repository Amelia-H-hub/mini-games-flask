import random
import string

class HangmanCopy:
  words = [
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

  difficulties = {'easy': 0, 'medium': 1, 'hard': 2}
  chosen_difficulty = 0
  guess_times = 0

  def choose_level():
      global chosen_difficulty
      while True:
          level = input(
              "Choose the level of game you would like to play (Easy, Medium, Hard), or type 'q' to quit: ").strip().lower()

          if level == "q":
              print("See you next time!")
              break

          elif level in difficulties:
              chosen_difficulty = difficulties[level]
              set_guess_times()
              start_guess()
              break

          else:
              print("Invalid level. Please enter a valid level or 'q'.")

  def set_guess_times():
      global chosen_difficulty
      global guess_times
      if chosen_difficulty == 0:
          guess_times = 7
      elif chosen_difficulty == 1:
          guess_times = 6
      else:
          guess_times = 5

  def start_guess():
      global guess_times
      result = random.choice(words).upper()
      result_underline = [" " if ch == " " else "_" for ch in result]
      letters = string.ascii_uppercase

      print("Answer: ", "".join(result))

      while list(result) != result_underline:
          show_info(letters, result_underline)
          guess_letter = input("Guess a letter (case-insensitive) or type 'quit' to quit: ").upper()
          if guess_letter == "QUIT":
              confirm_quit = input("Are you sure you want to quit? (Y/n, default: Y): ").lower()
              if confirm_quit == "y" or confirm_quit == "":
                  print("See you next time!")
                  return
              elif confirm_quit == "n":
                  continue
              else:
                  print("Invalid input. Please enter Y or N (case-insensitive).")
          if not is_valid_guess(guess_letter, letters):
              continue
          is_correct = False
          for i in range(len(result)):
              if result[i] == guess_letter:
                  result_underline[i] = guess_letter
                  is_correct = True
                  print(f"Nice catch! You found {guess_letter}!")

          if not is_correct:
              guess_times -= 1
              print(f"{guess_letter} is not in the mystery word.")

          letters = letters.replace(guess_letter, " ")

          if guess_times == 0:
              print(f"You've used up all your guesses. The answer is '{result}'.\n")
              is_continue()
              return

      print("Bingo! You guessed the mystery word!")
      print(f"\nMystery word: {" ".join(result_underline)} \n")
      is_continue()

  def show_info(remain_letters, result_underline):
      global guess_times
      print(f"\nMystery word: {" ".join(result_underline)} \n")
      print("Guesses left: ", guess_times)
      print("Remaining letters: ")
      for i in range(0, len(remain_letters), 7):
          group_letter = remain_letters[i:i + 7]
          print(" ".join(group_letter))
      print()

  def is_valid_guess(guess, letters):
      if not guess.isalpha():
          print("Invalid input. Please enter a valid letter (A~Z).")
          return False
      if len(guess) == 0:
          print("Please enter a letter (A~Z).")
          return False
      if len(guess) > 1:
          print("Please enter ONLY a single letter.")
          return False
      if guess not in letters:
          print(f"{guess} has already been guessed.")
          return False
      return True

  def is_continue():
      is_continue_playing = input("Play again? (Y/n, default: Y): ").lower()

      if is_continue_playing == "y" or is_continue_playing == "":
          is_change_level = input("Would you like to change level? (Y/n, default: Y): ").lower()
          if is_change_level == "y" or is_change_level == "":
              choose_level()
          elif is_change_level == "n":
              set_guess_times()
              start_guess()
          else:
              print("Invalid input. Please enter Y or N (case-insensitive).")
      elif is_continue_playing == "n":
          print("See you next time!")
      else:
          print("Invalid input. Please enter Y or N (case-insensitive).")



  # Game starts
  print("Welcome to the Hangman Game!")
  choose_level()

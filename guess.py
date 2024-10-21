import random
guess = ""
def value():
  global guess
  blah = random.randint(1, 690)
  guess = blah
  return guess
def game():
  n= int(input("Guess the number: "))
  if n == guess:
    print("Damn You got it!")
    value()
  elif n > guess:
    print(f"Lower than that")
    game()
  elif n < guess:
    print(f"Higher than that")
    game()
  choice = input("Wanna replay? (y/n)")
  if choice.lower() == "y":
    game()
value()
game()

  
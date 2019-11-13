import random

print ("Welcome to Billy\'s game of hangman.")
print ("Goodluck!")
print ()

def get_guess():
  
  dashes = "*" * len(secret_word)
  guesses_left = 7

  while guesses_left > -1 and not dashes == secret_word:
    
    # amount of dashes and guesses left
    print(dashes)
    print ()
    print ("guesses left: " + str(guesses_left))
    print ()
    
    # user input
    guess = input("Please enter your next guess:")
    
    # incorrect guess
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      
    elif guess in secret_word:
      print ("correct! that letter is in the word")
      dashes = update_dashes(secret_word, dashes, guess)
      
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose.")
  
  else:
    print ("Congratulations You win.")
    
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
  return result
    
words = ["rarely", "universe", "notice", "sugar", "interface", "constitution", "we", "minus", "breath", "clarify", "take", "recording", "amendment", "hut", "tip", "logical", "cast", "title", "brief", "none", "relative", "recently", "detail", "port", "such", "complex", "bath", "soul", "holder", "pleasant", "buy", "federal", "lay", "currently", "saint", "for", "simple", "deliberately", "means", "peace", "prove", "sexual", "chief", "department", "bear", "injection", "off", "son", "reflect", "fast", "ago", "education", "prison", "birthday", "variation", "exactly", "expect", "engine", "difficulty", "apply", "hero", "contemporary", "that", "surprised", "fear", "convert", "daily", "yours", "pace", "shot", "income", "democaracy", "albeit", "genuinely", "commit", "caution", "try", "membership", "elderly", "enjoy", "pet", "detective", "powerful", "argue", "escape", "timetable", "proceeding", "sector", "cattle", "dissolve", "suddenly", "teach", "spring", "negotiation", "solid", "seek", "enough", "surface", "small", "search"]

secret_word = random.choice(words)
get_guess()

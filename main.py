#A Python Wordle Clone!
import random as r
import history

#Returns colored (green, yellow, or red) string (using 256 colors)
def color(msg, clr):
  if clr == "green":
    #\003(esc)[38 (foreground);5 (placeholder);40 (color code)m (color func)
    return(f"\033[38;5;40m{msg}\033[0;0m")
  if clr == "yellow":
    #\003(esc)[38 (foreground);5 (placeholder);220 (color code) (color func)
    return(f"\033[38;5;220m{msg}\033[0;0m")
  if clr == "gray" or clr == "grey":
    #\003(esc)[38 (foreground);5 (placeholder);246 (color code)m (color func)
    return(f"\033[38;5;246m{msg}\033[0;0m")
  if clr == "red":
    #\003(esc)[38 (foreground);5 (placeholder);196 (color code)m (color func)
    return(f"\033[38;5;196m{msg}\033[0;0m")
  #If none of the above worked,
  return msg

#Reads answer txt file and stores in a var
with open("wordle-answers.txt") as f:
  txt = f.read()
  answers = txt.split("\n")

#Selects a random answer
answer = r.choice(answers)

#Chooses colors for word
def shader(guess, answer):
  
  #Colors to be shaded in
  colors = ["" for i in range(5)]

  #Gray check
  for i, letter in enumerate(guess):
    if guess[i] != answer[i]:
      colors[i] = "gray"

  #Count of time a letter from answer is yellowed
  letter_count = {
    "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0,
    "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, 
    "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0,
    "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
    "y" : 0, "z" : 0
    }

  #Green check
  for i, letter in enumerate(guess):
    if letter == answer[i]:
      colors[i] = "green"
      letter_count[letter] += 1
  
  #Yellow check
  for i, letter in enumerate(guess):
    if letter in answer and answer.count(letter) > letter_count[letter] and colors[i] != "green":
      colors[i] = "yellow"
      letter_count[letter] += 1
    
  return colors

#Colors word
def colorer(word, colors):
  colored = ""
  for i in range(len(word)):
    colored += color(word[i], colors[i])
  
  return colored

#Elimintes impossible answers
def eliminator(guess, colors, answers):

  #Words to be removed
  to_remove = []
  
  #Loops thru guess
  for i, letter in enumerate(guess):
    
    #If guess is shaded gray
    if colors[i] == "gray":
      #Loop thru answers
      for word in answers:
        #And eliminate words that don't fit
        if letter in word:
          if word not in to_remove and word.count(letter) > answer.count(letter):
            to_remove.append(word)
    
    #If guess is shaded yellow
    elif colors[i] == "yellow":
      #Loop thru answers
      for word in answers:
        #And eliminate words that don't fit
        if letter not in word or word[i] == letter:
          if word not in to_remove:
            to_remove.append(word)

    #If guess is shaded green
    else:
      #Loop thru answers
      for word in answers:
        #And eliminate words that don't fit
        if word[i] != letter:
          if word not in to_remove:
            to_remove.append(word)

  #Removes all invalid words from to_remove
  for word in to_remove:
    answers.remove(word)

  #Returns final list
  return answers

#Format
print("Guess  Answer  # of Remaining Possible Guesses")
print("_____  ______  _______________________________")
print("")
  
#Runs thru with crane
guess = "crane"
shaded = shader(guess, answer)
colored = colorer(guess, shaded)
answers = eliminator(guess, shaded, answers)
print(f"{colored}  {color(answer, 'green')}   {len(answers)}")

if guess == answer:
  print(f"\nGuessed in 1! Wow!")
  history.add(1)
  won = True
else:
  won = False

#Runs again with (up to) 5 other word
for i in range(2, 7):
  if won == True:
    break
  guess = answers[0]
  shaded = shader(guess, answer)
  colored = colorer(guess, shaded)
  answers = eliminator(guess, shaded, answers)
  print(f"{colored}  {color(answer, 'green')}   {len(answers)}")

  if guess == answer:
    print(f"\nGuessed in {i}")
    history.add(i)
    break

  if i == 6:
    print("\nNo more guesses")
    history.add("X")


print("\n\n ---History--- \n")
print(f"Average Score: {history.avg()}")
print(f"""Individual Counts: 
      {history.individual()}""")
print(f"Failure Count: {history.failures()}")
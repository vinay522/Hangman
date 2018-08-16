import random
def main():
  word = ""
  dictionary = []
  with open("words.txt") as f:
    for line in f:
      dictionary.append(line.rstrip())
  word = random.choice(dictionary)
  alreadyguess = []
  counter = 0
  print("You have 7 guesses")
  print(" _______     ")
  print("|       |    ") 
  print("|           ") 
  print("|            ") 
  print("|            ") 
  print("|            ") 
  print("|            ") 
			
  while(True):
    for i in range(0,len(word)):
      print("_", end= " ") if not(word[i] in alreadyguess) else print(word[i],end=" ")
    print()
    print("You have already guessed: "," ".join(alreadyguess))
    guessletter=input("Enter your guessed letter: ")
    if not(guessletter.isalpha()):
      print("Your guessed letter is not valid, please try again")
      continue
    if (guessletter in alreadyguess):
      print("You have already guessed this letter")
      continue
    alreadyguess.append(guessletter)
    if guessletter in word:
      print("Yes, your letter is in the word")
    if not(guessletter in word):
      print("No, your letter is not in the word")
      counter = counter +1
    if counter == 7:
      print("You ran out of guesses")
      break
    if all([i in alreadyguess for i in word]) == True:
      print("You win!")
      break
    if counter == 0:
      print(" _______     ")
      print("|       |    ") 
      print("|           ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
    if counter == 1:
      print(" _______     ") 
      print("|       |    ") 
      print("|       O    ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
    
    if counter == 2:
      print(" _______     ") 
      print("|       |    ") 
      print("|       O    ") 
      print("|       |    ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
    
    if counter == 3:
      print(" _______     ") 
      print("|       |    ") 
      print("|       O    ") 
      print("|      /|    ") 
      print("|            ") 
      print("|            ") 
      print("|            ") 
    
    if counter == 4:
      print(" _______     ")
      print("|       |    ")
      print("|       O    ")
      print("|      /|\\  ")
      print("|            ")
      print("|            ")
      print("|            ")
    
    if counter == 5:
      print(" _______     ")
      print("|       |    ")
      print("|       O    ")
      print("|      /|\\  ")
      print("|       |    ")
      print("|            ")
      print("|            ")
    
    if counter == 6:
      print(" _______     ")
      print("|       |    ")
      print("|       O    ")
      print("|      /|\\  ")
      print("|       |   ")
      print("|      /     ")
      print("|            ")
    if counter == 7:
      print(" _______     ") 
      print("|       |    ") 
      print("|       O    ") 
      print("|      /|\\  ") 
      print("|       |\\ ") 
      print("|      / \\ ") 
      print("|            ") 
  print(word)

if __name__ == "__main__":
  main()

import random
from replit import clear 
from icons import logo,stages,win,lose
from names import animals,fruits,fashion_brands,famous_companies,Car_brands

print(logo +"\n")
lives = 6

print("Welcome to Hangman. Choose a Category from which i shall generate a random word")
category = input("Choose from the following categories:-(Just type the number to choose the category.\n 1.Animals\n 2.Fruits\n 3.Fashion Brands\n 4.Famous Companies\n 5.Car Brands\n")

if category == "1": 
  word_list = (animals).split(",")
elif category == "2":
  word_list = (fruits).split(",")
elif category == "3":
  word_list = (fashion_brands).split(",")
elif category == "4":
  word_list = (famous_companies).split(",")
elif category == "5":
  word_list = (Car_brands).split(",")
else:
  print("Invalid Choice. ERROR!")

clear()
# word_list = (words).split(",")
random_word = (random.choice(word_list)).lower()

word_length = len(random_word)
# print(random_word)
blanks = []
for _ in range(0,word_length):
  blanks += "_"
# print(blanks)
print(' '.join(blanks))
end_of_game = False


while not end_of_game:
  print(f"You have {lives} lives")
  guess = input("\nGuess a letter\n").lower()
  clear()
  
  if guess in blanks:
    print("You have already guessed this letter")
  for position in range(word_length):
    letter = random_word[position]
    if guess == letter:
      blanks[position] = letter 
  # print(blanks)
  
  if guess not in random_word :
    print(f"You guessed '{guess}' and it is not in the word.You lose a life")
    lives -= 1
    if lives ==0:
      end_of_game = True
      # print("You Lose")
      print(lose)
      
      print(f"The word was {random_word}")
  
  if "_" not in blanks:
    end_of_game = True
    # print("You win")
    print(win)
    
  print(' '.join(blanks))    
  # print(f"{' '.join(blanks)}")
  print(stages[lives])  
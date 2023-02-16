import random


def check_word(correct, incorrect, word, tries):
  guess = input('Guess a letter: ')

  if guess in incorrect or guess in correct:
    print('You already guessed that!')
    
  elif guess in word:
    correct.append(guess)
    print('Nice! The letter is there\n')
  else:
    incorrect.append(guess)
    tries += 1
    print('Uh oh, that was wrong\n')
  return tries
  




def print_word(word,correct):
  progress = ''
  for character in word:
    if character in correct:
      progress = progress + character
    else:
      progress = progress + '_'
  return progress




def print_spider(tries,spiderList):
  spiderList[tries]()
  
    



def generate_word():
  wordList = open('words.txt').read().split()
  word = random.choice(wordList)
  print('Word = ' + '_'*len(word))
  return word


  

def introduction():
  print('Welcome to ArachnoPhonics!\n')
  playerName = input('What is your name? ')
  print(f'\n{playerName}, your goal is to guess the mystery word, letter by letter\n')
  print('\n Each time you guess the wrong letter each body part of a spider will be drawn.')
  print('\n Good Luck playing!')



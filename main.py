import spiderDraw as sd
import functions as md
import time, os


correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True 

spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]


md.introduction()
time.sleep(2)

word = md.generate_word()  



while game: 
  progress = ''
  tries = md.check_word(correct, incorrect,word, tries)
  time.sleep(1)
  os.system('clear')
  progress = md.print_word(word,correct)
  print(f'Word = {progress}')
  md.print_spider(tries,spiderList)
  print(f'Incorrect Guesses = {incorrect}')



  if '_' not in progress:
    print('Congrats, you won!')
    reset = input('Do you want to play again? Enter y or n ')
    if reset =='y' or reset == 'yes':
      os.system('clear')
      correct.clear()
      incorrect.clear()
      tries = 0
      word = md.generate_word() 
    else:
      print('Bye!')
      game = False
  elif tries > 5:
    print('The spider has eaten you!')
    reset = input('Do you want to play again? Enter y or n: ')
    if reset =='y' or reset == 'yes':
      os.system('clear')
      correct.clear()
      incorrect.clear()
      tries = 0
      word = md.generate_word() 
    else:
      print('Bye!')
      game = False
    
  
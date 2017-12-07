# Paste your code into this box
high = 100
low = 0
median = int((high+low)/2)
print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(median)+ '?')
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while guess != 'c':
  if guess == 'h':
    high = median
    median = int((high+low)/2)
  if guess == 'l':
      low = median
      median = int((high + low) / 2)
  if guess != 'h' and guess != 'l':
      print('sorry, I did not understand your input')
  print('Is your secret number ' + str(median)+ '?')
  guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print('Game over. Your secret number was: ' + str(median))

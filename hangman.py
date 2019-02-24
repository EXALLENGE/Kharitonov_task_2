from random import randint

words = {1 : 'python', 2 : 'java', 3 : 'ruby', 4 : 'javascript'}

name = input('Enter your name: ')
word = words[randint(1, 4)]
temp = '*' * len(word)
print('Hello, %s! Welcome to the game "Hangman". You have five attempts to guess the word. Your word is: ' % name)
print(temp)

mistakes = 0
while mistakes < 5:
    letter = input('Guess a letter: ')
    if letter in word:
        print('Hit!')
        for i in range(len(word)):
            if word[i] == letter:
                temp = temp[0: i] + letter + temp[i + 1: len(word) + 1]
        print('The word: %s\n' % temp)
        if '*' not in temp:
            print('You won!')
            break
    else:
        mistakes += 1
        print('Missed, mistake %s out of 5' % mistakes)
        print('The word: %s\n' % temp)
if mistakes == 5:
    print('You lost!')

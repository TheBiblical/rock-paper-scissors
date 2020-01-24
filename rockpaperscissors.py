from random import randint

game = ['rock','paper','scissors']
com = game[randint(0,2)] #return random integer
player = False 

while player == False:
    input(print('Rock, Paper. or Scissors? \n'))
    if player == com:
        print('Same same!')
    elif player == 'rock':
        if com == 'paper':
            print('I win, sucker!')
        elif com == 'scissors':
            print('Lucky')
    elif player == 'paper':
        if com == 'scissors':
            print('I win, sucker!')
        elif com == 'rock':
            print('Lucky')
    elif player == 'scissors':
        if com == 'paper':
            print('I win, sucker!')
        elif com == 'rock':
            print('Lucky')
    player == False #set player to False to continue loop
    


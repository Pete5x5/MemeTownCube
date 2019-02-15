import random   #Enable random number functionality
print('''CUBE RANDOMIZER - SEALED

How many players?''')

while True: #Get number of players to be generated
    players = input()
    try:    #Make sure input is an int
         players = int(players)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if players < 1:  #Can't generate 0 players..
            print('Not enough players')
            continue
        elif players > 8:   #Cap on number of players
            print('That\'s too many players!')
            continue
        else:
            break

numcards = int(768 / players) #Get number of cards per player
print('Each player will get ' + str(numcards) + ' cards.')

cardschosen = [] #set all vars as lists
allcards = []
sealed = []

allcards=[line.strip() for line in open('TheCube.txt')] #Import card list and remove newlines

for v1 in range(players):
    sealedfile = open('sealed' + str(int(v1+1)) + '.txt', 'w')
    for card in range(numcards):
        if len(allcards) == 0:
            break
        else:
            card = allcards[random.randint(0,len(allcards)-1)]
            cardschosen += [card]
            allcards.remove(card)
            sealedfile.write(card + '\n')
        
    sealed.append(cardschosen)
    cardschosen = []
    print(sealed[v1])
    print('')
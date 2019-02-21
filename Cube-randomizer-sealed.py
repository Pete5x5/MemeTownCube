import random   #Enable random number functionality
import datetime #Enable date and time functionality
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
        if players < 2:
            print('Not enough players')
            continue
        elif players > 8:   #Cap on number of players
            print('That\'s too many players!')
            continue
        else:
            break

allcards=[line.strip() for line in open('TheCube.txt')] #Import card list and remove newlines

numcards = int(len(allcards) / players) #Get number of cards per player
print('Each player will get ' + str(numcards) + ' cards.')

cardschosen = [] #set all vars as lists
sealed = []
gendate = (datetime.datetime.now()).strftime('%Y%m%d-%H%M%S') #set the date and time the files are generated

for v1 in range(players): #repeat for each player
    sealedfile = open('sealed' + str(int(v1+1)) + '_' + gendate + '.txt', 'w') #create a new file for each player
    for card in range(numcards):
        card = allcards[random.randint(0,len(allcards)-1)] #pick a random card
        cardschosen += [card] #add the cosen card to it's list
        allcards.remove(card) #remove the chosen card from the card pool
        sealedfile.write(card + '\n') #write the card to it's text file
    sealed.append(cardschosen) #save the generated list in the sealed list
    cardschosen = [] #clear cards chosen
    print(sealed[v1]) #print the list to output
    print('')
import random   #Enable random number functionality
import datetime #Enable date and time functionality
import sys      #Enable system functionality
print('''CUBE RANDOMIZER - SEALED

How many players?''')

badarg = 0 #assume there is a valid command line argument

try: #Check to see if there's a command line argument
    players = int(sys.argv[1])
except (IndexError, ValueError): #if not (or it's not an int)
    badarg = 1 #ignore command line argument

while True: #Get number of players to be generated
    if badarg == 1:
        players = input()
        
    try:    #Make sure input is an int
        players = int(players)
    except ValueError:
        print('Invalid input')
        badarg = 1 #ignore command line argument
        continue
    else:
        if players < 2:
            print('Not enough players')
            badarg = 1 #ignore command line argument
            continue
        elif players > 8:   #Cap on number of players
            print('That\'s too many players!')
            badarg = 1 #ignore command line argument
            continue
        else:
            break

allcards=[line.strip() for line in open('TheCube.txt')] #Import card list and remove newlines

numcards = int(len(allcards) / players) #Get number of cards per player
unusedcards1 = int(len(allcards) - (players * numcards)) #get number of unused cards

print('Each player will get ' + str(numcards) + ' cards.')
print('There will be  ' + str(unusedcards1) + ' cards unused.')

if badarg == 1: #if the generator was not started with a command line argument...
    print('Press any key to start generating')
    input() #wait until the user presses a key to start

cardschosen = [] #set all vars as lists
sealed = []
gendate = (datetime.datetime.now()).strftime('%Y%m%d-%H%M%S') #set the date and time the files are generated

for v1 in range(players): #repeat for each player
    sealedfile = open('sealed' + str(int(v1+1)) + '_' + gendate + '.txt', 'w') #create a new file for each player
    for card in range(numcards):
        card = allcards[random.randint(0,len(allcards)-1)] #pick a random card
        cardschosen += [card] #add the chosen card to it's list
        allcards.remove(card) #remove the chosen card from the card pool
        sealedfile.write(card + '\n') #write the card to it's text file
    sealed.append(cardschosen) #save the generated list in the sealed list
    cardschosen = [] #clear cards chosen
    print(sealed[v1]) #print the list to output
    print('')

unusedcards2 = len(allcards) #get the number of cards remaining that have not been put into a sealed pack

if unusedcards2 > 0:
    sealedfile = open('unused.txt', 'w') #create a new file for the unused cards
    for card in range(unusedcards2):
        card = allcards[0] #take the first unused card
        allcards.remove(card) #remove the chosen card from the card pool
        sealedfile.write(card + '\n') #write the card to the text file
    sealed.append(cardschosen) #save the generated list in the sealed list
    cardschosen = [] #clear cards chosen
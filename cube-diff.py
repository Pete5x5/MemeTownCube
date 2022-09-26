import sys      #Enable system functionality

newCube=[line.strip() for line in open(sys.argv[1])] #Import new cube
oldCube=[line.strip() for line in open(sys.argv[2])] #Import old cube

sameCard = [] # set same cards as list 

for v1 in range(len(newCube)): # for each card in the new cube
    if newCube[v1] in oldCube: # check if it's in the old cube
        sameCard += [newCube[v1]] # if it is, add it to the same card list

for v2 in range(len(sameCard)): # for each same card
    newCube.remove(sameCard[v2]) # remove it from the new cube list
    oldCube.remove(sameCard[v2]) # remove it from the old cube list

def writeFILES(inputCards, outFile):
    for i in range(len(inputCards)): # for each card left in the list
        outFile.write(inputCards[i] + '\n') # write it to file

newFile = open('new.txt', 'w')
writeFILES(newCube, newFile)

oldFile = open('old.txt', 'w')
writeFILES(oldCube, oldFile)

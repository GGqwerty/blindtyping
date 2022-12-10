from random import randint

f = open('EngDictionary.txt')
dict = f.readline()
dict = dict.split(' ')
LEFT_BORDERS = [0,52,104,304,504,704,904,1104,1304,1504]
RIGHT_BORDERS = [51,103,303,503,703,903,1103,1303,1503,1703]

currWord = []
def find_word(currLength):
    while currLength!=0:
        if currLength >= 10:
            i = randint(1,10)-1
        else:
            i = randint(1,currLength)-1
        indexForDict = randint(LEFT_BORDERS[i],RIGHT_BORDERS[i])
        currWord.append(dict[indexForDict])
        currLength-=i+1
    return currWord
#sda
find_word(20)
print(currWord)

# dsadasdAs

print(len(dict))
f.close()
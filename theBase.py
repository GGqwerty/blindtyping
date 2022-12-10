from random import randint


# 1 - это англ, 0 - это русский
language = 1
if language:
    f = open('Dictionary.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 52, 104, 304, 504, 704, 904, 1104, 1304, 1504]
    RIGHT_BORDERS = [51, 103, 303, 503, 703, 903, 1103, 1303, 1503, 1703]
    bool = [0] * 1704
else:
    #   f = open('      Dictionary FOR RUSSIAN   .txt')
    # dict = f.readline()
    # dict = dict.split(' ')
    LEFT_BORDERS = [0,    66,     132,332,532,732,932,1132,1332,1532]
    RIGHT_BORDERS = [65,    131,    331,531,731,931,1131,1331,1531,1731]
    bool = [0] * 1732


currWord = []
def find_word(currLength):
    while currLength!=0:
        if currLength >= 10:
            i = randint(1,10)-1
        else:
            i = randint(1,currLength)-1
        indexForDict = randint(LEFT_BORDERS[i],RIGHT_BORDERS[i])
        if bool[indexForDict]:
            pass
        else:
            currWord.append(dict[indexForDict])
            currLength-=i+1
            bool[indexForDict] = 1
    return currWord

# INSERT THE LENGTH HERE
find_word(20)
print(currWord)
f.close()
from random import randint

print('Please enter the language that you want to test blind testing in:')
print('English: 1')
print('Russian: 0')
print('')
print('Пожалуйста, введите язык, на котором вы хотите опробовать печать вслепую: ')
print('Английский: 1')
print('Русский: 0')
print('')

valid=False
while not valid:
    try:
        language = int(input())
        if language != 1 and language != 0:
            raise ZeroDivisionError
        else:
            valid = True
    except:
        print('Invalid input: try again!')
        print('Неверный ввод: попробуйте снова!')


if language:
    f = open('Dictionary.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 52, 104, 304, 504, 704, 904, 1104, 1304, 1504]
    RIGHT_BORDERS = [51, 103, 303, 503, 703, 903, 1103, 1303, 1503, 1703]
    bool = [0] * 1704
    f.close()
else:
    f = open('DictionaryRUS.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 66, 116, 316, 516, 716, 916, 1116, 1316, 1516]
    RIGHT_BORDERS = [65, 115, 315, 515, 715, 915, 1115, 1315, 1515, 1715]
    bool = [0] * 1716
    f.close()


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

def word_for_length(theLength):
    theLength-=1
    indexForDict = randint(LEFT_BORDERS[theLength],RIGHT_BORDERS[theLength])
    while bool[indexForDict]:
        indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
    oneWord = dict[indexForDict]
    bool[indexForDict] = 1
    return oneWord


# INSERT THE LENGTH HERE
find_word(20)
print(currWord)
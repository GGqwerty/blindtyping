lengthall = 20
chancesOfRandom=[3,9,17,25,33,41,49,57,65,73]           # шансы: 3,6,8,8,8,8,8,8,8,8
from random import randint

print('Please enter the language that you want to test blind testing in:')
print('English: 1')
print('Russian: 0')
print('')
print('Пожалуйста, введите язык, на котором вы хотите опробовать печать вслепую: ')
print('Английский: 1')
print('Русский: 0')
print('')

valid = False
while not valid:
    try:
        language = int(input())
        if (language != 1) and (language != 0):
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
    howMuchElements = 1704
    bool = [0] * howMuchElements
    f.close()
else:
    f = open('DictionaryRUS.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 66, 116, 316, 516, 716, 916, 1116, 1316, 1516]
    RIGHT_BORDERS = [65, 115, 315, 515, 715, 915, 1115, 1315, 1515, 1715]
    howMuchElements = 1716
    bool = [0] * howMuchElements
    f.close()

currWord = []


def clearing(index):
    if bool[LEFT_BORDERS[index]:RIGHT_BORDERS[index] + 1].count(0) == 0:
        for j in range(LEFT_BORDERS[index], RIGHT_BORDERS[index] + 1):
            bool[j] = 0


def find_word(currLength):
    currWord = []
    while currLength != 0:
        if currLength >= 10:
            bufferIndex = randint(1, 73)
            i = 0
            if bufferIndex in range(1, 4):
                pass
            else:
                while i < 9 and bufferIndex > chancesOfRandom[i]:
                    i += 1
            clearing(i)

        else:
            bufferIndex = randint(1, chancesOfRandom[currLength - 1])
            i = 0
            if bufferIndex in range(1, 4):
                pass
            else:
                while i < 9 and bufferIndex > chancesOfRandom[i]:
                    i += 1
            clearing(i)

        indexForDict = randint(LEFT_BORDERS[i], RIGHT_BORDERS[i])
        while dict[indexForDict] == 1:
            indexForDict = randint(LEFT_BORDERS[i], RIGHT_BORDERS[i])
        # if bool[indexForDict]:
        #    pass
        # else:
        currWord.append(dict[indexForDict])
        currLength -= i + 1
        # if indexForDict != 0:          // это старое правило для единиц; отныне единицы чищатся, как и другие
        bool[indexForDict] = 1
    return currWord


def word_for_length(theLength):
    theLength -= 1
    indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
    while bool[indexForDict]:
        indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
    oneWord = dict[indexForDict]
    bool[indexForDict] = 1
    return oneWord


""""""
Flag = False

while lengthall > 0 and lengthall < 120:

    if not (Flag):
        str1 = find_word(lengthall)
    else:
        str1 = strarray
    for i in str1:
        print(i, end=' ')
    print()

    strarray = []
    str2 = input().split(' ')
    flagYbav = True
    Flag = False

    if len(str1) > len(str2):
        Flag = True
        flagYbav = False

    for i in range(len(str1)):
        flagDlinnee = False
        buf = []
        for j in range(len(str1[i])):
            buf.append(1)
        if i > len(str2) - 1:
            for j in range(len(str1[i])):
                buf[j] += 1
                lengthall += 1


        else:
            for j in range(len(str1[i])):
                if j > len(str2[i]) - 1:
                    Flag = True
                    buf[j] += 1
                    lengthall += 1
                    flagYbav = False
                else:
                    if str1[i][j] != str2[i][j]:
                        Flag = True
                        buf[j] += 1
                        lengthall += 1
                        flagYbav = False
            if len(str1[i]) < len(str2[i]):
                flagDlinnee = True
                Flag = True
                flagYbav = False

        s = ''
        k = []
        if Flag:
            for j in range(len(str1[i])):

                for g in range(buf[j]):
                    s = s + str1[i][j]
        else:
            s = str1[i]
        if (len(s) == len(str1[i])) and (not (flagDlinnee)):
            k = find_word(len(str1[i]))
            strarray = strarray + k
        else:
            strarray.append(s)
    print()
    if flagYbav:
        lengthall -= 2

if language:
    if lengthall <= 0:
        print('You are winner sun')
    else:
        print('Unfortunately, you are loser, sun')
else:
    if lengthall <= 0:
        print('Вы победили!')
    else:
        print('К сожалению, вы проиграли!')




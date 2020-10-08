import random
import time

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
0    |
     |
     |
    ===''', '''
+---+
0   |
|   | 
    |
   ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея ' \
        'индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось ' \
        'лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук ' \
        'питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ' \
        'ящерица'.split()

alphabet = 'йцукенгшщзхъэждолрпавыфячсмитьбюё'


def chooseWord():
    wordIndex = random.randint(1, len(words))
    return list(words[wordIndex])


def checkLetter(userLetter, choosenWord, board):
    if userLetter in board:
        print('Такая буква уже есть')
    elif userLetter not in alphabet:
        print('Вы ввели не букву')
    elif userLetter in choosenWord:
        print('Есть такая буква')
        return True
    else:
        print('Такой буквы нет')
        return False


def addLetter(userLetter, choosenWord):
    for index, letter in enumerate(choosenWord):
        if userLetter == letter:
            board[index] = userLetter
    return print(''.join(board))


def endOfGame(yes):
    if yes == 'да':
        return True
    else:
        return False


yes = 'да'
while endOfGame(yes):
    print('Я загадал слово')
    choosenWord = chooseWord()
    board = []
    for i in range(len(choosenWord)):
        board.append('*')
    print(''.join(board))
    i = 0
    missedLetter = []
    while choosenWord != board and i != 6:
        print('Введите букву')
        userLetter = input()
        time.sleep(1)
        if checkLetter(userLetter, choosenWord, board):
            addLetter(userLetter, choosenWord)
            print(HANGMAN_PICS[i])
            print('Этих букв в слове нет: ' + ', '.join(missedLetter))
        else:
            missedLetter.append(userLetter)
            i += 1

            print(''.join(board))
            print(HANGMAN_PICS[i])
            print('Этих букв в слове нет: ' + ', '.join(missedLetter))
        if i == 6:
            print('Вас повесили')
            print('Было загадано слово ' + ''.join(choosenWord))
        if choosenWord == board:
            print('Вы угадали слово')
    yes = input('Сыграем еще раз (да или нет)? ')

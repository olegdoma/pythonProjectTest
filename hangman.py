import random

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
print(len(words))


def chooseWord():
    wordIndex = random.randint(1, len(words))
    return words[wordIndex]


def checkLetter(letter, choosenWord):
    choosenWord = list(choosenWord)
    if letter in choosenWord:
        print('Есть такая буква')
        indexLetter = choosenWord.index(letter)
        starsWord = []
        for i in range(len(choosenWord)):
            starsWord.append('*')
        starsWord[indexLetter] = letter


    else:
        print('Такой буквы нет')



choosenWord = chooseWord()
print(choosenWord)
letter = input()
checkLetter(letter, choosenWord)


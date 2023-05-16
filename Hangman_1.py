import random

wordsEN = ['BOX', 'TIGER', 'APPLE', 'WAGE', 'WAIT', 'WAKE', 'WALK', 'WALL', 'WANDER', 'WANT', 'WAR', 'WARM', 'WARN', 'WARNING', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAVE', 'WAY', 'WE', 'WEAK', 'WEALTH', 'WEALTHY', 'WEAPON', 'WEAR', 'WEATHER', 'WEDDING', 'WEEK', 'WEEKEND', 'WEEKLY', 'WEIGH', 'WEIGHT', 'WELCOME', 'WELFARE', 'WELL', 'WEST', 'WESTERN', 'WET', 'WHAT', 'WHATEVER', 'WHEEL', 'WHEN', 'WHENEVER', 'WHERE', 'WHEREAS', 'WHETHER', 'WHICH', 'WHILE', 'WHISPER', 'WHITE', 'WHO', 'WHOLE', 'WHOM', 'WHOSE', 'WHY', 'WIDE', 'WIDELY', 'WIDESPREAD', 'WIFE', 'WILD', 'WILL', 'WILLING', 'WIN', 'WIND', 'WINDOW', 'WINE', 'WING', 'WINNER', 'WINTER', 'WIPE', 'WIRE', 'WISDOM', 'WISE', 'WISH', 'WITH', 'WITHDRAW', 'WITHIN', 'WITHOUT', 'WITNESS', 'WOMAN', 'WONDER', 'WONDERFUL', 'WOOD', 'WOODEN', 'WORD', 'WORK', 'WORKER', 'WORKING', 'WORKS', 'WORKSHOP', 'WORLD', 'WORRIED', 'WORRY', 'WORTH', 'WOULD', 'WOULD', 'WOUND', 'WRAP', 'WRITE', 'WRITER', 'WRITING', 'WRONG', 'YARD', 'YEAH', 'YEAR', 'YELL', 'YELLOW', 'YES', 'YESTERDAY', 'YET', 'YIELD', 'YOU', 'YOUNG', 'YOUR', 'YOURS', 'YOURSELF', 'YOUTH', 'ZONE']
wordsGR = ["ΠΕΡΟΥΚΑ", "ΛΥΚΟΣ", "ΕΥΘΡΑΥΣΤΟΣ", "ΠΡΟΦΙΛ", "ΠΡΟΣΘΕΤΩ", "ΚΑΤΕΥΝΑΖΩ", "ΣΑΟΥΝΑ", "ΚΟΥΡΕΥΩ", "ΚΑΡΦΙΤΣΑ", "ΕΛΑΧΙΣΤΟΣ", "ΑΥΛΑΙΑ", "ΣΥΓΓΡΑΦΕΑΣ", "ΣΠΙΡΤΟ", "ΤΣΑΙ", "ΚΑΜΠΙΝΑ", "ΠΕΤΡΩΔΗΣ", "ΓΕΝΝΗΤΡΙΑ", "ΚΟΝΤΟΣ", "ΜΑΘΑΙΝΩ", "ΓΥΡΗ", "ΕΝΙΚΟΣ", "ΕΠΙΤΑΧΥΝΣΗ", "ΤΣΕΛΟ", "ΥΠΝΟΣ"]

choosingLanguage = int(input(" 1. Θες να παίξουμε στα Eλληνικά? \n 2. Do you want to play in English? "))

while choosingLanguage != 1 and choosingLanguage != 2:
    choosingLanguage = int(input('Press 1 or 2 '))

if choosingLanguage == 1:
    print('Ας παίξουμε στα Ελληνικά ')
    currentWord = random.choice(wordsGR)
elif choosingLanguage == 2:
    print("Let's play in English")
    currentWord = random.choice(wordsEN)

Length = len(currentWord)

inputString = (Length * "_")

print(inputString)

# print(currentWord)
# print(lenght)

errors = 0
wrong_letters = []

while errors < 5:
    letter = input("letter: ")

    letter = letter.upper()

    if letter not in currentWord:
        errors = errors + 1
        wrong_letters.append(letter)
        print("wrong letter")

    range_obj = range(Length)

    for index in range_obj:
        if currentWord[index] == letter:
            if letter in currentWord:
                inputString = inputString[:index] + letter + inputString[index+1:]
        #        print(inputString)
    else:
                print('  _______')
                print('  |/      |')
                print('  |      ' + (' O' if errors >= 1 else ''))
                print('  |      ' + ('\ /' if errors >= 2 else ''))
                print('  |      ' + (' |' if errors >= 3 else ''))
                print('  |      ' + ('/ \\' if errors >= 4 else ''))
                print('  |')
                print('__|___')
                print()
    print(inputString)
    my_string = ", ".join(wrong_letters)
    print('wrong_letters:', my_string)

    if "_" not in inputString:
        print("You Won!")
        break
    if errors == 5:
        print("You Lost!")
        print("The word was: ", currentWord)






def move(chptr):
    movements = open('movements.txt', 'r')
    chnum = str(chptr)
    for i in movements:  # prints movement options
        if (chnum + 'choicetext') in i:
            print(i[14:-2])
    choice = input('>>> ').capitalize()
    movements.close()
    movements = open('movements.txt', 'r')
    for line in movements:
        if choice in line:
            if (chnum + choice) == line[:-7]:
                x = float(line[-6:-2])
                print('(' + str(x) + ')')
                return x
    print('/!\ Invalid movement /!\ ')
    move(chptr)


move(0.2)

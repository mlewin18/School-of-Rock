class Center:
    def __init__(self, initial):
        print()
        print('Line up the arrows with the right edge of your screen by entering the number of dashes to add.')
        print('Type \"exit\" when you finish.')
        self.spacers = initial
        self.center = open('center.txt', 'w')
        self.indicator_bar()
        self.center.write(str(self.spacers))

    def indicator_bar(self):
        print('-' * self.spacers + '><--')
        print('\n\n\n')
        bump = input('>>> ').capitalize()
        if bump != 'Exit':
            self.spacers += int(bump)
            self.indicator_bar()


def center_finder():
    for i in open('center.txt', 'r'):
        return ((int(i) + 1) // 2)-5


if __name__ == '__main__':
    Center(50)

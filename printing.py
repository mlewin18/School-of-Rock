from screenSetup import *
from time import sleep
import sys
import School_of_rock


speed = 0.04
cent = 105
spd = 0.04


def down(spaces):
    if spaces == 0:
        print('\n'*35)
    else:
        print('\n' * spaces)


def wait(time):
    if School_of_rock.test:
        pass
    else:
        sleep(time)


class Type:
    def __init__(self, string, speed=2, bump=0, header=0, footer=0, oneline=False, lag=0.5):
        center = center_finder()
        if bump == 0:
            self.centerSpaces = center - (len(string) // 2)
        else:
            self.centerSpaces = center+bump
        self.oneline = oneline
        self.speed = self.findsleep(speed)
        self.header(header)
        if School_of_rock.test:
            self.sprint(string, 0)
        else:
            self.sprint(string, lag)
        self.footer(footer)

    def findsleep(self, speed):
        if speed == 0:
            return 0
        elif speed == 1:
            return 0.01
        elif speed == 2:
            return 0.04
        elif speed == 3:
            return 0.07

    def header(self, spacing):
        if self.header != 0:
            print('\n'*spacing)

    def sprint(self, txt, lag):
        wait(lag)
        print(' ' * self.centerSpaces, end='')
        for i in range(len(txt)):
            if i != len(txt):
                print(txt[i], end='')
            else:
                print(txt[i])
            sys.stdout.flush()
            wait(self.speed)

    def footer(self, spacing):
        if spacing > 0:
            print('\n'*(spacing-1))


if __name__ == '__main__':
    text = input('>>> ')
    Type(text)

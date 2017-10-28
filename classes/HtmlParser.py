from classes.ExceptionLog import logg

text = 'Empty'
with open('/Users/Ilya/Desktop/workfile1.txt', mode='r') as file:
    for i, line in enumerate(file):
            print(i, line, sep='', end='')


def printFile():
    print('+++++++++++++\n', text.__str__(), sep='', end='\n+++++++++++++\n')

def printOddLine():
    digits = ''
    for letter in text:
        if letter.isdigit():
            digits+=letter
    return digits

# if __name__ == '__main__':
#     printFile()
    # print(printOddLine())


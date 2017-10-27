from classes.ExceptionLog import logg

text = 'Empty'
try:
    # file = open('/Users/Ilya/Desktop/workfile1.txt', mode='r', encoding='UTF-8')
    file = open('C:\\Users\\bukreyev\\Desktop\\workfile11.txt', mode='r', encoding='UTF-8')
    text = file.read()
    file.close()
except Exception as er1:
    logg(er1)

print('+++++++++++++\n', text.__str__(), sep='', end='\n+++++++++++++\n')

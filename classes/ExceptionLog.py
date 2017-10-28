import datetime


def logg(e):
    f = open('/Users/Ilya/Desktop/log.txt', mode='a', newline='\n')
    # f = open('C:\\Users\\bukreyev\\Desktop\\log.txt', mode='a', newline='\n')
    s = str (datetime.datetime.now()) + str (e)
    f.write(s)
    f.close()

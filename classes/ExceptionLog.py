import datetime
def logg(e):
    f = open('/Users/Ilya/Desktop/log.txt', mode='a',newline='\n')
    s = str(datetime.datetime.now() + e)
    f.write(s)
    f.close()
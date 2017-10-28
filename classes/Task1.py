# 'What do you want to do: write or write an objects?'
# Put in console some people: name, surname, age, salary.
# Save data after each input
# Save it to *.txt file, and try to read from file ''back''.
# Make about 3 classes, e.g. 'worker', 'ceo', 'manager'. Implement the inheritance between them, add some features.
# Realize functionality via web browser

# csv?

# 1
def writeObj(name, surname, age, salary):
    with open('/Users/Ilya/Desktop/workers.txt', 'a') as file:
        s = name+' '+surname+' '+age+' '+salary+'\n'
        file.write(s)

def readObj(line):
    with open('/Users/Ilya/Desktop/workers.txt', 'r') as file:
#        for line, l in enumerate(file):
 #           if l == line:
  #              print(l)

inp1 = input("What do you want to do: write or read an objects?\n")
if inp1 == 'write':
    inpN = input('Type a name\n')
    inpS = input('Type a surname\n')
    inpA = input('Type an age\n')
    inpSl = input('Type a salary\n')
    writeObj(inpN, inpS, inpA, inpSl)
elif inp1 == 'read':
    readObj(1)


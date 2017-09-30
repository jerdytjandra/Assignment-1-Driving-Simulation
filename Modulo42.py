def Modulo42():

    b = 42
    a = []

    for i in range(0,10):
        inserted_number = int(input('Please enter a number:'))
        modul  = int(inserted_number%b) #%= module = the remainder of a division
        a.append(modul)

    r = len(set(a))
    print('\n' + str(r)) #the distinct value

Modulo42()

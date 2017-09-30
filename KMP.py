def KMP():
    name = input('Please enter a name:').split('-') #input name of a person
    data = []

    for i in name:
        data.append(i[0])          #append = to include the name in the data
    print(('').join(data).upper()) #upper = capitalize the letter
KMP()

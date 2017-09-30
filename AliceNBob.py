def AliceNBob():

    number_of_stones = int(input('Please insert the number of stone:'))

    if (number_of_stones%2 == 1):
        print('\nAlice will win.')
    else:
        print('\nBob will win.')

AliceNBob()
#if number of stone left = odd  = Alice wins
#if .................... = even =   Bob wins

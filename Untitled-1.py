# Fizz Buzz Deluxe

def main():
    # TODO (1): output program title

    print '== Fizz Buzz Deluxe =='
    # print('== Fizz Buzz Deluxe ==')

    # TODO (2): input (and validate) a pair of words

    print 'Enter two words (each from 3-6 chars long):'
    # print('Enter two words (each from 3-6 chars long):')
    word1 = raw_input('Word1 :')
    print word1
    while not(3 <= len(word1) <= 6):
        word1 = raw_input('  Word ONE: ')

    word2 = raw_input('  Word TWO: ')
    while not(3 <= len(word2) <= 6):
        word2 = raw_input('  Word TWO: ')
        
    # TODO (3): input (and validate) a pair of divisors
    
    print 'Enter two different integers (between 2 and 15):'
    # print('Enter two different integers (between 2 and 15):')
    div1 = int(input('  Divisor ONE: '))
    while not(2 <= div1 <= 15):
        div1 = int(input('  Divisor ONE: '))
    div2 = int(input('  Divisor TWO: '))
    while not(2 <= div2 <= 15):
        div2 = int(input('  Divisor TWO: '))
    if div2 == div1:
        div2 = int(input('  Divisor TWO: '))
    print
    # print()
    print word1, word2, 'with', div1, 'and', div2, '...'
    # print(word1, word2, 'with', div1, 'and', div2, '...')
    print
    # print()
             
    # TODO (4): Output "fizz buzz" sequence from 1 to 100

    for i in range(1,101):
        if (i % div1 == 0) and (i % div2 == 0):
            print'', word1 + word2,
            # print('', word1 + word2, end='')
        elif (i % div1 == 0):
            print '', word1,
            # print('', word1, end='')
        elif (i % div2 == 0):
            print '', word2,
            # print('', word2, end='')
        else:
            print '', i,
            # print('', i, end='')
        if (i == 10) or (i == 20) or (i == 30) or (i == 40) or (i == 50) or (i == 60) or (i == 70) or (i == 80) or (i == 90):
            print
            # print('\n', end='')

    # TODO (5): Output "fizz buzz" symbol map
    print
    # print('\n')
    for i in range(1,101):
        if (i % div1 == 0) and (i % div2 == 0):
            print '', '#',
            # print('', '#', end='')
        elif (i % div1 == 0):
            print '', '+',
            # print('', '+', end='')
        elif (i % div2 == 0):
            print '', '*',
            # print('', '*', end='')
        else:
            print '', '.',
            # print('', '.', end='')
        # if (i == 10) or (i == 20) or (i == 30) or (i == 40) or (i == 50) or (i == 60) or (i == 70) or (i == 80) or (i == 90) or (i == 100):
        if (i%10 == 0):
            print
            # print('\n', end='')

if __name__ == '__main__':
    main()

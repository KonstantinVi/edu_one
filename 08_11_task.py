''' Chapter 8
Programming exercises №11
Программа для расстановки пробелов
'''


def main():
    '''The main function of the module.'''

    try:

        one_letter = input('Введите предложение: ')
        two_letter = one_letter[0]

        for i in range(1, len(one_letter)):
            if one_letter[i].isupper():
                two_letter += f' {one_letter[i].lower()}'
            else:
                two_letter += one_letter[i]

        print(two_letter)


    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

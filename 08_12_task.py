''' Chapter 8
Programming exercises №12
Программа для представления молодёжного сленга
'''


def main():
    '''The main function of the module.'''

    try:

        one_letter = input('Введите словосочетание: ')
        one_letter = one_letter.split()
        two_letter = []

        for i in one_letter:
            two_letter.append(f'{i[1:]}{i[:1]}КИ')

        print(*two_letter)

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

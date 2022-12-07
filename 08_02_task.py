''' Chapter 8
Programming exercises №02
'''


def main():
    '''The main function of the module.'''

    try:

        number = input('Введите число: ')
        sum_a = 0

        for i in number:
            sum_a += int(i)

        print(sum_a)

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

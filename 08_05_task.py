''' Chapter 8
Programming exercises №05
'''


def main():
    '''The main function of the module.'''

    try:

        user_line = input('Введите номер телефона в формате XXX-XXX-XXXXX: ')
        user_line = user_line.upper()

        dict_tel = {'A': 2, 'B': 2, 'C': 2,
                    'D': 3, 'E': 3, 'F': 3,
                    'G': 4, 'H': 4, 'I': 4,
                    'J': 5, 'K': 5, 'L': 5,
                    'M': 6, 'N': 6, 'O': 6,
                    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
                    'T': 8, 'U': 8, 'V': 8,
                    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
                    }

        out_line = ''

        for i in user_line:
            if i in dict_tel:
                out_line += str(dict_tel[i])
            else:
                out_line += i

        print(out_line)

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

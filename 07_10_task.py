''' Chapter 7
Programming exercises №10
'''


def main():
    '''The main function of the module.'''

    try:

        name = input('Введите имя команды: ')
        file_open = open(r'D:\Python\Work_01\edu_one\WorldSeriesWinners.txt',
                         'r')

        str_file = file_open.readline()
        counter = 0
        counter_year = 1903

        while str_file != '':
            str_file = str_file.rstrip('\n')
            if counter_year != 1904 and counter_year != 1994:
                if name == str_file:
                    counter += 1
            else:
                counter_year += 1
                continue
            counter_year += 1
            str_file = file_open.readline()

        file_open.close()
        print(counter)

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

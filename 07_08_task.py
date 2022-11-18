''' Chapter 7
Programming exercises №8
'''


def main():
    '''The main function of the module.'''

    try:

        def name_list(name, floor):
            '''Convert file data to sheet.'''

            if floor == 'M':
                incoming_file = 'D:\Python\Work_01\edu_one\BoyNames.txt'
            elif floor == 'W':
                incoming_file = 'D:\Python\Work_01\edu_one\GirlNames.txt'

            list_file = open(rf'{incoming_file}', 'r')
            one_line = list_file.readline()
            line = one_line.rstrip('\n')
            a_mass = []

            while one_line != '':
                a_mass.append(line)
                one_line = list_file.readline()
                line = one_line.rstrip('\n')

            list_file.close()

            if name in a_mass:
                flag = True
            else:
                flag = False

            return flag

        name, floor = map(str, input(
            'Enter name and gender separated by a space ').split())

        if name_list(name, floor):
            print('This name is popular.')
        else:
            print('This name is not popular.')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

''' Chapter 7
Programming exercises №9
'''


def main():
    '''The main function of the module.'''

    try:

        def number_list():
            '''Convert file data to sheet.'''

            # File upload
            list_file = open(rf'D:\Python\Work_01\edu_one\USPopulation.txt',
                             'r')
            one_line = list_file.readline()
            line = one_line.rstrip('\n')
            a_mass = []

            while one_line != '':
                a_mass.append(int(line))
                one_line = list_file.readline()
                line = one_line.rstrip('\n')

            # Closing a file
            list_file.close()

            return a_mass

        def math_file():
            '''Mathematical calculation.'''

            a_mass = number_list()
            a_average = int(sum(a_mass) / len(a_mass))

            one_min = a_mass[0]
            one_max = 0
            year_max = a_mass[0]
            year_min = 0

            for i in range(1, len(a_mass)):
                if abs(a_mass[i - 1] - a_mass[i]) > one_max:
                    one_max = abs(a_mass[i - 1] - a_mass[i])
                    year_max = i + 1951
                elif abs(a_mass[i - 1] - a_mass[i]) < one_min:
                    one_min = abs(a_mass[i - 1] - a_mass[i])
                    year_min = i + 1951

            print(f'Average annual population: {a_average}')
            print(f'Year with the highest population: {year_max}')
            print(f'Year with lowest population: {year_min}')

        math_file()

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

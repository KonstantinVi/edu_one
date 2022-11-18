''' Chapter 7
Programming exercises №7
'''


def main():
    '''The main function of the module.'''
    a_mass = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C',
              'A', 'D', 'C', 'B', 'B', 'D', 'A']

    try:
        def read_file():
            '''Reading a file and writing it to a list.'''
            file_one = open(r'D:\Python\Work_01\edu_one\student_solution.txt',
                            'r')
            line_file = file_one.readline()
            b_mass = []
            while line_file != '':
                line_file = line_file.rstrip('\n')
                b_mass.append(line_file)
                line_file = file_one.readline()
            file_one.close()
            return b_mass

        def getting_test_result():
            flag = True
            b_mass = read_file()
            if b_mass != 0 and len(a_mass) == len(b_mass):
                for i in range(len(a_mass)):
                    if a_mass[i] != b_mass[i]:
                        flag = False
                        break
            return flag

        if getting_test_result():
            print('Success!')
        else:
            print('Not success!')


    except IOError:
        print('File not found')
    except IndexError:
        print('Indexing error')
    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()

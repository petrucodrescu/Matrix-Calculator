def menu() -> int:
    print('Welcome to Matrix Calculator V1')
    print('Please Choose From Below:')
    print('-------------------------')
    choice = 0
    while choice not in [1,2,3]:
        print('1) Addition')
        print('2) Multiplication')
        print('3) Strassen Algorithm')
        choice = int(input('Enter your choice: '))
        if choice not in [1,2,3]:
            print('Invalid Choice, try again')
    return choice
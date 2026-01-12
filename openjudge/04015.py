while True:
    try:
        data = input().strip()
        if data.count('@') != 1 or data[0] == '@' or data[0] == '.' or data[-1] == '@' or data[-1] == '.':
            print('NO')
            continue
        index = data.find('@')
        if data[index-1] == '.' or data[index+1] == '.':
            print('NO')
            continue
        if '.' not in data[index+1:]:
            print('NO')
            continue
        print('YES')

    except EOFError:
        break

def main():
    m = int(input())
    dic = {}
    cnt_dic = {}
    sum_dic = {}
    for i in range(m):
        data = input().split(',')
        if data[0] not in dic:
            dic[data[0]] = {}
            cnt_dic[data[0]] = 0
            sum_dic[data[0]] = 0
        if data[1] not in dic[data[0]]:
            dic[data[0]][data[1]] = False
        sum_dic[data[0]] += 1
        if data[2] == 'yes':
            if not dic[data[0]][data[1]]:
                cnt_dic[data[0]] += 1
            dic[data[0]][data[1]] = True

    name = list(dic.keys())
    name.sort(key=lambda x: (-cnt_dic[x], sum_dic[x],x))
    for i in range(12):
        if i+1 <= len(name):
            print(f'{i+1} {name[i]} {cnt_dic[name[i]]} {sum_dic[name[i]]}')

if __name__ == '__main__':
    main()
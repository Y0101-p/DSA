def check(ord_num:int,heavy:bool)->bool:
    if heavy:
        for alist in l:
            if chr(ord_num+65) in alist[0]:
                if alist[-1]!='up':
                    return False
            elif chr(ord_num+65) in alist[1]:
                if alist[-1]!='down':
                    return False
            else:
                if alist[-1]!='even':
                    return False
        return True
    else:
        for alist in l:
            if chr(ord_num+65) in alist[0]:
                if alist[-1]!='down':
                    return False
            elif chr(ord_num+65) in alist[1]:
                if alist[-1]!='up':
                    return False
            else:
                if alist[-1]!='even':
                    return False
        return True
n=int(input())
for i in range(n):
    l=[]
    for j in range(3):
        l.append(input().split())
    for j in range(12):
        if check(j,heavy=True):
            print(f'{chr(j+65)} is the counterfeit coin and it is heavy.')
            break
        if check(j,heavy=False):
            print(f'{chr(j+65)} is the counterfeit coin and it is light.')
            break
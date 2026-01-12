def quicksort(list1):
    if len(list1)<2:
        return list1
    else:
        basic=list1[0]
        lower=[]
        upper=[]
        for i in list1[1:]:
            if i <=basic:
                lower.append(i)
            else:
                upper.append(i)
        return quicksort(lower)+[basic]+quicksort(upper)

i=list(map(int,input().split()))
print(quicksort(i))
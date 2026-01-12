def find_max(num_list):
    cur_max = num_list[0]
    max_num = num_list[0]
    for i in range(1,len(num_list)):
        cur_max = max(cur_max+num_list[i], num_list[i])
        max_num=max(max_num,cur_max)
    return max_num

def begin_find(matrix):
    total_max =find_max(matrix[0])
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            num_list=[0]*len(matrix)
            for k in range(len(matrix)):
                num_list[k]=matrix[j][k]-matrix[i][k]
            total_max=max(total_max,find_max(num_list))
    return total_max
n=int(input())
data=[]
while True:
    try:
        data.extend(map(int,input().split()))
    except EOFError:
        break
matrix=[[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j]=data[i*n+j]
        if i>0:
            matrix[i][j]+=matrix[i-1][j]
print(begin_find(matrix))
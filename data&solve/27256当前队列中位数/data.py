import random
import os

random.seed(121969)

for i in range(1, 19):
    n = random.randint(2, 10 ** (i // 5 + 1) // 4)
    f = open(f'data/{i}.in', 'w')
    f.write(str(int(n * 4)) + '\n')
    for step in range(n):
        # 2:1:1
        f.write(f"add {random.randint(0, 10000)}\n")
        f.write(f"add {random.randint(0, 10000)}\n")
        f.write('query\n')
        f.write("del\n")

    f.close()
    os.system(f"python3 solve.py <data/{i}.in >data/{i}.out")

i = 19
n = 20000
f = open(f'data/{i}.in', 'w')
f.write(str(int(n * 5)) + '\n')
for step in range(n):
    f.write(f"add {step * 3 + 2}\n")
    f.write(f"add {step * 3}\n")
    f.write(f"add {step * 3 - 2}\n")
    f.write('query\n')
    f.write("del\n")

f.close()
os.system(f"python3 solve.py <data/{i}.in >data/{i}.out")

i = 20
n = 20000
f = open(f'data/{i}.in', 'w')
f.write(str(int(n * 5)) + '\n')
for step in range(n):
    f.write(f"add {random.randint(0, 100000)}\n")
    f.write(f"add {random.randint(0, 100000)}\n")
    f.write(f"add {random.randint(0, 100000)}\n")
    f.write('query\n')
    f.write("del\n")

f.close()
os.system(f"python3 solve.py <data/{i}.in >data/{i}.out")
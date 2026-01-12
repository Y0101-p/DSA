class Bit:
    def __init__(self, arr):
        self.n = len(arr)
        self.bits = [0 for i in range(self.n+1)]
        for i in range(self.n):
            self.bit_update(i+1, arr[i])

    def bit_sum(self, i):
        s = 0
        while i > 0:
            s += self.bits[i]
            i -= i & -i
        return s

    def bit_update(self, i, v):
        while i<=self.n:
            self.bits[i] += v
            i += i & -i


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
BIT=Bit(arr)
print(f'BIT: ', *BIT.bits)
print("Sum of elements in arr[0..5] is " + str(BIT.bit_sum(5)))
arr[3] += 6
BIT.bit_update(3, 6)
print(f'BIT: ', *BIT.bits)
print("Sum of elements in arr[0..5]" +
" after update is " + str(BIT.bit_sum(5)))

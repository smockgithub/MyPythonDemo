#尾递归 可能会溢出
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(50))

#尾递归 --需要编译器支持，否则还是溢出

L=list(range(100))
print(L)

print(L[-10:-1])

print(L[0:50:2])#取0开始到49，每2个取一个
print(L[::2])#取所有，每2个取一个
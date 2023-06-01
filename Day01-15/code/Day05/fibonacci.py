"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
a= 0
b= 1
print(b,end=' ')
for i in range(19):
    c = a + b
    print(c,end=' ')
    a = b
    b = c
print('\n')


a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

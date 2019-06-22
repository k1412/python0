# -*- coding: UTF-8 -*-

#输出指定个数的斐波那契数列

def fibGenerate(num):
    fib = 0
    if num == 1:
        fib = 0
    if num == 2:
        fib = 1
    if num >= 3:
        fib = fibGenerate(num-1) + fibGenerate(num-2)
    return fib

def fib(num):
    l = []
    for i in range(0,num):
        l.append(fibGenerate(i+1))
    return l

number = int(raw_input("指定斐波那契数列个数：\n"))
print fib(number)






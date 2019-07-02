# -*- coding: UTF-8 -*-

def fibGenerate(num):
    '返回斐波那契数列第n个数字'
    fib = 0
    if num == 1:
        fib = 0
    if num == 2:
        fib = 1
    if num >= 3:
        fib = fibGenerate(num-1) + fibGenerate(num-2)
    return fib

def fib():
    """
    要求输入“指定斐波那契数列个数”，返回相应个数的斐波那契数列，数据的格式为一个列表
    """
    num = int(raw_input("指定斐波那契数列个数：\n"))
    l = []
    for i in range(0,num):
        l.append(fibGenerate(i+1))
    return l

print fib.__doc__;print fibGenerate.__doc__
print help(fibGenerate)
print help(fib)

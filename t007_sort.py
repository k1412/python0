# -*- coding: UTF-8 -*-
#归并排序以及自然合并排序
"""
主要的合并算法：
对原数组进行扫描 得到自然（两两顺序对）顺序对
列如分成 5组 需要插入4个点（存储4个位置）
单数个组时，前面偶数组先归并，最后一个放置
或者先消除奇数组，先前两个进行归并一次
进行归并操作后对原来数组的修改
"""

l = [2,4,1,3,3,7,9,5,6,3,2,5,6,7]  #一共14个数字

position = [4,6,8,9,13]  #组数为个数加一 一共7组
position = [2,7,9,10]  #组数为个数加一 一共5组

def merge(left,middle,right):  #归并发生在相邻的组之间
    leftNum = middle - left
    rightNum = right - middle
    flagLength = 0 #默认左边比右边长
    templ = []
    if leftNum>rightNum:
        maxNum = leftNum
        minNum = rightNum
    else:
        maxNum = rightNum
        minNum = leftNum
        flagLength = 1
    for idx in range(0,minNum):
        if l[left+idx]>l[middle+idx]:
            templ.append(l[middle+idx])
            templ.append(l[left+idx])
        else:
            templ.append(l[left+idx])
            templ.append(l[middle+idx])
    if flagLength == 0:
        for i in range(minNum,maxNum):
            templ.append(l[left+i])
    else:
        for i in range(minNum,maxNum):
            templ.append(l[right+i])
    for j in range(0,maxNum):
        l[left+j] = templ[j]
    return templ

# def mergelist(position):
#     length = len(l)
#     posLength = len(position) + 1
#     if posLength%2 != 0:
#         merge(position[-2],position[-1],length-1)
#         del position[-1]
#         posLength = len(position) + 1
#     while(len(position) != 1):
#         for i in range(0,posLength-1,2):
                                                                                          
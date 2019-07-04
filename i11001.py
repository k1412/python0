import sys
import fileinput
#文件IO的系列操作：
"""
1、文件的打开关闭
2、文件的整体读取以及按行读取
3、文件的迭代读取
"""

#文件的打开关闭，使用不同的属性,按行读取
f_a = open('a.txt','r+',1)
str1 = f_a.readlines()
print str1[2]
f_a.close()

#文件的按字节循环读取
f_b = open('a.txt')
f_list = ['a','b']
f_list2 = []
f_list3 = []
f_list4 = []
while True:
    char = f_b.read(1)
    if not char:break
    f_list.insert(0,str(char))
f_b.close()
print f_list

#文件的按行循环读取
f_c = open('a.txt')
while True:
    line = f_c.readline()
    if not line:break
    f_list2.insert(0,line)
f_c.close()
print f_list2

#文件迭代进行----fileinput 进行懒惰行迭代
for line in fileinput.input('a.txt'):
    f_list3.insert(0,line)
print f_list3

#文件用本身进行行迭代
for line in open('a.txt'):
    f_list4.insert(0,line)
print f_list4

#文件的随机访问----文件的定位
#tell()方法告诉你文件内的当前位置
#seek(offset[,from])方法改变当前文件的位置, from 为0 开头，1，当前位置为参考位置，2，该文件的末尾将作为参考位置

fo = open('a.txt','r+')
str2 = fo.read(10)
print "读取的字符串是：",str2

#查找当前位置
position = fo.tell()
print "当前文件位置：",position
#把指针再次重新定位到文件开头
position = fo.seek(0,0)
str2 = fo.read(50)
print "重新读取字符串：",str2
#关闭打开的文件
fo.close()

#文件的写

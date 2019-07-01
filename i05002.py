from math import sqrt

for n in range(99, 80, -1):
    root = sqrt(n)

    if root == int(root):
        print n
        print "we find it!"
        break
else:
    print "Don't find it!"

print [x*x for x in range(1,10)]

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold','bob']

combine_list = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]

print combine_list

#利用字典的键值对进行匹配的方法
letter_girl = {}
combine_list2 = []

for girl in girls:
    letter_girl.setdefault(girl[0],girl)

combine_list2  = [b+"+"+letter_girl[b[0]] for b in boys]
print combine_list2

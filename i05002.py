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
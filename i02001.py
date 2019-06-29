die_1 = int(raw_input('die_1:\n'))
die_2 = int(raw_input('die_2:\n'))

dice = die_1 + die_2

if dice in (2,3,12):
    print 'win'
elif dice in(7,11):
    print 'loss'
elif dice in(5,6,8,9,10):
    print 'point'
else:
    raise Exception('Design Problem Here: not all conditions accounted for')


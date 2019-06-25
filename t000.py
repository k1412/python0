

position = [2,7,9,10]

l = len(position)
print l

if l!=4:
    print"no"
else:
    print"yes"

del(position[-1])

l = len(position)
print position
print l
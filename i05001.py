names = ['anne','beth','george','damon']
ages = [12,45,32,102]

for name,age in zip(names,ages):
    print name, 'is', age, 'year old'

#一个字符串列表中更替所有包含‘xxx'的子字符串

str1 = 'This is a island'
str2 = str1.replace('is','zazz')

print str2
print 'This is a island'.replace('is','az')



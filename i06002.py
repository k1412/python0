#字典创建子字典的方法：
s = {}
s['first'] = {}
s['middle'] = {}
s['last'] = {}
me = "Magnus Lie Hetland"
my_sister = "Anne Lie Hetland"
s['first']['Magnus'] = [me]
s['middle']['Lie'] = [me]
s['last']['Hetland'] = [me]

s['first'].setdefault('Anne',[]).append(my_sister)
s['middle'].setdefault('Lie',[]).append(my_sister)
s['last'].setdefault('Hetland',[]).append(my_sister)
print s
print s['middle']['Lie']

#字典创建子字典的方法：
# s = {}
# s['first'] = {}
# s['middle'] = {}
# s['last'] = {}
# me = "Magnus Lie Hetland"
# my_sister = "Anne Lie Hetland"
# s['first']['Magnus'] = [me]
# s['middle']['Lie'] = [me]
# s['last']['Hetland'] = [me]

# s['first'].setdefault('Anne',[]).append(my_sister)
# s['middle'].setdefault('Lie',[]).append(my_sister)
# s['last'].setdefault('Hetland',[]).append(my_sister)
# print s
# print s['middle']['Lie']

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = []
def lookup(data,label,name):
    return data[label].get(name)
def store(data,full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,names)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

Mynames = {}
init(Mynames)
store(Mynames,'Magnus Lie Hetland')
lookup(Mynames,'middle','Lie')
store(Mynames,'Robin Hood')
store(Mynames,'Mr. Gumby')

lookup(Mynames,'first','Robin')
lookup(Mynames,'middle','')

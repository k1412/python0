#测试‘exec’以及‘eval’两个函数

#特定条件下执行某段代码，执行用户代码，在各自的命名空间执行代码


#在特定条件下执行代码

str_code1 = ""
nameSpace_typeA = {}
hasChagedFlog = 0
systemValue1 = 1412
systemValue2 = 1212
systemValue3 = 1122
exec 'systemValue1=0' in nameSpace_typeA
exec 'systemValue2=0' in nameSpace_typeA
exec 'systemValue3=0' in nameSpace_typeA
exec 'resultValue=0' in nameSpace_typeA
password = 1510
input_password = int(raw_input('please enter the password:\n'))
for try_count in range(10):
    if input_password == password:
        print 'successful vaildation!!'
        #hasChagedFlog=1
        str_code1 = str(raw_input('Enter the command you want to execute:\n'))
        exec str_code1 in nameSpace_typeA
        #eval str_code1
        break
    input_password = int(raw_input('please enter the password again:\n'))
else:
    print 'password entered too many times, please try later!!!'


if hasChagedFlog == 0:
    resultValue = systemValue1+systemValue2+systemValue3

print 'the result of run is:',resultValue
print 'the result of run in nameSpace_typeA is:',nameSpace_typeA['resultValue']


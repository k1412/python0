from fractions import Fraction

my_data = ('Rice',Fraction('1/4'),'cups')
one_tuple = ('item')
a = len(one_tuple)
print a 
print my_data[1]


ingredient, amount, unit = my_data

print  ingredient,amount, unit
print (ingredient,amount, unit)

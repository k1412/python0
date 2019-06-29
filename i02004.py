position = -1
sample_2 = "name_only"
for position in range(len(sample_2)):
    if sample_2[position] in "=:":
        break
if position == -1:
    print ('name=', None, 'value=', None)
elif not(sample_2[position] in "=:"):
    print ('name=', sample_2, 'value=', None)
else:
    print('name=', sample_2[:position],
         'value=', sample_2[position+1:])
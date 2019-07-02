sample_2 = "name_only"


if len(sample_2) > 0:
    name, value= sample_2, None
else:
    name, value = None,None

for position in range(len(sample_2)):
    if sample_2[position] in "=:":
        name, value = sample_2[:position], sample_2[position:]       
print('name=', name,.
    'value=', value)
    
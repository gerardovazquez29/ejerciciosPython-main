
ids = ['X12','M45','Z10']

ids_a = ['0' + value for  value in ids]
print(ids_a)

ids_b = []
for value in ids:
    new_value = '1' + value 
    ids_b.append(new_value)
print(ids_b)

"""
['0X12', '0M45', '0Z10']
['1X12', '1M45', '1Z10']
"""
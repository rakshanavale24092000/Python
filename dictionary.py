#dictioneries are unordered and mutable

d = {'k1':100, 'k2':50 , 'k3':200, 'k4':80, 'k5':600}
#d.values() gives the values, d.keys() gives keys, d.items() gives both key value pairs

values = d.values()
print(f'the values are {values}')
#output->the values are dict_values([100, 50, 200, 80, 600])

list_values = list(values)

#ascending order
print(f'the values sorted in ascending order are {sorted(list_values)}')
#output-> the values sorted in ascending order are [50, 80, 100, 200, 600]

#if 'reverse' is not assigned to True then by default the list is sorted in ascending order

#descending order
print(f'the values sorted in descending order are {sorted(list_values,reverse=True)}')
#output->the values sorted in descending order are [600, 200, 100, 80, 50]




# Make the keys and the values reversed.
d = {'a':1, 'b':2, 'c':3}
flipped_d = { value : key for key, value in d.items() } 
print(flipped_d)
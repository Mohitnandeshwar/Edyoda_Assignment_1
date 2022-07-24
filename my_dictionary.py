# Create the dictionary
my_dict = {}
 
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i
 
print(my_dict)
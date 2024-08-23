#Creating dictionary
Dict = dict([(1,'Rahul'), (2,'Rohit'), (3,'raj'), (4,'kavita'), (5,'ramesh')])
print("Dictionary with each item as a pair:",Dict) #printing dictionary

#adding element in dictionary
Dict[6] = 'Nitya'
print("\n Dictionary with new item added:",Dict)

#updating values in dictionary
Dict[3] = 'Navdisha'
print("\n Dictionary with updated values:",Dict)

print("\n Accessing one value in Dictionary:",Dict[1])

#deleting value from drictionary
del Dict[6]
print("\n Delete a value from a Dictionary:",Dict)

#creating a nested dictionary
Dict1 = {1: 'Rahul', 2: 'Rohit',
        3:{'Age' : 18, 'Branch' : 'CSE', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])

#printing keys present in the dictionary
# Define the dictionary
my_dict = dict([(1, 'Rahul'), (2, 'Rohit'), (3, 'Raj'), (4, 'Kavita'), (5, 'Ramesh')])

# Print the keys of the dictionary
print("Keys in the dictionary:")

for key in my_dict.keys():
    print(key)

# Delete a value from a dictionary
# Define the dictionary
my_dict = {1: 'Rahul', 2: 'Rohit', 3: 'Raj', 4: 'Kavita', 5: 'Ramesh'}

# Key to delete
key_to_delete = 3

# Delete the key-value pair using pop()
if key_to_delete in my_dict:
    removed_value = my_dict.pop(key_to_delete)
    print(f"Deleted key {key_to_delete} with value '{removed_value}'.")
else:
    print(f"Key {key_to_delete} not found.")

# Print the updated dictionary
print("Updated dictionary:", my_dict)


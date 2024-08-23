# Write a method to remove duplicate elements from an array.

#Initialize array
arr = [12,21,33,12,44,55]
finalarr = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)
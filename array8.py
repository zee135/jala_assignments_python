# Write a function to find the minimum and maximum value of an array.

#Initialize array
arr = [20,300,400,366,48,78,81]

#minimum value of array
minposition = arr.index(min(arr))
print ("The minimum is at position:", minposition)

#maximum value of array
maxposition = arr.index(max(arr))
print ("The maximum is at position::", maxposition)
# Write a method to find number of even number and odd numbers in an array.

#Initialize array
arr = [1,2,3,4,5,6,7,8,9]
evennumbers = 0
oddnumbers = 0
#using loop to find even and odd numbers in array
for i in arr:
    if i % 2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)
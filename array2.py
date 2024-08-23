# Write a function to calculate the average value of an array of integers.

def cal_average(num):
    sum_num = 0
    #Loop through the array to average value of elements
    for i in num:
        sum_num = sum_num + i

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average([10,21,32,43,54]))



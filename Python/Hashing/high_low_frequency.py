#here I am calculating the highest and the lowest frequent element from a given array

def calculate(array):
    n = len(array)
    highest_count = -1
    lowest_count = float('inf')
    print(lowest_count)
    highest_item = None
    lowest_item = None

    mt = {}

    for i in range(n):
        if array[i] in mt:
            mt[array[i]] += 1
        else:
            mt[array[i]] = 1

    
    for key,value in mt.items():
        if value > highest_count:
            highest_item = key
            highest_count = value
        
        if value < lowest_count:
            lowest_item = key
            lowest_count = value

    return highest_item,highest_count,lowest_item,lowest_count

array = [1,2,5,1,4,1,4,1,8,1,9,9,6,5]
highest_item, highest_count, lowest_item, lowest_count = calculate(array)
print(f"Highest Frequency : {highest_item} - {highest_count} \n Lowest Frequency : {lowest_item} - {lowest_count} ")
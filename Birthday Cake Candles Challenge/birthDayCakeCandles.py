
    ####### SOLUTION CODE ########

def birthdayCakeCandles(candles):
    ## initializing an integer to hold the value of the highest value
    highest = 0
    ## count of highest to calculate how many the highest value is found in the array
    count_of_highest = 0

    ## iterate over the array to determine the highest value
    for i in candles:
        if i > highest:
            highest = i
    ## iterate over the array to determine how many time the highest value occurs
    for i in candles:
        if i == highest:
            count_of_highest += 1

    ## Returning the number of times the highest value is found in the array
    return count_of_highest



## Simple Test
print(birthdayCakeCandles([2, 4, 6, 6]))


"""
OUTPUT:
2
## as the highest number is 6 and it occurs two times in the array
"""

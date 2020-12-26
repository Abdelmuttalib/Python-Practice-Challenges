## CHALLENGE QUESTION
"""
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .

Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):

int candles[n]: the candle heights
Returns

int: the number of candles that are tallest
Input Format

The first line contains a single integer, n, the size of candles.
The second line contains n space-separated integers, where each integer  describes the height of candles[i].

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2

Explanation 0

Candle heights are [3, 2, 1, 3]. The tallest candles are 3 units, and there are  of them.
"""

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

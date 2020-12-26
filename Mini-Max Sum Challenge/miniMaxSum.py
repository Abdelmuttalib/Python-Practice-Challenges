## CHALLENGE QUESTION
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:

Sum everything except 1, the sum is 2 + 3 + 4 + 5 = 14.
Sum everything except 2, the sum is 1 + 3 + 4 + 5 = 13.
Sum everything except 3, the sum is 1 + 2 + 4 + 5 = 12.
Sum everything except 4, the sum is 1 + 2 + 3 + 5 = 11.
Sum everything except 5, the sum is 1 + 2 + 3 + 4 = 10.
Hints: Beware of integer overflow! Use 64-bit Integer.
"""

     ######## SOLUTION CODE ########

def miniMaxSum(arr):
    ## Calculating all possibilites to then find the Minimum & Maximum out of all
    first = arr[1] + arr[2] + arr[3] + arr[4]
    second = arr[0] + arr[2] + arr[3] + arr[4]
    third = arr[0] + arr[1] + arr[3] + arr[4]
    four = arr[0] + arr[1] + arr[2] + arr[4]
    five = arr[0] + arr[1] + arr[2] + arr[3]
    ## Create array of calculated possibilites to easily iterate and find the Minimum & Maximum
    calculated_arr = [first, second, third, four, five]
    ## initializing the Maximum & Minimum to compare it to elements of the calculated array
    max = first
    min = first
    ## iterate throw the calculated possibilites array and determine the Minimum & Maximum
    for i in calculated_arr:
        if i > max:
            max = i
        elif i < min:
            min = i
    ## printing the final result of the Minimum & Maximum
    print(min, max)


## Simple Test
miniMaxSum([1, 2, 3, 4, 5])

"""
OUTPUT:
10 14
"""

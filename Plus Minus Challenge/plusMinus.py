## CHALLENGE QUESTION
""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
"""

    ######### SOLUTION CODE ##########

def plusMinus(arr):
    
    array_length = len(arr)
    ## for the Number of Positive, Negative, zero that will be found in the array
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    #iterating throw the array and specifing Positive, Negative and Zeros and it's number
    for i in arr:
        if i > 0: ## Number is Positive
            positive_numbers += 1
        elif i < 0: ## Number is Negative
            negative_numbers += 1
        else: ## Number is zero
            zeros += 1
    ## Calculating Ratio of each category and Formatting to 6 Decimal points
    positives_ratio = "{0:.6f}".format(positive_numbers / array_length)
    negatives_ratio = "{0:.6f}".format(negative_numbers / array_length)
    zeros_ratio = "{0:.6f}".format(zeros / array_length)
    ## Printing Out the Result 
    print(positives_ratio + "\n" + negatives_ratio + "\n" + zeros_ratio)

## Simple Test
plusMinus([-4, 3, -9, 0, 4, 1])

## OUTPUT
"""
0.500000
0.333333
0.166667
"""
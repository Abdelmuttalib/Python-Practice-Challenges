## CHALLENGE QUESTION
"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
"""

   ######### SOLUTION CODE ##########
def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    array_length = len(arr)

    secondary_diagonal_index = len(arr) - 1

    for i in range(len(arr)):
        ## initializing the indexes of each diagonal values throughtout the loop
        primary_diagonal_value = arr[i][i]
        secondary_diagonal_value = arr[i][secondary_diagonal_index]
        ## adding values to each specified diagonal
        primary_diagonal += primary_diagonal_value
        secondary_diagonal += secondary_diagonal_value
        ## to get the index of the secondary diagonal
        secondary_diagonal_index -= 1
    ## calculating the difference between the two diagonals using abs function
    difference_of_the_two_diagonals = abs(primary_diagonal - secondary_diagonal)
    ## returning the diagonal difference
    return "Diagonal Difference is " + str(difference_of_the_two_diagonals)

## Simple test, 9 by 9 list
print(diagonalDifference([[6, 6, 7, -10, 9, -3, 8, 9, -1],
                    [9, 7, -10, 6, 4, 1, 6, 1, 1],
                    [-1, -2, 4, -6, 1, -4, -6, 3, 9],
                    [-8, 7, 6, -1, -6, -6, 6, -7, 2],
                    [-10, -4, 9, 1, -7, 8, -5, 3, -5],
                    [-8, -3, -4, 2, -3, 7, -5, 1, -5],
                    [-2, -7, -4, 8, 3, -1, 8, 2, 3],
                    [-3, 4, 6, -7, -7, -8, -3, 9, -6],
                    [-2, 0, 5, 4, 4, 4, -3, 3, 0]]))

## OUTPUT:
## Diagonal Difference is 52

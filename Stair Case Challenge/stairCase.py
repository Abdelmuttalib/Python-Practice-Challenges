### CHALLEMGE QUESTION
"""
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer, , denoting the size of the staircase.

Constraints

 .

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
"""

    ######### SOLUTION CODE #########

def staircase(n):
    ## initializing stairs before adding and shaping
    ## 'stairs' is the final result shape
    stairs = ""
    ## holding a value of input 'a' to determine total string width when aligning it to the right with 'rjust' Function
    reverse_width = n - 1
    ## saving the final shape result as one value
    full_stairs_shape = ""

    for i in range(1, n+1):
        ## Shaping the stairs
        row = "#" * i 
        ## length of the row after Shaping it
        row_length = len(row)
        ## Aligning String to the right specifing a Width
        ## Parameter: calculated string length in total after padding for "rjust" FUNCTION
        total_width = row_length + reverse_width
        stairs = row.rjust(total_width)
        ## Adding each row to end up with a full stairs value in full_stairs_shape, Not used
        full_stairs_shape += stairs + "\n"
        ## Printing the Stairs Row
        print(stairs)
        ## decrement to adjust string width for "rjust" as String output Becomes Larger
        reverse_width -= 1

## Simple Test
staircase(6)

"""
OUTPUT
     #
    ##
   ###
  ####
 #####
######
"""
## CHALLENGE QUESTION
"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = '12:01:00PM'

Return '12:01:00'.

--
s = '12:01:00AM'

Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
Input Format

A single string  that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""

    ######## SOLUTION CODE ########


def timeConversion(s):
	## Splitting the time string to find the time label
	switched = s.split(':')

	## initialize array to hold the final changed string format
	fixed_time = s[:-2].split(':')
	## Cutting the time label (AM or PM) from the string
	cut_time_label = switched[len(switched) - 1]
	day_time_label = cut_time_label[2:]
	## to check the first number (hour) and change it accordingly to 24-hour format
	time_switcher = fixed_time[0]
	## array of possible values after 12PM, to check which matched the inputed hour and change it to 24-hour format
	check_array = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

	## if the day time label is AM, then the only case we need to change the hour format is at 12:00:00 AM to 00:00:00
	if day_time_label == 'AM' and time_switcher == '12':
		time_switcher = '00'
	## if day time label is PM then change hour format accordingly by adding 12 to it
	elif day_time_label == 'PM':
		for j in check_array:
			if time_switcher == j:
				## change value to integer to perform math addition then return again as string
				time_switcher = str(int(j) + 12)
	## assigning the value of the fixed hour format to the array of time (divided into: hour, min, sec),
	## we are assigning only the correct hour format after fixing it to 24-hour format,
	## as the Minutes & Seconds are not different in 24-hour format
	fixed_time[0] = time_switcher

	## final time string after converting to 24-hour format
	final_time_shape = ""
	## iterate over the array of converted (hour, min, sec) and adding it as string to 'final_time_shape'
	for i in range(len(fixed_time)):
		## when selected value is the last  (second), do not add ':'
		if i == len(fixed_time) - 1:
			final_time_shape += fixed_time[i]
		else:
			## only add ':' to seperate hour, min & sec if the selected value isn't the seconds
			final_time_shape += fixed_time[i] + ":"

	## Returning the final time result converted in 24-hour format
	return final_time_shape



## Simple Test
print(timeConversion('04:44:01PM'))

"""
Output:
16:44:01
"""

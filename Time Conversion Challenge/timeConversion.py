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
	splited_time = s.split(':')
	## holding the time label (AM or PM) in variable to determine day time and convert to 24-hour format properly
	day_time_label = splited_time[2][2:]

	## if the day time label is AM, then the only case we need to change the hour format is at 12:00:00 AM to 00:00:00
	## also remove the day_time_label (AM) from the string
	if day_time_label == 'AM' and splited_time[0] == '12':
		splited_time[0] = '00'
		splited_time[2] = splited_time[2].replace("AM", "")

	## if day time label is PM then change hour format accordingly by adding 12 to it
	## and remove the day_time_label (PM) from the string
	elif day_time_label == 'PM':
		if splited_time[0] != '12':
			splited_time[0] = str(int(splited_time[0]) + 12)
			splited_time[2] = splited_time[2].replace("PM", "")

	## final converted time to 24-hour format
	## join the list to string seperated by ':'
	final_converted_time = ":".join(splited_time)

	## returning the final result
	return final_converted_time



## Simple Tests with different inputs
print(timeConversion('04:44:01PM'))
print(timeConversion('11:59:59PM'))
"""
Output:
16:44:01
23:59:59
"""

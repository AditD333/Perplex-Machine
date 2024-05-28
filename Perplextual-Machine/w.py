import calendar as c
import os
import sys
import time
import platform
from functools import lru_cache
from random import randint as rand

plat = platform.system()


#[For Variable "a"]
#iOS Compliant, since os.get_terminal_size() is DISALLOWED!
#Default is PRESET TO 0, change the number if you want in INTEGER to Create Dash ("-") Borders!

aa=0




# [For Variable "a"] Write in integer form (No Quotes) Years per cycle, Minimum of 1 (!)

a=



# [For Variable "b"] Write in integer form (No Quotes) ranges From 0 to Maximum of (a-1) (!)

b=



# [For Variable "super_cycle_index"] Minimal of 1 (!), 400-Full-Cycle Index. For Example:

# 0 = First 400-full cycle (00 to 399)
# 1 = Second 400-full cycle (400 to 799)
# K = 400-full cycles of (400[K] to 400[K]+399) [K IS ZERO-BASED INDEX AND NUMBERING!]

# If need to include a specific year, input this equation AT EXACT, indicated the following row below:
# [targetted_year] // (400*a) ["//" is a floor division so write it accordingly!]
# Example: 2024 // (400*a)

#Note: Targetted_year may not be contained in the final result, but the key is:
#It will automatically map the cycle phase index to the super cycle that contains the [targetted_year] 

super_cycle_index=



# [For Variable "month"] Select From 1 - 12 (!)

month=



# [For Variable "date_group"] Select Date Group of the month(from 1 to 7) described as below:
# 1 = Targetted Days Are 01, 08, 15, 22, 29 (For Month 02 [February], 29 is applicable when leap-year(s) only)
# 2 = Targetted Days Are 02, 09, 16, 23, 30 (30 is Not Applicable in Any Month 02 [February])
# 3 = Targetted Days Are 03, 10, 17, 24, 31 (31st is Not Applicable for Any Non-31-Day-Month)
# 4 = Targetted Days Are 04, 11, 18, 25
# 5 = Targetted Days Are 05, 12, 19, 26
# 6 = Targetted Days Are 06, 13, 20, 27
# 7 = Targetted Days Are 07, 14, 21, 28

date_group=



# [For Variable "week_system"] PLEASE PAY ATTENTION TO THESE DESCRIPTION BELOW FOR Week number lookup:

#Week begins from and ends with? Write the LETTER Between A and G (case-insensitive) between QUOTES ('') !

#Example -> To start the week on Sunday, write 'A' or 'a', or if start Monday, write 'B' or 'b' and so on...

# A = Sunday - Saturday
# B = Monday - Sunday
# C = Tuesday - Monday
# D = Wednesday - Tuesday
# E = Thursday - Wednesday
# F = Friday - Thursday
# G = Saturday - Friday

week_system=



# [For Variable "added_digits"]
#Add Minimum Of Digits (MANDATORY, SET TO 0 IF NOT NEEDED)!
#The number of digits when dealing with years LESS THAN 1000 will be forced to 4-digit format!
#You can add it by a NON-NEGATIVE INTEGER specifying to:
# 0 = No minimum of digits added, keep it to 4
# 1 = 1 digit added to minimum output, i.e forced to 5-digit format for less than 10000
# 2 = 2 digits added to minimum output, i.e forced to 6-digits format less than year 100000
# And so on, MIND YOUR RAM PERFORMANCE AS WELL!

added_digits=







s = time.time()
@lru_cache(None)



def clear():
	if plat == 'Windows':
		os.system('cls')
	else:
		os.system('clear')



clear()



if sys.version_info[0] < 3:
	print("Error! Please use Python 3 and above!")
	input("\n\nPress Enter To Exit!")
	sys.exit()
elif sys.version_info[0] == 3:
	if sys.version_info[1] >= 11:
		sys.set_int_max_str_digits(0)
	elif 7 <= sys.version_info[1] <= 9:
		if sys.version_info[2] >= 14:
			sys.set_int_max_str_digits(0)
	elif sys.version_info[1] == 10:
		if sys.version_info[2] >= 7:
			sys.set_int_max_str_digits(0)



clear()



if type(aa) != int or aa < 0:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if a is None or type(a) != int or a < 1:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if b is None or type(b) != int or b < 0 or b >= a:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if super_cycle_index is None or type(super_cycle_index) != int or super_cycle_index < 0:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if month is None or type(month) != int or month < 1 or month > 12:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if date_group is None or type(date_group) != int or date_group < 1 or date_group > 7:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if week_system is None or type(week_system) != str or len(week_system) != 1 or ord(week_system.upper()) < 65 or ord(week_system.upper()) > 71:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if added_digits is None or type(added_digits) != int or added_digits < 0:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()



sun = mon = tue = wed = thu = fri = sat = 0



dlis = ['Sunday - Saturday','Monday - Sunday','Tuesday - Monday','Wednesday - Tuesday','Thursday - Wednesday','Friday - Thursday','Saturday - Friday']
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []



if os.path.exists('02_super_cycle.txt'):
	os.remove('02_super_cycle.txt')

clear()

with open('02_super_cycle.txt','w') as occ:
	occ.write("Week System ---> [%s] %s\n\n\n" % (week_system.upper(),dlis[ord(week_system.upper())-65]))
	occ.write("\nMandatory Minimum Of Digits IS 4\n")
	occ.write("\n\n\nAdded Minimum of Digits ---> %d\n" % (added_digits))
	occ.write("\n\n\nYear(s) Per Cycle ---> %d\n" % (a))
	occ.write(f"\n\n\nElement <X - #> ---> {b:0>{len(str(a-1))}}\n")
	occ.write("\n\n\nTargetted Super-Cycle Phase Index ---> %d\n" % (super_cycle_index))
	occ.write("\n\n\nTargetted Month ---> %02d\n" % (month))
	if date_group == 1:
		if month == 2:
			occ.write("\n\n\nTargetted Dates---> 01, 08, 15, 22 [29 for leap-year(s) only]\n\n\n\n\n\n\n\n")
		else:
			occ.write("\n\n\nTargetted Dates---> 01, 08, 15, 22, 29\n\n\n\n\n\n\n\n")
	elif date_group == 2:
		if month == 2:
			occ.write("\n\n\nTargetted Dates---> 02, 09, 16, 23\n\n\n\n\n\n\n\n")
		else:
			occ.write("\n\n\nTargetted Dates---> 02, 09, 16, 23, 30\n\n\n\n\n\n\n\n")
	elif date_group == 3:
		if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
			occ.write("\n\n\nTargetted Dates---> 03, 10, 17, 24\n\n\n\n\n\n\n\n")
		else:
			occ.write("\n\n\nTargetted Dates---> 03, 10, 17, 24, 31\n\n\n\n\n\n\n\n")
	elif date_group == 4:
		occ.write("\n\n\nTargetted Dates---> 04, 11, 18, 25\n\n\n\n\n\n\n\n")
	elif date_group == 5:
		occ.write("\n\n\nTargetted Dates---> 05, 12, 19, 26\n\n\n\n\n\n\n\n")
	elif date_group == 6:
		occ.write("\n\n\nTargetted Dates---> 06, 13, 20, 27\n\n\n\n\n\n\n\n")
	elif date_group == 7:
		occ.write("\n\n\nTargetted Dates---> 07, 14, 21, 28\n\n\n\n\n\n\n\n")
	


	if week_system.upper() == 'A':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)

	elif week_system.upper() == 'B':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)

	elif week_system.upper() == 'C':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)

	elif week_system.upper() == 'D':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)

	elif week_system.upper() == 'E':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)

	elif week_system.upper() == 'F':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)


	elif week_system.upper() == 'G':
		for x in range (0,400):
			v = a*(x+(400*super_cycle_index)) + b
			if c.weekday(v%400,month,date_group) == c.SATURDAY:
				sat += 1
				d1.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.SUNDAY:
				sun += 1
				d2.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.MONDAY:
				mon += 1
				d3.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.TUESDAY:
				tue += 1
				d4.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.WEDNESDAY:
				wed += 1
				d5.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.THURSDAY:
				thu += 1
				d6.append(f"{v:0>{4+added_digits}}")
			elif c.weekday(v%400,month,date_group) == c.FRIDAY:
				fri += 1
				d7.append(f"{v:0>{4+added_digits}}")

		occ.write("[1] Saturday = %d" % (sat))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d1)
		occ.write("\n\n\n\n\n")

		occ.write("[2] Sunday = %d" % (sun))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d2)
		occ.write("\n\n\n\n\n")

		occ.write("[3] Monday = %d" % (mon))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d3)
		occ.write("\n\n\n\n\n")

		occ.write("[4] Tuesday = %d" % (tue))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d4)
		occ.write("\n\n\n\n\n")

		occ.write("[5] Wednesday = %d" % (wed))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d5)
		occ.write("\n\n\n\n\n")

		occ.write("[6] Thursday = %d" % (thu))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d6)
		occ.write("\n\n\n\n\n")

		occ.write("[7] Friday = %d" % (fri))
		occ.write("\n\n\n\n\n")
		occ.write("%s" % d7)







print("-"*aa)
print("\nGenerated! See ---> 02_super_cycle.txt In The Same Folder As This Code!\n")
print("\nMandatory Minimum Of Digits IS 4\n")
print("\nAdded Minimum of Digits ---> %d\n" % (added_digits))
print("\nYear(s) Per Cycle ---> %d\n" % (a))
print("\nElement <X - #> ---> %02d\n" % (b))
print("\nTargetted Super-Cycle Phase Index ---> %d\n" % (super_cycle_index))
print("\nWeek System ---> [%s] %s\n" % (week_system.upper(),dlis[ord(week_system.upper())-65]))
print("\nTargetted Month ---> %02d\n" % (month))
if date_group == 1:
	if month == 2:
		print("\nTargetted Dates---> 01, 08, 15, 22. [29 for leap-year(s) only]\n")
	else:
		print("\nTargetted Dates---> 01, 08, 15, 22, 29\n")
elif date_group == 2:
	if month == 2:
		print("\nTargetted Dates---> 02, 09, 16, 23\n")
	else:
		print("\nTargetted Dates---> 02, 09, 16, 23, 30\n")
elif date_group == 3:
	if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
		print("\nTargetted Dates---> 03, 10, 17, 24\n")
	else:
		print("\nTargetted Dates---> 03, 10, 17, 24, 31\n")
elif date_group == 4:
	print("\nTargetted Dates---> 04, 11, 18, 25\n")
elif date_group == 5:
	print("\nTargetted Dates---> 05, 12, 19, 26\n")
elif date_group == 6:
	print("\nTargetted Dates---> 06, 13, 20, 27\n")
elif date_group == 7:
	print("\nTargetted Dates---> 07, 14, 21, 28\n")
e = time.time()
print("\nProcessed In ---> %02d : %02d\n" % ((e-s)//60,(e-s)%60))
print("-"*aa)
input("\n\nPress Enter To Exit!")
if plat == 'Windows':
	os.system('cls')
else:
	os.system('clear')
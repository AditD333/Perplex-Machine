import calendar as c
import os,sys
import time
from random import randint as rand
import datetime as dt
import platform
from functools import lru_cache

plat = platform.system()


#[For Variable "a"]
#iOS Compliant, since os.get_terminal_size() is DISALLOWED!
#Default is PRESET TO 0, change the number if you want in INTEGER to Create Dash ("-") Borders!

a=0



# [For Variable "k"] Number Year(s) per cycle,

#Enter the number of minimal 1-year cycle INSIDE THE QUOTES!
#Ex -> '10' for 10-years = Decade
#Ex -> '100' for 100-years = Century
#Ex -> '12' for 12-years = Duodecennial

#Or if you want longer, use a natural number to randomize number of years per cycle, MINIMAL of 1, for example:
# 1 = 1 up to 10 (or 10^1) year-cycle
# 2 = 11 (or 10^1 + 1) up to 100 (or 10^2) year-cycle
# N = (10^[N-1] + 1) up to 10^N year-cycle [Mathematical Exception for 1]

k=



# [For Variable "year"] Follow the instructions below!

#Fill the year var with (All inputted years interpretted in PROLEPTIC GREGORIAN CALENDAR!):
#1. Any DIGIT from 0 - 9 inside the quote! e.g year 2000 ==> '2000' For year(s) 0000 and Above
#2. Or, if you want to random a bunch of digits, and without quote(s) Write any natural number(s) MINIMAL of 1 (MIND YOUR RAM!)
#3. Note for that the in range of 1 - 4 for steps 1 and 2:
	# 1 --> Years are forced to print to 4-digit format (0000 - 0009)
	# 2 --> Years are forced to print to 4-digit format (0000 - 0099)
	# 3 --> Years are forced to print to 4-digit format (0000 - 0999)
	# 4 --> Years are to printed normally to 4-digit format (0000 - 9999)
	# More than 4 = Follows the number of digits
#4. NO NEGATIVE INPUTS AS WELL!

year=



# [For Variable "set_exact_position"] Also Follow the instructions below!

#Set the variable to 0 if wanting user-defined starting day of the week
#Set to 1 if you want to create your calendar with January 01 casted as a user-defined Nth day of the week
#Set to 2 to determine the week-system BASED ON WEEK 01's ENDING (JANUARY(S) 01 THROUGH 07)
#Or set to 3 if you want that date part of the group falls on the particular Nth day of the week

set_exact_position=



# [For Variable "week_system"] PLEASE PAY ATTENTION TO THESE DESCRIPTION BELOW FOR Week number lookup:

#If set_exact_position is set to 0: 

#Week begins from and ends with? Write the LETTER Between A and G (case-insensitive) between QUOTES ('') !

#Example -> To start the week on Sunday, write 'A' or 'a', or if start Monday, write 'B' or 'b' and so on...

# A = Sunday - Saturday
# B = Monday - Sunday
# C = Tuesday - Monday
# D = Wednesday - Tuesday
# E = Thursday - Wednesday
# F = Friday - Thursday
# G = Saturday - Friday



#If set_exact_position is set to 1 (ALSO CONTAINS WEEK SYSTEM FROM THE LIST ABOVE AS RESULT LATER!):

#Set the variable as an INTEGER FORM(s) Between 1 - 7:
# 1 = Start the year as 1st day of the week
# 2 = Start the year as 2nd day of the week
# 3 = Start the year as 3rd day of the week
# 4 = Start the year as 4th day of the week
# 5 = Start the year as 5th day of the week
# 6 = Start the year as 6th day of the week
# 7 = Start the year as 7th day of the week



#If set_exact_position is set to 2 (ALSO CONTAINS WEEK SYSTEM FROM THE LIST ABOVE AS RESULT LATER!):

#Determining first day of the week BASED FROM WEEK 01's ENDING 
# Write as INTEGER FORM Between 1 - 7 (JANUARY(S) 01 THROUGH 07):
# 1 = Where Week 01 ends January 01
# 2 = Where Week 01 ends January 02
# 3 = Where Week 01 ends January 03
# 4 = Where Week 01 ends January 04
# 5 = Where Week 01 ends January 05
# 6 = Where Week 01 ends January 06
# 7 = Where Week 01 ends January 07



#However, if set_exact_position is set to 3 (ALSO CONTAINS WEEK SYSTEM FROM THE LIST ABOVE AS RESULT LATER!):

#Determining week-system / first day of the week BASED FROM SPECIFIED DATE GROUP OF A SPECIFIED MONTH
# Write as an exactly a 3-CHARACTER STRING FORMAT with format below (case-insensitive):

# "([A-L] or [a-l])[1-7][1-7]"

# Character 1 [A-L] or [a-l] represents 12 months:
# A = January, B = February,........, L = December

# Character 2 [1-7] represents date-groups, pay attention to the description below!:
# 1 = Targetted Days Are 01, 08, 15, 22, 29 (For Month 02 [February], 29 is applicable when leap-year(s) only)
# 2 = Targetted Days Are 02, 09, 16, 23, 30 (30 is Not Applicable in Any Month 02 [February])
# 3 = Targetted Days Are 03, 10, 17, 24, 31 (31st is Not Applicable for Any Non-31-Day-Month)
# 4 = Targetted Days Are 04, 11, 18, 25
# 5 = Targetted Days Are 05, 12, 19, 26
# 6 = Targetted Days Are 06, 13, 20, 27
# 7 = Targetted Days Are 07, 14, 21, 28

# Character 3 [1-7] represents validation form the first 2 characters, in which the position of the week must comply with:
# 1 = A specified date-group of the month must casted as 1st day of the week
# 2 = A specified date-group of the month must casted as 2nd day of the week
# 3 = A specified date-group of the month must casted as 3rd day of the week
# 4 = A specified date-group of the month must casted as 4th day of the week
# 5 = A specified date-group of the month must casted as 5th day of the week
# 6 = A specified date-group of the month must casted as 6th day of the week
# 7 = A specified date-group of the month must casted as 7th day of the week

# For example usage: "A11" or 'a11'
# Meaning a calendar in which it will determine a week-system of a calendar year in which JANUARY(s) 01, 08, 15, 22, AND 29 must CASTED AS THE 1ST DAY OF THE WEEK

# Another example: "E54" or 'e54'
# Meaning a calendar in which it will determine a week-system of a calendar year in which MAY(s) 05, 12, 19, AND 26, must CASTED AS THE 4TH DAY OF THE WEEK

week_system=



# [For Variable "show_grid_calendar"] Follow the instructions below!
#Show Grid Calendar or Not? Be careful that sometimes the result can be ZIG-ZAGGED!
#Also, because the years will take the last 4 digits, it is important that:
	#Any given years ENDING IN 0000 - 0999 will shown as A 1-3-DIGIT NUMBER, regardless to the full-year number
#Input:
#0 = DISABLE grid calendar (Perfect For Fancy Fonts)
#1 = ENABLE grid calendar (Perfect For Supported CLI-Like Fonts!)

show_grid_calendar=



# [For Variable "cycle_format"] Extend the current cycle number or only position of the cycle? (0 for position only, or 1 for full-extended)

cycle_format=



# [For "mode"] Output format: (0) Calendar only with weeklist system, or (1) Observance(s) only

mode=







@lru_cache(None)
def clear():
	if plat == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

clear()

if sys.version_info[0] < 3:
	print("Error! Please use Python 3 or above!")
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
		else:
			pass
elif sys.version_info[0] >= 4:
	sys.set_int_max_str_digits(0)



clear()




if type(a) != int or a < 0:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if k is None:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if type(k) == str:
	if len(k) < 1:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()

elif type(k) == int:
	if k < 1:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()

if year is None:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if type(year) == str:
	if len(year) < 1 or year.isnumeric == False:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	random_trigger = 0

elif type(year) == int:
	if year < 1:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	random_trigger = 1

else:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if set_exact_position is None or type(set_exact_position) != int or set_exact_position < 0 or set_exact_position > 3:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if set_exact_position == 0:
	if week_system is None or type(week_system) != str:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	else:
		if len(week_system) != 1 or ord(week_system.upper()) < 65 or ord(week_system.upper()) > 71:
			print("Error!")
			input("\n\nPress Enter To Exit!")
			sys.exit()

elif set_exact_position == 1 or set_exact_position == 2:
	if week_system is None or type(week_system) != int:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	else:
		if week_system < 1 or week_system > 7:
			print("Error!")
			input("\n\nPress Enter To Exit!")
			sys.exit()

elif set_exact_position == 3:
	if week_system is None or type(week_system) != str:
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	else:
		if len(week_system) != 3 or ord(week_system[0].upper()) < 65 or ord(week_system[0].upper()) > 76 or ord(week_system[1]) < 49 or ord(week_system[1]) > 55 or ord(week_system[2]) < 49 or ord(week_system[2]) > 55:
			print("Error!")
			input("\n\nPress Enter To Exit!")
			sys.exit()


if show_grid_calendar is None or type(show_grid_calendar) != int or show_grid_calendar < 0 or show_grid_calendar > 1:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()


if cycle_format is None or type(cycle_format) != int or cycle_format < 0 or cycle_format > 1:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()

if mode is None or type(mode) != int or mode < 0 or mode > 1:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()



start = time.time()



if type(k) == str:
	if k.isnumeric() is False:
		stop = time.time()
		print("Error!")
		sys.exit()
	else:
		k2 = int(k)
		if k2 < 1:
			stop = time.time()
			print("Error!")
			input("\n\nPress Enter To Exit!")
			sys.exit()
		else:
			pass



elif type(k) == int:
	d0 = '0123456789'
	e0 = []
	k_indicate = []
	for h0 in d0:
		e0.append(h0)
	for random in range(0,k):
		k_indicate.append(e0[rand(0,9)])
	if len(k_indicate) > 1:
		if k_indicate[0] == "0":
			k_indicate[0] = "1"
	else:
		pass
	k1 = "".join(k_indicate)
	k2 = int(k1) + 1



else:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()



if type(year) == str:
	if len(year) < 1 or year.isnumeric == False:
		stop = time.time()
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	random_trigger = 0



elif type(year) == int:
	if year < 1:
		stop = time.time()
		print("Error!")
		input("\n\nPress Enter To Exit!")
		sys.exit()
	random_trigger = 1



else:
	print("Error!")
	input("\n\nPress Enter To Exit!")
	sys.exit()



cf = ["Short","Long"]
weekstart_letter = ['A','B','C','D','E','F','G']
weekstart_dayoftheweek = ['Sunday - Saturday','Monday - Sunday','Tuesday - Monday','Wednesday - Tuesday','Thursday - Wednesday','Friday - Thursday','Saturday - Friday']
weekstart_detect = [c.SUNDAY,c.MONDAY,c.TUESDAY,c.WEDNESDAY,c.THURSDAY,c.FRIDAY,c.SATURDAY]
contains = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']



if mode == 0:
	fname = "00_calendar_only.txt"
	if os.path.exists(fname):
		os.remove(fname)
	else:
		pass
elif mode == 1:
	fname = "01_observance(s)_list_only.txt"
	if os.path.exists(fname):
		os.remove(fname)
	else:
		pass



with open(fname,'w') as w:
	w.write(":"*a)
	w.write("\n\n\n\n")
	if random_trigger == 1:
		d = '0123456789'
		e = []
		y_indicate = []
		for h in d:
			e.append(h)
		for random in range(0,year):
			y_indicate.append(e[rand(0,9)])
		if year < 4:
			for add in range (0,4-year):
				y_indicate.insert(0,'0')
		y1 = "".join(y_indicate)
		y2 = "".join(y_indicate[-64:])
		y = int(y1)
		y1064 = (int(y2))%10**64
		y400 = y1064%400
		y10k = y1064%10000
		y_full = y%68400000
	elif random_trigger == 0:
		e = []
		for h in year:
			e.append(h)
		e_real = len(e)
		if e_real < 4:
			for add in range (0,4-e_real):
				e.insert(0,'0')
		y1 = "".join(e)
		y2 = "".join(e[-64:])
		y = int(y1)
		y1064 = (int(y2))%10**64
		y400 = y1064%400
		y10k = y1064%10000
		y_full = y%68400000
	ws = week_system
	if set_exact_position == 3:
		wsx = int(week_system[2])
		wsx1 = int(week_system[1])
		wsx2 = ord(week_system[0].upper())-64
	if set_exact_position == 1:
		if c.weekday(y400,1,(9-week_system)) == c.SUNDAY:
			week_system = 'A'
		elif c.weekday(y400,1,(9-week_system)) == c.MONDAY:
			week_system = 'B'
		elif c.weekday(y400,1,(9-week_system)) == c.TUESDAY:
			week_system = 'C'
		elif c.weekday(y400,1,(9-week_system)) == c.WEDNESDAY:
			week_system = 'D'
		elif c.weekday(y400,1,(9-week_system)) == c.THURSDAY:
			week_system = 'E'
		elif c.weekday(y400,1,(9-week_system)) == c.FRIDAY:
			week_system = 'F'
		elif c.weekday(y400,1,(9-week_system)) == c.SATURDAY:
			week_system = 'G'
	elif set_exact_position == 2:
		if c.weekday(y400,1,(1+week_system)) == c.SUNDAY:
			week_system = 'A'
		elif c.weekday(y400,1,(1+week_system)) == c.MONDAY:
			week_system = 'B'
		elif c.weekday(y400,1,(1+week_system)) == c.TUESDAY:
			week_system = 'C'
		elif c.weekday(y400,1,(1+week_system)) == c.WEDNESDAY:
			week_system = 'D'
		elif c.weekday(y400,1,(1+week_system)) == c.THURSDAY:
			week_system = 'E'
		elif c.weekday(y400,1,(1+week_system)) == c.FRIDAY:
			week_system = 'F'
		elif c.weekday(y400,1,(1+week_system)) == c.SATURDAY:
			week_system = 'G'
	elif set_exact_position == 3:
		if c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.SUNDAY:
			if int(week_system[2]) == 1:
				week_system = 'A'
			elif int(week_system[2]) == 2:
				week_system = 'G'
			elif int(week_system[2]) == 3:
				week_system = 'F'
			elif int(week_system[2]) == 4:
				week_system = 'E'
			elif int(week_system[2]) == 5:
				week_system = 'D'
			elif int(week_system[2]) == 6:
				week_system = 'C'
			elif int(week_system[2]) == 7:
				week_system = 'B'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.MONDAY:
			if int(week_system[2]) == 1:
				week_system = 'B'
			elif int(week_system[2]) == 2:
				week_system = 'A'
			elif int(week_system[2]) == 3:
				week_system = 'G'
			elif int(week_system[2]) == 4:
				week_system = 'F'
			elif int(week_system[2]) == 5:
				week_system = 'E'
			elif int(week_system[2]) == 6:
				week_system = 'D'
			elif int(week_system[2]) == 7:
				week_system = 'C'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.TUESDAY:
			if int(week_system[2]) == 1:
				week_system = 'C'
			elif int(week_system[2]) == 2:
				week_system = 'B'
			elif int(week_system[2]) == 3:
				week_system = 'A'
			elif int(week_system[2]) == 4:
				week_system = 'G'
			elif int(week_system[2]) == 5:
				week_system = 'F'
			elif int(week_system[2]) == 6:
				week_system = 'E'
			elif int(week_system[2]) == 7:
				week_system = 'D'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.WEDNESDAY:
			if int(week_system[2]) == 1:
				week_system = 'D'
			elif int(week_system[2]) == 2:
				week_system = 'C'
			elif int(week_system[2]) == 3:
				week_system = 'B'
			elif int(week_system[2]) == 4:
				week_system = 'A'
			elif int(week_system[2]) == 5:
				week_system = 'G'
			elif int(week_system[2]) == 6:
				week_system = 'F'
			elif int(week_system[2]) == 7:
				week_system = 'E'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.THURSDAY:
			if int(week_system[2]) == 1:
				week_system = 'E'
			elif int(week_system[2]) == 2:
				week_system = 'D'
			elif int(week_system[2]) == 3:
				week_system = 'C'
			elif int(week_system[2]) == 4:
				week_system = 'B'
			elif int(week_system[2]) == 5:
				week_system = 'A'
			elif int(week_system[2]) == 6:
				week_system = 'G'
			elif int(week_system[2]) == 7:
				week_system = 'F'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.FRIDAY:
			if int(week_system[2]) == 1:
				week_system = 'F'
			elif int(week_system[2]) == 2:
				week_system = 'E'
			elif int(week_system[2]) == 3:
				week_system = 'D'
			elif int(week_system[2]) == 4:
				week_system = 'C'
			elif int(week_system[2]) == 5:
				week_system = 'B'
			elif int(week_system[2]) == 6:
				week_system = 'A'
			elif int(week_system[2]) == 7:
				week_system = 'G'
		elif c.weekday(y400,ord(week_system[0].upper())-64,int(week_system[1])) == c.SATURDAY:
			if int(week_system[2]) == 1:
				week_system = 'G'
			elif int(week_system[2]) == 2:
				week_system = 'F'
			elif int(week_system[2]) == 3:
				week_system = 'E'
			elif int(week_system[2]) == 4:
				week_system = 'D'
			elif int(week_system[2]) == 5:
				week_system = 'C'
			elif int(week_system[2]) == 6:
				week_system = 'B'
			elif int(week_system[2]) == 7:
				week_system = 'A'
	else:
		pass
	if week_system.upper() == 'A':
		es0 = '1'
		sun_number = '1'
		mon_number = '2'
		tue_number = '3'
		wed_number = '4'
		thu_number = '5'
		fri_number = '6'
		sat_number = '7'
		week_system_ordinal = 1
	elif week_system.upper() == 'B':
		es0 = '7'
		sun_number = '7'
		mon_number = '1'
		tue_number = '2'
		wed_number = '3'
		thu_number = '4'
		fri_number = '5'
		sat_number = '6'
		week_system_ordinal = 2
	elif week_system.upper() == 'C':
		es0 = '6'
		sun_number = '6'
		mon_number = '7'
		tue_number = '1'
		wed_number = '2'
		thu_number = '3'
		fri_number = '4'
		sat_number = '5'
		week_system_ordinal = 3
	elif week_system.upper() == 'D':
		es0 = '5'
		sun_number = '5'
		mon_number = '6'
		tue_number = '7'
		wed_number = '1'
		thu_number = '2'
		fri_number = '3'
		sat_number = '4'
		week_system_ordinal = 4
	elif week_system.upper() == 'E':
		es0 = '4'
		sun_number = '4'
		mon_number = '5'
		tue_number = '6'
		wed_number = '7'
		thu_number = '1'
		fri_number = '2'
		sat_number = '3'
		week_system_ordinal = 5
	elif week_system.upper() == 'F':
		es0 = '3'
		sun_number = '3'
		mon_number = '4'
		tue_number = '5'
		wed_number = '6'
		thu_number = '7'
		fri_number = '1'
		sat_number = '2'
		week_system_ordinal = 6
	elif week_system.upper() == 'G':
		es0 = '2'
		sun_number = '2'
		mon_number = '3'
		tue_number = '4'
		wed_number = '5'
		thu_number = '6'
		fri_number = '7'
		sat_number = '1'
		week_system_ordinal = 7
	
	c.setfirstweekday(weekstart_detect[ord(week_system.upper())-65])
	
	tx = (c.weekday(y400,1,1)+2-week_system_ordinal)%7+1
	if tx == 1:
		tx_ordinal = "st"
	elif tx == 2:
		tx_ordinal = "nd"
	elif tx == 3:
		tx_ordinal = "rd"
	else:
		tx_ordinal = "th"

	if set_exact_position == 3:
		if int(wsx) == 1:
			tx_ordinal1 = "st"
		elif int(wsx) == 2:
			tx_ordinal1 = "nd"
		elif int(wsx) == 3:
			tx_ordinal1 = "rd"
		else:
			tx_ordinal1 = "th"

	if set_exact_position == 0:
		w.write("Week System ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
		w.write("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
		w.write("\n\nAnd Week %s01 Ends On ---> January %02d" % (weekstart_letter[ord(week_system.upper())-65],8-tx))
	elif set_exact_position == 1:
		w.write("January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
		w.write("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
		w.write("\n\nWhere Week %s01 Ends On ---> January %02d" % (week_system,8-tx))
	elif set_exact_position == 2:
		w.write("Week %s1 Ends On ---> January %02d" % (week_system,8-tx))
		w.write("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
		w.write("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
	elif set_exact_position == 3:
		w.write("Required Date ---> Column Starting %s %02d, As The %s%s Day Of The Week" % (c.month_name[wsx2],wsx1,wsx,tx_ordinal1))
		w.write("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
		w.write("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
		w.write("\n\nAnd Week %s01 Ends On ---> January %02d" % (week_system,8-tx))

	if type(year) == int:
		if year == 1:
			w.write("\n\nDigit Group ---> 1 (Forced 0000 - 0009)\n\n\n\n\n\n\n\n")
		elif year == 2:
			w.write("\n\nDigit Group ---> 2 (Forced 0000 - 0099)\n\n\n\n\n\n\n\n")
		elif year == 3:
			w.write("\n\nDigit Group ---> 3 (Forced 0000 - 0999)\n\n\n\n\n\n\n\n")
		elif year == 4:
			w.write("\n\nDigit Group ---> 4 (Normal 0000 - 9999)\n\n\n\n\n\n\n\n")
		else:
			w.write("\n\nDigit Group ---> %d (Adjusted By Number Of Digits)\n\n\n\n\n\n\n\n" % (year))
	elif type(year) == str:
		if e_real == 1:
			w.write("\n\nDigit Group ---> 1 (Forced 0000 - 0009)\n\n\n\n\n\n\n\n")
		elif e_real == 2:
			w.write("\n\nDigit Group ---> 2 (Forced 0000 - 0099)\n\n\n\n\n\n\n\n")
		elif e_real == 3:
			w.write("\n\nDigit Group ---> 3 (Forced 0000 - 0999)\n\n\n\n\n\n\n\n")
		elif e_real == 4:
			w.write("\n\nDigit Group ---> 4 (Normal 0000 - 9999)\n\n\n\n\n\n\n\n")
		else:
			w.write("\n\nDigit Group ---> %d (Adjusted By Number Of Digits)\n\n\n\n\n\n\n\n" % (e_real))
	

	if random_trigger == 1:
		for array in y_indicate:
			w.write("%s" % array)

	elif random_trigger == 0:
		for array in e:
			w.write("%s" % array)

	
	prefix = y%k2
	if cycle_format == 0:
		w.write("\n\n\n\n\n\n\n\n(S) Years Per Cycle ---> %s" % (k2))
		w.write("\n\n\n\n")
		w.write(f"<{prefix:0>{len(str(k2-1))}}>")
		w.write("\n\n\n\n")
	elif cycle_format == 1:
		w.write("\n\n\n\n\n\n\n\n(L) Years Per Cycle ---> %s" % (k2))
		if type(year) == int:
			w.write("\n\n\n\n(%d)\n\n\n\n" % (y//k2))
			w.write(f"<{prefix:0>{len(str(k2-1))}}>")
			w.write("\n\n\n\n")
		elif type(year) == str:
			w.write("\n\n\n\n(%d)\n\n\n\n" % (y//k2))
			w.write(f"<{prefix:0>{len(str(k2-1))}}>")
			w.write("\n\n\n\n")
	if show_grid_calendar == 1:
		w.write("Show Grid-Based Calendar ---> Yes\n\n\n\n")
	else:
		w.write("Show Grid-Based Calendar ---> No\n\n\n\n")
	animals = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Ram"]
	element = ["Metal","Metal","Water","Water","Wood","Wood","Fire","Fire","Earth","Earth"]
	if show_grid_calendar == 1:
		w.write("\n\n\n\n")
		w.write("Please Note If The Last 4 Digits Is In The Form \"0xxx\", It Will Form As Their Proper Writings!\n\n\n\n")
		w.write(c.calendar(y10k))
		w.write("\n\n\n\n")
	else:
		pass
	w.write("\n\n\n\nYear Of The : %s %s - %s %s" % (element[(y_full-1)%10],animals[(y_full-1)%12],element[y_full%10],animals[y_full%12]))
	w.write("\n\n\n\n")

	w.write("\n\nPotential 9-First-Day-Of-Lunar-Month-Beginning Is 90.79102661%")
	w.write("\n\nWhile Potential Only 8-First-Day-Of-Lunar-Month-Beginning Is Only 09.20897339%")



	w.write("\n\n\n")
	def gaussEaster(y_full,mode):
		A = y_full % 19
		B = y_full % 4
		C = y_full % 7
		 
		P = (y_full // 100)
		Q = ((13 + 8 * P) // 25)
		M = (15 - Q + P - P // 4) % 30
		N = (4 + P - P // 4) % 7
		D = (19 * A + M) % 30
		E = (2 * B + 4 * C + 6 * D + N) % 7
		days = (22 + D + E)

	

	  #----------------------------EASTER DIFFERENT MODE DIFFERENT OUTPUT STYLE!----------------------------#

		

		if ((D == 29) and (E == 6)):
			w.write(("\n    %s - [%s] - Sun - 03 - 01  : Shrove Sunday\n") % ((dt.datetime(2000+y400,3,1).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 03 - 02  : Shrove Monday\n") % ((dt.datetime(2000+y400,3,2).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 03 - 03  : Shrove Tuesday\n") % ((dt.datetime(2000+y400,3,3).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 03 - 04  : Ash Wednesday\n") % ((dt.datetime(2000+y400,3,4).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Sun - 03 - 29  : Mothering Sunday (U.K's Mothers Day)\n") % ((dt.datetime(2000+y400,3,29).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Sun - 04 - 12  : Palm Sunday\n") % ((dt.datetime(2000+y400,4,12).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 04 - 13  : Holy Monday\n") % ((dt.datetime(2000+y400,4,13).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 04 - 14  : Holy Tuesday\n") % ((dt.datetime(2000+y400,4,14).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 04 - 15  : Holy Wednesday\n") % ((dt.datetime(2000+y400,4,15).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Thu - 04 - 16  : Maundy Thursday\n") % ((dt.datetime(2000+y400,4,16).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Fri - 04 - 17  : Good Friday\n") % ((dt.datetime(2000+y400,4,17).strftime("%j")),fri_number))
			w.write(("    %s - [%s] - Sat - 04 - 18  : Holy Saturday\n") % ((dt.datetime(2000+y400,4,18).strftime("%j")),sat_number))
			w.write(("    %s - [%s] - Sun - 04 - 19  : Easter Sunday\n") % ((dt.datetime(2000+y400,4,19).strftime("%j")),es0))
			w.write(("    %s - [%s] - Mon - 04 - 20  : Easter Monday\n") % ((dt.datetime(2000+y400,4,20).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 04 - 21  : Easter Tuesday\n") % ((dt.datetime(2000+y400,4,21).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 04 - 22  : Easter Wednesday\n") % ((dt.datetime(2000+y400,4,22).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Thu - 04 - 23  : Easter Thursday\n") % ((dt.datetime(2000+y400,4,23).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Fri - 04 - 24  : Easter Friday\n") % ((dt.datetime(2000+y400,4,24).strftime("%j")),fri_number))
			w.write(("    %s - [%s] - Sat - 04 - 25  : Easter Saturday\n") % ((dt.datetime(2000+y400,4,25).strftime("%j")),sat_number))
			w.write(("    %s - [%s] - Thu - 05 - 28  : Ascencion Day\n") % ((dt.datetime(2000+y400,5,28).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Sun - 06 - 07  : Whit Sunday (Pentecost Sunday)\n") % ((dt.datetime(2000+y400,6,7).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 06 - 08  : Whit Monday (Pentecost Monday)\n") % ((dt.datetime(2000+y400,6,8).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 06 - 09  : Whit Tuesday (Pentecost Tuesday)\n") % ((dt.datetime(2000+y400,6,9).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Sun - 06 - 14  : Trinity Sunday\n") % ((dt.datetime(2000+y400,6,14).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Thu - 06 - 18  : Corpus Christi (Thursday State)\n") % ((dt.datetime(2000+y400,6,18).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Sun - 06 - 21  : Corpus Christi (Sunday State)\n") % ((dt.datetime(2000+y400,6,21).strftime("%j")),sun_number))
			
		 

		elif ((D == 28) and (E == 6) and A > 10):
			if (y_full % 4 == 0 and y_full % 100 == 0 and y_full % 400 == 0):
				w.write(("\n    %s - [%s] - Sun - 02 - 29  : Shrove Sunday\n") % ((dt.datetime(2000+y400,2,29).strftime("%j")),sun_number))
			elif (y_full % 4 == 0 and y_full % 100 == 0 and y_full % 400 != 0):
				w.write(("\n    %s - [%s] - Sun - 02 - 28  : Shrove Sunday\n") % ((dt.datetime(2000+y400,2,28).strftime("%j")),sun_number))
			elif (y_full % 4 == 0 and y_full % 100 != 0 and y_full % 400 != 0):
				w.write(("\n    %s - [%s] - Sun - 02 - 29  : Shrove Sunday\n") % ((dt.datetime(2000+y400,2,29).strftime("%j")),sun_number))
			elif (y_full % 4 != 0 and y_full % 100 != 0 and y_full % 400 != 0):
				w.write(("\n    %s - [%s] - Sun - 02 - 28  : Shrove Sunday\n") % ((dt.datetime(2000+y400,2,28).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 03 - 01  : Shrove Monday\n") % ((dt.datetime(2000+y400,3,1).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 03 - 02  : Shrove Tuesday\n") % ((dt.datetime(2000+y400,3,2).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 03 - 03  : Ash Wednesday\n") % ((dt.datetime(2000+y400,3,3).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Sun - 03 - 28  : Mothering Sunday (U.K's Mothers Day)\n") % ((dt.datetime(2000+y400,3,28).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Sun - 04 - 11  : Palm Sunday\n") % ((dt.datetime(2000+y400,4,11).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 04 - 12  : Holy Monday\n") % ((dt.datetime(2000+y400,4,12).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 04 - 13  : Holy Tuesday\n") % ((dt.datetime(2000+y400,4,13).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 04 - 14  : Holy Wednesday\n") % ((dt.datetime(2000+y400,4,14).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Thu - 04 - 15  : Maundy Thursday\n") % ((dt.datetime(2000+y400,4,15).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Fri - 04 - 16  : Good Friday\n") % ((dt.datetime(2000+y400,4,16).strftime("%j")),fri_number))
			w.write(("    %s - [%s] - Sat - 04 - 17  : Holy Saturday\n") % ((dt.datetime(2000+y400,4,17).strftime("%j")),sat_number))
			w.write(("    %s - [%s] - Sun - 04 - 18  : Easter Sunday\n") % ((dt.datetime(2000+y400,4,18).strftime("%j")),es0))
			w.write(("    %s - [%s] - Mon - 04 - 19  : Easter Monday\n") % ((dt.datetime(2000+y400,4,19).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 04 - 20  : Easter Tuesday\n") % ((dt.datetime(2000+y400,4,20).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Wed - 04 - 21  : Easter Wednesday\n") % ((dt.datetime(2000+y400,4,21).strftime("%j")),wed_number))
			w.write(("    %s - [%s] - Thu - 04 - 22  : Easter Thursday\n") % ((dt.datetime(2000+y400,4,22).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Fri - 04 - 23  : Easter Friday\n") % ((dt.datetime(2000+y400,4,23).strftime("%j")),fri_number))
			w.write(("    %s - [%s] - Sat - 04 - 24  : Easter Saturday\n") % ((dt.datetime(2000+y400,4,24).strftime("%j")),sat_number))
			w.write(("    %s - [%s] - Thu - 05 - 27  : Ascencion Day\n") % ((dt.datetime(2000+y400,5,27).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Sun - 06 - 06  : Whit Sunday (Pentecost Sunday)\n") % ((dt.datetime(2000+y400,6,6).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Mon - 06 - 07  : Whit Monday (Pentecost Monday)\n") % ((dt.datetime(2000+y400,6,7).strftime("%j")),mon_number))
			w.write(("    %s - [%s] - Tue - 06 - 08  : Whit Tuesday (Pentecost Tuesday)\n") % ((dt.datetime(2000+y400,6,8).strftime("%j")),tue_number))
			w.write(("    %s - [%s] - Sun - 06 - 13  : Trinity Sunday\n") % ((dt.datetime(2000+y400,6,13).strftime("%j")),sun_number))
			w.write(("    %s - [%s] - Thu - 06 - 17  : Corpus Christi (Thursday State)\n") % ((dt.datetime(2000+y400,6,17).strftime("%j")),thu_number))
			w.write(("    %s - [%s] - Sun - 06 - 20  : Corpus Christi (Sunday State)\n") % ((dt.datetime(2000+y400,6,20).strftime("%j")),sun_number))
		


		else:
			if (days > 31):
				cha0w = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-49)
				cha0x = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-48)
				cha0 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-47)
				cha1 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-46)
				cha2 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-21)
				cha3a = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-7)
				cha3b = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-6)
				cha3c = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-5)
				cha3d = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-4)
				cha3e = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-3)
				cha3f = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-2)
				cha3g = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(-1)
				cha3h = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(1)
				cha3i = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(2)
				cha3j = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(3)
				cha3k = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(4)
				cha3l = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(5)
				cha3m = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(6)
				cha4 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(39)
				cha5 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(49)
				cha5a = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(50)
				cha6a = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(51)
				cha6 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(56)
				cha7 = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(60)
				cha7a = dt.datetime(2000+y400, 4, days-31) + dt.timedelta(63)
				w.write(("\n\n    %s - [%s] - Sun - %02d - %02d  : Shrove Sunday\n") % ((dt.datetime(2000+y400,cha0w.month,cha0w.day).strftime("%j")),sun_number,cha0w.month,cha0w.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Shrove Monday\n") % ((dt.datetime(2000+y400,cha0x.month,cha0x.day).strftime("%j")),mon_number,cha0x.month,cha0x.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Shrove Tuesday\n") % ((dt.datetime(2000+y400,cha0.month,cha0.day).strftime("%j")),tue_number,cha0.month,cha0.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Ash Wednesday\n") % ((dt.datetime(2000+y400,cha1.month,cha1.day).strftime("%j")),wed_number,cha1.month,cha1.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Mothering Sunday (U.K's Mothers Day)\n") % ((dt.datetime(2000+y400,cha2.month,cha2.day).strftime("%j")),sun_number,cha2.month,cha2.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Palm Sunday\n") % ((dt.datetime(2000+y400,cha3a.month,cha3a.day).strftime("%j")),sun_number,cha3a.month,cha3a.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Holy Monday\n") % ((dt.datetime(2000+y400,cha3b.month,cha3b.day).strftime("%j")),mon_number,cha3b.month,cha3b.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Holy Tuesday\n") % ((dt.datetime(2000+y400,cha3c.month,cha3c.day).strftime("%j")),tue_number,cha3c.month,cha3c.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Holy Wednesday\n") % ((dt.datetime(2000+y400,cha3d.month,cha3d.day).strftime("%j")),wed_number,cha3d.month,cha3d.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Maundy Thursday\n") % ((dt.datetime(2000+y400,cha3e.month,cha3e.day).strftime("%j")),thu_number,cha3e.month,cha3e.day))
				w.write(("    %s - [%s] - Fri - %02d - %02d  : Good Friday\n") % ((dt.datetime(2000+y400,cha3f.month,cha3f.day).strftime("%j")),fri_number,cha3f.month,cha3f.day))
				w.write(("    %s - [%s] - Sat - %02d - %02d  : Holy Saturday\n") % ((dt.datetime(2000+y400,cha3g.month,cha3g.day).strftime("%j")),sat_number,cha3g.month,cha3g.day))
				w.write(("    %s - [%s] - Sun - 04 - %02d  : Easter Sunday\n") % ((dt.datetime(2000+y400,4,days-31).strftime("%j")),es0,days-31))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Easter Monday\n") % ((dt.datetime(2000+y400,cha3h.month,cha3h.day).strftime("%j")),mon_number,cha3h.month,cha3h.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Easter Tuesday\n") % ((dt.datetime(2000+y400,cha3i.month,cha3i.day).strftime("%j")),tue_number,cha3i.month,cha3i.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Easter Wednesday\n") % ((dt.datetime(2000+y400,cha3j.month,cha3j.day).strftime("%j")),wed_number,cha3j.month,cha3j.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Easter Thursday\n") % ((dt.datetime(2000+y400,cha3k.month,cha3k.day).strftime("%j")),thu_number,cha3k.month,cha3k.day))
				w.write(("    %s - [%s] - Fri - %02d - %02d  : Easter Friday\n") % ((dt.datetime(2000+y400,cha3l.month,cha3l.day).strftime("%j")),fri_number,cha3l.month,cha3l.day))
				w.write(("    %s - [%s] - Sat - %02d - %02d  : Easter Saturday\n") % ((dt.datetime(2000+y400,cha3m.month,cha3m.day).strftime("%j")),sat_number,cha3m.month,cha3m.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Ascencion Day\n") % ((dt.datetime(2000+y400,cha4.month,cha4.day).strftime("%j")),thu_number,cha4.month,cha4.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Whit Sunday (Pentecost Sunday)\n") % ((dt.datetime(2000+y400,cha5.month,cha5.day).strftime("%j")),sun_number,cha5.month,cha5.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Whit Monday (Pentecost Monday)\n") % ((dt.datetime(2000+y400,cha5a.month,cha5a.day).strftime("%j")),mon_number,cha5a.month,cha5a.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Whit Tuesday (Pentecost Tuesday)\n") % ((dt.datetime(2000+y400,cha6a.month,cha6a.day).strftime("%j")),tue_number,cha6a.month,cha6a.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Trinity Sunday\n") % ((dt.datetime(2000+y400,cha6.month,cha6.day).strftime("%j")),sun_number,cha6.month,cha6.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Corpus Christi (Thursday State)\n") % ((dt.datetime(2000+y400,cha7.month,cha7.day).strftime("%j")),thu_number,cha7.month,cha7.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Corpus Christi (Sunday State)\n") % ((dt.datetime(2000+y400,cha7a.month,cha7a.day).strftime("%j")),sun_number,cha7a.month,cha7a.day))



			elif (days <= 31):
				cha0w = dt.datetime(2000+y400, 3, days) + dt.timedelta(-49)
				cha0x = dt.datetime(2000+y400, 3, days) + dt.timedelta(-48)
				cha0 = dt.datetime(2000+y400, 3, days) + dt.timedelta(-47)
				cha1 = dt.datetime(2000+y400, 3, days) + dt.timedelta(-46)
				cha2 = dt.datetime(2000+y400, 3, days) + dt.timedelta(-21)
				cha3a = dt.datetime(2000+y400, 3, days) + dt.timedelta(-7)
				cha3b = dt.datetime(2000+y400, 3, days) + dt.timedelta(-6)
				cha3c = dt.datetime(2000+y400, 3, days) + dt.timedelta(-5)
				cha3d = dt.datetime(2000+y400, 3, days) + dt.timedelta(-4)
				cha3e = dt.datetime(2000+y400, 3, days) + dt.timedelta(-3)
				cha3f = dt.datetime(2000+y400, 3, days) + dt.timedelta(-2)
				cha3g = dt.datetime(2000+y400, 3, days) + dt.timedelta(-1)
				cha3h = dt.datetime(2000+y400, 3, days) + dt.timedelta(1)
				cha3i = dt.datetime(2000+y400, 3, days) + dt.timedelta(2)
				cha3j = dt.datetime(2000+y400, 3, days) + dt.timedelta(3)
				cha3k = dt.datetime(2000+y400, 3, days) + dt.timedelta(4)
				cha3l = dt.datetime(2000+y400, 3, days) + dt.timedelta(5)
				cha3m = dt.datetime(2000+y400, 3, days) + dt.timedelta(6)
				cha4 = dt.datetime(2000+y400, 3, days) + dt.timedelta(39)
				cha5 = dt.datetime(2000+y400, 3, days) + dt.timedelta(49)
				cha5a = dt.datetime(2000+y400, 3, days) + dt.timedelta(50)
				cha6a = dt.datetime(2000+y400, 3, days) + dt.timedelta(51)
				cha6 = dt.datetime(2000+y400, 3, days) + dt.timedelta(56)
				cha7 = dt.datetime(2000+y400, 3, days) + dt.timedelta(60)
				cha7a = dt.datetime(2000+y400, 3, days) + dt.timedelta(63)
				w.write(("\n\n    %s - [%s] - Sun - %02d - %02d  : Shrove Sunday\n") % ((dt.datetime(2000+y400,cha0w.month,cha0w.day).strftime("%j")),sun_number,cha0w.month,cha0w.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Shrove Monday\n") % ((dt.datetime(2000+y400,cha0x.month,cha0x.day).strftime("%j")),mon_number,cha0x.month,cha0x.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Shrove Tuesday\n") % ((dt.datetime(2000+y400,cha0.month,cha0.day).strftime("%j")),tue_number,cha0.month,cha0.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Ash Wednesday\n") % ((dt.datetime(2000+y400,cha1.month,cha1.day).strftime("%j")),wed_number,cha1.month,cha1.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Mothering Sunday (U.K's Mothers Day)\n") % ((dt.datetime(2000+y400,cha2.month,cha2.day).strftime("%j")),sun_number,cha2.month,cha2.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Palm Sunday\n") % ((dt.datetime(2000+y400,cha3a.month,cha3a.day).strftime("%j")),sun_number,cha3a.month,cha3a.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Holy Monday\n") % ((dt.datetime(2000+y400,cha3b.month,cha3b.day).strftime("%j")),mon_number,cha3b.month,cha3b.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Holy Tuesday\n") % ((dt.datetime(2000+y400,cha3c.month,cha3c.day).strftime("%j")),tue_number,cha3c.month,cha3c.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Holy Wednesday\n") % ((dt.datetime(2000+y400,cha3d.month,cha3d.day).strftime("%j")),wed_number,cha3d.month,cha3d.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Maundy Thursday\n") % ((dt.datetime(2000+y400,cha3e.month,cha3e.day).strftime("%j")),thu_number,cha3e.month,cha3e.day))
				w.write(("    %s - [%s] - Fri - %02d - %02d  : Good Friday\n") % ((dt.datetime(2000+y400,cha3f.month,cha3f.day).strftime("%j")),fri_number,cha3f.month,cha3f.day))
				w.write(("    %s - [%s] - Sat - %02d - %02d  : Holy Saturday\n") % ((dt.datetime(2000+y400,cha3g.month,cha3g.day).strftime("%j")),sat_number,cha3g.month,cha3g.day))
				w.write(("    %s - [%s] - Sun - 03 - %02d  : Easter Sunday\n") % ((dt.datetime(2000+y400,3,days).strftime("%j")),es0,days))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Easter Monday\n") % ((dt.datetime(2000+y400,cha3h.month,cha3h.day).strftime("%j")),mon_number,cha3h.month,cha3h.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Easter Tuesday\n") % ((dt.datetime(2000+y400,cha3i.month,cha3i.day).strftime("%j")),tue_number,cha3i.month,cha3i.day))
				w.write(("    %s - [%s] - Wed - %02d - %02d  : Easter Wednesday\n") % ((dt.datetime(2000+y400,cha3j.month,cha3j.day).strftime("%j")),wed_number,cha3j.month,cha3j.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Easter Thursday\n") % ((dt.datetime(2000+y400,cha3k.month,cha3k.day).strftime("%j")),thu_number,cha3k.month,cha3k.day))
				w.write(("    %s - [%s] - Fri - %02d - %02d  : Easter Friday\n") % ((dt.datetime(2000+y400,cha3l.month,cha3l.day).strftime("%j")),fri_number,cha3l.month,cha3l.day))
				w.write(("    %s - [%s] - Sat - %02d - %02d  : Easter Saturday\n") % ((dt.datetime(2000+y400,cha3m.month,cha3m.day).strftime("%j")),sat_number,cha3m.month,cha3m.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Ascencion Day\n") % ((dt.datetime(2000+y400,cha4.month,cha4.day).strftime("%j")),thu_number,cha4.month,cha4.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Whit Sunday (Pentecost Sunday)\n") % ((dt.datetime(2000+y400,cha5.month,cha5.day).strftime("%j")),sun_number,cha5.month,cha5.day))
				w.write(("    %s - [%s] - Mon - %02d - %02d  : Whit Monday (Pentecost Monday)\n") % ((dt.datetime(2000+y400,cha5a.month,cha5a.day).strftime("%j")),mon_number,cha5a.month,cha5a.day))
				w.write(("    %s - [%s] - Tue - %02d - %02d  : Whit Tuesday (Pentecost Tuesday)\n") % ((dt.datetime(2000+y400,cha6a.month,cha6a.day).strftime("%j")),tue_number,cha6a.month,cha6a.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Trinity Sunday\n") % ((dt.datetime(2000+y400,cha6.month,cha6.day).strftime("%j")),sun_number,cha6.month,cha6.day))
				w.write(("    %s - [%s] - Thu - %02d - %02d  : Corpus Christi (Thursday State)\n") % ((dt.datetime(2000+y400,cha7.month,cha7.day).strftime("%j")),thu_number,cha7.month,cha7.day))
				w.write(("    %s - [%s] - Sun - %02d - %02d  : Corpus Christi (Sunday State)\n") % ((dt.datetime(2000+y400,cha7a.month,cha7a.day).strftime("%j")),sun_number,cha7a.month,cha7a.day))

		for novadvent in range(27,31):
				if c.weekday(y400,11,novadvent) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 11 - %02d  : Start Of Advent\n") % ((dt.datetime(2000+y400,11,novadvent).strftime("%j")),sun_number,novadvent))
				else:
					pass

		for decadvent in range(1,4):
			if c.weekday(y400,12,decadvent) == c.SUNDAY:
				w.write(("    %s - [%s] - Sun - 12 - %02d  : Start Of Advent\n") % ((dt.datetime(2000+y400,12,decadvent).strftime("%j")),sun_number,decadvent))
		


	def month(y400,y,m,d,week,week_system_ordinal):
		day_of_year_list = dt.datetime(2000+(y400),m,d)
		if m < 3:
		  y1 = y-1
		  month = m + 12
		  d = d
		elif m >=3 :
			y1 = y
			month = m
			d = d
		century = y1//100
		centdiv4 = century//4 
		calib = 2-century+centdiv4
		d1 = 36525*(y1+4716)//100
		e = 306001 * (month+1) // 10000
		f = calib + d + d1 + e - 1525
		

		jddiv = (f - 2451549)
		ddiv = (jddiv*70499183//2081882250)
		dmod = (jddiv * 70499183) % 2081882250
		dic = (dmod/70499183)
		resultdiv = (ddiv + 17049) // 12
		resultmod0 = (ddiv + 17049) % 12
		hijri_month = ["01","02","03","04","05","06","07","08","09","10","11","12"]


		if (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 11 and resultdiv == -1):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64),hijri_month[(resultmod0+1)%12]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64),hijri_month[(resultmod0+1)%12]))

		elif (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 11 and resultdiv >= 0):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64),hijri_month[(resultmod0+1)%12]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64),hijri_month[(resultmod0+1)%12]))

		elif (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 != 11 and resultdiv >= 0):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64),hijri_month[resultmod0+1]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64),hijri_month[resultmod0+1]))

		elif (dic >= 0 and dic <= 6 + (28169441/70499183) and resultdiv >= 0):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64),hijri_month[resultmod0]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %04d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64),hijri_month[resultmod0]))
				


		elif (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 11 and resultdiv <= -1):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64) - 10**64,hijri_month[(resultmod0+1)%12]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, (resultdiv+1) % (10**64) - 10**64,hijri_month[(resultmod0+1)%12]))

		elif (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 != 11 and resultdiv <= -1):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64) - 10**64,hijri_month[resultmod0+1]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64) - 10**64,hijri_month[resultmod0+1]))

		elif (dic >= 0 and dic <= 6 + (28169441/70499183) and resultdiv <= -1):
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64) - 10**64,hijri_month[resultmod0]))
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s   [H  %05d - %s - 01]\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic, resultdiv % (10**64) - 10**64,hijri_month[resultmod0]))

		else:
			if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
				w.write("\n\n\n%s%02d :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic))			
			else:
				if d == 1:
					w.write("\n\n\n%s%02d (Continued) :\n\n\n\n" % (week_system.upper(),week))
				w.write("    %s - [%d] - %s - %02d - %02d  <---->  %s\n" % (day_of_year_list.strftime("%j"), (c.weekday(y400,m,d)+2-week_system_ordinal)%7+1, c.day_abbr[c.weekday(y400,m,d)], m, d, dic))
	
	

	if c.weekday(y400,1,1) == weekstart_detect[ord(week_system.upper()) - 65]:
		week = 0
	else:
		week = 1
	






	if mode == 0:
		w.write("\n\n\n\n\n\n\n")
		gaussEaster(y_full,mode)
		w.write(("    %s - [%d] - %s - 12 - 24  : Christmas Eve\n") % ((dt.datetime(2000+y400,12,24).strftime("%j")),(c.weekday(y400,12,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,24)]))
		w.write(("    %s - [%d] - %s - 12 - 25  : Christmas Day\n") % ((dt.datetime(2000+y400,12,25).strftime("%j")),(c.weekday(y400,12,25)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,25)]))
		w.write(("    %s - [%d] - %s - 12 - 26  : Seven Days After Christmas, Day 01\n") % ((dt.datetime(2000+y400,12,26).strftime("%j")),(c.weekday(y400,12,26)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,26)]))
		w.write(("    %s - [%d] - %s - 12 - 27  : Seven Days After Christmas, Day 02\n") % ((dt.datetime(2000+y400,12,27).strftime("%j")),(c.weekday(y400,12,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,27)]))
		w.write(("    %s - [%d] - %s - 12 - 28  : Seven Days After Christmas, Day 03\n") % ((dt.datetime(2000+y400,12,28).strftime("%j")),(c.weekday(y400,12,28)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,28)]))
		w.write(("    %s - [%d] - %s - 12 - 29  : Seven Days After Christmas, Day 04\n") % ((dt.datetime(2000+y400,12,29).strftime("%j")),(c.weekday(y400,12,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,29)]))
		w.write(("    %s - [%d] - %s - 12 - 30  : Seven Days After Christmas, Day 05\n") % ((dt.datetime(2000+y400,12,30).strftime("%j")),(c.weekday(y400,12,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,30)]))
		w.write(("    %s - [%d] - %s - 12 - 31  : Seven Days After Christmas, Day 06\n") % ((dt.datetime(2000+y400,12,31).strftime("%j")),(c.weekday(y400,12,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,31)]))
		w.write(("    %s - [%d] - %s - 01 - 01  : Seven Days After Christmas, Day 07 (At Next Year)\n") % ((dt.datetime(2000+y400+1,1,1).strftime("%j")),(c.weekday(y400+1,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400+1,1,1)]))	
		
		

		for m in range (1,2):
			w.write("\n\n\n\n\n\n\n[01] January %04d (Week %s01 Always Contains First %s of January)\n\n\n\n\n" % (y10k,week_system.upper(),contains[ord(week_system.upper())-65]))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
				
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")
		if y400%4 == 0 and y400%100 == 0 and y400%400 == 0:
			w.write("\n\n[02] February %04d\n\n\n\n\n" % (y10k))
			for m in range (2,3):
				for d in range (1,30):
					if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
						week += 1
					month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		elif y400%4 == 0 and y400%100 == 0 and y400%400 != 0:
			w.write("\n\n[02] February %04d\n\n\n\n\n" % (y10k))
			for m in range (2,3):
				for d in range (1,29):
					if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
						week += 1
					month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		elif y400%4 == 0 and y400%100 != 0 and y400%400 != 0:
			w.write("\n\n[02] February %04d\n\n\n\n\n" % (y10k))
			for m in range (2,3):
				for d in range (1,30):
					if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
						week += 1
					month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		elif y400%4 != 0:
			w.write("\n\n[02] February %04d\n\n\n\n\n" % (y10k))
			for m in range (2,3):
				for d in range (1,29):
					if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
						week += 1
					month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (3,4):
			w.write("\n\n[03] March %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (4,5):
			w.write("\n\n[04] April %04d\n\n\n\n\n" % (y10k))
			for d in range (1,31):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (5,6):
			w.write("\n\n[05] May %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (6,7):
			w.write("\n\n[06] June %04d\n\n\n\n\n" % (y10k))
			for d in range (1,31):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (7,8):
			w.write("\n\n[07] July %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (8,9):
			w.write("\n\n[08] August %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (9,10):
			w.write("\n\n[09] September %04d\n\n\n\n\n" % (y10k))
			for d in range (1,31):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (10,11):
			w.write("\n\n[10] October %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (11,12):
			w.write("\n\n[11] November %04d\n\n\n\n\n" % (y10k))
			for d in range (1,31):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
			w.write("\n\n\n\n")

		for m in range (12,13):
			w.write("\n\n[12] December %04d\n\n\n\n\n" % (y10k))
			for d in range (1,32):
				if c.weekday(y400,m,d) == weekstart_detect[ord(week_system.upper()) - 65]:
					week += 1
					if d == 25:
						week = 53
					elif d >= 26:
						week = 1
				month(y400,y,m,d,week,week_system_ordinal)
			w.write("\n\n\n\n")
			w.write(":"*a)
		






	elif mode == 1:
		w.write("\n\n\n\n\n")
		def c_000(y):
			d0 = dt.datetime(2000+(y400),12,26)
			d1 = dt.datetime(2000+(y400),1,1)
			d1a = dt.datetime(2001+(y400),1,1)
			for i in range (1,8):
				if c.weekday(y400,1,i) == c.MONDAY:
					dtyim = dt.datetime(2000+(y400),1,i)
			for i in range (8,15):
				if c.weekday(y400,1,i) == c.MONDAY:
					dcoad = dt.datetime(2000+(y400),1,i)
			for i in range (15,22):
				if c.weekday(y400,1,i) == c.MONDAY:
					d2 = dt.datetime(2000+(y400),1,i)
			dscd0 = dt.datetime(2000+(y400),2,8)
			for i in range (8,15):
				if c.weekday(y400,2,i) == c.SUNDAY:
					dsb = dt.datetime(2000+(y400),2,i)
			for i in range (15,22):
				if c.weekday(y400,2,i) == c.SUNDAY:
					dnbaas = dt.datetime(2000+(y400),2,i)
			dval = dt.datetime(2000+(y400),2,14)
			for i in range (15,22):
				if c.weekday(y400,2,i) == c.MONDAY:
					d3 = dt.datetime(2000+(y400),2,i)
			dscdworld = dt.datetime(2000+(y400),2,22)
			for i in range (8,15):
				if c.weekday(y400,3,i) == c.SUNDAY:
					dst1 = dt.datetime(2000+(y400),3,i)
			dscd1 = dt.datetime(2000+(y400),3,12)
			dsp = dt.datetime(2000+(y400),3,17)
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SUNDAY:
					dsteurope1 = dt.datetime(2000+(y400),3,i)
			dapf = dt.datetime(2000+(y400),4,1)
			dedm = dt.datetime(2000+(y400),4,20)
			for i in range (18,25):
				if c.weekday(y400,3,i) == c.SATURDAY:
					deh0 = dt.datetime(2000+(y400),3,i)
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SATURDAY:
					deh1 = dt.datetime(2000+(y400),3,i)
			for i in range (1,8):
				if c.weekday(y400,5,i) == c.MONDAY:
					dmetgala = dt.datetime(2000+(y400),5,i)
			for i in range (8,15):
				if c.weekday(y400,5,i) == c.SUNDAY:
					dmd = dt.datetime(2000+(y400),5,i)
			for i in range (15,22):
				if c.weekday(y400,5,i) == c.SATURDAY:
					darmed = dt.datetime(2000+(y400),5,i)
			for i in range (24,31):
				if c.weekday(y400,5,i) == c.SUNDAY:
					dip = dt.datetime(2000+(y400),5,i)
			for i in range (25,32):
				if c.weekday(y400,5,i) == c.MONDAY:
					d4 = dt.datetime(2000+(y400),5,i)
			for i in range (15,22):
				if c.weekday(y400,6,i) == c.SUNDAY:
					dfd = dt.datetime(2000+(y400),6,i)
			d5 = dt.datetime(2000+(y400),6,19)
			dcrown = dt.datetime(2000+(y400),7,3)
			d6 = dt.datetime(2000+(y400),7,4)
			d60 = dt.datetime(2000+(y400),7,5)
			d61 = dt.datetime(2000+(y400),7,6)
			for i in range (1,8):
				if c.weekday(y400,9,i) == c.MONDAY:
					d7 = dt.datetime(2000+(y400),9,i)
			for i in range (8,15):
				if c.weekday(y400,10,i) == c.MONDAY:
					d8 = dt.datetime(2000+(y400),10,i)
			dhl = dt.datetime(2000+(y400),10,31)
			for i in range (1,8):
				if c.weekday(y400,11,i) == c.SUNDAY:
					dst0 = dt.datetime(2000+(y400),11,i)
			for i in range (2,9):
				if c.weekday(y400,11,i) == c.TUESDAY:
					delc = dt.datetime(2000+(y400),11,i)
			d9 = dt.datetime(2000+(y400),11,11)
			for i in range (22,29):
				if c.weekday(y400,11,i) == c.THURSDAY:
					d10 = dt.datetime(2000+(y400),11,i)
					d10a = dt.datetime(2000+(y400),11,i) + dt.timedelta(1)
					d10b = dt.datetime(2000+(y400),11,i) + dt.timedelta(2)
					d10c = dt.datetime(2000+(y400),11,i) + dt.timedelta(3)
					d10d = dt.datetime(2000+(y400),11,i) + dt.timedelta(4)
					d10e = dt.datetime(2000+(y400),11,i) + dt.timedelta(5)
					d10f = dt.datetime(2000+(y400),11,i) + dt.timedelta(6)
			d11 = dt.datetime(2000+(y400),12,31)
			dwiki = dt.datetime(2000+(y400),1,15)
			dedu = dt.datetime(2000+(y400),1,24)
			dradio = dt.datetime(2000+(y400),2,13)
			darmy = dt.datetime(2000+(y400),4,6)
			dhealth = dt.datetime(2000+(y400),4,7)
			dswd = dt.datetime(2000+(y400),5,4)
			dsixth = dt.datetime(2000+(y400),5,6)
			dplc = dt.datetime(2000+(y400),5,15)
			dghd = dt.datetime(2000+(y400),2,2)
			dex0 = dt.datetime(2000+(y400),3,3)
			dex1 = dt.datetime(2000+(y400),6,6)
			dex2 = dt.datetime(2000+(y400),9,11)
			dex3 = dt.datetime(2000+(y400),9,9)
			dex4 = dt.datetime(2000+(y400),7,7)
			dex404 = dt.datetime(2000+(y400),4,4)
			dmovie = dt.datetime(2000+(y400),3,5)
			dmath = dt.datetime(2000+(y400),3,14)
			dmathx = dt.datetime(2000+(y400),3,15)
			dmath1x = dt.datetime(2000+(y400),3,4)
			dmath1 = dt.datetime(2000+(y400),3,5)
			dmath2x = dt.datetime(2000+(y400),4,4)
			dmath2 = dt.datetime(2000+(y400),4,5)
			dmath414 = dt.datetime(2000+(y400),4,14)
			dmath823 = dt.datetime(2000+(y400),8,23)
			for i in range (9,11):
				if dt.datetime(2000+(y400),11,i).strftime("%j") == "314":
					dmath3 = dt.datetime(2000+(y400),11,i)
			for i in range (10,12):
				if dt.datetime(2000+(y400),11,i).strftime("%j") == "315":
					dmath3x = dt.datetime(2000+(y400),11,i)
			dmath4 = dt.datetime(2000+(y400),7,22)
			dmath4x = dt.datetime(2000+(y400),7,23)
			dwater = dt.datetime(2000+(y400),3,22)
			dintw = dt.datetime(2000+(y400),3,8)
			dasmr = dt.datetime(2000+(y400),4,9)
			dex5 = dt.datetime(2000+(y400),4,10)
			dpet = dt.datetime(2000+(y400),4,11)
			dstandard = dt.datetime(2000+(y400),4,13)
			dstandardori = dt.datetime(2000+(y400),10,14)
			dmario = dt.datetime(2000+(y400),3,10)
			dart = dt.datetime(2000+(y400),4,15)
			for i in range (15,22):
				if c.weekday(y400,4,i) == c.MONDAY:
					dpatr = dt.datetime(2000+(y400),4,i)
			dearth = dt.datetime(2000+(y400),4,22)
			dbook = dt.datetime(2000+(y400),4,23)
			ddance = dt.datetime(2000+(y400),4,29)
			ddance1 = dt.datetime(2000+(y400),4,30)
			for i in range (24,31):
				if c.weekday(y400,4,i) == c.SATURDAY:
					dtc = dt.datetime(2000+(y400),4,i)
			dlab = dt.datetime(2000+(y400),5,1)
			dcdm = dt.datetime(2000+(y400),5,5)
			dtech = dt.datetime(2000+(y400),5,11)
			dbiology = dt.datetime(2000+(y400),5,22)
			dbiology1 = dt.datetime(2000+(y400),5,23)
			denv = dt.datetime(2000+(y400),6,5)
			docean = dt.datetime(2000+(y400),6,8)
			for i in range (8,15):
				if c.weekday(y400,6,i) == c.SUNDAY:
					dchild = dt.datetime(2000+(y400),6,i)
			dflag = dt.datetime(2000+(y400),6,14)		
			dmus = dt.datetime(2000+(y400),6,21)
			dtau = dt.datetime(2000+(y400),6,28)
			dtau1 = dt.datetime(2000+(y400),6,9)
			dtau2 = dt.datetime(2000+(y400),7,9)
			dtau728 = dt.datetime(2000+(y400),7,28)
			dcanada = dt.datetime(2000+(y400),7,1)
			dvgj = dt.datetime(2000+(y400),7,8)
			dmoji = dt.datetime(2000+(y400),7,17)
			dfriend = dt.datetime(2000+(y400),7,30)
			dwww = dt.datetime(2000+(y400),8,1)
			dcat = dt.datetime(2000+(y400),8,8)
			dyouth = dt.datetime(2000+(y400),8,12)
			dphoto = dt.datetime(2000+(y400),8,19)
			dliteracy = dt.datetime(2000+(y400),9,8)
			if y400%4 == 0 and y400%100 == 0 and y400%400 == 0:
				dprogrammer = dt.datetime(2000+(y400),9,12)

			elif y400%4 == 0 and y400%100 == 0 and y400%400 != 0:
				dprogrammer = dt.datetime(2000+(y400),9,13)
			
			elif y400%4 == 0 and y400%100 != 0 and y400%400 != 0:
				dprogrammer = dt.datetime(2000+(y400),9,12)
			elif y400%4 != 0:
				dprogrammer = dt.datetime(2000+(y400),9,13)		
			dvg = dt.datetime(2000+(y400),9,12)
			dmexico = dt.datetime(2000+(y400),9,16)
			dpeace = dt.datetime(2000+(y400),9,21)
			dtour = dt.datetime(2000+(y400),9,27)
			dteach = dt.datetime(2000+(y400),10,5)
			dex6 = dt.datetime(2000+(y400),10,10)
			dex7 = dt.datetime(2000+(y400),12,11)
			dex8 = dt.datetime(2000+(y400),12,12)
			dspt = dt.datetime(2000+(y400),10,16)
			dun = dt.datetime(2000+(y400),10,24)
			dinternet = dt.datetime(2000+(y400),10,29)
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SUNDAY:
					dsteurope2 = dt.datetime(2000+(y400),10,i)
			daids = dt.datetime(2000+(y400),12,1)
			dfut = dt.datetime(2000+(y400),12,2)
			daviation = dt.datetime(2000+(y400),12,7)
			dhumr = dt.datetime(2000+(y400),12,10)
			for i in range (17,24):
				if c.weekday(y400,12,i) == c.SATURDAY:
					dsupersaturday = dt.datetime(2000+(y400),12,i)
			dastro = dt.datetime(2000+(y400),10,9)
			dmus1 = dt.datetime(2000+(y400),10,1)
			dsm = dt.datetime(2000+(y400),6,30)
			dfam0 = dt.datetime(2000+(y400),1,1)
			dfam1 = dt.datetime(2000+(y400),5,15)
			for i in range (22,29):
				if c.weekday(y400,9,i) == c.FRIDAY:
					dnative = dt.datetime(2000+(y400),9,i)
			dhl1 = dt.datetime(2000+(y400),11,1)
			dhl2 = dt.datetime(2000+(y400),11,2)
			dhl3a = dt.datetime(2000+(y400),2,11)
			dhl3b = dt.datetime(2000+(y400),11,3)
			dstandardmo = dt.datetime(2000+(y400),6,1)
			dhumr0 = dt.datetime(2000+(y400),12,9)
			dmeteo = dt.datetime(2000+(y400),3,23)
			for i in range (8,15):
				if c.weekday(y400,2,i) == c.SATURDAY:
					dmovieint = dt.datetime(2000+(y400),2,i)
			for i in range (22,29):
				if c.weekday(y400,7,i) == c.SUNDAY:
					dfd1 = dt.datetime(2000+(y400),7,i)
			dmiku = dt.datetime(2000+(y400),3,9)
			dzm1 = dt.datetime(2000+(y400),11,19)
			dmonth02 = dt.datetime(2000+(y400),2,1)
			dmonth03 = dt.datetime(2000+(y400),3,1)
			dmonth09 = dt.datetime(2000+(y400),9,1)
			dun0000 = dt.datetime(2000+(y400),1,4)
			dun0001 = dt.datetime(2000+(y400),7,13)
			dun0001a = dt.datetime(2000+(y400),7,14)
			dun0002 = dt.datetime(2000+(y400),2,4)
			dun0003 = dt.datetime(2000+(y400),2,10)
			dun0004 = dt.datetime(2000+(y400),2,11)
			dun0005 = dt.datetime(2000+(y400),2,17)
			dun0006 = dt.datetime(2000+(y400),2,20)
			dun0007 = dt.datetime(2000+(y400),3,30)
			dun0008 = dt.datetime(2000+(y400),4,12)
			dun0009 = dt.datetime(2000+(y400),2,21)
			dun000B = dt.datetime(2000+(y400),3,20)
			dun000C = dt.datetime(2000+(y400),3,21)
			dkd = dt.datetime(2000+(y400),4,21)
			dun000D = dt.datetime(2000+(y400),4,24)
			dun000E = dt.datetime(2000+(y400),4,25)
			dun000F = dt.datetime(2000+(y400),4,27)
			dun000G = dt.datetime(2000+(y400),5,2)
			dun0010 = dt.datetime(2000+(y400),5,3)
			dun0011 = dt.datetime(2000+(y400),5,10)
			dun0012 = dt.datetime(2000+(y400),5,12)
			dun0013 = dt.datetime(2000+(y400),5,13)
			dun0014 = dt.datetime(2000+(y400),5,16)
			dun0015 = dt.datetime(2000+(y400),5,17)
			dun0016 = dt.datetime(2000+(y400),5,20)
			dun0017 = dt.datetime(2000+(y400),5,21)
			dun0018 = dt.datetime(2000+(y400),5,29)
			dun0019 = dt.datetime(2000+(y400),5,31)
			dun001A = dt.datetime(2000+(y400),6,3)
			dun001B = dt.datetime(2000+(y400),6,7)
			dun001C = dt.datetime(2000+(y400),6,18)
			dun001D = dt.datetime(2000+(y400),6,20)
			dun001E = dt.datetime(2000+(y400),6,23)
			dun001F = dt.datetime(2000+(y400),6,24)
			dun001G = dt.datetime(2000+(y400),6,25)
			dstitch = dt.datetime(2000+(y400),6,26)
			dun0020 = dt.datetime(2000+(y400),6,27)
			dun0021 = dt.datetime(2000+(y400),6,29)
			dun0022 = dt.datetime(2000+(y400),7,2)
			dun0023 = dt.datetime(2000+(y400),7,11)
			dun0024 = dt.datetime(2000+(y400),7,15)
			dun0025 = dt.datetime(2000+(y400),7,18)
			dun0026 = dt.datetime(2000+(y400),7,20)
			dun0027 = dt.datetime(2000+(y400),8,9)
			dun0028 = dt.datetime(2000+(y400),8,31)
			dun0029 = dt.datetime(2000+(y400),9,5)
			dun002A = dt.datetime(2000+(y400),9,7)
			dun002B = dt.datetime(2000+(y400),9,15)
			dun002C = dt.datetime(2000+(y400),9,23)
			dun002D = dt.datetime(2000+(y400),9,28)
			dun002E = dt.datetime(2000+(y400),9,30)
			dhabt = dt.datetime(2000+(y400),10,2)
			dun002F = dt.datetime(2000+(y400),10,7)
			dun002G = dt.datetime(2000+(y400),10,15)
			dun0030 = dt.datetime(2000+(y400),10,17)
			dun0031 = dt.datetime(2000+(y400),10,27)
			dun0032 = dt.datetime(2000+(y400),11,16)
			dun0033 = dt.datetime(2000+(y400),11,21)
			dun0035 = dt.datetime(2000+(y400),12,3)
			dun0036 = dt.datetime(2000+(y400),12,4)
			dun0037 = dt.datetime(2000+(y400),12,5)
			dun0038 = dt.datetime(2000+(y400),12,18)
			dun0039 = dt.datetime(2000+(y400),12,20)
			dicecream = dt.datetime(2000+(y400),7,16)
			dtiger = dt.datetime(2000+(y400),7,29)
			dmma = dt.datetime(2000+(y400),1,3)
			depi = dt.datetime(2000+(y400),1,6)
			daom = dt.datetime(2000+(y400),8,15)
			for i in range (1,8):
				if c.weekday(y400,3,i) == c.SUNDAY:
					dsunday = dt.datetime(2000+(y400),3,i)
			for i in range (1,8):
				if c.weekday(y400,10,i) == c.FRIDAY:
					dsmile = dt.datetime(2000+(y400),10,i)
			w.write(("    %s - [%d] - %s - 01 - 01  : New Year's Day %04d\n") % (d1.strftime("%j"),(c.weekday(y400,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,1)],y10k))
			w.write(("    %s - [%d] - %s - 01 - 01  : Start Of January %04d [MONTH 01]\n") % (d1.strftime("%j"),(c.weekday(y400,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,1)],y10k))
			w.write(("    %s - [%d] - %s - 01 - 01  : Global Family Day\n") % (dfam0.strftime("%j"),(c.weekday(y400,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,1)]))
			for i in range (1,8):
				if c.weekday(y400,1,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 01 - %02d  : Thank God It's Monday Day\n") % (dtyim.strftime("%j"),mon_number,i))
			w.write(("    %s - [%d] - %s - 01 - 04  : World Braille Day\n") % (dun0000.strftime("%j"),(c.weekday(y400,1,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,4)]))
			w.write(("    %s - [%d] - %s - 01 - 06  : Epiphany\n") % (depi.strftime("%j"),(c.weekday(y400,1,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,6)]))
			for i in range (8,15):
				if c.weekday(y400,1,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 01 - %02d  : Coming Of Age Day\n") % (dcoad.strftime("%j"),mon_number,i))
			w.write(("    %s - [%d] - %s - 01 - 15  : Wikipedia Day\n") % (dwiki.strftime("%j"),(c.weekday(y400,1,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,15)]))
			for i in range (15,22):
				if c.weekday(y400,1,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 01 - %02d  : Martin Luther King Jr. Day\n") % (d2.strftime("%j"),mon_number,i))
			w.write(("    %s - [%d] - %s - 01 - 24  : International Education Day\n") % (dedu.strftime("%j"),(c.weekday(y400,1,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,1,24)]))
			w.write(("    %s - [%d] - %s - 02 - 01  : Start Of February %04d [MONTH 02]\n") % (dmonth02.strftime("%j"),(c.weekday(y400,2,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,1)],y10k))
			w.write(("    %s - [%d] - %s - 02 - 02  : Groundhog Day\n") % (dghd.strftime("%j"),(c.weekday(y400,2,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,2)]))
			w.write(("    %s - [%d] - %s - 02 - 04  : World Human Fraternity Day\n") % (dun0002.strftime("%j"),(c.weekday(y400,2,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,4)]))
			w.write(("    %s - [%d] - %s - 02 - 08  : U.S' Boy-Scout's Day\n") % (dscd0.strftime("%j"),(c.weekday(y400,2,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,8)]))
			w.write(("    %s - [%d] - %s - 02 - 10  : World Pulses Day\n") % (dun0003.strftime("%j"),(c.weekday(y400,2,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,10)]))
			w.write(("    %s - [%d] - %s - 02 - 11  : International Day Of Women And Girls In Science\n") % (dun0004.strftime("%j"),(c.weekday(y400,2,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,11)]))
			w.write(("    %s - [%d] - %s - 02 - 11  : Latest Solar Noon Day (Preferable Date)\n") % (dhl3a.strftime("%j"),(c.weekday(y400,2,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,11)]))
			for i in range (8,15):
				if c.weekday(y400,2,i) == c.SATURDAY:
					w.write(("    %s - [%s] - Sat - 02 - %02d  : World Film/Movie Day\n") % (dmovieint.strftime("%j"),sat_number,i))
			for i in range (8,15):
				if c.weekday(y400,2,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 02 - %02d  : Super Bowl Sunday %04d (Adjusted To Second Sunday Of February)\n") % (dsb.strftime("%j"),sun_number,i,y10k))
			for i in range (15,22):
				if c.weekday(y400,2,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 02 - %02d  : NBA All-Stars Day %04d (Adjusted To Third Sunday Of February)\n") % (dnbaas.strftime("%j"),sun_number,i,y10k))
			for i in range (15,22):
				if c.weekday(y400,2,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 02 - %02d  : President's Day %04d\n") % (d3.strftime("%j"),mon_number,i,y10k))
			w.write(("    %s - [%d] - %s - 02 - 13  : World Radio Day\n") % (dradio.strftime("%j"),(c.weekday(y400,2,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,13)]))
			w.write(("    %s - [%d] - %s - 02 - 14  : Valentine's Day\n") % (dval.strftime("%j"),(c.weekday(y400,2,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,14)]))
			w.write(("    %s - [%d] - %s - 02 - 17  : Global Tourism Resilience Day\n") % (dun0005.strftime("%j"),(c.weekday(y400,2,17)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,17)]))
			w.write(("    %s - [%d] - %s - 02 - 20  : World Social Justice Day\n") % (dun0006.strftime("%j"),(c.weekday(y400,2,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,20)]))
			w.write(("    %s - [%d] - %s - 02 - 21  : International Mother Language Day\n") % (dun0009.strftime("%j"),(c.weekday(y400,2,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,21)]))
			w.write(("    %s - [%d] - %s - 02 - 22  : World Founders Day / World Thinking Day / World Scouts Day\n") % (dscdworld.strftime("%j"),(c.weekday(y400,2,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,22)]))
			w.write(("    %s - [%d] - %s - 02 - 22  : National California Day\n") % (dscdworld.strftime("%j"),(c.weekday(y400,2,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,2,22)]))
			w.write(("    %s - [%d] - %s - 03 - 01  : Start Of March %04d [MONTH 03]\n") % (dmonth03.strftime("%j"),(c.weekday(y400,3,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,1)],y10k))
			w.write(("    %s - [%d] - %s - 03 - 01  : World Seagrass Day\n") % (dmonth03.strftime("%j"),(c.weekday(y400,3,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,1)]))
			w.write(("    %s - [%d] - %s - 03 - 03  : World Wildlife Day\n") % (dex0.strftime("%j"),(c.weekday(y400,3,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,3)]))
			w.write(("    %s - [%d] - %s - 03 - 04  : Pi-Day Approximation 01A\n") % (dmath1x.strftime("%j"),(c.weekday(y400,3,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,4)]))
			w.write(("    %s - [%d] - %s - 03 - 05  : Pi-Day Approximation 01B\n") % (dmath1.strftime("%j"),(c.weekday(y400,3,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,5)]))
			w.write(("    %s - [%d] - %s - 03 - 05  : U.S' Film Day\n") % (dmovie.strftime("%j"),(c.weekday(y400,3,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,5)]))
			w.write(("    %s - [%d] - %s - 03 - 08  : International Women's Day\n") % (dintw.strftime("%j"),(c.weekday(y400,3,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,8)]))
			w.write(("    %s - [%d] - %s - 03 - 09  : 03 - 09 (Mi - Ku) Day\n") % (dmiku.strftime("%j"),(c.weekday(y400,3,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,9)]))
			for i in range (8,15):
				if c.weekday(y400,3,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 03 - %02d  : U.S' Daylight Saving Starts %04d\n") % (dst1.strftime("%j"),sun_number,i,y10k))
			w.write(("    %s - [%d] - %s - 03 - 10  : International Mario Day / MAR10 Day %04d\n") % (dmario.strftime("%j"),(c.weekday(y400,3,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,10)],y10k))
			w.write(("    %s - [%d] - %s - 03 - 12  : U.S' Girl-Scout's Day\n") % (dscd1.strftime("%j"),(c.weekday(y400,3,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,12)]))
			w.write(("    %s - [%d] - %s - 03 - 14  : White Day\n") % (dmath.strftime("%j"),(c.weekday(y400,3,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,14)]))
			w.write(("    %s - [%d] - %s - 03 - 14  : International Mathematics Day (Pi-Day [Centered])\n") % (dmath.strftime("%j"),(c.weekday(y400,3,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,14)]))
			w.write(("    %s - [%d] - %s - 03 - 15  : Pi-Day [Centered] (Elapsed 14.1592653... days)\n") % (dmathx.strftime("%j"),(c.weekday(y400,3,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,15)]))
			w.write(("    %s - [%d] - %s - 03 - 17  : St. Patrick's Day\n") % (dsp.strftime("%j"),(c.weekday(y400,3,17)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,17)]))
			w.write(("    %s - [%d] - %s - 03 - 20  : International Day Of Happiness\n") % (dun000B.strftime("%j"),(c.weekday(y400,3,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,20)]))
			w.write(("    %s - [%d] - %s - 03 - 20  : International French Language Day\n") % (dun000B.strftime("%j"),(c.weekday(y400,3,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,20)]))
			w.write(("    %s - [%d] - %s - 03 - 21  : World Poetry Day\n") % (dun000C.strftime("%j"),(c.weekday(y400,3,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,21)]))
			w.write(("    %s - [%d] - %s - 03 - 21  : World Forests Day\n") % (dun000C.strftime("%j"),(c.weekday(y400,3,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,21)]))
			w.write(("    %s - [%d] - %s - 03 - 22  : World Water Day\n") % (dwater.strftime("%j"),(c.weekday(y400,3,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,22)]))
			w.write(("    %s - [%d] - %s - 03 - 23  : World Meteorogical Day\n") % (dmeteo.strftime("%j"),(c.weekday(y400,3,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,23)]))
			w.write(("    %s - [%d] - %s - 03 - 30  : World Zero-Waste Day\n") % (dun0007.strftime("%j"),(c.weekday(y400,3,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,3,30)]))
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 03 - %02d  : Europe's Daylight Saving Starts %04d\n") % (dsteurope1.strftime("%j"),sun_number,i,y10k))
			w.write(("\n\n    For Earth Hour, Technically Look to LAST SATURDAY IN MARCH, But Pay Attention to the Constraint!"))
			for i in range (18,25):
				if c.weekday(y400,3,i) == c.SATURDAY:
					w.write(("\n\n    %s - [%s] - Sat - 03 - %02d  : Earth Hour Day %04d (NO COINCIDENCE TO HOLY SATURDAY! Refer to Section II to Check!)\n") % (deh0.strftime("%j"),sat_number,i,y10k))
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SATURDAY:
					w.write(("    %s - [%s] - Sat - 03 - %02d  : Earth Hour Day %04d (NO COINCIDENCE TO HOLY SATURDAY! Refer to Section II to Check!)\n\n\n") % (deh1.strftime("%j"),sat_number,i,y10k))
			w.write(("    %s - [%d] - %s - 04 - 01  : Start Of April %04d [MONTH 04]\n") % (dapf.strftime("%j"),(c.weekday(y400,4,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,1)],y10k))
			w.write(("    %s - [%d] - %s - 04 - 01  : April Fools' Day %04d\n") % (dapf.strftime("%j"),(c.weekday(y400,4,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,1)],y10k))
			w.write(("    %s - [%d] - %s - 04 - 04  : 404 Day\n") % (dex404.strftime("%j"),(c.weekday(y400,4,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,4)]))
			w.write(("    %s - [%d] - %s - 04 - 04  : Pi-Day Approximation 02A\n") % (dmath2x.strftime("%j"),(c.weekday(y400,4,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,4)]))
			w.write(("    %s - [%d] - %s - 04 - 05  : Pi-Day Approximation 02B\n") % (dmath2.strftime("%j"),(c.weekday(y400,4,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,5)]))
			w.write(("    %s - [%d] - %s - 04 - 05  : International Day Of Conscience\n") % (dmath2.strftime("%j"),(c.weekday(y400,4,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,5)]))
			w.write(("    %s - [%d] - %s - 04 - 06  : International Sports Day\n") % (darmy.strftime("%j"),(c.weekday(y400,4,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,6)]))
			w.write(("    %s - [%d] - %s - 04 - 06  : U.S' Army Day\n") % (darmy.strftime("%j"),(c.weekday(y400,4,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,6)]))
			w.write(("    %s - [%d] - %s - 04 - 07  : World Health Day\n") % (dhealth.strftime("%j"),(c.weekday(y400,4,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,7)]))
			w.write(("    %s - [%d] - %s - 04 - 09  : World ASMR Day\n") % (dasmr.strftime("%j"),(c.weekday(y400,4,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,9)]))
			w.write(("    %s - [%d] - %s - 04 - 10  : National Siblings Day\n") % (dex5.strftime("%j"),(c.weekday(y400,4,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,10)]))
			w.write(("    %s - [%d] - %s - 04 - 11  : International Pets Day\n") % (dpet.strftime("%j"),(c.weekday(y400,4,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,11)]))
			w.write(("    %s - [%d] - %s - 04 - 12  : International Day Of Human Space Flight\n") % (dun0008.strftime("%j"),(c.weekday(y400,4,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,12)]))
			w.write(("    %s - [%d] - %s - 04 - 13  : International Plant Appreciation Day\n") % (dstandard.strftime("%j"),(c.weekday(y400,4,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,13)]))
			w.write(("    %s - [%d] - %s - 04 - 13  : Thomas Jefferson Day\n") % (dstandard.strftime("%j"),(c.weekday(y400,4,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,13)]))
			w.write(("    %s - [%d] - %s - 04 - 14  : Pi Approximation Day 02C\n") % (dmath414.strftime("%j"),(c.weekday(y400,4,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,14)]))
			w.write(("    %s - [%d] - %s - 04 - 15  : Pi Apporximation Day 02D\n") % (dart.strftime("%j"),(c.weekday(y400,4,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,15)]))
			w.write(("    %s - [%d] - %s - 04 - 15  : World Arts Day\n") % (dart.strftime("%j"),(c.weekday(y400,4,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,15)]))
			w.write(("    %s - [%d] - %s - 04 - 15  : International Anime Day %04d\n") % (dart.strftime("%j"),(c.weekday(y400,4,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,15)],y10k))
			for i in range (15,22):
				if c.weekday(y400,4,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 04 - %02d  : Patriots Day\n") % (dpatr.strftime("%j"),mon_number,i))
			w.write(("    %s - [%d] - %s - 04 - 20  : World Chinese Language Day\n") % (dedm.strftime("%j"),(c.weekday(y400,4,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,20)]))
			w.write(("    %s - [%d] - %s - 04 - 20  : World EDM Tribute Day %04d\n") % (dedm.strftime("%j"),(c.weekday(y400,4,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,20)],y10k))
			w.write(("    %s - [%d] - %s - 04 - 21  : World Creativity And Innovation Day\n") % (dkd.strftime("%j"),(c.weekday(y400,4,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,21)]))
			w.write(("    %s - [%d] - %s - 04 - 22  : International Earth Day %04d\n") % (dearth.strftime("%j"),(c.weekday(y400,4,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,22)],y10k))
			w.write(("    %s - [%d] - %s - 04 - 23  : World Book And Copyright Day %04d\n") % (dbook.strftime("%j"),(c.weekday(y400,4,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,23)],y10k))
			w.write(("    %s - [%d] - %s - 04 - 23  : English Language Day\n") % (dbook.strftime("%j"),(c.weekday(y400,4,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,23)]))
			w.write(("    %s - [%d] - %s - 04 - 23  : Spanish Language Day\n") % (dbook.strftime("%j"),(c.weekday(y400,4,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,23)]))
			w.write(("    %s - [%d] - %s - 04 - 24  : Multirateral And Diplomacy For Peace Day\n") % (dun000D.strftime("%j"),(c.weekday(y400,4,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,24)]))
			w.write(("    %s - [%d] - %s - 04 - 25  : World Delegate's Day\n") % (dun000E.strftime("%j"),(c.weekday(y400,4,25)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,25)]))
			w.write(("    %s - [%d] - %s - 04 - 27  : World Girls In ICT Day\n") % (dun000F.strftime("%j"),(c.weekday(y400,4,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,27)]))
			for i in range (24,31):
				if c.weekday(y400,4,i) == c.SATURDAY:
					w.write(("    %s - [%s] - Sat - 04 - %02d  : World Tai-Chi And Qi-Gong Day %04d\n") % (dtc.strftime("%j"),sat_number,i,y10k))
			w.write(("    %s - [%d] - %s - 04 - 29  : International Dance Day\n") % (ddance.strftime("%j"),(c.weekday(y400,4,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,29)]))
			w.write(("    %s - [%d] - %s - 04 - 30  : International Jazz Day\n") % (ddance1.strftime("%j"),(c.weekday(y400,4,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,4,30)]))
			w.write(("    %s - [%d] - %s - 05 - 01  : Start Of May %04d [MONTH 05]\n") % (dlab.strftime("%j"),(c.weekday(y400,5,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,1)],y10k))
			w.write(("    %s - [%d] - %s - 05 - 01  : International Labors Day %04d\n") % (dlab.strftime("%j"),(c.weekday(y400,5,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,1)],y10k))
			for i in range (1,8):
				if c.weekday(y400,5,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 05 - %02d  : Met Gala %04d (Adjusted To First Monday Of May)\n") % (dmetgala.strftime("%j"),mon_number,i,y10k))
			w.write(("    %s - [%d] - %s - 05 - 02  : World Tuna Day\n") % (dun000G.strftime("%j"),(c.weekday(y400,5,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,2)]))
			w.write(("    %s - [%d] - %s - 05 - 03  : World Press Freedom Day\n") % (dun0010.strftime("%j"),(c.weekday(y400,5,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,3)]))
			w.write(("    %s - [%d] - %s - 05 - 04  : Star Wars Day %04d\n") % (dswd.strftime("%j"),(c.weekday(y400,5,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,4)],y10k))
			w.write(("    %s - [%d] - %s - 05 - 05  : Revenge Of The Fifth %04d\n") % (dcdm.strftime("%j"),(c.weekday(y400,5,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,5)],y10k))
			w.write(("    %s - [%d] - %s - 05 - 05  : Fifth Of May (Cinco De Mayo)\n") % (dcdm.strftime("%j"),(c.weekday(y400,5,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,5)]))
			w.write(("    %s - [%d] - %s - 05 - 05  : World Portuguese Language Day\n") % (dcdm.strftime("%j"),(c.weekday(y400,5,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,5)]))
			w.write(("    %s - [%d] - %s - 05 - 06  : Revenge Of The Sixth %04d\n") % (dsixth.strftime("%j"),(c.weekday(y400,5,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,6)],y10k))
			for i in range (8,15):
				if c.weekday(y400,5,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 05 - %02d  : U.S' Mothers Day %04d\n") % (dmd.strftime("%j"),sun_number,i,y10k))
			w.write(("    %s - [%d] - %s - 05 - 10  : International Argania Day\n") % (dun0011.strftime("%j"),(c.weekday(y400,5,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,10)]))
			w.write(("    %s - [%d] - %s - 05 - 11  : National Technology Day\n") % (dtech.strftime("%j"),(c.weekday(y400,5,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,11)]))
			w.write(("    %s - [%d] - %s - 05 - 12  : Plants Health Day\n") % (dun0012.strftime("%j"),(c.weekday(y400,5,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,12)]))
			w.write(("    %s - [%d] - %s - 05 - 13  : World Migratory Bird Day (May Edition)\n") % (dun0013.strftime("%j"),(c.weekday(y400,5,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,13)]))
			w.write(("    %s - [%d] - %s - 05 - 15  : International Family Day\n") % (dfam1.strftime("%j"),(c.weekday(y400,5,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,15)]))
			w.write(("    %s - [%d] - %s - 05 - 15  : U.S' Peace Officers Memorial Day (General Observed Date)\n") % (dplc.strftime("%j"),(c.weekday(y400,5,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,15)]))
			w.write(("    %s - [%d] - %s - 05 - 16  : International Day Of Light\n") % (dun0014.strftime("%j"),(c.weekday(y400,5,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,16)]))
			w.write(("    %s - [%d] - %s - 05 - 16  : International Day Of Peace Living\n") % (dun0014.strftime("%j"),(c.weekday(y400,5,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,16)]))
			w.write(("    %s - [%d] - %s - 05 - 17  : World Telecommunication And Information Society Day\n") % (dun0015.strftime("%j"),(c.weekday(y400,5,17)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,17)]))
			w.write(("    %s - [%d] - %s - 05 - 20  : World Bee Day\n") % (dun0016.strftime("%j"),(c.weekday(y400,5,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,20)]))
			w.write(("    %s - [%d] - %s - 05 - 21  : World Tea Day\n") % (dun0017.strftime("%j"),(c.weekday(y400,5,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,21)]))
			w.write(("    %s - [%d] - %s - 05 - 21  : World Cultural Diversity Day\n") % (dun0017.strftime("%j"),(c.weekday(y400,5,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,21)]))
			for i in range (15,22):
				if c.weekday(y400,5,i) == c.SATURDAY:
					w.write(("    %s - [%s] - Sat - 05 - %02d  : U.S' Armed Forces Day\n") % (darmed.strftime("%j"),sat_number,i))
			w.write(("    %s - [%d] - %s - 05 - 22  : International Day Of Biological Diversity\n") % (dbiology.strftime("%j"),(c.weekday(y400,5,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,22)]))
			w.write(("    %s - [%d] - %s - 05 - 23  : World Turtle Day\n") % (dbiology1.strftime("%j"),(c.weekday(y400,5,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,23)]))
			for i in range (24,31):
				if c.weekday(y400,5,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 05 - %02d  : Indianapolis 500 %04d (Adjusted To Sunday Next To Day)\n") % (dip.strftime("%j"),sun_number,i,y10k))
			for i in range (25,32):
				if c.weekday(y400,5,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 05 - %02d  : Memorial Day %04d\n") % (d4.strftime("%j"),mon_number,i,y10k))
			w.write(("    %s - [%d] - %s - 05 - 29  : International Day Of UN Peacekeeping\n") % (dun0018.strftime("%j"),(c.weekday(y400,5,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,29)]))
			w.write(("    %s - [%d] - %s - 05 - 31  : International Day Of Anti-Tobacco\n") % (dun0019.strftime("%j"),(c.weekday(y400,5,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,5,31)]))
			w.write(("    %s - [%d] - %s - 06 - 01  : Start Of June %04d [MONTH 06]\n") % (dstandardmo.strftime("%j"),(c.weekday(y400,6,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,1)],y10k))
			w.write(("    %s - [%d] - %s - 06 - 01  : International Children Day\n") % (dstandardmo.strftime("%j"),(c.weekday(y400,6,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,1)]))
			w.write(("    %s - [%d] - %s - 06 - 01  : Global Parents Day\n") % (dstandardmo.strftime("%j"),(c.weekday(y400,6,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,1)]))
			w.write(("    %s - [%d] - %s - 06 - 03  : World Bicycle Day\n") % (dun001A.strftime("%j"),(c.weekday(y400,6,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,3)]))
			w.write(("    %s - [%d] - %s - 06 - 05  : World Environment Day\n") % (denv.strftime("%j"),(c.weekday(y400,6,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,5)]))
			w.write(("    %s - [%d] - %s - 06 - 06  : Russian Language Day\n") % (dex1.strftime("%j"),(c.weekday(y400,6,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,6)]))
			w.write(("    %s - [%d] - %s - 06 - 06  : D-Day Remembrance Day\n") % (dex1.strftime("%j"),(c.weekday(y400,6,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,6)]))
			w.write(("    %s - [%d] - %s - 06 - 07  : World Food Safety Day\n") % (dun001B.strftime("%j"),(c.weekday(y400,6,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,7)]))
			w.write(("    %s - [%d] - %s - 06 - 08  : World Ocean Day\n") % (docean.strftime("%j"),(c.weekday(y400,6,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,8)]))
			w.write(("    %s - [%d] - %s - 06 - 08  : Tau Approximation Day 01A\n") % (docean.strftime("%j"),(c.weekday(y400,6,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,8)]))
			w.write(("    %s - [%d] - %s - 06 - 09  : Tau Approximation Day 01B\n") % (dtau1.strftime("%j"),(c.weekday(y400,6,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,9)]))
			w.write(("    %s - [%d] - %s - 06 - 09  : Global Integrity Day\n") % (dtau1.strftime("%j"),(c.weekday(y400,6,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,9)]))
			for i in range (8,15):
				if c.weekday(y400,6,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 06 - %02d  : U.S' Children Day\n") % (dchild.strftime("%j"),sun_number,i))
			w.write(("    %s - [%d] - %s - 06 - 14  : U.S' Flag Day\n") % (dflag.strftime("%j"),(c.weekday(y400,6,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,14)]))
			for i in range (15,22):
				if c.weekday(y400,6,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 06 - %02d  : U.S' Fathers Day %04d\n") % (dfd.strftime("%j"),sun_number,i,y10k))
			w.write(("    %s - [%d] - %s - 06 - 18  : World Sustainable Gastronomy Day\n") % (dun001C.strftime("%j"),(c.weekday(y400,6,18)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,18)]))
			w.write(("    %s - [%d] - %s - 06 - 19  : Juneteenth\n") % (d5.strftime("%j"),(c.weekday(y400,6,19)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,19)]))
			w.write(("    %s - [%d] - %s - 06 - 20  : World Refugee Day\n") % (dun001D.strftime("%j"),(c.weekday(y400,6,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,20)]))
			w.write(("    %s - [%d] - %s - 06 - 21  : U.S' Music Day %04d\n") % (dmus.strftime("%j"),(c.weekday(y400,6,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,21)],y10k))
			w.write(("    %s - [%d] - %s - 06 - 21  : International Yoga Day %04d\n") % (dmus.strftime("%j"),(c.weekday(y400,6,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,21)],y10k))
			w.write(("    %s - [%d] - %s - 06 - 23  : World Public Service Day\n") % (dun001E.strftime("%j"),(c.weekday(y400,6,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,23)]))
			w.write(("    %s - [%d] - %s - 06 - 24  : Women In Diplomacy Day\n") % (dun001F.strftime("%j"),(c.weekday(y400,6,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,24)]))
			w.write(("    %s - [%d] - %s - 06 - 25  : Seafarer Day\n") % (dun001G.strftime("%j"),(c.weekday(y400,6,25)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,25)]))
			w.write(("    %s - [%d] - %s - 06 - 26  : 0626 Day (Originated From Stitch 626 Jargon Number)\n") % (dstitch.strftime("%j"),(c.weekday(y400,6,26)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,26)]))
			w.write(("    %s - [%d] - %s - 06 - 27  : Micro To Medium-Sized Enterprise Day\n") % (dun0020.strftime("%j"),(c.weekday(y400,6,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,27)]))
			w.write(("    %s - [%d] - %s - 06 - 28  : Tau Day\n") % (dtau.strftime("%j"),(c.weekday(y400,6,28)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,28)]))
			w.write(("    %s - [%d] - %s - 06 - 29  : International Tropics Day\n") % (dun0021.strftime("%j"),(c.weekday(y400,6,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,29)]))
			w.write(("    %s - [%d] - %s - 06 - 30  : World/International Social Media Day\n") % (dsm.strftime("%j"),(c.weekday(y400,6,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,30)]))
			w.write(("    %s - [%d] - %s - 06 - 30  : World/International Asteroid Day\n") % (dsm.strftime("%j"),(c.weekday(y400,6,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,30)]))
			w.write(("    %s - [%d] - %s - 06 - 30  : World/International Parliament Day\n") % (dsm.strftime("%j"),(c.weekday(y400,6,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,30)]))
			w.write(("    %s - [%d] - %s - 07 - 01  : Start Of July %04d [MONTH 07]\n") % (dcanada.strftime("%j"),(c.weekday(y400,7,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,1)],y10k))
			w.write(("    %s - [%d] - %s - 07 - 01  : Canada Day %04d\n") % (dcanada.strftime("%j"),(c.weekday(y400,7,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,1)],y10k))
			w.write(("    %s - [%d] - %s - 07 - 02  : International Cooperatives Day\n") % (dun0022.strftime("%j"),(c.weekday(y400,7,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,6,29)]))
			w.write(("    %s - [%d] - %s - 07 - 03  : Crown Day\n") % (dcrown.strftime("%j"),(c.weekday(y400,7,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,3)]))
			w.write(("    %s - [%d] - %s - 07 - 04  : U.S' Independence Day %04d\n") % (d6.strftime("%j"),(c.weekday(y400,7,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,4)],y10k))
			w.write(("    %s - [%d] - %s - 07 - 05  : U.S' Independence Post-Day %04d Day 01\n") % (d60.strftime("%j"),(c.weekday(y400,7,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,5)],y10k))
			w.write(("    %s - [%d] - %s - 07 - 06  : U.S' Independence Post-Day %04d Day 02\n") % (d61.strftime("%j"),(c.weekday(y400,7,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,6)],y10k))
			w.write(("    %s - [%d] - %s - 07 - 06  : World Fried Chicken Day\n") % (d61.strftime("%j"),(c.weekday(y400,7,6)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,6)]))
			w.write(("    %s - [%d] - %s - 07 - 07  : International Kiswahili Language Day\n") % (dex4.strftime("%j"),(c.weekday(y400,7,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,7)]))
			w.write(("    %s - [%d] - %s - 07 - 07  : International Peace And Love Day\n") % (dex4.strftime("%j"),(c.weekday(y400,7,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,7)]))
			w.write(("    %s - [%d] - %s - 07 - 08  : National Day Of Video Games (July Edition)\n") % (dvgj.strftime("%j"),(c.weekday(y400,7,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,8)]))
			w.write(("    %s - [%d] - %s - 07 - 08  : Tau Approximation Day 02A\n") % (dvgj.strftime("%j"),(c.weekday(y400,7,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,8)]))
			w.write(("    %s - [%d] - %s - 07 - 09  : Tau Approximation Day 02B\n") % (dtau2.strftime("%j"),(c.weekday(y400,7,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,9)]))
			w.write(("    %s - [%d] - %s - 07 - 11  : World Population Day\n") % (dun0023.strftime("%j"),(c.weekday(y400,7,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,11)]))
			w.write(("    %s - [%d] - %s - 07 - 13  : National French Fries Day\n") % (dun0001.strftime("%j"),(c.weekday(y400,7,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,13)]))
			w.write(("    %s - [%d] - %s - 07 - 14  : French Independence Day\n") % (dun0001a.strftime("%j"),(c.weekday(y400,7,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,14)]))
			w.write(("    %s - [%d] - %s - 07 - 15  : World Youth Skills Day\n") % (dun0024.strftime("%j"),(c.weekday(y400,7,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,15)]))
			w.write(("    %s - [%d] - %s - 07 - 16  : National Ice Cream Day\n") % (dicecream.strftime("%j"),(c.weekday(y400,7,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,16)]))
			w.write(("    %s - [%d] - %s - 07 - 17  : World Emoji Day\n") % (dmoji.strftime("%j"),(c.weekday(y400,7,17)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,17)]))
			w.write(("    %s - [%d] - %s - 07 - 18  : World Nelson Mandela Day\n") % (dun0025.strftime("%j"),(c.weekday(y400,7,18)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,18)]))
			w.write(("    %s - [%d] - %s - 07 - 20  : World Moon Day\n") % (dun0026.strftime("%j"),(c.weekday(y400,7,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,20)]))
			w.write(("    %s - [%d] - %s - 07 - 20  : World Chess Day\n") % (dun0026.strftime("%j"),(c.weekday(y400,7,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,20)]))
			w.write(("    %s - [%d] - %s - 07 - 22  : Pi-Day Approximation 03A\n") % (dmath4.strftime("%j"),(c.weekday(y400,7,22)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,22)]))
			w.write(("    %s - [%d] - %s - 07 - 23  : Pi-Day Approximation 03B\n") % (dmath4x.strftime("%j"),(c.weekday(y400,7,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,23)]))
			w.write(("    %s - [%d] - %s - 07 - 28  : Tau Approximation Day 03A\n") % (dtau728.strftime("%j"),(c.weekday(y400,7,28)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,28)]))
			w.write(("    %s - [%d] - %s - 07 - 29  : Tau Approximation Day 03B\n") % (dtiger.strftime("%j"),(c.weekday(y400,7,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,29)]))
			for i in range (22,29):
				if c.weekday(y400,7,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 07 - %02d  : U.S' Parents Day\n") % (dfd1.strftime("%j"),sun_number,i))
			w.write(("    %s - [%d] - %s - 07 - 29  : World Tiger Day\n") % (dtiger.strftime("%j"),(c.weekday(y400,7,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,29)]))
			w.write(("    %s - [%d] - %s - 07 - 30  : International Friendship Day\n") % (dfriend.strftime("%j"),(c.weekday(y400,7,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,7,30)]))
			w.write(("    %s - [%d] - %s - 08 - 01  : Start Of August %04d [MONTH 08]\n") % (dwww.strftime("%j"),(c.weekday(y400,8,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,1)],y10k))
			w.write(("    %s - [%d] - %s - 08 - 01  : World Wide Web Day\n") % (dwww.strftime("%j"),(c.weekday(y400,8,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,1)]))
			w.write(("    %s - [%d] - %s - 08 - 08  : International Cat Day\n") % (dcat.strftime("%j"),(c.weekday(y400,8,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,8)]))
			w.write(("    %s - [%d] - %s - 08 - 08  : ASEAN Day\n") % (dcat.strftime("%j"),(c.weekday(y400,8,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,8)]))
			w.write(("    %s - [%d] - %s - 08 - 09  : World Indigenous Day\n") % (dun0027.strftime("%j"),(c.weekday(y400,8,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,9)]))
			w.write(("    %s - [%d] - %s - 08 - 12  : International Youth Day\n") % (dyouth.strftime("%j"),(c.weekday(y400,8,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,12)]))
			w.write(("    %s - [%d] - %s - 08 - 15  : Assumption Of Mary\n") % (daom.strftime("%j"),(c.weekday(y400,8,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,15)]))
			w.write(("    %s - [%d] - %s - 08 - 19  : World Photography Day\n") % (dphoto.strftime("%j"),(c.weekday(y400,8,19)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,19)]))
			w.write(("    %s - [%d] - %s - 08 - 19  : World Humanitarian Day\n") % (dphoto.strftime("%j"),(c.weekday(y400,8,19)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,19)]))
			w.write(("    %s - [%d] - %s - 08 - 23  : Pi-Day Approximation 04\n") % (dmath823.strftime("%j"),(c.weekday(y400,8,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,23)]))
			w.write(("    %s - [%d] - %s - 08 - 31  : World People Of African Descent Day\n") % (dun0028.strftime("%j"),(c.weekday(y400,8,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,31)]))
			w.write(("    %s - [%d] - %s - 08 - 31  : International Vocaloid Day %04d\n") % (dun0028.strftime("%j"),(c.weekday(y400,8,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,8,31)],y10k))
			w.write(("    %s - [%d] - %s - 09 - 01  : Start Of September %04d [MONTH 09]\n") % (dmonth09.strftime("%j"),(c.weekday(y400,9,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,1)],y10k))
			for i in range (1,8):
				if c.weekday(y400,9,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 09 - %02d  : U.S' Labors Day %04d\n") % (d7.strftime("%j"),mon_number,i,y10k))
			w.write(("    %s - [%d] - %s - 09 - 05  : International Charity Day\n") % (dun0029.strftime("%j"),(c.weekday(y400,9,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,5)]))
			w.write(("    %s - [%d] - %s - 09 - 07  : International Clean Air For Blue Skies Day\n") % (dun002A.strftime("%j"),(c.weekday(y400,9,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,7)]))
			w.write(("    %s - [%d] - %s - 09 - 08  : International Literacy Day\n") % (dliteracy.strftime("%j"),(c.weekday(y400,9,8)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,8)]))
			w.write(("    %s - [%d] - %s - 09 - 09  : 09 - 09 Day\n") % (dex3.strftime("%j"),(c.weekday(y400,9,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,9)]))
			w.write(("    %s - [%d] - %s - 09 - 11  : 09 - 11 Remembrance Day\n") % (dex2.strftime("%j"),(c.weekday(y400,9,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,11)]))
			w.write(("    %s - [%d] - %s - 09 - 12  : National Day Of Video Games (September Edition)\n") % (dvg.strftime("%j"),(c.weekday(y400,9,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,12)]))
			if y400%4 == 0 and y400%100 == 0 and y400%400 == 0:
				w.write(("    %s - [%d] - %s - 09 - 12  : World Programmers Day %04d\n") % (dprogrammer.strftime("%j"),(c.weekday(y400,9,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,12)],y10k))
			elif y400%4 == 0 and y400%100 == 0 and y400%400 != 0:
				w.write(("    %s - [%d] - %s - 09 - 13  : World Programmers Day %04d\n") % (dprogrammer.strftime("%j"),(c.weekday(y400,9,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,13)],y10k))
			elif y400%4 == 0 and y400%100 != 0 and y400%400 != 0:
				w.write(("    %s - [%d] - %s - 09 - 12  : World Programmers Day %04d\n") % (dprogrammer.strftime("%j"),(c.weekday(y400,9,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,12)],y10k))
			elif y400%4 != 0:
				w.write(("    %s - [%d] - %s - 09 - 13  : World Programmers Day %04d\n") % (dprogrammer.strftime("%j"),(c.weekday(y400,9,13)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,13)],y10k))
			w.write(("    %s - [%d] - %s - 09 - 15  : International Democracy Day\n") % (dun002B.strftime("%j"),(c.weekday(y400,9,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,15)]))
			w.write(("    %s - [%d] - %s - 09 - 16  : Mexico's Independence Day\n") % (dmexico.strftime("%j"),(c.weekday(y400,9,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,16)]))
			w.write(("    %s - [%d] - %s - 09 - 21  : International Day Of Peace\n") % (dpeace.strftime("%j"),(c.weekday(y400,9,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,21)]))
			w.write(("    %s - [%d] - %s - 09 - 23  : International Sign-Language Day\n") % (dun002C.strftime("%j"),(c.weekday(y400,9,23)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,23)]))
			for i in range (22,29):
				if c.weekday(y400,9,i) == c.FRIDAY:
					w.write(("    %s - [%s] - Fri - 09 - %02d  : Native Day (California Date)\n") % (dnative.strftime("%j"),fri_number,i))
			w.write(("    %s - [%d] - %s - 09 - 27  : World Tourism Day\n") % (dtour.strftime("%j"),(c.weekday(y400,9,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,27)]))
			w.write(("    %s - [%d] - %s - 09 - 28  : International Maritime Day\n") % (dun002D.strftime("%j"),(c.weekday(y400,9,28)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,28)]))
			w.write(("    %s - [%d] - %s - 09 - 30  : International Translation Day\n") % (dun002E.strftime("%j"),(c.weekday(y400,9,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,9,30)]))
			w.write(("    %s - [%d] - %s - 10 - 01  : Start Of October %04d [MONTH 10]\n") % (dmus1.strftime("%j"),(c.weekday(y400,10,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,1)],y10k))
			for i in range (1,8):
				if c.weekday(y400,10,i) == c.FRIDAY:
					w.write(("    %s - [%s] - Fri - 10 - %02d  : World Smile Day\n") % (dsmile.strftime("%j"),fri_number,i))
			w.write(("    %s - [%d] - %s - 10 - 01  : International Day Of Older Persons Day\n") % (dmus1.strftime("%j"),(c.weekday(y400,10,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,1)]))
			w.write(("    %s - [%d] - %s - 10 - 01  : World/International Music Day\n") % (dmus1.strftime("%j"),(c.weekday(y400,10,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,1)]))
			w.write(("    %s - [%d] - %s - 10 - 01  : World/International Coffee Day\n") % (dmus1.strftime("%j"),(c.weekday(y400,10,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,1)]))
			w.write(("    %s - [%d] - %s - 10 - 02  : World Habitat And Non-Violence Day\n") % (dhabt.strftime("%j"),(c.weekday(y400,10,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,2)]))
			w.write(("    %s - [%d] - %s - 10 - 05  : World Teachers Day\n") % (dteach.strftime("%j"),(c.weekday(y400,10,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,5)]))
			w.write(("    %s - [%d] - %s - 10 - 07  : World Cotton Day\n") % (dun002F.strftime("%j"),(c.weekday(y400,10,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,7)]))
			w.write(("    %s - [%d] - %s - 10 - 09  : World/International Astronomy Day\n") % (dastro.strftime("%j"),(c.weekday(y400,10,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,9)]))
			w.write(("    %s - [%d] - %s - 10 - 09  : World/International Post Day\n") % (dastro.strftime("%j"),(c.weekday(y400,10,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,9)]))
			w.write(("    %s - [%d] - %s - 10 - 10  : World Mental Health Day\n") % (dex6.strftime("%j"),(c.weekday(y400,10,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,10)]))
			for i in range (8,15):
				if c.weekday(y400,10,i) == c.MONDAY:
					w.write(("    %s - [%s] - Mon - 10 - %02d  : Columbus Day\n") % (d8.strftime("%j"),mon_number,i))
			w.write(("    %s - [%d] - %s - 10 - 14  : World Migratory Bird Day (October Edition)\n") % (dstandardori.strftime("%j"),(c.weekday(y400,10,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,14)]))
			w.write(("    %s - [%d] - %s - 10 - 14  : World's Standards Day\n") % (dstandardori.strftime("%j"),(c.weekday(y400,10,14)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,14)]))
			w.write(("    %s - [%d] - %s - 10 - 15  : World Rural Women Day\n") % (dun002G.strftime("%j"),(c.weekday(y400,10,15)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,15)]))
			w.write(("    %s - [%d] - %s - 10 - 16  : U.S' Sports Day\n") % (dspt.strftime("%j"),(c.weekday(y400,10,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,16)]))
			w.write(("    %s - [%d] - %s - 10 - 16  : Boss Day\n") % (dspt.strftime("%j"),(c.weekday(y400,10,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,16)]))
			w.write(("    %s - [%d] - %s - 10 - 16  : World Food Day\n") % (dspt.strftime("%j"),(c.weekday(y400,10,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,16)]))
			w.write(("    %s - [%d] - %s - 10 - 17  : Eradication Of Poverty Day\n") % (dun0030.strftime("%j"),(c.weekday(y400,10,17)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,17)]))
			w.write(("    %s - [%d] - %s - 10 - 24  : United Nations Day %04d\n") % (dun.strftime("%j"),(c.weekday(y400,10,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,24)],y10k))
			w.write(("    %s - [%d] - %s - 10 - 27  : World Audiovisual Heritage Day\n") % (dun0031.strftime("%j"),(c.weekday(y400,10,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,27)]))
			w.write(("    %s - [%d] - %s - 10 - 29  : National Internet Day\n") % (dinternet.strftime("%j"),(c.weekday(y400,10,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,29)]))
			w.write(("    %s - [%d] - %s - 10 - 31  : Halloween %04d\n") % (dhl.strftime("%j"),(c.weekday(y400,10,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,31)],y10k))
			w.write(("    %s - [%d] - %s - 10 - 31  : World Cities Day\n") % (dhl.strftime("%j"),(c.weekday(y400,10,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,10,31)]))
			for i in range (25,32):
				if c.weekday(y400,3,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 10 - %02d  : Europe's Daylight Saving Ends %04d\n") % (dsteurope2.strftime("%j"),sun_number,i,y10k))
			w.write(("    %s - [%d] - %s - 11 - 01  : Start Of November %04d [MONTH 11]\n") % (dhl1.strftime("%j"),(c.weekday(y400,11,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,1)],y10k))
			for i in range (1,8):
				if c.weekday(y400,11,i) == c.SUNDAY:
					w.write(("    %s - [%s] - Sun - 11 - %02d  : U.S' Daylight Saving Ends %04d\n") % (dst0.strftime("%j"),sun_number,i,y10k))
			w.write(("    %s - [%d] - %s - 11 - 01  : All Saints Day\n") % (dhl1.strftime("%j"),(c.weekday(y400,11,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,1)]))
			w.write(("    %s - [%d] - %s - 11 - 02  : Day Of The Dead (Mexico)\n") % (dhl2.strftime("%j"),(c.weekday(y400,11,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,2)]))
			w.write(("    %s - [%d] - %s - 11 - 03  : Earliest Solar Noon Day (Preferable Date)\n") % (dhl3b.strftime("%j"),(c.weekday(y400,11,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,3)]))
			for i in range (2,9):
				if c.weekday(y400,11,i) == c.TUESDAY:
					w.write(("    %s - [%s] - Tue - 11 - %02d  : U.S' Election's Day %04d (Annual U.S' Election Tuesday)\n") % (delc.strftime("%j"),tue_number,i,y10k))
			for i in range (9,11):
				if dt.datetime(2000+(y400),11,i).strftime("%j") == "314":
					w.write(("    %s - [%d] - %s - 11 - %02d  : Pi-Day Approximation 05A\n") % (dmath3.strftime("%j"),(c.weekday(y400,11,i)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,i)],i))
			for i in range (10,12):
				if dt.datetime(2000+(y400),11,i).strftime("%j") == "315":
					w.write(("    %s - [%d] - %s - 11 - %02d  : Pi-Day Approximation 05B\n") % (dmath3x.strftime("%j"),(c.weekday(y400,11,i)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,i)],i))
			w.write(("    %s - [%d] - %s - 11 - 11  : U.S' Veterans Day %04d\n") % (d9.strftime("%j"),(c.weekday(y400,11,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,11)],y10k))
			w.write(("    %s - [%d] - %s - 11 - 16  : World Tolerance And Philosophy Day\n") % (dun0032.strftime("%j"),(c.weekday(y400,11,16)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,16)]))
			w.write(("    %s - [%d] - %s - 11 - 19  : International Men's Day\n") % (dzm1.strftime("%j"),(c.weekday(y400,11,19)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,19)]))
			w.write(("    %s - [%d] - %s - 11 - 21  : World Television Day\n") % (dun0033.strftime("%j"),(c.weekday(y400,11,21)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,11,21)]))
			for i in range (22,29):
				if c.weekday(y400,11,i) == c.THURSDAY:
					w.write(("    %s - [%s] - Thu - 11 - %02d  : Thanksgiving Day %04d\n") % (d10.strftime("%j"),thu_number,i,y10k))
					w.write(("    %s - [%s] - Fri - 11 - %02d  : Black Friday %04d\n") % (d10a.strftime("%j"),fri_number,i+1,y10k))
					w.write(("    %s - [%s] - Sat - 11 - %02d  : Small Business Saturday %04d\n") % (d10b.strftime("%j"),sat_number,i+2,y10k))
					w.write(("    %s - [%s] - Sun - %02d - %02d  : Secondhand Sunday %04d\n") % (d10c.strftime("%j"),sun_number,d10c.month,d10c.day,y10k))
					w.write(("    %s - [%s] - Mon - %02d - %02d  : Cyber Monday %04d\n") % (d10d.strftime("%j"),mon_number,d10d.month,d10d.day,y10k))
					w.write(("    %s - [%s] - Tue - %02d - %02d  : Giving Tuesday %04d\n") % (d10e.strftime("%j"),tue_number,d10e.month,d10e.day,y10k))
					w.write(("    %s - [%s] - Wed - %02d - %02d  : Package Protection Wednesday %04d\n") % (d10f.strftime("%j"),wed_number,d10f.month,d10f.day,y10k))
			w.write(("    %s - [%d] - %s - 12 - 01  : Start Of December %04d [MONTH 12]\n") % (daids.strftime("%j"),(c.weekday(y400,12,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,1)],y10k))
			w.write(("    %s - [%d] - %s - 12 - 01  : World AIDS Day\n") % (daids.strftime("%j"),(c.weekday(y400,12,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,1)]))
			w.write(("    %s - [%d] - %s - 12 - 02  : World Futures Day\n") % (dfut.strftime("%j"),(c.weekday(y400,12,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,2)]))
			w.write(("    %s - [%d] - %s - 12 - 02  : World Nuclear Day\n") % (dfut.strftime("%j"),(c.weekday(y400,12,2)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,2)]))
			for i in range (17,24):
				if c.weekday(y400,12,i) == c.SATURDAY:
					w.write(("    %s - [%s] - Sat - 12 - %02d  : Super Saturday %04d \n") % (dsupersaturday.strftime("%j"),sat_number,i,y10k))
			w.write(("    %s - [%d] - %s - 12 - 03  : International Disability People's Day\n") % (dun0035.strftime("%j"),(c.weekday(y400,12,3)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,3)]))
			w.write(("    %s - [%d] - %s - 12 - 04  : International Banks Day\n") % (dun0036.strftime("%j"),(c.weekday(y400,12,4)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,4)]))
			w.write(("    %s - [%d] - %s - 12 - 05  : International Soil Day\n") % (dun0037.strftime("%j"),(c.weekday(y400,12,5)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,5)]))
			w.write(("    %s - [%d] - %s - 12 - 07  : International Aviation Day\n") % (daviation.strftime("%j"),(c.weekday(y400,12,7)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,7)]))
			w.write(("    %s - [%d] - %s - 12 - 09  : International Anticorruption Day\n") % (dhumr0.strftime("%j"),(c.weekday(y400,12,9)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,9)]))
			w.write(("    %s - [%d] - %s - 12 - 10  : International Human Rights Day\n") % (dhumr.strftime("%j"),(c.weekday(y400,12,10)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,10)]))
			w.write(("    %s - [%d] - %s - 12 - 11  : International Mountain Day\n") % (dex7.strftime("%j"),(c.weekday(y400,12,11)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,11)]))
			w.write(("    %s - [%d] - %s - 12 - 12  : Universal Health Coverage Day\n") % (dex8.strftime("%j"),(c.weekday(y400,12,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,12)]))
			w.write(("    %s - [%d] - %s - 12 - 12  : National Poinsettia Day\n") % (dex8.strftime("%j"),(c.weekday(y400,12,12)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,12)]))
			w.write(("    %s - [%d] - %s - 12 - 18  : International Migrants Day\n") % (dun0038.strftime("%j"),(c.weekday(y400,12,18)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,18)]))
			w.write(("    %s - [%d] - %s - 12 - 18  : Arabic Language Day\n") % (dun0038.strftime("%j"),(c.weekday(y400,12,18)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,18)]))
			w.write(("    %s - [%d] - %s - 12 - 20  : Human Solidarity Day\n") % (dun0039.strftime("%j"),(c.weekday(y400,12,20)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,20)]))
			w.write(("    %s - [%d] - %s - 12 - 26  : Boxing Day\n") % (d0.strftime("%j"),(c.weekday(y400,12,26)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,26)]))
			w.write(("    %s - [%d] - %s - 12 - 31  : End Of The Year\n") % (d11.strftime("%j"),(c.weekday(y400,12,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,31)]))
			w.write(("    %s - [%d] - %s - 01 - 01  : Start Of January %04d [MONTH 01]\n") % (d1a.strftime("%j"),(c.weekday(y400+1,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400+1,1,1)],(y10k+1)%10000))
			w.write(("    %s - [%d] - %s - 01 - 01  : New Year's Day %04d\n") % (d1a.strftime("%j"),(c.weekday(y400+1,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400+1,1,1)],(y10k+1)%10000))

		

		def lunar(y400,m,d): #Rewrite for Observance(s) listing purposes
			day_of_year_list = dt.datetime(2000+(y400),m,d)
			if m < 3:
			  y1 = y-1
			  month = m + 12
			  d = d
			elif m >= 3:
				y1 = y
				month = m
				d = d
			century = y1//100
			centdiv4 = century//4 
			calib = 2-century+centdiv4
			d1 = 36525*(y1+4716)//100
			e = 306001 * (month+1) // 10000
			f = calib + d + d1 + e - 1525
			
			jddiv = (f - 2451549)
			ddiv = (jddiv*70499183//2081882250)
			dmod = (jddiv * 70499183) % 2081882250
			dic = (dmod/70499183)
			resultdiv = (ddiv + 17049) // 12
			resultmod0 = (ddiv + 17049) % 12



			if resultdiv >= 0:
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 0) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 11):
					if resultmod0 == 11:
						w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 01  [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(resultdiv+1) % (10**64),dic))
					else:
						w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 01  [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 1) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 0):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 02 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 2) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 1):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 03 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 3) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 2):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 04 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 4) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 3):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 05 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 5) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 4):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 06 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 6) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 5):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 07 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 7) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 6):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 08 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 8) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 7):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 09 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 9) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 8):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 10 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 10) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 9):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 11 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 11) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 10):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 12 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64),dic))


			
			elif resultdiv <= -1:
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 0) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 11):
					if resultmod0 == 11:
						if resultdiv + 1 < 0:
							w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 01 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(resultdiv+1) % (10**64) - 10**64,dic))
						elif resultdiv + 1 == 0:
							w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 01 [H] %04d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(resultdiv+1) % (10**64),dic))
					else:
						w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 01 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv  % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 1) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 0):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 02 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 2) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 1):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 03 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 3) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 2):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 04 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 4) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 3):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 05 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 5) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 4):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 06 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 6) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 5):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 07 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 7) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 6):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 08 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 8) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 7):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 09 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 9) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 8):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 10 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 10) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 9):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 11 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))
				if (dic >= 0 and dic <= 6 + (28169441/70499183) and resultmod0 == 11) or (dic >= 1905046394/70499183 and dic < (2081882250/70499183) and resultmod0 == 10):
					w.write(("\n    %s - [%d] - %s - %02d - %02d  : Month 12 [H] %05d  [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,resultdiv % (10**64) - 10**64,dic))

		def lunar_bc(y400,m,d):
			day_of_year_list = dt.datetime(2000+(y400),m,d)
			if m < 3:
			  y1 = y_full-1
			  month = m + 12
			  d = d
			elif m >=3:
				y1 = y_full
				month = m
				d = d
			century = y1//100
			centdiv4 = century//4 
			calib = 2-century+centdiv4
			d1 = 36525*(y1+4716)//100
			e = 306001 * (month+1) // 10000
			f = calib + d + d1 + e - 1525
			


			jddiv = (f - 2451549)
			ddiv = (jddiv*70499183//2081882250)
			dmod = (jddiv * 70499183) % 2081882250
			dic = (dmod/70499183)
			
			
			
			if ((dic >= 0 and dic <= 5 + (28169441/70499183)) or (dic >= 1834547211/70499183 and dic < (2081882250/70499183))) and (1 <= m <= 2):
				w.write(("    %s - [%d] - %s - %02d - %02d  : Chinese New Year's Day [HD] %04d [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(y1064+2698)%10**64,dic))

			if (dic >= 10 + (34661693/70499183) and dic <= 19 + (28169441/70499183) and (5 <= m <= 6)):
				w.write(("    %s - [%d] - %s - %02d - %02d  : Vesak Day [HD] %04d [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(y1064+2698)%10**64,dic))
				
			if (dic >= 10 + (34661693/70499183) and dic <= 19 + (28169441/70499183) and (9 <= m <= 10)):
				w.write(("    %s - [%d] - %s - %02d - %02d  : Chinese Mid-Autumn's Day [HD] %04d [%s]\n") % ((day_of_year_list.strftime("%j")),(c.weekday(y400,m,d)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,m,d)],m,d,(y1064+2698)%10**64,dic))


		w.write("Note : All year value(s) in mod 10^64 (!) Except In Section I. Chinese Calendar is forced to use HuangDi! Where Year 0000 C.E = [HD] 2697 - 2698\n\n")
		w.write("\n\n\nI. Most Notable Observance(s) (Not All Shown, And Some Are Experimental):\n\n\n\n")
		
		c_000(y)		
		
		w.write("\n\n\n\n\n\n\nFrom Sections II To VI Are Global Configurated For Known Religious Holidays \n\nWith Extreme Super Rare Points Included\n\n")

		w.write("\n\n\n\nII. Notable Christian Observance(s) (Movable Date Only) + Christmas, Using Gauss' Algorithm:\n\n")
		gaussEaster(y_full,mode)
		
		w.write(("    %s - [%d] - %s - 12 - 24  : Christmas Eve\n") % ((dt.datetime(2000+y400,12,24).strftime("%j")),(c.weekday(y400,12,24)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,24)]))
		w.write(("    %s - [%d] - %s - 12 - 25  : Christmas Day\n") % ((dt.datetime(2000+y400,12,25).strftime("%j")),(c.weekday(y400,12,25)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,25)]))
		w.write(("    %s - [%d] - %s - 12 - 26  : Seven Days After Christmas, Day 01\n") % ((dt.datetime(2000+y400,12,26).strftime("%j")),(c.weekday(y400,12,26)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,26)]))
		w.write(("    %s - [%d] - %s - 12 - 27  : Seven Days After Christmas, Day 02\n") % ((dt.datetime(2000+y400,12,27).strftime("%j")),(c.weekday(y400,12,27)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,27)]))
		w.write(("    %s - [%d] - %s - 12 - 28  : Seven Days After Christmas, Day 03\n") % ((dt.datetime(2000+y400,12,28).strftime("%j")),(c.weekday(y400,12,28)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,28)]))
		w.write(("    %s - [%d] - %s - 12 - 29  : Seven Days After Christmas, Day 04\n") % ((dt.datetime(2000+y400,12,29).strftime("%j")),(c.weekday(y400,12,29)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,29)]))
		w.write(("    %s - [%d] - %s - 12 - 30  : Seven Days After Christmas, Day 05\n") % ((dt.datetime(2000+y400,12,30).strftime("%j")),(c.weekday(y400,12,30)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,30)]))
		w.write(("    %s - [%d] - %s - 12 - 31  : Seven Days After Christmas, Day 06\n") % ((dt.datetime(2000+y400,12,31).strftime("%j")),(c.weekday(y400,12,31)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400,12,31)]))
		w.write(("    %s - [%d] - %s - 01 - 01  : Seven Days After Christmas, Day 07 (At Next Year)\n") % ((dt.datetime(2000+y400+1,1,1).strftime("%j")),(c.weekday(y400+1,1,1)+2-week_system_ordinal)%7+1,c.day_abbr[c.weekday(y400+1,1,1)]))

		w.write("\n\n\n\nIII. Chinese New Year Observance (01 - 20 To 02 - 21 Method) :\n\n")
	
		for m in range (1,2):
			for d in range (20,32):
				lunar_bc(y400,m,d)
		for m in range (2,3):
			for d in range (1,22):
				lunar_bc(y400,m,d)

		w.write("\n\n\n\nIV. Buddhist's Vesak Observance (05 - 05 To 06 - 06 Method) :\n\n")
	
		for m in range (5,6):
			for d in range (5,32):
				lunar_bc(y400,m,d)
		for m in range (6,7):
			for d in range (1,7):
				lunar_bc(y400,m,d)

		w.write("\n\n\n\nV. Chinese Mid-Autumn Observance (09 - 06 To 10 - 08 Method) :\n\n")
	
		for m in range (9,10):
			for d in range (6,31):
				lunar_bc(y400,m,d)
		for m in range (10,11):
			for d in range (1,9):
				lunar_bc(y400,m,d)

		w.write("\n\n\n\nVI. Islamic Hijri Calendar Year's Month Starts:\n")
		for m in range (1,2):
			for d in range (1,32):
				lunar(y400,m,d)

		if y400%4 == 0 and y400%100 == 0 and y400%400 == 0:
			for m in range (2,3):
				for d in range (1,30):
					lunar(y400,m,d)

		elif y400%4 == 0 and y400%100 == 0 and y400%400 != 0:
			for m in range (2,3):
				for d in range (1,29):
					lunar(y400,m,d)

		elif y400%4 == 0 and y400%100 != 0 and y400%400 != 0:
			for m in range (2,3):
				for d in range (1,30):
					lunar(y400,m,d)

		elif y400%4 != 0:
			for m in range (2,3):
				for d in range (1,29):
					lunar(y400,m,d)

		for m in range (3,4):
			for d in range (1,32):
				lunar(y400,m,d)

		for m in range (4,5):
			for d in range (1,31):
				lunar(y400,m,d)

		for m in range (5,6):
			for d in range (1,32):
				lunar(y400,m,d)

		for m in range (6,7):
			for d in range (1,31):
				lunar(y400,m,d)

		for m in range (7,8):
			for d in range (1,32):
				lunar(y400,m,d)

		for m in range (8,9):
			for d in range (1,32):
				lunar(y400,m,d)

		for m in range (9,10):
			for d in range (1,31):
				lunar(y400,m,d)

		for m in range (10,11):
			for d in range (1,32):
				lunar(y400,m,d)

		for m in range (11,12):
			for d in range (1,31):
				lunar(y400,m,d)

		for m in range (12,13):
			for d in range (1,32):
				lunar(y400,m,d)

	





clear()
print("-"*a)
print("\nGenerated! See ---> {} In The Same Folder As This Code!".format(fname))
print("\n\nCycle Output Mode ---> %d (%s)" % (cycle_format,cf[cycle_format]))
if type(year) == int:
	if year == 1:
		print("\n\nDigit Group ---> 1 (Forced 0000 - 0009)")
	elif year == 2:
		print("\n\nDigit Group ---> 2 (Forced 0000 - 0099)")
	elif year == 3:
		print("\n\nDigit Group ---> 3 (Forced 0000 - 0999)")
	elif year == 4:
		print("\n\nDigit Group ---> 4 (Normal 0000 - 9999)")
	else:
		print("\n\nDigit Group ---> %d (Adjusted By Number Of Digits)" % (year))
elif type(year) == str:
	if e_real == 1:
		print("\n\nDigit Group ---> 1 (Forced 0000 - 0009)")
	elif e_real == 2:
		print("\n\nDigit Group ---> 2 (Forced 0000 - 0099)")
	elif e_real == 3:
		print("\n\nDigit Group ---> 3 (Forced 0000 - 0999)")
	elif e_real == 4:
		print("\n\nDigit Group ---> 4 (Normal 0000 - 9999)")
	else:
		print("\n\nDigit Group ---> %d (Adjusted By Number Of Digits)" % (e_real))
if cycle_format == 0:
	print("\n\n(S) Years Per Cycle ---> %d" % (k2))
elif cycle_format == 1:
	print("\n\n(L) Years Per Cycle ---> %d" % (k2))
if set_exact_position == 0:
	print("\n\nWeek System ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
	print("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
	print("\n\nAnd Week %s01 Ends On ---> January %02d" % (weekstart_letter[ord(week_system.upper())-65],8-tx))
elif set_exact_position == 1:
	print("\n\nJanuary 1 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
	print("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
	print("\n\nWhere Week %s01 Ends On ---> January %02d" % (week_system,8-tx))
elif set_exact_position == 2:
	print("\n\nWeek %s01 Ends On ---> January %02d" % (week_system,8-tx))
	print("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
	print("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
elif set_exact_position == 3:
	print("\n\nRequired Date ---> Column Starting %s %02d, As The %s%s Day Of The Week" % (c.month_name[wsx2],wsx1,wsx,tx_ordinal1))
	print("\n\nWeek System Setting Result ---> [%s] %s" % (weekstart_letter[ord(week_system.upper())-65],weekstart_dayoftheweek[ord(week_system.upper())-65]))
	print("\n\nWhere January 01 Is Casted As ---> The %s%s Day Of The Week" % (tx,tx_ordinal))
	print("\n\nAnd Week %s01 Ends On ---> January %02d" % (week_system,8-tx))
end = time.time()
if show_grid_calendar == 1:
	print("\n\nShow Grid-Based Calendar ---> Yes")
else:
	print("\n\nShow Grid-Based Calendar ---> No")
print("\n\nProcessed In ---> %02d : %02d\n" % ((end-start)//60,(end-start)%60))
print("-"*a)
input("\n\nPress Enter To Exit!")
if plat == 'Windows':
	os.system('cls')
else:
	os.system('clear')
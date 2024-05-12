# Perplextual-Machine

**Python3-Based IDEs or Multi-Programming IDEs needed to run the script!**

**Compatible for any devices, either handheld (Android, iOS), or computer-based (Windows, Linux, macOS). For Linux-Distro OS-es, you may have to have a tool like WINE, or any that support to run Microsoft Excel.**

Recommended for each of the build:

Android --> **PyDroid3**

iOS --> **PyTo3 or Pythonista 3**

Windows, Linux, or macOS --> **VSCode or Sublime Text**






This repository focuses on a **Perpetual Gregorian Calendar** with direct conversion to other well-known calendars in the world.

**_Please download/clone it as a full folder to use the script/sheet, since this is a text-file-based output!_**

Designed as an **"editable-inside"** script for everyone, including programming learners, history fans, or even mathematics enthusiasts and day-off maniacs to determine specific occurrences within any Gregorian Calendar day. Please pay attention that most of the holidays are mainly **U.S Based**, in which deals through specific understandings of date placings of the calendar.


***There Are 3 (Three) files provide: Two Pythons, One Excel***

## r.py

This is a main Python script that focuses on creating line-based calendar and occurrence lists within one Perpetual Gregorian Calendar year. Create a calendar or occurrence lists file of your own by **following the instructions inside the script** (in the script, mandatory fill from lines 16, up to 167).

## w.py

This script allows you to determine the specified Perpetual Gregorian Calendar years that are satisfied with the some part of the given specified year-cycle, and current cycle position like what full-year that satisfies the 1st year of the decade, 21st year of the century, etc. And listed of **any given starting day of the week.** by **following the instructions inside the script** (in the script, mandatory fill from lines 16, up to 96).

## x.xlsx

This is the Excel spreadsheet file as an assist to determine the 1st to 52nd/53rd week of any given last **Four Digits** of the given Proleptic Gregorian Calendar. You need to run at least from any of the 2010s Microsoft Excel Editions. Latest edition is fully recommended to ensure your own digital security! A prompt to sign-in might occur, unless you can bypass it ;)







## Additional Notes

1. In the _**line calendar mode**_ at **r.py**, a Hijri-date in format ( [H] - YYYY - MM - 01 ) will be shown either **1 up to (8 or 9) times consecutively** due to some applications of hijri date offsetting. This also applies to Chinese calendars but you need to go to _**occurrences only mode's**_ THIRD AND FOURTH SECTION (The Vesak uses Chinese Calendar) with leaving at must **1 (one) calendar day up to 2 (two) beginning of Hijri dates below its referenced first-lunar-month-day**.

  Example:

  Lunar First Day Of The Month
  
  [H] YYYY - MM - DD [In format from 27.02xx - 6.399xx]
  

2. All the years are written by at least 4-digit year format, un-limited, EXCEPT:

   - Both Quotient (Current cycle) and Remainder (Sequence part of the cycle from 00 to [N-1]) of the full year from Year-Cycle Divisor written in at least 2 digits
   - Non-Gregorian Calendars are modulo-ed by 10^64 (10 Vigintillion, or 1 Followed by 64 zeroes)

3. All the dates are written in 2 digit month and date!

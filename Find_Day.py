# -*- coding: utf-8 -*-
"""
Project Description: Finding the day for any specific date of any year

Function Paramters: find_day(month in number format, date in number format, year as a 4 digit number)

Sample Input: find_day(1, 1, 2000)
    
Sample Output: "Saturday"

"""

import math

def find_day(month, date, year):

  rounded_year = (math.floor(year / 100)) * 100
  common_century_codes = {0 : 2100, 2 : 2000, 3 : 1900, 5 : 1800}
  for century_code, sample_year in common_century_codes.items():
    if (abs(rounded_year - sample_year) / 400).is_integer():
      break
  
  year_last_two_digits = str(year)[2:]
  if year_last_two_digits[0] == "0" and year_last_two_digits[1] == "0":
    year_last_two_digits = int(year_last_two_digits[0])
  elif year_last_two_digits[0] == "0":
    year_last_two_digits = int(year_last_two_digits.replace(year_last_two_digits[0], ""))
  year_last_two_digits = int(year_last_two_digits)

  quotient = year_last_two_digits // 12
  remainder = year_last_two_digits % 12
  fourth_number = remainder // 4

  doomsday_dates_general = {1 : 3, 2 : 28, 3 : 14, 4 : 4, 5 : 9, 6 : 6, 7 : 11, 8 : 8, 9 : 5, 10 : 10, 11 : 7, 12 : 12}
  doomsday_dates_leap_year = {1 : 4, 2 : 29, 3 : 14, 4 : 4, 5 : 9, 6 : 6, 7 : 11, 8 : 8, 9 : 5, 10 : 10, 11 : 7, 12 : 12}

  def find_fifth_number(doomsday_dates):
    global fifth_number
    for sample_month, doomsday_date in doomsday_dates.items():
      if month == sample_month:
        fifth_number = 0 
        if ((date - doomsday_date) != 0) or ((date - doomsday_date) != 7):
          fifth_number = abs(date - doomsday_date)
          sign = lambda x : math.copysign(1, x)
          math_sign = int(sign(date - doomsday_date))
          while abs(fifth_number) > 7:
            fifth_number = abs(fifth_number) - 7
          fifth_number *= math_sign

  if (year / 4).is_integer():
    if (year / 100).is_integer():
      if (year / 400).is_integer():
        find_fifth_number(doomsday_dates_leap_year)
      else:
        find_fifth_number(doomsday_dates_general)  
    else:
      find_fifth_number(doomsday_dates_leap_year)
  else:
    find_fifth_number(doomsday_dates_general)

  sum = century_code + quotient + remainder + fourth_number + fifth_number
  while sum > 6:
    sum -= 7
  while sum < 0:
    sum += 7
  
  days = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}
  
  for code, day in days.items():
    if code == sum:
      return day
  
    
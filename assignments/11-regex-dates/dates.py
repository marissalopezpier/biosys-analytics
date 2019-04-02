#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 3 25 2019
Purpose: Python program for 99 bottles
"""
import os
import sys
import re


# Set up main fuction
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        exit(1)

    date = args[0]

    output = get_date( date )

    if output != None:
        year,month,day = output
        if day == None:
            day = '01'
        if len(year)==2:
            year = '20'+year
        print('-'.join([year,'{:>02}'.format(month),'{:>02}'.format(day)]))
    else:
        print('No match')
        #need to add no match

def get_date( date ):
    YEAR = None
    MONTH = None
    DAY = None

    months_abrv = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']

    month_name2num = {}
    for i, month in enumerate(months_abrv):
        month_name2num[month] = '{:>02}'.format(i+1)
        #need to convert int to str
    for i, month in enumerate(months):
        month_name2num[month] = '{:>02}'.format(i+1)

    # Check pattern 1

    pattern1 = "^(\d\d\d\d)-(\d\d)-(\d\d)T.*$"
    output1 = re.match(pattern1, date)
    if output1 != None:
        YEAR = output1.group(1)
        MONTH = output1.group(2)
        DAY =output1.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 2

    pattern2 = "^(\d\d\d\d)-(\d\d?)-(\d\d?)T.*$"
    output2 = re.match(pattern2, date)
    if output2 != None:
        YEAR = output2.group(1)
        MONTH = output2.group(2)
        DAY =output2.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 3
    pattern3 = "^(\d\d\d\d)-(\d\d)-(\d\d)Z$"
    output3 = re.match(pattern3, date)
    if output3 != None:
        YEAR = output3.group(1)
        MONTH = output3.group(2)
        DAY =output3.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 4
    pattern4 = "^(\d\d\d\d)-(\d\d?)$"
    output4 = re.match(pattern4, date)
    if output4 != None:
        YEAR = output4.group(1)
        MONTH = output4.group(2)
        return (YEAR,MONTH,DAY)

    # Check pattern 4b
    pattern4b = "^(\d\d\d\d)-(\d\d)-(\d\d)$"
    output4b = re.match(pattern4b, date)
    if output4b != None:
        YEAR = output4b.group(1)
        MONTH = output4b.group(2)
        DAY =output4b.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 5
    pattern5 = "^(\d\d\d\d)-(\d\d?)\/.*$"
    output5 = re.match(pattern5, date)
    if output5 != None:
        YEAR = output5.group(1)
        MONTH = output5.group(2)
        return (YEAR,MONTH,DAY)

    # Check pattern 5b
    pattern5b = "^(\d\d\d\d)-(\d\d?)-(\d\d?)\/.*$"
    output5b = re.match(pattern5b, date)
    if output5b != None:
        YEAR = output5b.group(1)
        MONTH = output5b.group(2)
        DAY = output5b.group(3)
        return (YEAR,MONTH,DAY)
    # Check pattern 6
    pattern6 = "^(\d\d\d\d)-(\d\d?)-(\d\d?)\/.*$"
    output6 = re.match(pattern6, date)
    if output6 != None:
        YEAR = output6.group(1)
        MONTH = output6.group(2)
        DAY =output6.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 7

    pattern7 = "^(\d\d\d\d)(\d\d)(\d\d)$"
    output7 = re.match(pattern7, date)
    if output7 != None:
        YEAR = output7.group(1)
        MONTH = output7.group(2)
        DAY =output7.group(3)
        return (YEAR,MONTH,DAY)

    # Check pattern 8

    pattern8 = "^(\d\d)\/(\d\d)$"
    output8 = re.match(pattern8, date)
    if output8 != None:
        YEAR = output8.group(2)
        MONTH = output8.group(1)
        return (YEAR,MONTH,DAY)

    # Check pattern 9
    pattern9 = "^(\d\d?)\/(\d\d)$"
    output9 = re.match(pattern9, date)
    if output9 != None:
        MONTH = output9.group(1)
        YEAR = output9.group(2)
        return (YEAR,MONTH,DAY)

    # Check pattern 10
    pattern10 = "^(\d\d?)\/(\d\d)-.*$"
    output10 = re.match(pattern10, date)
    if output10 != None:
        MONTH = output10.group(1)
        YEAR = output10.group(2)
        return (YEAR,MONTH,DAY)

    # Check pattern 11
    pattern11 = "^(\d\d\d\d)-(\d\d)-(\d\d)Z$"
    output11 = re.match(pattern11, date)
    if output11 != None:
        MONTH = output11.group(1)
        YEAR = output11.group(2)
        return (YEAR,MONTH,DAY)

    # Check pattern 12
    pattern12 = "^("+'|'.join(months_abrv)+")\-(\d\d\d\d)$"
    output12 = re.match(pattern12, date)
    if output12 != None:
        YEAR = output12.group(2)
        MONTH = output12.group(1)
        MONTH = month_name2num[MONTH]
        return (YEAR,MONTH,DAY)

    # Check pattern 13
    pattern13 = "^("+'|'.join(months_abrv)+")\, (\d\d\d\d)$"
    output13 = re.match(pattern13, date)
    if output13 != None:
        YEAR = output13.group(2)
        MONTH = output13.group(1)
        MONTH = month_name2num[MONTH]
        return (YEAR,MONTH,DAY)

    # Check pattern 14
    pattern14 = "^("+'|'.join(months)+")\-(\d\d\d\d)$"
    output14 = re.match(pattern14, date)
    if output14 != None:
        YEAR = output14.group(2)
        MONTH = output14.group(1)
        MONTH = month_name2num[MONTH]
        return (YEAR,MONTH,DAY)

    # Check pattern 15
    pattern15 = "^("+'|'.join(months)+")\, (\d\d\d\d)$"
    output15 = re.match(pattern15, date)
    if output15 != None:
        YEAR = output15.group(2)
        MONTH = output15.group(1)
        MONTH = month_name2num[MONTH]
        return (YEAR,MONTH,DAY)
    return None


main() # Call main function


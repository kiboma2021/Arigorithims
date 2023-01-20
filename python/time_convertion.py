'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

'''

def timeConversion(s):
    # Write your code here
    mil_hrs={'12':'12','01':'13','02':'14','03':'15','04':'16','05':'17',
    '06':'18','07':'19','08':'20','09':'21','10':'22','11':'23'}
    if 'AM' in s:
        if s[0:2]=='12':
            s=s.replace(s[0:2],'00')
        military_hr=s.replace('AM',"")
    else:
        s=s.replace(s[0:2],mil_hrs[s[0:2]])
        military_hr=s.replace('PM',"")
        
    return military_hr
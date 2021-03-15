#region Task
'''
Given a time in 12-hour AM/PM format, convert it to
military (24-hour) time.

Note: 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour
clock.

12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour
clock.

-------------------
Example:
s= "12:01:00PM"
    return "12:01:00"
s = "12:01:00AM"
    return "00:01:00"
-------------------
'''
#endregion

def timeConversion(s):
    hr, mn, sc = s[:-2].split(":")
    #Am or PM
    if s[-2:] == "PM" and int(hr) != 12:
        hr = str(int(hr) + 12)
    elif s[-2:] == "AM" and int(hr) == 12:
        hr = "00"

    return ":".join([hr, mn, sc])


if __name__ == "__main__":
    s = input()
    result = timeConversion(s)
    print(result)
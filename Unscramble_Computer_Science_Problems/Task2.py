from datetime import datetime
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
durationdict = {}
timesec = 0
for call in calls:
    calledby = call[0]
    recievedby = call[1] 
    time = call[2] 
    duration = call[3]
    date = datetime.strptime(time, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        if calledby not in durationdict:
            durationdict[calledby] = int(duration)
        else:
            durationdict[calledby] += int(duration)
        if recievedby not in durationdict:
            durationdict[recievedby] = int(duration)
        else:
            durationdict[recievedby] += int(duration)

longest = max(durationdict.items(), key=lambda find: find[1])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest[0], longest[1]))

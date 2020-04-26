"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
firsttext = texts[0]
lastcall = calls[-1]
print("First record of texts, {} texts {} at time {}".format(firsttext[0], firsttext[1], firsttext[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(lastcall[0],lastcall[1],lastcall[2],lastcall[3]))

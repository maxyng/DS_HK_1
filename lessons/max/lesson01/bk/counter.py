#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
sumImpressions = 0
sumAge = 0
sumClicks = 0
count = 0
maxAge = 0
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  sumImpressions = sumImpressions + int(line.strip().split(',')[2])
  sumClicks = sumClicks + int(line.strip().split(',')[3])
  age = int(line.strip().split(',')[0])
  sumAge = sumAge + age
  if age > 0:
	count = count + 1

  if age > maxAge:
	maxAge = age

#The average age in the file
#Click through rate (avg clicks per impression)
#The oldest person in the file
line1 =  'Click Through Rate: '+ str(round(sumClicks / float(sumImpressions) * 100,2))
line2 =  'Average Age: '+ str(sumAge / count)
line3 =  'Maximum age: '+ str(maxAge)

print line1
print line2
print line3

file = open("nytimes_result.txt", "w")
file.write(line1+"\n")
file.write(line2+"\n")
file.write(line3+"\n")
file.close()
#!/usr/bin/python
# Import required libraries
from __future__ import division
import sys

#define sum and max values
sumImpressions = 0
sumAge = 0
sumClicks = 0
sumGender = 0
sumSignedIn = 0
count = 0
maxClick = 0
maxImpression = 0

lines = sys.stdin.readlines()
#lines.pop(0)  #remove the header, remove the first line

# For each line, find the sum of index 2 in the list.
for line in lines:

		
  newline = line.strip().split(',')
  #if first value is not numeric, skip
  try:
  	int(newline[0])
  except ValueError:
  	continue

  count += 1
  age = int(newline[0])
  gender = int(newline[1])
  impression = int(newline[2])
  clicks = int(newline[3])
  signedIn = int(newline[4])

  sumImpressions += impression
  sumGender += gender 
  sumClicks += clicks 
  sumAge += age
  sumSignedIn += signedIn
  
  if impression > maxImpression:
  	maxImpression = impression
  if clicks > maxClick:
  	maxClick = clicks

#age, gender, signedIn, avg_click, avg_impression, max_click, max_impression
line1 =  str(sumAge / count)
line2 =  str(sumGender / count)
line3 =  str(sumImpressions / count)
line4 = str(sumClicks / count)
line5 = str(sumSignedIn / count)
line6 = str(maxClick)
line7 = str(maxImpression)

print 'Age Average: '+ line1
print 'Gender Average: '+ line2
print 'Impression Average: '+ line3
print 'Clicks Average: '+ line4
print 'SignedIn Average: ' + line5
print 'Maximum Click: ' + line6
print 'Maximum Impression: ' + line7


file = open("nytimes_result.txt", "w")
file.write("\"age\",\"gender\",\"signed_in\",\"avg_click\",\"avg_impression\",\"max_click\",\"max_impression\""+"\n")
file.write(line1+","+line2+","+line3+","+line4+","+line5+","+line6+","+line7)
file.close()
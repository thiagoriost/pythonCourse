import sys, re

print(sys.path)

text = "My phone number is 3106777777, the country code is 57, my luky number es 3"
result = re.findall('[0-9]+', text)
print("result => ", result)

import time
timestamp = time.time()
print("timestamp => ", timestamp)
localTime = time.asctime(time.localtime())
print("localTime => ", localTime)

import collections
numbers = [1,2,1,2,1,3,54,3,5,5,2,4,1]
counter = collections.Counter(numbers)
print("counter => ", counter)

#!/usr/bin/python3 
with open("mytextfile.txt", "r") as f:
    string = f.read()
import re
first1 = re.search(r"(\+\d{2})-(\d{2})-(\d{4})-(\d{4})", string)
result1 = "%s(%s)%s%s" % (first1.group(1),first1.group(2),first1.group(3),first1.group(4))
print(result1)
first2 = re.search(r"(\d{3})-(\d{3})-(\d{3})", string)
result2 = "(%s)%s%s" % (first2.group(1),first2.group(2),first2.group(3))
print(result2)

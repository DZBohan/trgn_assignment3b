#!/usr/bin/python3
# import sys
# mytextfile = sys.argv[1] 
# with open(mytextfile, "r") as f:
#     string = f.read()
# import re
# first1 = re.search(r"(\+\d{2})-(\d{2})-(\d{4})-(\d{4})", string)
# result1 = "%s(%s)%s%s" % (first1.group(1),first1.group(2),first1.group(3),first1.group(4))
# print(result1)
# first2 = re.search(r"(\d{3})-(\d{3})-(\d{3})", string)
# result2 = "(%s)%s%s" % (first2.group(1),first2.group(2),first2.group(3))
# print(result2)
import argparse
import re
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('path',type=str)
with open(parser.parse_args().path, "r") as f:
    string = f.read()
for i in string.split(' '):
    if re.match(r"(\+\d{2})-(\d{2})-(\d{4})-(\d{4})", i):
        first = re.search(r"(\+\d{2})-(\d{2})-(\d{4})-(\d{4})", i)
        result = "%s (%s) %s%s" % (first.group(1), first.group(
            2), first.group(3), first.group(4))
        print(result)
    elif re.match(r"(\d{3})-(\d{3})-(\d{3})", i):
        first = re.search(r"(\d{3})-(\d{3})-(\d{3})", i)
        result = "(%s)%s%s" % (first.group(
            1), first.group(2), first.group(3))
        print(result)

#! /usr/bin/env python3
from operator import itemgetter
import sys

print("Output #1: I'm excited to learn Python.")

#두 수를 더한다.
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

#두 리스트를 더한다.
a = [1,2,3,4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a,b,c))

#파일 읽기
#하나의 텍스트 파일 읽기(과거방식)
print("Output #139: ")
input_file = sys.argv[1]
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()

#파일 읽기 새방식
input_file = sys.argv[1]
print("Output #140: ")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))


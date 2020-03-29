#-*- coding: utf-8 -*-
#! /usr/bin/env python3
from operator import itemgetter
import sys
import glob
import os


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
# print("Output #139: ")
# input_file = sys.argv[1]
# filereader = open(input_file, 'r')
# for row in filereader:
#     print(row.strip())
# filereader.close()

#파일 읽기 새방식
# input_file = sys.argv[1]
# print("Output #140: ")
# with open(input_file, 'r', newline='') as filereader:
#     for row in filereader:
#         print("{}".format(row.strip()))

#다수의 파일 읽기
# print("Output #141: ")
# inputPath = sys.argv[1]
# for input_file in glob.glob(os.path.join(inputPath, '*read.txt')):
#     with open(input_file, 'r', newline='', encoding='UTF-8') as filereader:
#         for row in filereader:
#             print("{}".format(row.strip()))
            
# 파일 쓰기
# 하나의 텍스트 파일 작성하기
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #142: Output written to file")

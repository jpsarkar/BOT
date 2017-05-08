import csv
import sys

#input number you want to search
number = "random_name5"

#read csv, and split on ";" the line
csv_file = csv.reader(open('output.csv', "rb"), delimiter=";")


#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[17]:
         print row

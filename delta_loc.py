######################################################################################
# delta_loc.py
# AS, 2/19/21
#
# inputs: 	.csv with payload locations
#		.csv with payload locations according to AUT
#		position of AUT
#
# outputs: 	location difference in meters
######################################################################################



import csv
import math
import numpy as np
import sys

# we need 2 points for the line, and we know one of them is always gonna
# be (0,0,0), since that's where our AUT is. We might as well define that and the radius,
# since we're not gonna have that information

# get payload loc compared to AUT position
payload_data = sys.argv[1]
print
print("Payload Data File:")
print(payload_data)
print
aut_data = sys.argv[2]
print("AUT Data File:")
print(aut_data)
print

rad = 10 # meters
debug = 1 # 1 to print everything, 0 to print nothing
AUT_loc = np.array([0,0,0]) # assumed, can be changed

# get number of rows
with open('cartesian_test.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter = ',')
    data = list(reader)
    row_count = len(data)
    if debug: print(row_count)

# iterate through rows
for row_num in range(row_count):
    if debug: print(row_num)
    with open('cartesian_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        current_row = [row for idx, row in enumerate(csv_reader) if idx == row_num]
        x1 = float(current_row[0][0])
        y1 = float(current_row[0][1])
        z1 = float(current_row[0][2])
        real_loc = np.array([x1,y1,z1])
        if debug: print(x1,y1,z1)  
    with open('AUTdata_test.csv') as csv_file2:
        csv_reader2 = csv.reader(csv_file2, delimiter=',')
        current_row = [row for idx, row in enumerate(csv_reader2) if idx == row_num] 
        azi = float(current_row[0][0])*math.pi/180
        ele = float(current_row[0][1])*math.pi/180
        x2 = rad*math.cos(ele)*math.cos(azi)
        y2 = rad*math.cos(ele)*math.sin(azi)
        z2 = rad*math.sin(ele)
        guess_loc = np.array([x2,y2,z2])
        if debug: print(x2,y2,z2)
        delta_loc = np.linalg.norm(np.cross(real_loc-AUT_loc, AUT_loc-guess_loc))/np.linalg.norm(real_loc-AUT_loc)
        if debug: print(delta_loc)

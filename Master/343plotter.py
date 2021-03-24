import csv
import matplotlib.pyplot as plt
import numpy as np

L  = 0.2
W  = 0.2
er = 5.18
e0 = 8.854

with open('result_navigator.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # for row in reader:
    #     # print(', '.join(row))
    #     plt.scatter(row[1],row[7])\
    h  = []
    c  = []
    ci = []
    pd = []
    for row in reader:
        h.append(float(row[1]))
        c.append(float(row[7])*1000000000000)
        ci.append(er*e0*W*L/(float(row[1])*0.001))
        pd.append( 200 * ( float(row[7])*1000000000000 - (er*e0*W*L/(float(row[1])*0.001)) ) / ( float(row[7])*1000000000000 + (er*e0*W*L/(float(row[1])*0.001)) ))
   



    # plt.scatter(h,ci)
    # plt.scatter(h,c)

    plt.scatter(h,pd)


    plt.xscale("log")
    # plt.yscale("log")
    plt.xlabel("H_d (mm)")
    plt.ylabel("%")
    plt.title("Ideal vs. Modeled Percent Difference")
    plt.xlim(1)
    plt.ylim(1)
    plt.show()
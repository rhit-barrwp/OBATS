import pprint as pp
import statistics
import matplotlib.pyplot as plt
from pyproj import Proj
import utm

file = open('log/19test3.txt','r')
newFile = open('log/19test3_dd.txt','w')
lines = file.readlines()

totLat = 0
totLon = 0

lats = []
lons = []
alts = []
utmLats = []
utmLons = []

newFile.write('Time,Latitude,Longitude,Altitude\n')
for line in lines:
    x = line.split(',')
    if (x[0] == 'Altitude'):
        newFile.write(x[2] + ',' + x[5] + ',' + x[3] + ',' + x[0] + '\n')
        continue
    ddLat = (( float( x[5] ) - ( float( x[5] ) % 100 ) ) / 100 + ( float( x[5] ) % 100 ) / 60 ) * (((x[6] == 'S') * -2) + 1)
    ddLon = (( float( x[3] ) - ( float( x[3] ) % 100 ) ) / 100 + ( float( x[3] ) % 100 ) / 60 ) * (((x[4] == 'W') * -2) + 1)
    newFile.write(x[2] + ',' + str(ddLat) + ',' + str(ddLon) + ',' + x[0] + '\n')
    
    # totLat += ddLat
    # totLon += ddLon

    u = utm.from_latlon(ddLat,ddLon)
    utmLats.append(u[0])
    utmLons.append(u[1])

    lats.append(ddLat)
    lons.append(ddLon)
    alts.append(float(x[0]))

print('Latitude Mean:  ' + str(statistics.mean(lats)))
print('Latitude Stdev: ' + str(statistics.stdev(lats)))
print('Longitude Mean: ' + str(statistics.mean(lons)))
print('Longitude Stdev: ' + str(statistics.stdev(lons)))
print('Altitude Mean: ' + str(statistics.mean(alts)))
print('Altitude Stdev: ' + str(statistics.stdev(alts)))
print('---------------')
print('Latitude Mean:  ' + str(statistics.mean(utmLats)))
print('Latitude Stdev: ' + str(statistics.stdev(utmLats)))
print('Longitude Mean: ' + str(statistics.mean(utmLons)))
print('Longitude Stdev: ' + str(statistics.stdev(utmLons)))

u = utm.from_latlon(39.485472666666666,-87.32547000000001)
# print(u[0])

# plt.plot(lats,lons,'o')
# plt.show()


fig = plt.figure()
ring = fig.add_subplot(111, projection='3d')
ring.scatter(utmLats,utmLons,alts)
pt = utm.from_latlon(39.48542946296296,-87.32540642592593)
# point = fig.add_subplot(111, projection='3d')
ring.scatter(pt[0],pt[1],60)
plt.show()



# avgLat = totLat / len(lines)
# print('Average Latitude: ' + str(avgLat))
# avgLon = totLon / len(lines)
# print('Average Longitude: ' + str(avgLon))
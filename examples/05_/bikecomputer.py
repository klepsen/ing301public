from datetime import datetime
from typing import List


class Sensor:

    def __init__(self):
        pass


class BikeComputer:
    pass


class Display:
    
    def __init__(self):
        self.speed = 0.0
        self.average


class GPSPoint:

    def __init__(self, timestamp: datetime, latitude: float, longitude: float, height: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.next = None

    def __repr__(self):
        return f"{self.timestamp} ({self.latitude}, {self.longitude}), {self.height}"


class AbstractRoute:

    def __init__(self):
        self.totalLength = None
        self.totalHeight = None
        self.averageSpeed = None
        self.maxSpeed = None
        self.usedCalories = None


    def calculateStatistic(self):
        pass

class RouteIterator:
    
    def __init__(self, current: Optional[GPSPoint]):
        self.current = current

    def __next__(self):
        result = self.current
        if not result:
            raise StopIteration()

        self.current = result.next
        
        return result

class Route(AbstractRoute):
    def __init__(self):
        self.first = None
        self.second = None

    def add_point(self, point: GPSPoint):
        if self.first:
            self.first = point
            self.last = point
        else:
            self.last.next = point
            self.last = point

    def __init__(self):
        return RouteIterator(self.first)

    

class RouteGroup(AbstractRoute):

    
    pass


class GPSSensor(Sensor):
    pass


class Speedometer(Sensor):
    pass


class TemperatureSensor(Sensor):
    pass


class HeartFrequencySensor(Sensor):
    pass

file = open("../03_gpsdata_oo/gpslogs/short.csv")

route = Route()
skip_count = 0
for line in file.readlines():
    if skip_count > 1:
        split = line.split(",")
        route.add_point(GPSPoint(timestamp=datetime.fromisoformat(split[0]),
        latitude=float(split[1]),
        longitude=float(split[2]),
        height=float(split[3])))
    skip_count += 1

file.close()

print(route.first)
print(route.last)

for point in route:
    print(point)








"""
p = GPSPoint(datetime(2023, 1, 24, 12, 23), 2.3455, 31.88723, "10.5")
print(p.height)

s = GPSSensor()
print(s.x)
"""
def manhatten_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

class Sensor:
    def __init__(self, position, closest_beacon_position):
        self.position = position
        self.closest_beacon_position = closest_beacon_position
        self.distance_to_closest_beacon = manhatten_distance(self.position, self.closest_beacon_position)

    def __str__(self):
        return f"Sensor at {self.position} with nearest beacon at {self.closest_beacon_position}"

    def __repr__(self):
        return f"Sensor at {self.position} with nearest beacon at {self.closest_beacon_position}"

def coordinate_string_to_tuple(coordinates):
    x = int(coordinates[2:coordinates.index(',')])
    y = int(coordinates[coordinates.index('y=')+2:])
    return (x, y)

def parse_data(lines):
    sensors = []
    beacons = set()
    for line in lines:
        sensor_position = line[10:line.index(':')]
        nearest_beacon = line[line.index('is at ')+6:]
        beacon_position = coordinate_string_to_tuple(nearest_beacon)
        sensors.append(Sensor(coordinate_string_to_tuple(sensor_position), beacon_position))
        beacons.add(beacon_position)
    return sensors, beacons

def could_be_beacon_at(position, list_of_sensors):
    for sensor in list_of_sensors:
        if manhatten_distance(position, sensor.position) <= sensor.distance_to_closest_beacon:
            return False
    return True

def solution(path, y):
    with open(path) as f:
        data = f.readlines()
        sensors, beacons = parse_data(data)
    count = 0
    x_min = 0
    x_max = 0
    for sensor in sensors:
        closest_point_on_line = (sensor.position[0], y)
        distance_to_closest_point = abs(y - sensor.position[1])
        if manhatten_distance(closest_point_on_line, sensor.position) > sensor.distance_to_closest_beacon:
            continue
        else:
            remaining_distance = sensor.distance_to_closest_beacon - distance_to_closest_point
            left_most_point = sensor.position[0] - remaining_distance
            right_most_point = sensor.position[0] + remaining_distance
            x_min = min(left_most_point, x_min)
            x_max = max(right_most_point, x_max)
    print(x_min)
    print(x_max)
    for x in range(x_min, x_max+1):
        if (x, y) in beacons:
            continue
        elif not could_be_beacon_at((x, y), sensors):
            count += 1
    return count

print(solution('example_input.txt', 10))
print(solution('input.txt', 2000000))
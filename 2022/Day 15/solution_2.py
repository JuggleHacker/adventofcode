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

    def rightmost_ruled_out_in_row(self, y):
        closest_point_on_line = (self.position[0], y)
        distance_to_closest_point = abs(y - self.position[1])
        if manhatten_distance(closest_point_on_line, self.position) <= self.distance_to_closest_beacon:
            return self.position[0] + self.distance_to_closest_beacon - distance_to_closest_point
        else:
            return None



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
    for sensor_number, sensor in enumerate(list_of_sensors):
        if manhatten_distance(position, sensor.position) <= sensor.distance_to_closest_beacon:
            list_of_sensors[0], list_of_sensors[sensor_number] = list_of_sensors[sensor_number], list_of_sensors[0]
            return False, sensor
    return True, None

def x_min_and_max(sensors, y, max_coord):
    x_min = max_coord
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
    return x_min, x_max

def solution(path, max_coord):
    with open(path) as f:
        data = f.readlines()
        sensors, beacons = parse_data(data)
    for y in range(max_coord-1):
        x = 0
        while x < max_coord:
            if (x, y) in beacons:
                x += 1
                continue
            test_nearest = could_be_beacon_at((x, y), sensors)
            if not test_nearest[0]:
                nearest_sensor = test_nearest[1]
                max_x = nearest_sensor.rightmost_ruled_out_in_row(y)
                x = max_x + 1
            else:
                print(test_nearest[0])
                return f"Done! Beacon at {(x, y)}. Frequency: {x * 4000000 + y}"

print(solution('example_input.txt', 20))
print(solution('input.txt', 4000000))
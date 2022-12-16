from typing import List, Tuple

# Day 15: Beacon Exclusion Zone

test_data = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.split('\n')


class Sensor:

    def __init__(self, pos: Tuple[int, int], beacon: Tuple[int, int]):
        self.pos = pos
        self.beacon = beacon
        self.distance = self.manhattan_distance(pos, beacon)

    def in_distance(self, point: Tuple[int, int]) -> bool:
        return self.manhattan_distance(self.pos, point) <= self.distance

    def manhattan_distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        x0, y0 = a
        x1, y1 = b
        return abs(x1 - x0) + abs(y1 - y0)

    def __str__(self):
        return str(self.pos) + ' [' + str(self.distance) + ']'

    def __repr__(self):
        return self.__str__()


def get_sensor_list(data) -> List[Sensor]:
    sensors = []
    for line in data:
        # Sensor at x=2, y=0: closest beacon is at x=2, y=10
        pos = int(line.split('=')[1].split(',')[0]), int(line.split('=')[2].split(':')[0])
        beacon = int(line.split('=')[3].split(',')[0]), int(line.split('=')[-1])
        sensors.append(Sensor(pos, beacon))
    return sensors


def get_bounds(sensors) -> Tuple[int, int]:
    x_min, x_max = 10 ** 6, -(10 ** 6)
    for sensor in sensors:
        x_min = min(x_min, sensor.pos[0])
        x_min = min(x_min, sensor.beacon[0])
        x_max = max(x_max, sensor.pos[0])
        x_max = max(x_max, sensor.beacon[0])

    x_range = x_max - x_min
    x_start = x_min - int(x_range / 4)
    x_end = x_max + int(x_range / 4)
    return x_start, x_end


def part1(data: List[str], y: int) -> int:
    sensors = get_sensor_list(data)
    x_start, x_end = get_bounds(sensors)
    count = 0
    for x in range(x_start, x_end):
        point = (x, y)
        for sensor in sensors:
            if sensor.in_distance(point) and point != sensor.beacon:
                count += 1
                break
    return count


def in_distance(sensors, point) -> bool:
    for sensor in sensors:
        if sensor.in_distance(point):
            return True
    return False


def part2(data: List[str], bound: int) -> int:
    sensors = get_sensor_list(data)

    for sensor in sensors:
        # print('Checking outer bounds of sensor', sensor)
        p = sensor.pos
        d = sensor.distance
        pos = (p[0] - d - 1, p[1])
        end = (p[0], p[1] + d + 1)
        # Check outer bounds, left to top
        while pos != end:
            pos = (pos[0] + 1, pos[1] + 1)
            if pos[0] < 0 or pos[1] < 0 or pos[0] > bound or pos[1] > bound:
                continue
            if not in_distance(sensors, pos):
                return pos[0] * 4000000 + pos[1]


def main():
    with open('inputs/day15.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 10)
    assert part1_test_result == 26, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data, 2_000_000)
    assert part1_result == 4502208, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data, 20)
    assert part2_test_result == 56000011, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data, 4000000)
    assert part2_result == 13784551204480, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()

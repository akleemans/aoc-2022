import operator
from typing import List, Dict

# Day 19: Not Enough Minerals

test_data = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''.split(
    '\n')


def add(a: List[int], b: List[int]) -> List[int]:
    return list(map(operator.add, a, b))
    # return [sum(x) for x in zip(a, b)]


def sub(a: List[int], b: List[int]) -> List[int]:
    return list(map(operator.sub, a, b))


class State:
    def __init__(self, t: int, resources: List[int], robots: List[int]):
        # ore, clay, obsidian, geode
        self.t = t
        self.resources = resources
        self.robots = robots
        self.producing_robot = None

    def tick(self):
        # Time passes
        self.t -= 1

        # Resources are obtained
        self.resources = add(self.resources, self.robots)

        if self.producing_robot is not None:
            self.robots[self.producing_robot] += 1
            self.producing_robot = None

    def buy_options(self, recipes: Dict[int, List[int]], resources=None) -> List[int]:
        """Returns list of ints of possible robot"""
        if resources is None:
            resources = self.resources
        options = []
        for idx, recipe in recipes.items():
            if all(x >= 0 for x in sub(resources, recipe)):
                options.append(idx)
        return options[::-1]

    def buy_robot(self, robot_type: int, recipe: List[int]) -> 'State':
        resources = sub(self.resources, recipe)
        robots = [*self.robots]
        new_state = State(self.t, resources, robots)
        new_state.producing_robot = robot_type
        return new_state

    def get_geodes(self):
        return self.resources[3]

    def min_geodes(self):
        """Minimum of geodes this state will yield"""
        return self.resources[3] + self.robots[3] * self.t

    def max_reachable_geodes(self):
        """Max reachable geodes if only buying geode robots from now on"""
        max_reachable = self.resources[3]
        for i in range(self.t):
            max_reachable += self.robots[3] + i
        return max_reachable

    def __str__(self):
        return f'State t={self.t} resources={self.resources}, robots={self.robots}'

    def hash(self):
        return f'{self.t}{self.resources}{self.robots}'


class Blueprint:
    def __init__(self, idx, recipes: Dict[int, List[int]]):
        self.idx = idx
        self.recipes = recipes


def get_blueprints(data) -> List[Blueprint]:
    blueprints = []
    for line in data:
        idx = int(line.split(':')[0].split(' ')[1])
        recipes = {}
        key = 0
        for t in line.split('costs ')[1:]:
            parts = t.split('.')[0].split(' and ')
            ore = 0
            clay = 0
            obsidian = 0
            for part in parts:
                n = int(part.split(' ')[0])
                if 'ore' in part:
                    ore = n
                elif 'clay' in part:
                    clay = n
                elif 'obsidian' in part:
                    obsidian = n
            recipes[key] = [ore, clay, obsidian, 0]
            key += 1

        blueprints.append(Blueprint(idx, recipes))
    return blueprints


def solve(blueprint: Blueprint, t: int) -> int:
    start_state = State(t, [0, 0, 0, 0], [1, 0, 0, 0])
    queue = [start_state]
    recipes = blueprint.recipes
    max_costs = [0, 0, 0, 0]
    for recipe in recipes.values():
        for i in range(4):
            max_costs[i] = max(max_costs[i], recipe[i])

    already_seen = set()
    # count = 0
    highest_geodes = -1
    reachable_high = 0
    # t = time.time()
    while len(queue) > 0:
        # count += 1
        state = queue.pop()
        if state.hash() in already_seen:
            continue
        else:
            already_seen.add(state.hash())

        # if count % 100_000 == 0:
        #     print('Queue:', len(queue), 'state:', state, 't=', time.time() - t)

        if state.t == 0:
            if state.get_geodes() > highest_geodes:
                highest_geodes = state.get_geodes()
                # print('New high:', highest_geodes, 'state:', state)
                reachable_high = highest_geodes
            continue

        reachable_high = max(reachable_high, state.min_geodes())
        if reachable_high > state.max_reachable_geodes():
            continue

        buy_options = state.buy_options(recipes)

        for buy_option in buy_options:
            if buy_option < 3 and state.robots[buy_option] >= max_costs[buy_option]:
                continue
            if state.robots[2] > 0 and buy_option == 0:
                continue
            new_state = state.buy_robot(buy_option, recipes[buy_option])
            new_state.tick()
            queue.append(new_state)

        # If waiting doesn't provide new kind of robot, must buy something now
        future_resources = add(state.resources, [r * 25 for r in state.robots])
        if len(buy_options) > 0 and buy_options == state.buy_options(recipes, future_resources):
            continue
        else:
            state.tick()
            queue.append(state)

    return highest_geodes


def part1(data: List[str]):
    blueprints = get_blueprints(data)

    total_quality_level = 0
    # t = time.time()
    for blueprint in blueprints:
        # print('Solving blueprint', blueprint.idx)
        total_quality_level += blueprint.idx * solve(blueprint, 24)

    # print('Time for all blueprints:', time.time() - t)
    # Initial time: 203s
    # With robots max cost: 19.2s
    # With simple robot arch: 12s

    return total_quality_level


def part2(data: List[str]):
    blueprints = get_blueprints(data)
    m = 1
    # t = time.time()
    for blueprint in blueprints[:3]:
        # print('Solving blueprint', blueprint.idx)
        m *= solve(blueprint, 32)
        # print('m=', m, 'total t=', time.time() - t)
    return m


def main():
    with open('inputs/day19.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 33, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 817, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)  # 3472 = 63*56
    assert part2_test_result == 3472, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 4216, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()

import itertools
from typing import List, Dict

# Day 16: Proboscidea Volcanium

test_data = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''.split('\n')

test_case_1 = '''Valve AA has flow rate=0; tunnels lead to valves BA
Valve BA has flow rate=2; tunnels lead to valves AA, CA
Valve CA has flow rate=4; tunnels lead to valves BA, DA
Valve DA has flow rate=6; tunnels lead to valves CA, EA
Valve EA has flow rate=8; tunnels lead to valves DA, FA
Valve FA has flow rate=10; tunnels lead to valves EA, GA
Valve GA has flow rate=12; tunnels lead to valves FA, HA
Valve HA has flow rate=14; tunnels lead to valves GA, IA
Valve IA has flow rate=16; tunnels lead to valves HA, JA
Valve JA has flow rate=18; tunnels lead to valves IA, KA
Valve KA has flow rate=20; tunnels lead to valves JA, LA
Valve LA has flow rate=22; tunnels lead to valves KA, MA
Valve MA has flow rate=24; tunnels lead to valves LA, NA
Valve NA has flow rate=26; tunnels lead to valves MA, OA
Valve OA has flow rate=28; tunnels lead to valves NA, PA
Valve PA has flow rate=30; tunnels lead to valves OA'''.split('\n')

test_case_2 = '''Valve AA has flow rate=0; tunnels lead to valves BA
Valve BA has flow rate=1; tunnels lead to valves AA, CA
Valve CA has flow rate=4; tunnels lead to valves BA, DA
Valve DA has flow rate=9; tunnels lead to valves CA, EA
Valve EA has flow rate=16; tunnels lead to valves DA, FA
Valve FA has flow rate=25; tunnels lead to valves EA, GA
Valve GA has flow rate=36; tunnels lead to valves FA, HA
Valve HA has flow rate=49; tunnels lead to valves GA, IA
Valve IA has flow rate=64; tunnels lead to valves HA, JA
Valve JA has flow rate=81; tunnels lead to valves IA, KA
Valve KA has flow rate=100; tunnels lead to valves JA, LA
Valve LA has flow rate=121; tunnels lead to valves KA, MA
Valve MA has flow rate=144; tunnels lead to valves LA, NA
Valve NA has flow rate=169; tunnels lead to valves MA, OA
Valve OA has flow rate=196; tunnels lead to valves NA, PA
Valve PA has flow rate=225; tunnels lead to valves OA'''.split('\n')


class Node:
    def __init__(self, name: str, flow_rate: int):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors: List['Node'] = []
        # {valve: distance}
        self.distances = {}
        self.opened = False

    def __str__(self):
        return self.name  # + ' [' + str(self.distances.values()) + ']'

    def __repr__(self):
        return self.__str__()


def get_nodes(data) -> Dict[str, Node]:
    nodes = {}
    for line in data:
        name = line.split(' ')[1]
        flow_rate = int(line.split('=')[1].split(';')[0])
        nodes[name] = Node(name, flow_rate)
    for line in data:
        name = line.split(' ')[1]
        # leads to valve GG
        # lead to valves AA, JJ
        neighbor_names = line[line.find('to valve') + 9:].strip().split(', ')
        neighbors = [nodes[v] for v in neighbor_names]
        nodes[name].neighbors = neighbors
    return nodes


def dijkstra(nodes: List[Node], source: Node) -> Dict[Node, int]:
    dist: Dict[Node, int] = {n: 999 for n in nodes}
    queue: List[Node] = [n for n in nodes]
    dist[source] = 0

    while len(queue) > 0:
        u = min(queue, key=dist.get)
        queue.remove(u)
        for v in u.neighbors:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
    return dist


def path_score(path, t):
    score = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        d = current_node.distances[next_node]
        t -= (d + 1)
        score += t * next_node.flow_rate
    return score


def dfs(start_node, t: int):
    paths = []

    def _dfs(node, t: int, visited: List[Node]):
        for next_node, d in node.distances.items():
            if next_node in visited or t - d - 1 <= 0:
                continue
            _dfs(next_node, t - d - 1, [*visited, next_node])
        paths.append(visited)

    _dfs(start_node, t, [])
    return paths


def part1(data: List[str]):
    nodes_dict = get_nodes(data)
    nodes = list(nodes_dict.values())

    # Calculate shortest paths for every node
    for node in nodes:
        all_distances = dijkstra(nodes, node)
        node.distances = {n: d for n, d in all_distances.items() if n.flow_rate > 0 and n != node}

    start_node = nodes_dict['AA']
    all_paths = dfs(start_node, 30)
    # print('Generated', len(paths), 'paths')

    best_score = max([path_score([start_node, *path], 30) for path in all_paths])
    # print('Returning best score:', best_score)
    return best_score


def part2(data: List[str]):
    nodes_dict = get_nodes(data)
    nodes = list(nodes_dict.values())

    for node in nodes:
        all_distances = dijkstra(nodes, node)
        node.distances = {n: d for n, d in all_distances.items() if n.flow_rate > 0 and n != node}

    start_node = nodes_dict['AA']
    all_single_paths = dfs(start_node, 26)
    print('Generated', len(all_single_paths), 'single paths')

    all_paths = []
    for p1, p2 in itertools.combinations(all_single_paths, 2):
        # print('Checking', p1, p2)
        if set(p1).isdisjoint(set(p2)):
            all_paths.append((p1, p2))
    print('Generated', len(all_paths), 'combined paths')

    best_score = max([path_score([start_node, *p1], 26) + path_score([start_node, *p2], 26) for p1, p2 in all_paths])
    print('Returning best score:', best_score)
    return best_score


def main():
    with open('inputs/day16.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 1651, f'Part 1 test input returned {part1_test_result}'
    # part1_test_result1 = part1(test_case_1)
    # assert part1_test_result1 == 2640, f'Part 1 test case 1 input returned {part1_test_result1}'
    # part1_test_result2 = part1(test_case_2)
    # assert part1_test_result2 == 13468, f'Part 1 test case 2 input returned {part1_test_result2}'
    part1_result = part1(data)
    assert part1_result == 1789, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 1707, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2496, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()

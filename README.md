# aoc-2022

My solution for [Advent of Code 2022](https://adventofcode.com/2022) in Python 3.

## Execution times

All code in Python 3, timed with `python3 run_all.py`:

| Day    | Time      |
|--------|-----------|
| Day 1  | 0.002s    |
| Day 2  | 0.004s    |
| Day 3  | 0.002s    |
| Day 4  | 0.005s    |
| Day 5  | 0.003s    |
| Day 6  | 0.006s    |
| Day 7  | 0.006s    |
| Day 8  | 0.778s    |
| Day 9  | 0.307s    |
| Day 10 | 0.001s    |
| Day 11 | 2.094s    |
| Day 12 | 0.789s    |
| Day 13 | 0.031s    |
| Day 14 | 1.938s    |
| Day 15 | 9.877s    |
| Day 16 | 63.893s   |
| Day 17 | 0.684s    |
| Day 18 | 16.043s   |
| Day 19 | 415.912s  |
| Day 20 | 16.844s   |
| Day 21 | 0.054s    |
| Day 22 | 0.165s    |
| Day 23 | 6995.641s |
| Day 24 | 6.917s    |
| Day 25 | 0.006s    |

## Learned along the way

* Compiling Python to Nuitka (nearly) or Codon (much faster, speedup 5-50x):

```bash
codon run -release run.py
```

Python code can be converted to work in Codon, but some caveats are:

* Using `typing` module (opened bug)
* Mixed types (like `[1, 'a']`)
* Using the `json` module (import differently?)
* Using `eval()`
* Using self-referential typings in class, like `List['Monkey']` inside of `Monkey` class

---

* Using `min()` and `max()` with key (Day 11)

```python
# Using property of object
min(coordinates, key=lambda c: c.x)

# Using a different dict
queue = [a, b]
neighbor_distances = {a: 3, b: 5}

lowest = min(queue, key=dist.get)
```

---

* Referencing own class inside a class (Day 11)

```python
class Monkey:
    monkey_list: List['Monkey']
    ...
```

---

* List comprehensions for `Dict` (Day 16)

```python
dist: Dict[Node, int] = {n: 999 for n in nodes}
```

---

* Unpacking with `*` (Day 16)

```python
_dfs(next_node, t, [*visited, next_node])
```

---

* Using Dijkstra for unweighted graphs (Day 16):

```python
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
```

---

* Proper DFS using internal function (Day 16)

Code can be much cleaner than tracking it iteratively.

```python
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
```

---

* Using a helper `Coord` class (Day 17)

```python
class Coord:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def add(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()
```

--- 

* Recursion depth of 1000 will not be enough sometimes (Day 18)

Rewrite using iterative approach (queue) is always possible.

---

* Using `next` to get first iterator item (Day 20)

```python
zero_item = next(i for i in all_items if i.n == 0)
```

---


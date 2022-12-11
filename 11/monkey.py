from typing import List, Dict, Tuple


class Monkey:
    def __init__(self, idx: str, start_items: List[int], operation: str, divisible_test: int,
        target_idx: Dict[bool, int], divide: bool, monkeys: List['Monkey']):
        self.items_inspected = 0
        self.idx = idx
        self.items = start_items
        self.operation = operation
        self.divide = divide
        self.divisible_test = divisible_test
        self.target_idx = target_idx
        self.monkey_list = monkeys
        self.modulo = None

    def process_items(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            target, updated_item = self.process_item(item)
            target_monkey: Monkey = self.monkey_list[target]
            if not self.divide:
                updated_item %= self.modulo
            target_monkey.add_item(updated_item)

    def process_item(self, item: int) -> Tuple[int, int]:
        self.items_inspected += 1
        query = self.operation.replace('old', str(item))
        result = eval(query)
        if self.divide:
            result = result // 3
        # print(self, 'is doing', self.operation, ':', query, '=', result)
        return self.target_idx[result % self.divisible_test == 0], result

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self):
        # return 'Monkey ' + self.idx + ' [' + str(self.items_inspected) + ']'
        return 'Monkey ' + self.idx + ' (' + str(self.items_inspected) + ') ' + str(self.items)

    def __repr__(self):
        return self.__str__()

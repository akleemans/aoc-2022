from typing import List

# Day 25: Full of Hot Air

test_data = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''.split('\n')


def to_base(n: int, b: int):
    BS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return '0' if not n else to_base(n // b, b).lstrip('0') + BS[n % b]


def dec_to_snafu(dec: str) -> str:
    dic = {'0': '0', '1': '1', '2': '2', '3': '=', '4': '-', '5': '0'}
    snafu = ''
    carry = 0
    base5 = str(to_base(int(dec), 5))

    for i in range(len(base5) + 1):
        if i == len(base5):
            if carry != 0:
                c = '0'
            else:
                break
        else:
            c = base5[len(base5) - 1 - i]
        c2 = str(int(c) + carry)
        snafu_c = dic[c2]
        if c2 in ['3', '4', '5']:
            carry = 1
        else:
            carry = 0
        snafu = snafu_c + snafu

    return snafu


def snafu_to_dec(snafu: str) -> str:
    dic = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
    m = 1
    n = 0
    for i in range(len(snafu)):
        c = snafu[len(snafu) - 1 - i]
        n += m * dic[c]
        m *= 5

    return str(n)


def part1(data: List[str]) -> str:
    total = 0
    for line in data:
        total += int(snafu_to_dec(line))

    return dec_to_snafu(str(total))


def part2(data: List[str]):
    return 1


def main():
    with open('inputs/day25.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == '2=-1=0', f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == '2-==10--=-0101==1201', f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 0, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    print('Part 2:', part2_result)  # remove
    assert part2_result == 0, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()

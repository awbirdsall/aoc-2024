from pathlib import Path
from collections import defaultdict


def get_input_lines():
    """Get raw lists of inputs from file"""
    input_lines = Path("input.txt").read_text(encoding="utf-8")
    l1 = []
    l2 = []
    for il in input_lines.split("\n"):
        if len(il) > 0:
            il1, il2 = il.split("   ")
            l1.append(int(il1))
            l2.append(int(il2))
    return l1, l2


def solve_part_1():
    l1, l2 = get_input_lines()
    l1 = sorted(l1)
    l2 = sorted(l2)
    summed = 0
    for li1, li2 in zip(l1, l2):
        summed += abs(li1 - li2)
    print(summed)


def solve_part_2():
    l1, l2 = get_input_lines()
    # get counts per number in l2
    counts = defaultdict(int)
    for li2 in l2:
        counts[li2] += 1
    sim_score = 0
    # add sim score contribution for each item in l1
    for li1 in l1:
        sim_score += li1 * counts[li1]
    print(sim_score)


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()

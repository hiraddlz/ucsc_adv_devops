#!/usr/bin/env python3
"""
part1_sum.py
Usage: python3 part1_sum.py input.txt

For each line: find the first digit and the last digit in the line (left-to-right).
Form the two-digit number (first*10 + last) and sum over all lines.
Lines with no digits are ignored (treated as 0).
"""

import sys
import re

def two_digit_from_line(line):
    digits = re.findall(r'\d', line)
    if not digits:
        return None
    return int(digits[0]) * 10 + int(digits[-1])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 part1_sum.py input.txt")
        sys.exit(1)

    path = sys.argv[1]
    total = 0
    no_digit_lines = 0

    with open(path, 'r', encoding='utf-8') as f:
        for lineno, line in enumerate(f, start=1):
            line = line.rstrip('\n')
            val = two_digit_from_line(line)
            if val is None:
                no_digit_lines += 1
            else:
                total += val

    print(total)
    if no_digit_lines:
        print(f"# warning: {no_digit_lines} line(s) contained no digits and were ignored", file=sys.stderr)

if __name__ == "__main__":
    main()

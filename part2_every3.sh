#!/usr/bin/env bash
# part2_every3.sh
# Usage: ./part2_every3.sh input.txt
# Sums the two-digit calibration values but only for every 3rd line (lines 3,6,9,...)

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 input.txt" >&2
  exit 1
fi

file="$1"
sum=0
lineno=0

while IFS= read -r line || [ -n "$line" ]; do
  lineno=$((lineno + 1))
  # only process every 3rd line
  if [ $((lineno % 3)) -ne 0 ]; then
    continue
  fi

  # extract digits in order
  digits=$(printf "%s" "$line" | tr -cd '[:digit:]')

  if [ -z "$digits" ]; then
    # no digits on this line -> skip
    continue
  fi

  # get first and last digit
  first=${digits:0:1}
  # portable: get last via length arithmetic
  len=${#digits}
  last=${digits:len-1:1}

  value=$(( first * 10 + last ))
  sum=$(( sum + value ))
done < "$file"

echo "$sum"

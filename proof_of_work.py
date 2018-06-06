#!/usr/bin/env python
from datetime import datetime
import hashlib
import time


def proof_of_work_tester():
    num_zeroes = 7
    x = 5
    # y = 0  # We don't know what y should be yet...
    # ans = str(x * y)
    my_hash = '2' * num_zeroes

    chars_to_find = '0' * num_zeroes
    cntr = 0
    # while my_hash[-2::] != '00' and y < 500:    # ends with 2 zeros
    for y in range(1, 1000000001):
        if my_hash[:num_zeroes] == chars_to_find:
            timestamp = str(datetime.now())
            print('{timestamp} Counter: {y} Solution: {my_hash}'.
                  format(timestamp=timestamp, y=y, my_hash=my_hash))
            cntr += 1

            time.sleep(5)

            if cntr == 1:
                break
        ans = str(x * y)
        my_hash = hashlib.sha256(ans.encode()).hexdigest()

    # print('The solution is y = {y} {my_hash}'.format(y=y, my_hash= my_hash))


if __name__ == '__main__':
    proof_of_work_tester()
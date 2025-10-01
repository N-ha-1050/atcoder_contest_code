import bisect
import sys

import numpy as np


def initialize():
    nums = np.empty(0, dtype=int)

    for a in range(1, 10):
        nums = np.append(nums, a)
        for d in range(-9, 9):
            n = dg = a
            for _ in range(17):
                dg += d
                if not (0 <= dg < 10):
                    break
                n = n * 10 + dg
                nums = np.append(nums, n)
    nums.sort()
    np.save("./tmp.npy", nums)


def main():
    X = int(input())
    res = solve(X)
    print(res)


def solve(X: int) -> int:
    nums = np.load("./tmp.npy")
    i = bisect.bisect_left(nums, X)
    return nums[i]


if __name__ == "__main__":
    if sys.argv[-1] == "ONLINE_JUDGE":
        initialize()
    else:
        main()

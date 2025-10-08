def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = [int(s) for s in input()]
        res = solve(N, S)
        print(res)


def solve(N: int, S: list[int]) -> int:
    res = -1
    for t in (0, 1):
        cnt = 0
        max_length = -1
        current_length = 0
        for s in S:
            if s == t:
                cnt += 1
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        else:
            max_length = max(max_length, current_length)
        r = 2 * (cnt - max_length) + (N - cnt)
        if res == -1 or r < res:
            res = r
    return res


if __name__ == "__main__":
    main()

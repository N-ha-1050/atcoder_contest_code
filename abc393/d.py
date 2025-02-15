def main():
    N = int(input())
    S = [int(s) for s in input()]
    res = solve(N, S)
    print(res)


def solve(N: int, S: list[int]) -> int:
    # S のうち 1 であるインデックスのリスト
    one_idxs = [i for i, s in enumerate(S) if s == 1]
    one_count = len(one_idxs)
    i_half = one_count // 2
    cnt = one_idxs[i_half] - i_half  # 左から cnt 番目を 1 の集団の左端にすることが最適
    return sum(
        cnt - (idx - i) if i < i_half else (idx - i) - cnt
        for i, idx in enumerate(one_idxs)
    )


if __name__ == "__main__":
    main()

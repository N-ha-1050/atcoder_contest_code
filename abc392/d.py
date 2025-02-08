def main():
    N = int(input())
    KA = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, KA)
    print(res)


def solve(N: int, KA: list[tuple[int, ...]]):
    K = [-1 for _ in range(N)]
    cnt: list[dict[int, int]] = [dict() for _ in range(N)]
    for i, (k, *a) in enumerate(KA):
        K[i] = k
        for aa in a:
            aa -= 1
            if aa not in cnt[i]:
                cnt[i][aa] = 0
            cnt[i][aa] += 1

    res = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            r = sum(cnt[i][key] * cnt[j][key] for key in cnt[i] if key in cnt[j])
            res = max(res, r / (K[i] * K[j]))

    return res


if __name__ == "__main__":
    main()

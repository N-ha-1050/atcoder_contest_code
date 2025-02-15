def main():
    N, M = map(int, input().split())
    uv = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    res = solve(N, M, uv)
    print(res)


def solve(N: int, M: int, uv: list[list[int]]) -> int:
    edges: set[tuple[int, int]] = set()
    cnt = 0
    for u, v in uv:
        if u == v:
            cnt += 1
            continue
        if u > v:
            u, v = v, u
        if (u, v) in edges:
            cnt += 1
            continue
        edges.add((u, v))
    return cnt


if __name__ == "__main__":
    main()

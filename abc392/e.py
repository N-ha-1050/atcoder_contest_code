from atcoder.dsu import DSU


def main():
    N, M = map(int, input().split())
    AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    res = solve(N, M, AB)
    print(len(res))
    for r in res:
        print(*r)


def solve(N: int, M: int, AB: list[tuple[int, ...]]):
    dsu = DSU(N)
    unused_edges: set[tuple[int, int, int]] = set()
    for i, (a, b) in enumerate(AB):
        if dsu.same(a, b):
            unused_edges.add((i, a, b))
        else:
            dsu.merge(a, b)

    leaders = {dsu.leader(i) for i in range(N)}
    res: list[tuple[int, int, int]] = []
    for i, a, b in unused_edges:
        if len(leaders) == 1:
            return res
        from_leader = dsu.leader(b)
        leaders.remove(from_leader)
        to_leader = leaders.pop()
        res.append((i + 1, b + 1, to_leader + 1))
        leaders.add(dsu.merge(b, to_leader))
    return res


if __name__ == "__main__":
    main()

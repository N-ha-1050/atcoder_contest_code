from collections import deque


def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    PX = [list(map(int, input().split())) for _ in range(Q)]
    res = solve(N, Q, AB, PX)
    print(*res)


def solve(N: int, Q: int, AB: list[list[int]], PX: list[list[int]]) -> list[int]:
    G: list[set[int]] = [set() for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        G[a].add(b)
        G[b].add(a)
    cnt = [0 for _ in range(N)]
    for p, x in PX:
        p -= 1
        cnt[p] += x
    visited = [False for _ in range(N)]
    que = deque([0])
    while que:
        v = que.popleft()
        if visited[v]:
            continue
        visited[v] = True
        for nv in G[v]:
            if visited[nv]:
                continue
            cnt[nv] += cnt[v]
            que.append(nv)
    return cnt


if __name__ == "__main__":
    main()

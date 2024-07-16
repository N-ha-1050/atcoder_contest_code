import heapq


def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    UVB = [tuple(map(int, input().split())) for _ in range(M)]
    res = solve(N, M, A, UVB)
    print(*res)


def solve(N, M, A, UVB):

    # 隣接リストでグラフを定義
    G = [set() for _ in range(N)]
    for u, v, b in UVB:

        # 辺の終点のコストも辺のコストに加えておく
        # →あとで、ダイクストラ法がそのまま行える
        G[u - 1].add((v - 1, b + A[v - 1]))
        G[v - 1].add((u - 1, b + A[u - 1]))

    # ダイクストラ法
    mem = [None for _ in range(N)]
    que = [(A[0], 0)]  # que[i] = (cost, node)
    while que:
        cost, now = heapq.heappop(que)
        if mem[now] is not None:
            continue
        mem[now] = cost
        for ne, c in G[now]:
            ne_cost = cost + c
            if mem[ne] is None or ne_cost < mem[ne]:
                heapq.heappush(que, (ne_cost, ne))

    # 頂点2(index 1)以降を返す
    return mem[1:]


if __name__ == "__main__":
    main()

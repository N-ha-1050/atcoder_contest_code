import heapq


def main():
    N = int(input())
    ABC = [list(map(int, input().split())) for _ in range(N - 1)]
    res = solve(N, ABC)
    print(res)


def solve(N, ABC):

    # 合計コスト
    total_cost = 0

    # 隣接リストを構築
    G = [set() for _ in range(N)]
    for a, b, c in ABC:
        G[a - 1].add((b - 1, c))
        G[b - 1].add((a - 1, c))
        total_cost += c

    # ダイクストラ法を2回行い、木の直径を求める

    # ダイクストラ法1回目: 頂点0から最も遠い点を探索
    mem = [None for _ in range(N)]
    que = [(0, 0)]

    while que:
        cost, now = heapq.heappop(que)
        if mem[now] is not None:
            continue
        mem[now] = cost
        for nex, c in G[now]:
            if mem[nex] is None or cost + c < mem[nex]:
                heapq.heappush(que, (cost + c, nex))

    st = mem.index(max(mem))

    # ダイクストラ法2回目: stから最も遠い点を探索
    mem2 = [None for _ in range(N)]
    que2 = [(0, st)]

    while que2:
        cost, now = heapq.heappop(que2)
        if mem2[now] is not None:
            continue
        mem2[now] = cost
        for nex, c in G[now]:
            if mem2[nex] is None or cost + c < mem2[nex]:
                heapq.heappush(que2, (cost + c, nex))

    # 木の直径
    l = max(mem2)

    return total_cost * 2 - l


if __name__ == "__main__":
    main()

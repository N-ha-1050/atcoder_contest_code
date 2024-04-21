from collections import deque


def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    res = solve(N, M, AB)
    print(res)


def solve(N, M, AB):
    def nC2(n):
        return n * (n - 1) // 2

    G = [set() for _ in range(N)]
    for a, b in AB:
        G[a - 1].add(b - 1)
        G[b - 1].add(a - 1)

    mem = [False for _ in range(N)]

    res = 0
    for i in range(N):
        # 確認済みなら次へ
        if mem[i]:
            continue

        # BFS
        deq = deque([i])
        cnt = 0  # 頂点数
        while deq:
            d = deq.popleft()
            if mem[d]:
                continue
            mem[d] = True
            cnt += 1
            for g in G[d]:
                deq.append(g)
        res += nC2(cnt)  # 辺の本数を加算

    res -= M  # もともと友達なMを引く
    return res


if __name__ == "__main__":
    main()

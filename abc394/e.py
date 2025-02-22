from collections import deque


def main():
    N = int(input())
    C = [input() for _ in range(N)]
    res = solve(N, C)
    for r in res:
        print(*r)


def solve(N: int, C: list[str]) -> list[list[int]]:
    # CPython だと TLE(PyPy なら通る)

    res = [[-1 for _ in range(N)] for _ in range(N)]
    next_nodes: list[set[tuple[int, str]]] = [set() for _ in range(N)]
    prev_nodes: list[set[tuple[int, str]]] = [set() for _ in range(N)]

    # (cost, start, end): 回文を短い順に記録、頂点iから頂点jまでの最短距離costを求める
    que: deque[tuple[int, int, int]] = deque()

    # 距離0
    for i in range(N):
        res[i][i] = 0
        que.append((0, i, i))
        if C[i][i] != "-":
            next_nodes[i].add((i, C[i][i]))
            prev_nodes[i].add((i, C[i][i]))

    # 距離1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if C[i][j] != "-":
                res[i][j] = 1
                que.append((1, i, j))
                next_nodes[i].add((j, C[i][j]))
                prev_nodes[j].add((i, C[i][j]))

    # 距離が短い順に作成
    while que:
        cost, start, end = que.popleft()

        # (startの前に接続できるすべての頂点) x (endの後に接続できるすべての頂点) の組み合わせを探索
        for start_prev, start_prev_char in prev_nodes[start]:
            for end_next, end_next_char in next_nodes[end]:
                if start_prev_char != end_next_char:
                    continue
                if res[start_prev][end_next] == -1:
                    res[start_prev][end_next] = cost + 2
                    que.append((cost + 2, start_prev, end_next))

    return res


if __name__ == "__main__":
    main()

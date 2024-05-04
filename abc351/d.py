from atcoder.dsu import DSU


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    res = solve(H, W, S)
    print(res)


def solve(H, W, S):

    # グリッド関係の関数の定義
    def is_in(i, j):
        """
        マス(i, j) がグリッド内に存在するかを返す
        """
        return 0 <= i < H and 0 <= j < W

    def t2o(i, j):
        """
        マス(i, j) を一次元化した値を返す
        """
        return i * W + j

    def o2t(n):
        """
        一次元化したら n になるマス(i, j)を返す
        n はグリッドに含まれるマスを一次元化した値であることが前提
        """
        return n // W, n % W

    # 周囲4マスを求めるためのリスト
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # DSU(Union-Find) を定義
    dsu = DSU(H * W)

    # 磁石に隣接するマスを求める
    adj_mag = [[False for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != "#":
                continue
            for di, dj in ds:
                ni, nj = i + di, j + dj
                if not is_in(ni, nj):
                    continue
                adj_mag[ni][nj] = True

    # 隣り合っていて、いずれも磁石に隣接しないマス同士を連結
    for i in range(H):
        for j in range(W):
            if adj_mag[i][j]:
                continue
            if is_in(i + 1, j) and not adj_mag[i + 1][j]:
                dsu.merge(t2o(i, j), t2o(i + 1, j))
            if is_in(i, j + 1) and not adj_mag[i][j + 1]:
                dsu.merge(t2o(i, j), t2o(i, j + 1))

    # 各マスと連結している頂点数を求める
    # → 磁石に隣接するマスを除いた到達できるマスの個数
    cnt = [None for _ in range(H * W)]
    for n in range(H * W):
        i, j = o2t(n)
        cnt[n] = 0 if S[i][j] == "#" else dsu.size(n)

    # 磁石に隣接しているマスの個数を足す
    for i in range(H):
        for j in range(W):
            if S[i][j] != "#" and adj_mag[i][j]:
                mem = set()
                for di, dj in ds:
                    ni, nj = i + di, j + dj
                    if not is_in(ni, nj):
                        continue
                    if S[ni][nj] == "#":
                        continue
                    if not adj_mag[ni][nj]:
                        mem.add(dsu.leader(t2o(ni, nj)))
                for leader in mem:
                    cnt[leader] += 1
    # 最大値を返す
    return max(cnt)


if __name__ == "__main__":
    main()

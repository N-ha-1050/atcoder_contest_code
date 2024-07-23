# CPython だと TLE(PyPy なら通る)

import heapq


def main():
    H, W, Y = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    res = solve(H, W, Y, A)
    print(*res, sep="\n")


def solve(H, W, Y, A):

    # 決定した区画を管理する優先度付きキュー
    # que[idx] := (a, (i, j))、区画(i, j)は標高aで決定済み
    que = []

    # 区画が決定しているかを管理する二重リスト
    # mem[i][j] := a、区画(i, j)は標高aで決定済み
    mem = [[None for _ in range(W)] for _ in range(H)]

    # 1年後からY年後までのうちに沈む区画の数を記録
    cnt = [0 for _ in range(Y)]

    def is_exist(i: int, j: int):
        """区画が存在するか

        与えられた区画(i, j)が存在するかを判定する。

        Args:
            i (int): 0-indexedで上から何番目の区画か
            j (int): 0-indexedで左から何番目の区画か

        Returns:
            bool: 区画が存在するか
        """
        return 0 <= i < H and 0 <= j < W

    def set(i, j, a):
        """区画を決定する

        与えられた区画(i, j)が沈む年をa年後で決定する。
        すでに決定済みの場合何もしない。
        区画(i, j)の存在を前提とする。

        Args:
            i (int): 0-indexedで上から何番目の区画か
            j (int): 0-indexedで左から何番目の区画か
            a (int): 区画(i, j)が何年後に沈むか

        Returns:
            bool: 今回の呼び出しで決定したか
        """

        # 区画が存在しない場合 Assertion Error
        assert is_exist(i, j)

        # すでに決定済みの場合 False を返す
        if mem[i][j] is not None:
            return False

        # キューとリストを更新
        mem[i][j] = a
        heapq.heappush(que, (a, (i, j)))
        if 1 <= a <= Y:
            cnt[a - 1] += 1
        return True

    # 海に隣接する区画(外周)を決定する
    for i in range(H):
        set(i, 0, A[i][0])
        set(i, W - 1, A[i][W - 1])
    for j in range(W):
        set(0, j, A[0][j])
        set(H - 1, j, A[H - 1][j])

    ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 周囲のマス

    while que:
        # 決定しいる区画のうち最も早く沈む区画を取り出す
        a, (i, j) = heapq.heappop(que)

        # 周囲のマスについて
        for di, dj in ds:
            ni, nj = i + di, j + dj

            # 区画が存在しない場合次へ
            if not is_exist(ni, nj):
                continue

            # 区画(ni, nj)について、
            # aよりも高ければA[ni][nj]年後に沈み、
            # aよりも低ければ区画(i, j)とともにa年後に沈むことを決定する。
            set(ni, nj, max(a, A[ni][nj]))

    # 答えの生成
    # →残っている区画を数える
    res = [None for _ in range(Y)]
    r = H * W
    for i in range(Y):
        r -= cnt[i]
        res[i] = r

    return res


if __name__ == "__main__":
    main()

class A:
    def main(self):
        S = input()
        res = self.solve(S)
        print(res)

    def solve(self, S):
        return S.split(".")[-1]


class B:
    def main(self):
        H, W, N = map(int, input().split())
        res = self.solve(H, W, N)
        print(*res, sep="\n")

    def solve(self, H, W, N):
        # grids[i][j] := (i, j)が黒いか(i, jは0-index)
        grids = [[False for _ in range(W)] for _ in range(H)]

        # 現在の座標
        i, j = 0, 0

        # 方向リストと現在のインデックス
        # インデックスが1増えると90度時計回り
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        idx = 0

        # シミュレーション
        for _ in range(N):
            if grids[i][j]:  # 黒いとき
                # 白にして反時計回り
                grids[i][j] = False
                idx -= 1
            else:  # 白いとき
                # 黒にして時計回り
                grids[i][j] = True
                idx += 1
            # インデックスを範囲内に正規化(mod4をとる)
            idx %= 4

            # そのインデックスの方向に進む
            di, dj = dirs[idx]
            i += di
            j += dj

            # トーラス状の処理
            i %= H
            j %= W

        # 回答を生成
        res = ["".join("#" if c else "." for c in grid) for grid in grids]
        return res


class C:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve(N, A)
        print(res)

    def solve(self, N, A):
        now, mem = 0, 0
        for a in A:
            now += a
            mem = min(mem, now)
        return now - mem


class D:
    def main(self):
        N = int(input())
        S = [input() for _ in range(N)]
        res = self.solve(N, S)
        print(-1 if res is None else res)

    def solve(self, N, S):
        # CPython だと TLE(PyPy なら通る)

        from collections import deque

        T = [[False for _ in range(N)] for _ in range(N)]
        p1, p2 = None, None
        for i, s in enumerate(S):
            for j, t in enumerate(s):
                if t == "#":
                    T[i][j] = True
                if t == "P":
                    if p1 is None:
                        p1 = (i, j)
                    else:
                        p2 = (i, j)

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_in(p):
            i, j = p
            return 0 <= i < N and 0 <= j < N

        def is_obstract(p):
            i, j = p
            return T[i][j]

        def move(p, d):
            i, j = p
            di, dj = d
            np = (i + di, j + dj)
            if not is_in(np):
                return p
            if is_obstract(np):
                return p
            return np

        mem = [
            [[[None for _ in range(N)] for _ in range(N)] for _ in range(N)]
            for _ in range(N)
        ]

        def mget(p, q):
            pi, pj = p
            qi, qj = q
            return mem[pi][pj][qi][qj]

        def mset(p, q, v):
            pi, pj = p
            qi, qj = q
            mem[pi][pj][qi][qj] = v

        mset(p1, p2, 0)

        que = deque([(p1, p2)])
        res = None
        while que:
            p, q = que.popleft()
            for d in dirs:
                np, nq = move(p, d), move(q, d)
                if mget(np, nq) is not None:
                    continue
                mset(np, nq, mget(p, q) + 1)
                if np == nq:
                    if res is None or mget(np, nq) < res:
                        res = mget(np, nq)
                    continue
                if res is not None and res <= mget(np, nq):
                    continue
                que.append((np, nq))
        return res


class E:
    def main(self):
        N, D = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve(N, D, A)
        print(res)

    def solve(self, N, D, A):
        # CPython だと TLE(PyPy なら通る)

        max_A = max(A)

        seg_init = [0 for _ in range(max_A + 1)]
        seg_n = max_A + 1
        seg_op = max
        seg_e = 0

        seg_size = 1 << (seg_n - 1).bit_length()
        seg = [seg_e for _ in range(2 * seg_size)]
        seg[seg_size : seg_size + seg_n] = seg_init

        def seg_set(i):
            seg[i] = seg_op(seg[i << 1], seg[(i << 1) + 1])

        for i in reversed(range(1, seg_size)):
            seg_set(i)

        def seg_update(i, x):
            i += seg_size
            seg[i] = x
            while i > 1:
                i >>= 1
                seg_set(i)

        def seg_get(l, r=None):
            if r is None:
                r = l + 1

            l += seg_size
            r += seg_size

            res_l = seg_e
            res_r = seg_e

            while l < r:
                if l & 1:
                    res_l = seg_op(res_l, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res_r = seg_op(seg[r], res_r)
                l >>= 1
                r >>= 1
            return seg_op(res_l, res_r)

        for a in A:
            v = seg_get(max(a - D, 0), min(a + D, max_A) + 1)
            seg_update(a, v + 1)

        return seg_get(0, max_A + 1)


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

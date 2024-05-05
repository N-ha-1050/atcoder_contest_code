class A:
    def main(self):
        A, B, D = map(int, input().split())
        res = self.solve(A, B, D)
        print(*res)

    def solve(self, A, B, D):
        return range(A, B + 1, D)


class B:
    def main(self):
        Q = int(input())
        tx = [tuple(map(int, input().split())) for _ in range(Q)]
        res = self.solve(Q, tx)
        print(*res, sep="\n")

    def solve(self, Q, tx):
        A = []
        res = []
        for t, x in tx:
            if t == 1:
                A.append(x)
            if t == 2:
                res.append(A[-x])
        return res


class C:
    def main(self):
        N = int(input())
        res = self.solve3(N)
        print(res)

    def solve(self, N):
        mem = {}  # メモ化用の辞書

        def calc(x):
            if x == 1:  # 終了条件
                return 0

            if x in mem:  # 呼ばれたことがあったらその時の値を返す
                return mem[x]

            # 呼ばれてなかったら計算して mem に追加
            mem[x] = calc(x // 2) + calc((x + 1) // 2) + x

            # 整数除算の切り上げ・切り捨て
            # 整数 x, y に対する除算 x ÷ y について、
            #   切り捨て: x // y
            #   切り上げ: (x + y - 1) // y または -(-x // y)
            # float を介すと誤差が出る可能性がある(競プロの場合、誤差が出るテストケースが必ずある!!)

            return mem[x]

        return calc(N)

    def solve2(self, N):
        mem = {1: 0}  # 終了条件を予め定義

        def calc(x):
            if x not in mem:
                mem[x] = calc(x // 2) + calc((x + 1) // 2) + x
            return mem[x]

        return calc(N)

    def solve3(self, N):
        from functools import cache

        @cache  # デコレータを使用
        def calc(x):
            return 0 if x == 1 else calc(x // 2) + calc((x + 1) // 2) + x

        return calc(N)


class D:
    def main(self):
        N = int(input())
        ABX = [map(int, input().split()) for _ in range(N - 1)]
        res = self.solve(N, ABX)
        print(res)

    def solve(self, N, ABX):
        import heapq

        # グラフを隣接リスト(集合)で構築
        G = [set() for _ in range(N)]

        for i, (a, b, x) in enumerate(ABX):
            G[i].add((i + 1, a))
            G[i].add((x - 1, b))

        # 頂点0からダイクストラ法
        dist = [None for _ in range(N)]
        dist[0] = 0
        done = [False for _ in range(N)]

        que = []
        heapq.heapify(que)

        heapq.heappush(que, (0, 0))

        while que:
            d, v = heapq.heappop(que)
            if done[v]:
                continue
            for end, leng in G[v]:
                if dist[end] is None or dist[v] + leng < dist[end]:
                    dist[end] = dist[v] + leng
                    heapq.heappush(que, (dist[end], end))
            done[v] = True

        # 頂点(N - 1) までの距離を返す
        return dist[N - 1]


class E:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) for a in input().split()]
        B = [int(b) for b in input().split()]
        res = self.solve2(N, M, A, B)
        print(*res)

    def solve(self, N, M, A, B):
        # CPython だと TLE(PyPy なら通る)

        # AtCoder Library を使用
        # https://github.com/not522/ac-library-python

        from atcoder.lazysegtree import LazySegTree

        # 遅延評価セグメント木を定義
        lst = LazySegTree(
            lambda x, y: 0,  # 今回は区間に対する演算はしないので適当
            0,  # 同上
            lambda lazy, data: lazy + data,  # 区間加算
            lambda add_lazy, prev_lazy: add_lazy + prev_lazy,  # 区間加算
            0,  # 加算の単位元0
            A,  # 初期リスト
        )

        # Bを順番にシミュレーション
        for b in B:
            x = lst.get(b)  # 箱b のボールの個数を x に代入
            lst.set(b, 0)  # 箱b を空にする
            q, r = x // N, x % N  # x を N で割った 商q と 余りr を求める
            lst.apply(0, N, q)  # 区間[0, N) (=全区間)の箱に q個 ずつ加える
            left, right = (
                b + 1,
                b + r + 1,
            )  # 配れてない r個 を配るために追加で 1個 ずつ配る区間を求める
            left %= N
            right %= N
            if right < left:  # 箱left → 箱(N-1) → 箱0 → 箱(right - 1) の場合
                lst.apply(left, N, 1)  # 区間[left, N) の箱に 1個 ずつ加える
                lst.apply(0, right, 1)  # 区間[0, right) の箱に 1個 ずつ加える
            else:  # (箱0 →) 箱left → 箱(right - 1) (→ 箱(N - 1)) の場合
                lst.apply(left, right, 1)  # 区間[left, right) の箱に 1個 ずつ加える

        res = [lst.get(i) for i in range(N)]  # 各箱に入っているボールの個数を求める
        return res

    def solve2(self, N, M, A, B):
        # CPython だと TLE(PyPy なら通る)

        # AtCoder Library を使用
        # https://github.com/not522/ac-library-python

        from atcoder.fenwicktree import FenwickTree

        # フェニック木を定義
        ft = FenwickTree(N)

        D = [a2 - a1 for a1, a2 in zip([0] + A, A)]
        for i, d in enumerate(D):
            ft.add(i, d)

        for b in B:
            x = ft.sum(0, b + 1)
            ft.add(b, -x)
            if b + 1 < N:
                ft.add(b + 1, x)

            q, r = x // N, x % N

            ft.add(0, q)
            left, right = b + 1, b + r + 1
            left %= N
            right %= N
            if right < left:
                ft.add(left, 1)
                ft.add(0, 1)
                ft.add(right, -1)
            else:
                ft.add(left, 1)
                ft.add(right, -1)

        return [ft.sum(0, i + 1) for i in range(N)]


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

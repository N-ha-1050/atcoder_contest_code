class A:
    def main(self):
        S = input()
        res = self.solve2(S)
        print("Yes" if res else "No")

    def solve(self, S):
        return S.istitle()

    def solve2(self, S):
        import re

        return re.fullmatch("[A-Z][a-z]*", S)


class B:
    def main(self):
        S = input()
        res = self.solve(S)
        print(res)

    def solve(self, S):
        import collections

        T = collections.Counter(S)
        return min(T.items(), key=lambda x: (-x[1], x[0]))[0]


class C:
    def main(self):
        N = int(input())
        Q = [int(q) for q in input().split()]
        A = [int(a) for a in input().split()]
        B = [int(b) for b in input().split()]
        res = self.solve(N, Q, A, B)
        print(res)

    def solve(self, N, Q, A, B):
        QAB = [(q, a, b) for q, a, b in zip(Q, A, B) if b != 0]

        def calc(x):
            y = None
            for q, a, b in QAB:
                c = q - a * x
                if c < 0:
                    return None
                d = c // b
                if y is None or d < y:
                    y = d
            return y

        res = 0
        ma = min(q // a for q, a in zip(Q, A) if a != 0)
        for x in range(ma + 1):
            y = calc(x)
            res = max(res, x + y)
        return res


class D:
    def main(self):
        N, M = map(int, input().split())
        X = [int(x) - 1 for x in input().split()]
        res = self.solve(N, M, X)
        print(res)

    def solve(self, N, M, X):
        cnt = 0  # 封印しない場合の最小距離

        # cost[i] := (橋iを封鎖したとき場合に最小距離から増加する距離)としてimos法を行うためのリスト
        cost = [0 for _ in range(N)]

        for x1, x2 in zip(X, X[1:]):
            if x2 < x1:
                x1, x2 = x2, x1

            dist1 = x2 - x1  # 橋(N - 1)を渡らない向きでの距離
            dist2 = N - dist1  # 橋(N - 1)を渡る向きでの距離

            diff = abs(
                dist1 - dist2
            )  # 距離の差、距離が短い方に含まれる橋を封鎖したときに増加する距離

            cnt += min(dist1, dist2)  # 橋を封鎖しないときは単純に最短距離の方で移動

            if dist2 < dist1:
                cost[x2] += diff

                cost[0] += diff
                cost[x1] -= diff
            else:
                cost[x1] += diff
                cost[x2] -= diff

        # imos法を行いながらcostの最小値を取得
        min_cost = cost[0]
        for i in range(1, N):
            cost[i] += cost[i - 1]
            min_cost = min(min_cost, cost[i])

        return cnt + min_cost


class E:
    def main(self):
        N = int(input())
        AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
        res = self.solve(N, AB)
        print("Yes" if res else "No")

    def solve(self, N, AB):
        from collections import deque

        cnt = [None for _ in range(2 * N)]
        for i, (a, b) in enumerate(AB):
            if b < a:
                a, b = b, a
            cnt[a] = (0, i)
            cnt[b] = (1, i)

        que = deque()

        for t, p in cnt:
            if t == 0:
                que.append(p)
            if t == 1:
                q = que.pop()
                if p != q:
                    return True
        return False


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

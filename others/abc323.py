class A:
    def main(self):
        S = input()
        res = self.solve(S)
        print("Yes" if res else "No")

    def solve(self, S):
        return all([int(s) == 0 for s in S][1::2])

    def test(self):
        pass


class B:
    def main(self):
        N = int(input())
        S = [input() for _ in range(N)]
        res = self.solve(N, S)
        print(*res)

    def solve(self, N, S):
        cnt = [0 for _ in range(N)]
        for i, ss in enumerate(S):
            for s in ss:
                if s == "o":
                    cnt[i] += 1
        res = sorted((-c, i) for i, c in enumerate(cnt))
        return [a + 1 for _, a in res]

    def test(self):
        pass


class C:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) for a in input().split()]
        S = [input() for _ in range(N)]
        res = self.solve(N, M, A, S)
        print(*res, sep="\n")

    def solve(self, N, M, A, S):
        sorted_A = sorted(((a, i) for i, a in enumerate(A)), reverse=True)
        T = [[s == "o" for s in ss] for ss in S]
        points = [sum([a for t, a in zip(tt, A) if t]) + i for i, tt in enumerate(T, 1)]
        ma = max(points)

        res = []
        for i, t in enumerate(T):
            point = points[i]
            cnt = 0
            for a, idx in sorted_A:
                if ma <= point:
                    break
                if t[idx]:
                    continue
                point += a
                cnt += 1
            res.append(cnt)

        return res

    def test(self):
        pass


class D:
    def main(self):
        N = int(input())
        SC = [tuple(map(int, input().split())) for _ in range(N)]
        res = self.solve2(N, SC)
        print(res)

    def solve(self, N, SC):
        # CPython だと TLE(PyPy なら通る)
        import heapq

        slimes = {s: c for s, c in SC}
        que = list(slimes)
        heapq.heapify(que)
        while que:
            s = heapq.heappop(que)
            c = slimes[s]
            slimes[s] = c % 2
            if ad := c // 2:
                if 2 * s in slimes:
                    slimes[2 * s] += ad
                else:
                    slimes[2 * s] = ad
                    heapq.heappush(que, 2 * s)
        return sum(slimes.values())

    def solve2(self, N, SC):
        slimes = {}
        for s, c in SC:
            while s & 1 == 0:
                s >>= 1
                c <<= 1
            slimes[s] = slimes.get(s, 0) + c

        return sum(c.bit_count() for c in slimes.values())

    def test(self):
        pass


class E:
    def main(self):
        N, X = map(int, input().split())
        T = [int(t) for t in input().split()]
        res = self.solve(N, X, T)
        print(res)

    def solve(self, N, X, T):
        MOD = 998244353
        inv_N = pow(N, -1, MOD)

        dp = [0 for _ in range(X + 1)]
        dp[0] = inv_N

        for t in range(X + 1):
            for dt in T:
                if X < t + dt:
                    continue
                dp[t + dt] += dp[t] * inv_N
                dp[t + dt] %= MOD

        return sum(dp[X - T[0] + 1 : X + 1]) % MOD

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

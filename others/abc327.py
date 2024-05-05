class A:
    def main(self):
        N = int(input())
        S = input()
        res = self.solve(N, S)
        print("Yes" if res else "No")

    def solve(self, N, S):
        return "ab" in S or "ba" in S

    def test(self):
        pass


class B:
    def main(self):
        B = int(input())
        res = self.solve(B)
        print(res)

    def solve(self, B):
        A = 1
        while pow(A, A) < B:
            A += 1
        return A if pow(A, A) == B else -1

    def test(self):
        pass


class C:
    def main(self):
        A = [tuple(map(int, input().split())) for _ in range(9)]
        res = self.solve(A)
        print("Yes" if res else "No")

    def solve(self, A):
        for i in range(9):
            mem = [False for _ in range(9)]
            for j in range(9):
                if mem[A[i][j] - 1]:
                    return False
                mem[A[i][j] - 1] = True

        for j in range(9):
            mem = [False for _ in range(9)]
            for i in range(9):
                if mem[A[i][j] - 1]:
                    return False
                mem[A[i][j] - 1] = True

        for kl in range(9):
            k, l = kl // 3, kl % 3
            mem = [False for _ in range(9)]
            for mn in range(9):
                m, n = mn // 3, mn % 3
                i, j = 3 * k + m, 3 * l + n
                if mem[A[i][j] - 1]:
                    return False
                mem[A[i][j] - 1] = True

        return True

    def test(self):
        pass


class D:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) for a in input().split()]
        B = [int(b) for b in input().split()]
        res = self.solve(N, M, A, B)
        print("Yes" if res else "No")

    def solve(self, N, M, A, B):
        from collections import deque

        G = [set() for _ in range(N)]
        for a, b in zip(A, B):
            G[a - 1].add(b - 1)
            G[b - 1].add(a - 1)
        mem = [None for _ in range(N)]
        for v in range(N):
            if mem[v] is not None:
                continue
            mem[v] = 0
            deq = deque([v])
            while deq:
                pv = deq.popleft()
                for nv in G[pv]:
                    if mem[nv] is not None:
                        if mem[nv] == mem[pv]:
                            return False
                        continue
                    mem[nv] = 1 - mem[pv]
                    deq.append(nv)
        return True

    def test(self):
        pass


class E:
    def main(self):
        N = int(input())
        P = [int(p) for p in input().split()]
        res = self.solve2(N, P)
        print(res)

    def solve(self, N, P):
        # CPython だと TLE(PyPy なら通る)

        # dp[i][k] := (P[0] ~ P[i]) から k + 1 個選んだときの最大値
        dp = [[None for _ in range(i + 1)] for i in range(N)]
        dp[0][0] = P[0]

        for i in range(N - 1):
            dp[i + 1][0] = max(P[i + 1], dp[i][0])

        for i in range(N - 1):
            for k in range(i + 1):
                dp[i + 1][k + 1] = 0.9 * dp[i][k] + P[i + 1]
                if k < i and dp[i + 1][k + 1] < dp[i][k + 1]:
                    dp[i + 1][k + 1] = dp[i][k + 1]

        calc = lambda v, k: (v / (10 * (1 - pow(0.9, k)))) - (1200 / pow(k, 0.5))
        return max(calc(v, k) for k, v in enumerate(dp[N - 1], 1))

    def solve2(self, N, P):
        # dp[k] := (P[0] ~ P[i]) から k + 1 個選んだときの最大値
        dp = [P[0]]

        for i in range(1, N):
            pdp = [d for d in dp]
            dp = [None for _ in range(i + 1)]
            dp[0] = max(P[i], pdp[0])
            for k in range(1, i + 1):
                dp[k] = 0.9 * pdp[k - 1] + P[i]
                if k < i and dp[k] < pdp[k]:
                    dp[k] = pdp[k]

        calc = lambda v, k: (v / (10 * (1 - pow(0.9, k)))) - (1200 / pow(k, 0.5))
        return max(calc(v, k) for k, v in enumerate(dp, 1))

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

class A:
    def main(self):
        N = int(input())
        S = input()
        res = self.solve(N, S)
        print(res)

    def solve(self, N, S):
        return -1 if (res := S.find("ABC")) == -1 else res + 1

    def test(self):
        pass


class B:
    def main(self):
        N, M = map(int, input().split())
        S = input()
        T = input()
        res = self.solve(N, M, S, T)
        print(res)

    def solve(self, N, M, S, T):
        return int(T[-N:] != S) + int(T[:N] != S) * 2

    def test(self):
        pass


class C:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve(N, M, A)
        print(*res, sep="\n")

    def solve(self, N, M, A):
        idx = M - 1
        res = []

        for d in range(N, 0, -1):
            if idx > 0 and d == A[idx - 1]:
                idx -= 1
            res.append(A[idx] - d)

        return reversed(res)

    def test(self):
        pass


class D:
    def main(self):
        P = [[input() for _ in range(4)] for _ in range(3)]
        res = self.solve(P)
        print("Yes" if res else "No")

    def solve(self, P):
        def s2b(Q):
            return [[q == "#" for q in qq] for qq in Q]

        def delete(Q):
            for _ in range(2):
                Q = [q for q in zip(*Q) if any(q)]
            return Q

        def size(Q):
            return (len(Q), len(Q[0]))

        def rotate(Q, h, w):
            return [[Q[h - j - 1][i] for j in range(h)] for i in range(w)], w, h

        def check(Q):
            return all([all(q) for q in Q])

        P = [s2b(p) for p in P]
        P = [delete(p) for p in P]
        size_P = [size(p) for p in P]

        grid = [[False for _ in range(4)] for _ in range(4)]

        def dfs(idx=0):
            if idx == 3:
                return check(grid)
            h, w = size_P[idx]
            Q = P[idx]
            for _ in range(4):
                for i in range(5 - h):
                    for j in range(5 - w):
                        res = True
                        R = [[False for _ in range(w)] for _ in range(h)]
                        for di in range(h):
                            for dj in range(w):
                                if grid[i + di][j + dj] and Q[di][dj]:
                                    res = False
                                R[di][dj] = grid[i + di][j + dj]
                                grid[i + di][j + dj] = grid[i + di][j + dj] or Q[di][dj]
                        if res and dfs(idx + 1):
                            return True
                        for di in range(h):
                            for dj in range(w):
                                grid[i + di][j + dj] = R[di][dj]
                Q, h, w = rotate(Q, h, w)
            return False

        return dfs()

    def test(self):
        pass


class E:
    def main(self):
        N, K, P = map(int, input().split())
        CA = [tuple(map(int, input().split())) for _ in range(N)]
        res = self.solve2(N, K, P, CA)
        print(-1 if res is None else res)

    def solve(self, N, K, P, CA):
        dp = {tuple(0 for _ in range(K)): 0}
        res = None
        for C, *A in CA:
            for D, c in dp.copy().items():
                idx = tuple(min(P, D[i] + A[i]) for i in range(K))
                cost = c + C
                if res is not None and cost >= res:
                    continue
                if all(a == P for a in idx):
                    res = cost
                    continue
                if idx in dp and cost < dp[idx] or idx not in dp:
                    dp[idx] = cost
        return res

    def solve2(self, N, K, P, CA):
        dp = [None for _ in range((P + 1) ** K)]
        dp[0] = 0
        for C, *A in CA:
            new_dp = dp.copy()
            for i in range((P + 1) ** K):
                if dp[i] is None:
                    continue
                b, c = 0, i
                idx = 0
                for j, a in enumerate(A):
                    b = c % (P + 1)
                    c //= P + 1
                    idx += min(b + a, P) * (P + 1) ** j
                if new_dp[idx] is None or dp[i] + C < new_dp[idx]:
                    new_dp[idx] = dp[i] + C
            dp = new_dp
        return dp[(P + 1) ** K - 1]

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

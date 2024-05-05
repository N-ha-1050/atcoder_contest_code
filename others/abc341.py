class A:
    def main(self):
        N = int(input())
        res = self.solve2(N)
        print(res)

    def solve(self, N):
        return "10" * N + "1"

    def solve2(self, N):
        return "0".join("1" * (N + 1))


class B:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        ST = [tuple(map(int, input().split())) for _ in range(N - 1)]
        res = self.solve(N, A, ST)
        print(res)

    def solve(self, N, A, ST):
        for i, (s, t) in enumerate(ST):
            A[i + 1] += t * (A[i] // s)
        return A[N - 1]


class C:
    def main(self):
        H, W, N = map(int, input().split())
        T = input()
        S = [input() for _ in range(H)]
        res = self.solve2(H, W, N, T, S)
        print(res)

    def solve(self, H, W, N, T, S):
        # CPython だと TLE(PyPy なら通る)
        dirs = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        i, j = 0, 0
        mem = {(0, 0)}
        mi_i, mi_j = 0, 0
        ma_i, ma_j = 0, 0
        for t in T:
            di, dj = dirs[t]
            i += di
            j += dj
            mi_i, mi_j = min(mi_i, i), min(mi_j, j)
            ma_i, ma_j = max(ma_i, i), max(ma_j, j)
            mem.add((i, j))
        UH, UW = (
            ma_i - mi_i + 1,
            ma_j - mi_j + 1,
        )
        U = [[False for j in range(UW)] for i in range(UH)]
        for i, j in mem:
            U[i - mi_i][j - mi_j] = True
        R = [[r == "." for r in ss] for ss in S]
        res = 0
        for si in range(H - UH + 1):
            for sj in range(W - UW + 1):
                for i in range(UH):
                    for j in range(UW):
                        if U[i][j] and not R[si + i][sj + j]:
                            break
                    else:
                        continue
                    break
                else:
                    res += 1
        return res

    def solve2(self, H, W, N, T, S):
        # CPython だと TLE(PyPy なら通る)
        res = 0
        for i in range(H):
            for j in range(W):
                if S[i][j] == "#":
                    continue
                (
                    I,
                    J,
                ) = (
                    i,
                    j,
                )
                for t in T:
                    match t:
                        case "L":
                            J -= 1
                        case "R":
                            J += 1
                        case "U":
                            I -= 1
                        case "D":
                            I += 1
                    if S[I][J] == "#":
                        break
                else:
                    res += 1
        return res


class D:
    def main(self):
        N, M, K = map(int, input().split())
        res = self.solve(N, M, K)
        print(res)

    def solve(self, N, M, K):
        # CPython だと TLE(PyPy なら通る)
        import math

        L = math.lcm(N, M)
        a = L // N - 1  # N * 1 to N * a
        b = L // M - 1  # M * 1 to M * b
        s = a + b
        q, r = (K - 1) // s, (K - 1) % s
        i, j = 1, 1
        res = 0
        for _ in range(r + 1):
            if N * i < M * j:
                res = N * i
                i += 1
            else:
                res = M * j
                j += 1
        return res + L * q


class E:
    def main(self):
        N, Q = map(int, input().split())
        S = tuple(map(int, input()))
        queries = [tuple(map(int, input().split())) for _ in range(Q)]
        res = self.solve2(N, Q, S, queries)
        print(*map(lambda x: "Yes" if x else "No", res), sep="\n")

    def solve(self, N, Q, S, queries):
        # CPython だと TLE(PyPy なら通る)
        bit = [0 for _ in range(N)]

        def update(i, a):
            while i < N:
                bit[i] += a
                i += i & -i

        def sum(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        for i, (s1, s2) in enumerate(zip(S, S[1:]), 1):
            update(i, 0 if s1 == s2 else 1)

        res = []
        for t, l, r in queries:
            l -= 1
            r -= 1
            if t == 1:
                if 0 <= l - 1:
                    update(l, 1 if sum(l) - sum(l - 1) == 0 else -1)
                if r < N - 1:
                    update(r + 1, 1 if sum(r + 1) - sum(r) == 0 else -1)

            elif t == 2:
                res.append(sum(r) - sum(l) == r - l)

        return res

    def solve2(self, N, Q, S, queries):
        # CPython だと TLE(PyPy なら通る)

        # AtCoder Library を使用
        # https://github.com/not522/ac-library-python

        from atcoder.fenwicktree import FenwickTree

        FT = FenwickTree(N)

        for i, (s1, s2) in enumerate(zip(S, S[1:])):
            FT.add(i, (s1 + s2) % 2)

        res = []
        for t, l, r in queries:
            l -= 1
            r -= 1
            if t == 1:
                if 0 <= l - 1:
                    FT.add(l - 1, 1 if FT.sum(l - 1, l) == 0 else -1)
                if r < N - 1:
                    FT.add(r, 1 if FT.sum(r, r + 1) == 0 else -1)

            elif t == 2:
                res.append(FT.sum(l, r) == r - l)

        return res


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

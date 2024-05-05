class A:
    def main(self):
        N, S, K = map(int, input().split())
        PQ = [tuple(map(int, input().split())) for _ in range(N)]
        res = self.solve2(N, S, K, PQ)
        print(res)

    def solve(self, N, S, K, PQ):
        res = sum(p * q for p, q in PQ)
        if res < S:
            res += K
        return res

    def solve2(self, N, S, K, PQ):
        return res + K if (res := sum(p * q for p, q in PQ)) < S else res


class B:
    def main(self):
        K, G, M = map(int, input().split())
        res = self.solve(K, G, M)
        print(*res)

    def solve(self, K, G, M):
        glass, mug = 0, 0
        for i in range(K):
            if glass == G:
                glass = 0
            elif mug == 0:
                mug = M
            else:
                water = min(mug, G - glass)
                mug -= water
                glass += water
        return glass, mug


class C:
    def main(self):
        N, M = map(int, input().split())
        S = map(int, input())
        res = self.solve2(N, M, S)
        print(res)

    def solve(self, N, M, S):
        muji, logo = M, 0
        res = 0
        for s in S:
            if s == 0:
                muji, logo = M, res
            elif s == 1:
                if muji > 0:
                    muji -= 1
                elif logo > 0:
                    logo -= 1
                else:
                    res += 1
            elif s == 2:
                if logo > 0:
                    logo -= 1
                else:
                    res += 1
        return res

    def solve2(self, N, M, S):
        S = list(S)
        S.append(0)

        muji, logo = 0, 0
        res = 0
        for s in S:
            if s == 0:
                res = max(res, muji + logo - M, logo)
                muji, logo = 0, 0
            elif s == 1:
                muji += 1
            elif s == 2:
                logo += 1
        return res


class D:
    def main(self):
        H, W = map(int, input().split())
        A = [tuple(map(int, input().split())) for _ in range(H)]
        B = [tuple(map(int, input().split())) for _ in range(H)]
        res = self.solve2(H, W, A, B)
        print(res)

    def solve(self, H, W, A, B):
        from collections import deque

        if all([A[i][j] == B[i][j] for i in range(H) for j in range(W)]):
            return 0
        Ei, Ej = tuple(range(H)), tuple(range(W))
        mem = {(Ei, Ej): 0}
        deq = deque([(Ei, Ej)])
        while deq:
            Pi, Pj = deq.popleft()
            for i1 in range(H - 1):
                i2 = i1 + 1
                Qi = (
                    Pi[:i1]
                    + Pi[i2 : i2 + 1]
                    + Pi[i1 + 1 : i2]
                    + Pi[i1 : i1 + 1]
                    + Pi[i2 + 1 :]
                )
                if (Qi, Pj) in mem:
                    continue
                mem[(Qi, Pj)] = mem[(Pi, Pj)] + 1
                for bi, ai in enumerate(Qi):
                    for bj, aj in enumerate(Pj):
                        if A[ai][aj] != B[bi][bj]:
                            break
                    else:
                        continue
                    break
                else:
                    return mem[(Qi, Pj)]
                deq.append((Qi, Pj))
            for j1 in range(W - 1):
                j2 = j1 + 1
                Qj = (
                    Pj[:j1]
                    + Pj[j2 : j2 + 1]
                    + Pj[j1 + 1 : j2]
                    + Pj[j1 : j1 + 1]
                    + Pj[j2 + 1 :]
                )
                if (Pi, Qj) in mem:
                    continue
                mem[(Pi, Qj)] = mem[(Pi, Pj)] + 1
                for bi, ai in enumerate(Pi):
                    for bj, aj in enumerate(Qj):
                        if A[ai][aj] != B[bi][bj]:
                            break
                    else:
                        continue
                    break
                else:
                    return mem[(Pi, Qj)]
                deq.append((Pi, Qj))
        return -1

    def solve2(self, H, W, A, B):
        from collections import deque

        if all([A[i][j] == B[i][j] for i in range(H) for j in range(W)]):
            return 0
        Ei, Ej = tuple(range(H)), tuple(range(W))
        mem = {(Ei, Ej): 0}
        deq = deque([(Ei, Ej)])
        while deq:
            Pi, Pj = deq.popleft()
            for i1 in range(H - 1):
                i2 = i1 + 1
                Qi = [i for i in Pi]
                Qi[i1], Qi[i2] = Qi[i2], Qi[i1]
                Qi = tuple(Qi)
                if (Qi, Pj) in mem:
                    continue
                mem[(Qi, Pj)] = mem[(Pi, Pj)] + 1
                for bi, ai in enumerate(Qi):
                    for bj, aj in enumerate(Pj):
                        if A[ai][aj] != B[bi][bj]:
                            break
                    else:
                        continue
                    break
                else:
                    return mem[(Qi, Pj)]
                deq.append((Qi, Pj))
            for j1 in range(W - 1):
                j2 = j1 + 1
                Qj = [j for j in Pj]
                Qj[j1], Qj[j2] = Qj[j2], Qj[j1]
                Qj = tuple(Qj)
                if (Pi, Qj) in mem:
                    continue
                mem[(Pi, Qj)] = mem[(Pi, Pj)] + 1
                for bi, ai in enumerate(Pi):
                    for bj, aj in enumerate(Qj):
                        if A[ai][aj] != B[bi][bj]:
                            break
                    else:
                        continue
                    break
                else:
                    return mem[(Pi, Qj)]
                deq.append((Pi, Qj))
        return -1


class E:
    def main(self):
        N, D = map(int, input().split())
        W = [int(w) for w in input().split()]
        res = self.solve2(N, D, W)
        print(res)

    def solve(self, N, D, W):
        # CPython だと TLE(PyPy なら通る)

        dp = [[None for _ in range(1 << N)] for _ in range(D)]

        for i in range(1 << N):
            x = 0
            for j in range(N):
                if (i >> j) & 1:
                    x += W[j]
            dp[0][i] = pow(x, 2)

        for d in range(D - 1):
            for i in range(1 << N):
                dp[d + 1][i] = dp[0][0] + dp[d][i]
                x = i
                while x > 0:
                    dp[d + 1][i] = min(dp[d + 1][i], dp[0][x] + dp[d][i - x])
                    x = (x - 1) & i

        # print(*dp, sep="\n")

        res = ((D * dp[D - 1][(1 << N) - 1]) - pow(sum(W), 2)) / pow(D, 2)
        return res

    def solve2(self, N, D, W):
        # CPython だと TLE(PyPy なら通る)

        W2 = [w * w for w in W]
        sum_w2 = sum(W2)

        dp = [[None for _ in range(1 << N)] for _ in range(D)]

        for i in range(N):
            dp[0][1 << i] = 0

        for i in range(N):
            for j in range(i + 1, N):
                dp[0][1 << i | 1 << j] = W[i] * W[j]

        for i in range(1 << N):
            if dp[0][i] is not None:
                continue
            dp[0][i] = 0
            for j in range(N):
                for k in range(j + 1, N):
                    if (i >> j) & (i >> k) & 1:
                        dp[0][i] += dp[0][1 << j | 1 << k]

        for i in range(D - 1):
            for j in range(1 << N):
                dp[i + 1][j] = dp[i][j] + dp[0][0]
                x = j
                while x > 0:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - x] + dp[0][x])
                    x = (x - 1) & j

        res = (D * (sum_w2 + 2 * dp[D - 1][(1 << N) - 1]) - sum(W) ** 2) / D**2
        return res


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

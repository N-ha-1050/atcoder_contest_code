class A:
    def main(self):
        M, D = map(int, input().split())
        y, m, d = map(int, input().split())
        res = self.solve2(M, D, y, m, d)
        print(*res)

    def solve(self, M, D, y, m, d):
        y -= 1
        m -= 1
        d -= 1

        d += 1
        m += d // D
        d %= D
        y += m // M
        m %= M

        y += 1
        m += 1
        d += 1

        return y, m, d

    def solve2(self, M, D, y, m, d):
        d += 1
        if d > D:
            d -= D
            m += 1
        if m > M:
            m -= M
            y += 1
        return y, m, d


class B:
    def main(self):
        N, S, M, L = map(int, input().split())
        res = self.solve(N, S, M, L)
        print(res)

    def solve(self, N, S, M, L):
        NS, NM, NL = 6, 8, 12
        res = None
        for s in range(N + 1):
            for m in range(N + 1):
                for l in range(N + 1):
                    if N <= s * NS + m * NM + l * NL:
                        cost = s * S + m * M + l * L
                        if res is None or cost < res:
                            res = cost
                            break
                if N <= s * NS + m * NM:
                    break
            if N <= s * NS:
                break
        return res


class C:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve2(N, A)
        print(*res)

    def solve(self, N, A):
        cnt = {}
        for a in A:
            cnt[a] = cnt.get(a, 0) + 1

        r = 0
        mem = {c: 0 for c in cnt}
        for c in sorted(cnt, reverse=True):
            mem[c] = r
            r += c * cnt[c]
        res = [mem[a] for a in A]
        return res

    def solve2(self, N, A):
        from collections import defaultdict

        cnt = defaultdict(list)
        for i, a in enumerate(A):
            cnt[a].append(i)

        res = [0 for _ in range(N)]
        r = 0
        for a, idxs in sorted(cnt.items(), reverse=True):
            for i in idxs:
                res[i] = r
            r += a * len(idxs)
        return res


class D:
    def main(self):
        N, Q = map(int, input().split())
        P = [input() for _ in range(N)]
        get = self.calc(N, P)
        for _ in range(Q):
            A, B, C, D = map(int, input().split())
            res = self.solve(get, A, B, C, D)
            print(res)

    def calc(self, N, P):
        T = [[int(p == "B") for p in pp] for pp in P]
        cum_T = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                cum_T[i + 1][j + 1] += T[i][j]
                cum_T[i + 1][j + 1] += cum_T[i + 1][j]
                cum_T[i + 1][j + 1] += cum_T[i][j + 1]
                cum_T[i + 1][j + 1] -= cum_T[i][j]

        def get(a, b):
            aq, ar = a // N, a % N
            bq, br = b // N, b % N

            res = 0
            res += cum_T[N][N] * aq * bq
            res += cum_T[ar][N] * bq
            res += cum_T[N][br] * aq
            res += cum_T[ar][br]
            return res

        return get

    def solve(self, get, A, B, C, D):
        res = 0
        res += get(A, B)
        res -= get(A, D + 1)
        res -= get(C + 1, B)
        res += get(C + 1, D + 1)
        return res


class E:
    def main(self):
        N, M, L = map(int, input().split())
        A = [int(a) for a in input().split()]
        B = [int(b) for b in input().split()]
        CD = {tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(L)}
        res = self.solve2(N, M, L, A, B, CD)
        print(res)

    def solve(self, N, M, L, A, B, CD):
        import heapq

        sorted_B = sorted(((b, j) for j, b in enumerate(B)), reverse=True)
        max_B = sorted_B[0][0]
        mem = [0 for _ in range(N)]
        pq = []  # (-cost, A_idx)
        for i, a in enumerate(A):
            heapq.heappush(pq, (-(a + max_B), i))
        while True:
            cost_, i = heapq.heappop(pq)
            cost = -cost_
            j = sorted_B[mem[i]][1]
            if (i, j) not in CD:
                return cost
            mem[i] += 1
            heapq.heappush(pq, (-(A[i] + sorted_B[mem[i]][0]), i))

    def solve2(self, N, M, L, A, B, CD):
        sorted_B = sorted([(b, j) for j, b in enumerate(B)], reverse=True)
        max_B = sorted_B[0][0]
        res = 0
        for i, a in enumerate(A):
            for b, j in sorted_B:
                if a + b <= res:
                    break
                if (i, j) not in CD:
                    r = a + b
                    if res < r:
                        res = r
                    break

        return res


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

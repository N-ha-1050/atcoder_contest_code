class A:
    def main(self):
        N, X = map(int, input().split())
        S = [int(s) for s in input().split()]
        res = self.solve(N, X, S)
        print(res)

    def solve(self, N, X, S):
        return sum(s for s in S if s <= X)

    def test(self):
        pass


class B:
    def main(self):
        N = int(input())
        D = [int(d) for d in input().split()]
        res = self.solve(N, D)
        print(res)

    def solve(self, N, D):
        res = 0
        for month, d in enumerate(D, 1):
            for day in range(1, d + 1):
                if len(set(str(month)) | set(str(day))) == 1:
                    res += 1
        return res

    def test(self):
        pass


class C:
    def main(self):
        N, Q = map(int, input().split())
        S = input()
        LR = [map(int, input().split()) for _ in range(Q)]
        L, R = zip(*LR)
        res = self.solve(N, Q, S, L, R)
        print(*res, sep="\n")

    def solve(self, N, Q, S, L, R):
        cnt = [0] + [int(s1 == s2) for s1, s2 in zip(S, S[1:])]
        cum = [0 for _ in range(N)]
        for i in range(N):
            cum[i] = cum[i - 1] + cnt[i]
        return [cum[r - 1] - cum[l - 1] for l, r in zip(L, R)]

    def test(self):
        pass


class D:
    def main(self):
        S = input()
        res = self.solve(S)
        print(res)

    def solve(self, S):
        from collections import deque

        deq = deque()
        cnt = 0
        for s in S:
            deq.append(s)
            cnt += 1
            if cnt >= 3 and deq[-3] == "A" and deq[-2] == "B" and deq[-1] == "C":
                for _ in range(3):
                    deq.pop()
                cnt -= 3
        return "".join(deq)

    def test(self):
        pass


class E:
    def main(self):
        N, M, K = map(int, input().split())
        T = [tuple(map(int, input().split())) for _ in range(M)]
        res = self.solve(N, M, K, T)
        print(res)

    def solve(self, N, M, K, T):
        # CPython だと TLE(PyPy なら通る)

        import itertools

        res = None
        for gs in itertools.combinations(range(M), N - 1):
            G = [-1 for _ in range(N)]

            def find(x):
                if G[x] < 0:
                    return x
                G[x] = find(G[x])
                return G[x]

            cnt = 0
            for j in gs:
                u, v, w = T[j]
                u = find(u - 1)
                v = find(v - 1)
                if u == v:
                    continue
                if G[u] > G[v]:
                    u, v = v, u
                G[u] += G[v]
                G[v] = u
                cnt += w
            if -G[find(0)] != N:
                continue
            if res is None or cnt % K < res:
                res = cnt % K
        return res

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

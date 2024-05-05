class A:
    def main(self):
        B, G = map(int, input().split())
        res = self.solve(B, G)
        print(res)

    def solve(self, B, G):
        return "Bat" if B > G else "Glove"


class B:
    def main(self):
        A, M, L, R = map(int, input().split())
        res = self.solve2(A, M, L, R)
        print(res)

    def solve(self, A, M, L, R):
        floor = lambda x, y: x // y
        ceil = lambda x, y: (x + y - 1) // y
        m = A % M
        l = L - m
        r = R - m
        return floor(r, M) - ceil(l, M) + 1

    def solve2(self, A, M, L, R):
        floor = lambda x, y: x // y
        ceil = lambda x, y: (x + y - 1) // y
        return floor(R - A, M) - ceil(L - A, M) + 1


class C:
    def main(self):
        N, K = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve2(N, K, A)
        print(res)

    def solve(self, N, K, A):
        dis = [A[i + 1] - A[i] for i in range(K - 1)]
        res = sum(d for i, d in enumerate(dis) if i % 2 == 0)
        if K % 2 == 1:
            cnt = res
            for i in range(2, K, 2):
                cnt += dis[K - i]
                cnt -= dis[K - i - 1]
                res = min(res, cnt)
        return res

    def solve2(self, N, K, A):
        dis_start = [A[i + 1] - A[i] for i in range(0, K - 1, 2)]
        cum_start = [0 for _ in range(K // 2 + 1)]
        for i, d in enumerate(dis_start):
            cum_start[i + 1] = cum_start[i] + d
        if K % 2 == 0:
            return cum_start[K // 2]
        dis_end = [A[i + 1] - A[i] for i in range(1, K - 1, 2)]
        cum_end = [0 for _ in range(K // 2 + 1)]
        for i, d in reversed(tuple(enumerate(dis_end))):
            cum_end[i] = cum_end[i + 1] + d
        res = min([cum_start[i] + cum_end[i] for i in range(K // 2 + 1)])
        return res


class D:
    def main(self):
        N, Q = map(int, input().split())
        R = sorted(map(int, input().split()))
        cum = [0 for _ in range(N)]
        for i, r in enumerate(R):
            cum[i] = cum[i - 1] + r
        for _ in range(Q):
            X = int(input())
            res = self.solve(N, Q, cum, X)
            print(res)

    def solve(self, N, Q, cum, X):
        import bisect

        res = bisect.bisect_right(cum, X)
        return res


class E:
    def main(self):
        H, W = map(int, input().split())
        S = [input() for _ in range(H)]
        res = self.solve(H, W, S)
        print(res)

    def solve(self, H, W, S):
        from collections import deque

        MOD = 998244353
        T = [S[i][j] == "#" for i in range(H) for j in range(W)]
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ij2n = lambda i, j: i * W + j
        n2ij = lambda n: (n // W, n % W)
        is_in = lambda i, j: 0 <= i < H and 0 <= j < W

        mem = [None for _ in range(H) for _ in range(W)]
        idx = 0
        for i in range(H):
            for j in range(W):
                n = ij2n(i, j)
                if not T[n]:
                    continue
                if mem[n] is not None:
                    continue
                mem[n] = idx
                deq = deque([n])
                while deq:
                    nn = deq.popleft()
                    ni, nj = n2ij(nn)
                    for di, dj in ds:
                        mi, mj = ni + di, nj + dj
                        if not is_in(mi, mj):
                            continue
                        mn = ij2n(mi, mj)
                        if not T[mn]:
                            continue
                        if mem[mn] is not None:
                            continue
                        mem[mn] = idx
                        deq.append(mn)
                idx += 1

        cnt = []
        for i in range(H):
            for j in range(W):
                n = ij2n(i, j)
                if T[n]:
                    continue
                idxs = set()
                for di, dj in ds:
                    ni, nj = i + di, j + dj
                    if not is_in(ni, nj):
                        continue
                    nn = ij2n(ni, nj)
                    if not T[nn]:
                        continue
                    idxs.add(mem[nn])
                cnt.append((idx - len(idxs) + 1) % MOD)
        r = 0
        for c in cnt:
            r += c
            r %= MOD
        res = r * pow(len(cnt), -1, MOD) % MOD
        return res


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

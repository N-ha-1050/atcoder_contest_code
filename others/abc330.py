class A:
    def main(self):
        N, L = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve(N, L, A)
        print(res)

    def solve(self, N, L, A):
        return sum(a >= L for a in A)

    def test(self):
        pass


class B:
    def main(self):
        N, L, R = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve2(N, L, R, A)
        print(*res)

    def solve(self, N, L, R, A):
        return (a if L <= a <= R else L if a < L else R for a in A)

    def solve2(self, N, L, R, A):
        return (min(max(L, a), R) for a in A)

    def test(self):
        pass


class C:
    def main(self):
        D = int(input())
        res = self.solve(D)
        print(res)

    def solve(self, D):
        x = 0
        y = max(0, int(D**0.5) - 5)
        while y**2 < D:
            y += 1

        res = D
        while 0 < y and x**2 <= D:
            y2 = D - x**2
            while 0 < y and y * y > y2:
                y -= 1
            res = min(res, abs(x**2 + y**2 - D))
            res = min(res, abs(x**2 + (y + 1) ** 2 - D))
            x += 1
        return res

    def test(self):
        pass


class D:
    def main(self):
        N = int(input())
        S = [input() for _ in range(N)]
        res = self.solve(N, S)
        print(res)

    def solve(self, N, S):
        T = [[s == "o" for s in ss] for ss in S]
        cnt_col = [sum(t) for t in T]
        cnt_row = [sum(t) for t in zip(*T)]

        res = 0
        for i in range(N):
            for j in range(N):
                if not T[i][j]:
                    continue
                res += (cnt_col[i] - 1) * (cnt_row[j] - 1)
        return res

    def test(self):
        pass


class E:
    def main(self):
        N, Q = map(int, input().split())
        A = [int(a) for a in input().split()]
        queries = [tuple(map(int, input().split())) for _ in range(Q)]
        res = self.solve2(N, Q, A, queries)
        print(*res, sep="\n")

    def solve(self, N, Q, A, queries):
        # CPython だと TLE(PyPy なら通る)

        seg_size = 1 << N.bit_length()
        cnt = [0 for _ in range(N + 1)]
        for a in A:
            if N < a:
                continue
            cnt[a] += 1
        seg = [
            cnt[i - seg_size] if seg_size <= i < seg_size + N + 1 else N
            for i in range(2 * seg_size)
        ]

        def set(i):
            seg[i] = min(seg[idx := (i << 1)], seg[idx + 1])

        for i in reversed(range(1, seg_size)):
            set(i)

        def update(i, x):
            i += seg_size
            seg[i] = x
            while i > 1:
                i >>= 1
                set(i)

        def get(l, r=None):
            if r is None:
                r = l + 1

            l += seg_size
            r += seg_size

            res_l = N
            res_r = N

            while l < r:
                if l & 1:
                    res_l = min(res_l, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res_r = min(seg[r], res_r)
                l >>= 1
                r >>= 1
            return min(res_l, res_r)

        res = [0 for _ in range(Q)]
        for qi, (i, x) in enumerate(queries):
            i -= 1
            a = A[i]
            if a != x:
                if a < N:
                    update(a, get(a) - 1)
                if x < N:
                    update(x, get(x) + 1)
                A[i] = x
            if get(0) == 0:
                continue

            l, r = 0, N
            while r - l > 1:
                m = (l + r) // 2
                if get(0, m + 1):
                    l = m
                else:
                    r = m
            res[qi] = r
        return res

    def solve2(self, N, Q, A, queries):
        import heapq

        cnt = [0 for _ in range(N + 1)]
        for a in A:
            if N < a:
                continue
            cnt[a] += 1

        mem = [i for i, c in enumerate(cnt) if c == 0]
        heapq.heapify(mem)

        mem_d = []

        res = [0 for _ in range(Q)]
        for qi, (i, x) in enumerate(queries):
            i -= 1
            a = A[i]
            if a != x:
                if a <= N:
                    cnt[a] -= 1
                    if cnt[a] == 0:
                        heapq.heappush(mem, a)
                        # mem.add(a)
                if x <= N:
                    if cnt[x] == 0:
                        heapq.heappush(mem_d, x)
                    cnt[x] += 1
                A[i] = x
            while mem_d and mem[0] == mem_d[0]:
                heapq.heappop(mem)
                heapq.heappop(mem_d)
            res[qi] = mem[0]
        return res

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

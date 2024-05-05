class A:
    def main(self):
        S, T = input().split()
        res = self.solve(S, T)
        print(res)

    def solve(self, S, T):
        return f"{S} san"

    def test(self):
        pass


class B:
    def main(self):
        T = 24
        N = int(input())
        cnt = [0 for _ in range(T)]
        for _ in range(N):
            W, X = map(int, input().split())
            cnt[X] += W
        res = self.solve2(T, N, cnt)
        print(res)

    def solve(self, T, N, cnt):
        D = 9
        res = mem = sum(cnt[:D])
        for i in range(T):
            mem -= cnt[i]
            mem += cnt[(D + i) % T]
            res = max(res, mem)
        return res

    def solve2(self, T, N, cnt):
        D = 9
        return max(sum(cnt[(i + j) % T] for j in range(D)) for i in range(T))

    def test(self):
        pass


class C:
    def main(self):
        H, W = map(int, input().split())
        S = [input() for _ in range(H)]
        res = self.solve2(H, W, S)
        print(res)

    def solve(self, H, W, S):
        from collections import deque

        mem = [[False if S[i][j] == "#" else None for j in range(W)] for i in range(H)]

        res = 0
        dis = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for i in range(H):
            for j in range(W):
                if mem[i][j] is None:
                    continue
                if mem[i][j]:
                    continue
                res += 1
                deq = deque([(i, j)])
                while deq:
                    x, y = deq.popleft()
                    if not (0 <= x < H):
                        continue
                    if not (0 <= y < W):
                        continue
                    if mem[x][y] is None:
                        continue
                    if mem[x][y]:
                        continue
                    mem[x][y] = True
                    deq.extend([(x + dx, y + dy) for dx, dy in dis])
        return res

    def solve2(self, H, W, S):
        from collections import deque

        def get_S(x):
            i = x // (W + 2)
            j = x % (W + 2)
            if 0 <= i - 1 < H and 0 <= j - 1 < W:
                return S[i - 1][j - 1] == "#"
            return False

        res = 0
        dis = [1, -W - 1, -W - 2, -W - 3, -1, W + 1, W + 2, W + 3]
        HW = (H + 2) * (W + 2)
        mem = [False if get_S(x) else None for x in range(HW)]
        is_skip = lambda x: not (0 <= x < HW) or mem[x] is None or mem[x]

        for x in range(HW):
            if is_skip(x):
                continue
            res += 1
            deq = deque([x])
            while deq:
                y = deq.popleft()
                if is_skip(y):
                    continue
                mem[y] = True
                deq.extend([y + d for d in dis])
        return res

    def test(self):
        pass


class D:
    def main(self):
        N = int(input())
        TD = [tuple(map(int, input().split())) for _ in range(N)]
        res = self.solve(N, TD)
        print(res)

    def solve(self, N, TD):
        import heapq

        cnt = {}
        for t, d in TD:
            cnt[t + d] = cnt.get(t + d, [])
            heapq.heappush(cnt[t + d], t)

        times = {}

        def get_time(t):
            if t not in times:
                return t
            times[t] = get_time(times[t])
            return times[t]

        def use_time(t):
            times[t] = get_time(t + 1)

        res = 0
        for et in sorted(cnt.keys()):
            while cnt[et]:
                st = heapq.heappop(cnt[et])
                t = get_time(st)
                if et < t:
                    break
                use_time(t)
                res += 1
        return res

    def test(self):
        pass


class E:
    def main(self):
        N, A, B, C = map(int, input().split())
        D = [tuple(map(int, input().split())) for _ in range(N)]
        res = self.solve2(N, A, B, C, D)
        print(res)

    def solve(self, N, A, B, C, D):
        import heapq

        car = [None for _ in range(N)]

        points = [(0, 0)]  # (最短時間, 頂点番号)

        while points:
            t, now = heapq.heappop(points)
            if car[now] is not None:
                continue
            car[now] = t
            for ne in range(N):
                if car[ne] is not None:
                    continue
                heapq.heappush(points, (car[now] + A * D[now][ne], ne))

        train = [None for _ in range(N)]

        points = [(0, 0)]

        while points:
            t, now = heapq.heappop(points)
            if train[now] is not None:
                continue
            train[now] = min(car[now], t)
            for ne in range(N):
                if train[ne] is not None:
                    continue
                heapq.heappush(points, (train[now] + B * D[now][ne] + C, ne))

        return train[N - 1]

    def solve2(self, N, A, B, C, D):
        import heapq

        car = [None for _ in range(N)]

        points = [(0, 0)]  # (最短時間, 頂点番号)

        while points:
            t, now = heapq.heappop(points)
            if car[now] is not None:
                continue
            car[now] = t
            for ne in range(N):
                if car[ne] is not None:
                    continue
                heapq.heappush(points, (car[now] + A * D[now][ne], ne))

        train = [None for _ in range(N)]

        points = [(0, N - 1)]

        while points:
            t, now = heapq.heappop(points)
            if train[now] is not None:
                continue
            train[now] = t
            for ne in range(N):
                if train[ne] is not None:
                    continue
                heapq.heappush(points, (train[now] + B * D[now][ne] + C, ne))

        return min(s + t for s, t in zip(car, train))

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

class A:
    def main(self):
        S = input()
        res = self.solve(S)
        print(res)

    def solve(self, S):
        return S[:-1] + "4"


class B:
    def main(self):
        N = int(input())
        res = self.solve(N)
        for r in res:
            print(*r)

    def solve(self, N):
        res = []
        for x in range(N + 1):
            for y in range(N + 1 - x):
                for z in range(N + 1 - x - y):
                    res.append((x, y, z))
        return res


class C:
    def main(self):
        N, Q = map(int, input().split())
        mem = [(i, 0) for i in range(N, 0, -1)]
        for _ in range(Q):
            query = input().split()
            res = self.solve(N, Q, mem, query)
            if res is not None:
                print(*res)

    def solve(self, N, Q, mem, query):
        t = int(query[0])
        dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        if t == 1:
            C = query[1]
            x, y = mem[-1]
            dx, dy = dirs[C]
            mem.append((x + dx, y + dy))
            return None
        if t == 2:
            p = int(query[1])
            return mem[-p]


class D:
    def main(self):
        N = int(input())
        res = self.solve(N)
        for r in res:
            print(*r)

    def solve(self, N):
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = -1, 0
        cnt = 1
        res = [[None for _ in range(N)] for _ in range(N)]
        res[N // 2][N // 2] = "T"

        def is_in(x, y):
            return 0 <= x < N and 0 <= y < N

        while cnt < N * N:
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                while is_in(nx, ny) and res[nx][ny] is None:
                    x, y = nx, ny
                    res[x][y] = str(cnt)
                    cnt += 1
                    nx, ny = x + dx, y + dy
        return res


class E:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) for a in input().split()]
        UV = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
        res = self.solve(N, M, A, UV)
        print(res)

    def solve(self, N, M, A, UV):
        G = [set() for _ in range(N)]
        UF = [-1 for _ in range(N)]

        def find(x):
            if UF[x] < 0:
                return x
            UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return x
            if UF[x] > UF[y]:
                x, y = y, x
            UF[x] += UF[y]
            UF[y] = x
            return x

        for u, v in UV:
            if A[u] == A[v]:
                union(u, v)

        for u, v in UV:
            u, v = find(u), find(v)
            if u == v:
                continue
            if A[u] > A[v]:
                u, v = v, u
            G[u].add(v)

        cnt = [0 for _ in range(N)]
        mem = [False for _ in range(N)]
        cnt[find(0)] = 1

        for i in sorted(range(N), key=lambda x: A[x]):
            i = find(i)
            if cnt[i] == 0:
                continue
            if mem[i]:
                continue
            mem[i] = True
            nc = cnt[i] + 1
            for g in G[i]:
                if nc < cnt[g]:
                    continue
                cnt[g] = nc

        return cnt[find(N - 1)]


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

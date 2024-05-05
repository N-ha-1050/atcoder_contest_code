class A:
    def main(self):
        X, Y = map(int, input().split())
        res = self.solve(X, Y)
        print("Yes" if res else "No")

    def solve(self, X, Y):
        return -3 <= Y - X <= 2

    def test(self):
        pass


class B:
    def main(self):
        N = int(input())
        res = self.solve(N)
        print(res)

    def solve(self, N):
        def is_ok(x):
            t = tuple(map(int, str(x)))
            return t[-3] * t[-2] == t[-1]

        while not is_ok(N):
            N += 1
        return N

    def test(self):
        pass


class C:
    def main(self):
        N, M = map(int, input().split())
        A = sorted([int(a) for a in input().split()])
        res = self.solve2(N, M, A)
        print(res)

    def solve(self, N, M, A):
        j = 0
        res = cnt = 0
        for i, a in enumerate(A):
            while j < N and A[j] < a + M:
                cnt += 1
                j += 1
            res = max(res, cnt)
            cnt -= 1
        return res

    def solve2(self, N, M, A):
        D = {}
        for a in A:
            D[a] = D.get(a, 0) + 1
        T = sorted(D.items())
        len_T = len(T)
        res = cnt = 0
        j = 0
        for i in range(len_T):
            while j < len_T and T[j][0] < T[i][0] + M:
                cnt += T[j][1]
                j += 1
            res = max(res, cnt)
            cnt -= T[i][1]
        return res

    def test(self):
        pass


class D:
    def main(self):
        N = int(input())
        R = input()
        C = input()
        res = self.solve(N, R, C)
        if res is None:
            print("No")
        else:
            print("Yes")
            for r in res:
                print(r)

    def solve(self, N, R, C):
        import itertools

        S = ".ABC"

        def check(cnt):
            for i in range(N):
                j = 0
                while not cnt[i][j]:
                    j += 1
                if S[cnt[i][j]] != R[i]:
                    return False

            for j in range(N):
                i = 0
                while not cnt[i][j]:
                    i += 1
                if S[cnt[i][j]] != C[j]:
                    return False
            return True

        def dfs(x=1, cnt=[[0 for _ in range(N)] for _ in range(N)]):
            if x > 3:
                if check(cnt):
                    return ["".join(S[i] for i in c) for c in cnt]
                return None
            for w in itertools.permutations(range(N), N):
                for i, j in enumerate(w):
                    if cnt[i][j]:
                        break
                    cnt[i][j] = x
                else:
                    res = dfs(x + 1, cnt)
                    if res is not None:
                        return res
                for i, j in enumerate(w):
                    if cnt[i][j] == x:
                        cnt[i][j] = 0
            return None

        return dfs()

    def test(self):
        pass


class E:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve2(N, A)
        print(res)

    def solve(self, N, A):
        MOD = 998244353
        N_inv = pow(N, -1, MOD)
        return sum([a * N_inv * pow(1 + N_inv, i, MOD) for i, a in enumerate(A)]) % MOD

    def solve2(self, N, A):
        MOD = 998244353
        N_inv = pow(N, -1, MOD)
        res = 0
        for i, a in enumerate(A):
            cnt = a
            cnt *= N_inv
            cnt %= MOD
            cnt *= pow(1 + N_inv, i, MOD)
            cnt %= MOD
            res += cnt
            res %= MOD
        return res

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

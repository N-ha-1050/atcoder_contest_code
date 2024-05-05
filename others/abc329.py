class A:
    def main(self):
        S = input()
        res = self.solve(S)
        print(res)

    def solve(self, S):
        return " ".join(S)

    def test(self):
        pass


class B:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve(N, A)
        print(res)

    def solve(self, N, A):
        return sorted(set(A))[-2]

    def test(self):
        pass


class C:
    def main(self):
        N = int(input())
        S = input()
        res = self.solve(N, S)
        print(res)

    def solve(self, N, S):
        mem = {s: 0 for s in set(S)}

        pre_s = S[0]
        cnt = 0

        for s in S + ".":
            if s == pre_s:
                cnt += 1
            else:
                mem[pre_s] = max(mem[pre_s], cnt)
                cnt = 1
                pre_s = s

        return sum(mem.values())

    def test(self):
        pass


class D:
    def main(self):
        N, M = map(int, input().split())
        A = [int(a) - 1 for a in input().split()]
        res = self.solve(N, M, A)
        print(*map(lambda x: x + 1, res), sep="\n")

    def solve(self, N, M, A):
        cnt = [0 for _ in range(N)]
        ma = None

        res = []

        for a in A:
            cnt[a] += 1
            if ma is None or cnt[ma] < cnt[a] or (cnt[ma] == cnt[a] and a < ma):
                ma = a
            res.append(ma)

        return res

    def test(self):
        pass


from collections import deque


class E:
    def main(self):
        N, M = map(int, input().split())
        S = list(input())
        T = list(input())
        res = self.solve2(N, M, S, T)
        print("Yes" if res else "No")

    def solve(self, N, M, S, T):
        que = deque([])
        mem = [False for _ in range(N)]

        def is_ok(i):
            if mem[i]:
                return False
            for j in range(M):
                if not 0 <= i + j < N:
                    return False
                if S[i + j] is not None and S[i + j] != T[j]:
                    return False
            return True

        def do(i):
            if not is_ok(i):
                return
            for j in range(M):
                S[i + j] = None
            mem[i] = True
            return

        for i in range(N - M + 1):
            if is_ok(i):
                que.append(i)

        while que:
            i = que.popleft()
            do(i)
            for j in range(i - (M - 1), i + M):
                if is_ok(j):
                    que.append(j)

        return all(s == None for s in S)

    def solve2(self, N, M, S, T):
        idx = 0
        while idx < N - M + 1:
            while idx < 0:
                idx += 1

            for i in range(M):
                if not 0 <= idx + i < N:
                    break
                if S[idx + i] is not None and S[idx + i] != T[i]:
                    break
            else:
                flg = False
                for i in range(M):
                    if S[idx + i] is not None:
                        S[idx + i] = None
                        flg = True
                if flg:
                    idx -= M
            idx += 1
        return all(s == None for s in S)

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

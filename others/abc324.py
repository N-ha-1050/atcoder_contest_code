class A:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve(N, A)
        print("Yes" if res else "No")

    def solve(self, N, A):
        return len(set(A)) == 1

    def test(self):
        pass


class B:
    def main(self):
        N = int(input())
        res = self.solve2(N)
        print("Yes" if res else "No")

    def solve(self, N):
        while N % 2 == 0:
            N //= 2
        while N % 3 == 0:
            N //= 3
        return N == 1

    def solve2(self, N):
        from collections import deque

        pow_3 = deque([3])
        i = 0
        while N % pow_3[i] == 0:
            pow_3.append(pow_3[i] * pow_3[i])
            i += 1

        while pow_3:
            x = pow_3.pop()
            if N % x == 0:
                N //= x

        return N & (N - 1) == 0

    def test(self):
        pass


class C:
    def main(self):
        _N, T_dash = input().split()
        N = int(_N)
        S = [input() for _ in range(N)]
        res = self.solve(N, T_dash, S)
        print(len(res))
        print(*res)

    def solve(self, N, T_dash, S):
        len_T_dash = len(T_dash)
        reversed_T_dash = list(reversed(T_dash))

        res = []

        def calc(S, T):
            for i, (s, t) in enumerate(zip(S, T)):
                if s != t:
                    return i
            return min(len(S), len(T))

        for i, s in enumerate(S, 1):
            a = calc(s, T_dash)
            b = calc(list(reversed(s)), reversed_T_dash)

            if a == len_T_dash == len(s):
                res.append(i)
            elif a + b >= len_T_dash - 1 == len(s):
                res.append(i)
            elif a + b >= len_T_dash == len(s) - 1:
                res.append(i)
            elif a + b == len_T_dash - 1 == len(s) - 1:
                res.append(i)

        return res

    def test(self):
        pass


class D:
    def main(self):
        N = int(input())
        S = input()
        res = self.solve2(N, S)
        print(res)

    def solve(self, N, S):
        # CPython だと TLE(PyPy なら通る)

        def calc(s):
            return [s.count(str(i)) for i in range(10)]

        min_S = int("".join(sorted(S)))
        max_S = int("".join(sorted(S, reverse=True)))
        cnt_S = calc(S)

        i = max(int(min_S ** (1 / 2)) - 1, 0)
        res = 0

        while (x := i * i) <= max_S:
            cnt_x = calc(str(x).zfill(N))
            if cnt_S == cnt_x:
                res += 1
            i += 1

        return res

    def solve2(self, N, S):
        sorted_S = sorted(S)
        min_S = int("".join(sorted_S))
        max_S = int("".join(reversed(sorted_S)))

        i = max(int(min_S ** (1 / 2)) - 1, 0)
        res = 0

        while (x := i * i) <= max_S:
            if sorted_S == sorted(str(x).zfill(N)):
                res += 1
            i += 1

        return res

    def test(self):
        pass


class E:
    def main(self):
        _N, T = input().split()
        N = int(_N)
        S = [input() for _ in range(N)]
        res = self.solve(N, T, S)
        print(res)

    def solve(self, N, T, S):
        len_T = len(T)

        def calc_front(S):
            idx = 0
            for s in S:
                if s == T[idx]:
                    idx += 1
                    if idx == len_T:
                        break
            return idx

        def calc_back(S):
            idx = len(T) - 1
            for s in reversed(S):
                if s == T[idx]:
                    idx -= 1
                    if idx == -1:
                        break
            return idx + 1

        fronts = tuple(map(calc_front, S))
        backs = tuple(map(calc_back, S))

        cnt_fronts = [0 for _ in range(len_T + 1)]
        for i in fronts:
            cnt_fronts[i] += 1

        cnt_backs = [0 for _ in range(len_T + 1)]
        for i in backs:
            cnt_backs[i] += 1

        cum_backs = [0 for _ in range(len_T + 1)]
        cum_backs[0] = cnt_backs[0]
        for i in range(len_T):
            cum_backs[i + 1] = cum_backs[i] + cnt_backs[i + 1]

        res = 0
        for i in range(len_T + 1):
            res += cnt_fronts[i] * cum_backs[i]
        return res

    def solve2(self, N, T, S):
        reversed_T = tuple(reversed(T))
        len_T = len(T)

        def calc(S, T):
            idx = 0
            for s in S:
                if s == T[idx]:
                    idx += 1
                    if idx == len_T:
                        break
            return idx

        fronts = [calc(s, T) for s in S]
        backs = [calc(reversed(s), reversed_T) for s in S]

        cnt_fronts = [0 for _ in range(len_T + 1)]
        for i in fronts:
            cnt_fronts[i] += 1

        cnt_backs = [0 for _ in range(len_T + 1)]
        for i in backs:
            cnt_backs[i] += 1

        cum_backs = [0 for _ in range(len_T + 2)]
        for i in range(len_T + 1):
            cum_backs[i + 1] = cum_backs[i] + cnt_backs[i]

        sum_backs = cum_backs[len_T + 1]

        res = 0
        for i in range(len_T + 1):
            res += cnt_fronts[i] * (sum_backs - cum_backs[len_T - i])

        return res

    def test(self):
        pass


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

class A:
    def main(self):
        N = input()
        res = self.solve(N)
        print(res)

    def solve(self, N):
        return N * int(N)


class B:
    def main(self):
        S1, S2 = input()
        T1, T2 = input()
        res = self.solve2(S1, S2, T1, T2)
        print("Yes" if res else "No")

    def solve(self, S1, S2, T1, T2):
        P = {p: i for i, p in enumerate("ABCDE")}

        def get_distance(x, y):
            dis = abs(P[x] - P[y])
            return min(dis, 5 - dis)

        return get_distance(S1, S2) == get_distance(T1, T2)

    def solve2(self, S1, S2, T1, T2):
        P = "ABCDEAEDCBA"
        return (S1 + S2 in P) == (T1 + T2 in P)


class C:
    def main(self):
        N = int(input())
        res = self.solve3(N)
        print(res)

    def solve(self, N):
        M = 12

        cnt = [int("1" * i) for i in range(1, M + 1)]

        mem = set()
        for i in range(M):
            a = cnt[i]
            for j in range(i, M):
                b = cnt[j]
                for k in range(j, M):
                    c = cnt[k]
                    mem.add(a + b + c)
        return sorted(mem)[N - 1]

    def solve2(self, N):
        M = 12

        cnt = [int("1" * i) for i in range(1, M + 1)]

        mem = set()
        for i in range(M):
            for j in range(i + 1):
                for k in range(j + 1):
                    N -= 1
                    if N == 0:
                        return cnt[i] + cnt[j] + cnt[k]

    def solve3(self, N):
        M = 12
        for d in range(1, M + 1):
            for a in range(d - 1, -1, -1):
                for b in range(d - a - 1, -1, -1):
                    c = d - a - b
                    N -= 1
                    if N == 0:
                        return "1" * a + "2" * b + "3" * c


class D:
    def main(self):
        N = int(input())
        uv = [tuple(map(int, input().split())) for _ in range(N - 1)]
        res = self.solve(N, uv)
        print(res)

    def solve(self, N, uv):
        G = [-1 for _ in range(N)]

        def find(x):
            if G[x] < 0:
                return x
            else:
                G[x] = find(G[x])
                return G[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return x
            if G[x] > G[y]:
                x, y = y, x
            G[x] += G[y]
            G[y] = x
            return x

        for u, v in uv:
            if u != 1:
                union(u - 1, v - 1)
        x = max(-g for g in G if g < 0)
        res = N - x
        return res


class E:
    def main(self):
        N = int(input())
        tx = [tuple(map(int, input().split())) for _ in range(N)]
        res1, res2 = self.solve2(N, tx)
        print(res1)
        if res1 != -1:
            print(*res2)

    def solve(self, N, tx):
        res1 = 0
        cnt1 = 0
        res2 = []
        cnt2 = [0 for _ in range(N)]
        for t, x in reversed(tx):
            if t == 1:
                if cnt2[x - 1] > 0:
                    res2.append(1)
                    cnt2[x - 1] -= 1
                    cnt1 -= 1
                else:
                    res2.append(0)
            elif t == 2:
                cnt2[x - 1] += 1
                cnt1 += 1
                res1 = max(res1, cnt1)
        if any(c > 0 for c in cnt2):
            return -1, None
        res2.reverse()

        return res1, res2

    def solve2(self, N, tx):
        from collections import deque

        potion_holder = [deque() for _ in range(N)]
        potion_result = []
        potion_count = 0
        imos = [0 for _ in range(N)]
        for turn, (t, x) in enumerate(tx):
            if t == 1:
                potion_result.append(False)
                potion_holder[x - 1].append((turn, potion_count))
                potion_count += 1
            elif t == 2:
                if not potion_holder[x - 1]:
                    return -1, None
                pre_turn, potion_index = potion_holder[x - 1].pop()
                imos[pre_turn] += 1
                imos[turn] -= 1
                potion_result[potion_index] = True
        cnt = [0 for _ in range(N)]
        for idx, i in enumerate(imos):
            cnt[idx] = cnt[idx - 1] + i

        return max(cnt), map(int, potion_result)


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

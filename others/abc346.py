class A:
    def main(self):
        N = int(input())
        A = [int(a) for a in input().split()]
        res = self.solve(N, A)
        print(*res)

    def solve(self, N, A):
        return [a1 * a2 for a1, a2 in zip(A, A[1:])]

    def solve2(self, N, A):
        return [A[i] * A[i + 1] for i in range(N - 1)]


class B:
    def main(self):
        W, B = map(int, input().split())
        res = self.solve2(W, B)
        print("Yes" if res else "No")

    def solve(self, W, B):
        nw, nb = W // 7, B // 5
        n = min(nw, nb)
        w, b = W - 7 * n, B - 5 * n

        S = "wbwbwwbwbwbw" * 2
        for i in range(12):
            T = S[i : i + b + w]
            if w == T.count("w") and b == T.count("b"):
                return True
        return False

    def solve2(self, W, B):
        S = "wbwbwwbwbwbw"
        N = len(S)

        for i in range(N):
            cnt = {"w": 0, "b": 0}
            for j in range(W + B):
                s = S[(i + j) % N]
                cnt[s] += 1
            if W == cnt["w"] and B == cnt["b"]:
                return True
        return False


class C:
    def main(self):
        N, K = map(int, input().split())
        A = [int(a) for a in input().split()]
        res = self.solve2(N, K, A)
        print(res)

    def solve(self, N, K, A):
        res = K * (K + 1) // 2
        for a in set(A):
            if a <= K:
                res -= a
        return res

    def solve2(self, N, K, A):
        from sortedcontainers import SortedSet

        # [sortedcontainers](https://pypi.org/project/sortedcontainers/) の SortedSet は、
        # データを平衡二分探索木という構造で管理するデータ構造です（組み込みのsetはハッシュで管理をします）。
        #
        # 解説の [Python で set を用いる場合の注意点](https://atcoder.jp/contests/abc346/editorial/9635) にあるように、
        # 組み込みの set は特定の条件下で極端に性能(速度)が低下してしまいます（ハッシュの衝突があった場合等）。
        #
        # SortedSet は組み込みの set に比べて、平均的に遅くなってしまいますが最悪の場合でも性能の悪化が抑えられます。

        res = K * (K + 1) // 2
        for a in SortedSet(A):
            if a <= K:
                res -= a
        return res


class D:
    def main(self):
        N = int(input())
        S = [int(s) for s in input()]
        C = [int(c) for c in input().split()]
        res = self.solve2(N, S, C)
        print(res)

    def solve(self, N, S, C):
        sum_C = sum(C)

        # dp[i][used][bit] := i(i = 0, 1, ..., N)文字目までについて、i文字目ががbit(bit = 0, 1)で、一致がused(used = True(1), False(0))のときの最小のコスト
        dp = [[[sum_C for _ in range(2)] for _ in range(2)] for _ in range(N)]

        dp[0][0][S[0]] = 0
        dp[0][0][1 - S[0]] = C[
            0
        ]  # s の 0 と 1 を反転させたいときは、 `1 - s` (1との差) または `s^1` (1との排他的論理和)

        for i, s in enumerate(S[1:]):
            dp[i + 1][0][s] = dp[i][0][1 - s]
            dp[i + 1][0][1 - s] = dp[i][0][s] + C[i + 1]
            dp[i + 1][1][s] = min(dp[i][1][1 - s], dp[i][0][s])
            dp[i + 1][1][1 - s] = min(
                dp[i][1][s] + C[i + 1], dp[i][0][1 - s] + C[i + 1]
            )

        return min(dp[N - 1][1])

    def solve2(self, N, S, C):
        L = [[0 for _ in range(N + 1)] for _ in range(2)]
        R = [[0 for _ in range(N + 1)] for _ in range(2)]

        for i in range(N):
            s = S[i]
            c = C[i]

            L[0][i + 1] = L[0][i]
            L[1][i + 1] = L[1][i]

            if (i % 2) == s:
                L[1][i + 1] += c
            else:
                L[0][i + 1] += c

        for i in reversed(range(N)):
            s = S[i]
            c = C[i]

            R[0][i] = R[0][i + 1]
            R[1][i] = R[1][i + 1]

            if (i % 2) == s:
                R[0][i] += c
            else:
                R[1][i] += c

        ans = L[0][1] + R[0][1]
        for i in range(1, N):
            ans = min(ans, L[0][i] + R[0][i])
            ans = min(ans, L[1][i] + R[1][i])

        return ans


class E:
    def main(self):
        H, W, M = map(int, input().split())
        TAX = [tuple(map(int, input().split())) for _ in range(M)]
        res = self.solve(H, W, M, TAX)
        print(len(res))
        for r in res:
            print(*r)

    def solve(self, H, W, M, TAX):
        HL, WL = [False for _ in range(H)], [False for _ in range(W)]

        cnt = {0: H * W}

        for t, a, x in reversed(TAX):
            i = a - 1
            if t == 1:
                if HL[i]:
                    continue
                HL[i] = True
                H -= 1
                cnt[0] -= W
                cnt[x] = cnt.get(x, 0) + W
            elif t == 2:
                if WL[i]:
                    continue
                WL[i] = True
                W -= 1
                cnt[0] -= H
                cnt[x] = cnt.get(x, 0) + H
        res = tuple((c, cnt[c]) for c in sorted(cnt) if cnt[c] > 0)
        return res


def main():
    task = E()
    task.main()


if __name__ == "__main__":
    main()

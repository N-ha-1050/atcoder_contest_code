import numpy as np


def main():
    N = int(input())
    KA = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, KA)
    print(res)


def solve(N: int, KA: list[tuple[int, ...]]):
    K = np.empty((N, 1), dtype=int)  # N x 1
    max_A = 0
    for i, (k, *a) in enumerate(KA):
        K[i, 0] = k
        max_A = max(max_A, max(a))

    C = np.zeros((N, max_A), dtype=int)  # N x max_A
    for i, (_, *a) in enumerate(KA):
        for aa in a:
            C[i, aa - 1] += 1

    X = C @ C.T  # N x N
    Y = K @ K.T  # N x N
    return np.tril(X / Y, k=-1).max()


if __name__ == "__main__":
    main()

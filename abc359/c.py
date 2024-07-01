def main():
    S = tuple(map(int, input().split()))
    T = tuple(map(int, input().split()))
    res = solve(S, T)
    print(res)


def solve(S, T):
    Sx, Sy = S
    Tx, Ty = T

    dy = abs(Sy - Ty)

    if (Sx + Sy) % 2 == 0:
        lx = Sx - dy
        rx = Sx + dy + 1
    else:
        lx = Sx - dy - 1
        rx = Sx + dy

    if lx <= Tx <= rx:
        return dy

    elif Tx < lx:
        return dy + (lx - Tx + 1) // 2

    elif rx < Tx:
        return dy + (Tx - rx + 1) // 2


if __name__ == "__main__":
    main()

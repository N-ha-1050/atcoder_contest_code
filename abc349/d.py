from collections import deque


def main():
    L, R = map(int, input().split())
    res = solve(L, R)
    print(len(res))
    for l, r in res:
        print(l, r)


def solve(L, R):
    res_l = deque()
    res_r = deque()

    mem = {0: 1}

    def pow2(x):
        if x not in mem:
            mem[x] = pow(2, x)
        return mem[x]

    def calc(x):
        i, j = 0, x
        while j != 0 and j % 2 == 0:
            i += 1
            j //= 2
        return i, j

    l = L
    li, lj = calc(l)
    while L != 0 and lj != 1:
        nl = pow2(li) * (lj + 1)
        if R < nl:
            break
        res_l.append((l, nl))
        l = nl
        li, lj = calc(l)

    r = R
    ri, rj = calc(r)
    while rj != 1:
        pr = pow2(ri) * (rj - 1)
        if pr < L:
            break
        res_r.appendleft((pr, r))
        r = pr
        ri, rj = calc(r)

    res_m = deque()

    li2 = pow2(li) * lj
    ri2 = pow2(ri) * rj

    if l == 0:
        res_m.append((0, ri2))
    elif rj == lj == 1:
        i = li2
        while i != ri2:
            ni = 2 * i
            res_m.append((i, ni))
            i = ni
    else:
        for i in range(li2, ri2):
            res_m.append((i, i + 1))

    res = deque()
    while res_l:
        res.append(res_l.popleft())
    while res_m:
        res.append(res_m.popleft())
    while res_r:
        res.append(res_r.popleft())

    return list(res)


if __name__ == "__main__":
    main()

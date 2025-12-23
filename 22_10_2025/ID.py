from collections import deque

def main():
    patt = input("Enter : ")

    # number of digits needed
    n = len(patt) + 1

    # create digits
    arr = list(range(1, n + 1))
    dq = deque(arr)

    res = []
    wait = []

    print(f"n : {n}")
    print(f"arr : {arr}")

    # only D case
    if "I" not in patt:
        arr.sort(reverse=True)
        print(*arr)
        return

    # only I case
    if "D" not in patt:
        arr.sort()
        print(*arr)
        return

    # mixed case
    print("mixed")
    for ch in patt:
        if ch == "I":
            if not wait:
                res.append(dq.popleft())
            else:
                wait.append(dq.popleft())
                wait.reverse()
                res.extend(wait)
                wait.clear()

        elif ch == "D":
            wait.append(dq.popleft())

    # final flush
    while dq:
        wait.append(dq.popleft())

    wait.reverse()
    res.extend(wait)

    print(res)

main()

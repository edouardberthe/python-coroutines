def countdown(n):
    while n > 0:
        yield n
        n -= 1

if __name__ == "__main__":
    c = countdown(5)
    for i in c:
        print(i, end=", ")
    print("")
    c = countdown(5)
    print(c)
    print(next(c))
    print(next(c))
N = int(input())

i = 1

while i <= N:
    if i % 2 == 0:
        print("{} ^ 2 = {}".format(i, i*i))
    i += 1
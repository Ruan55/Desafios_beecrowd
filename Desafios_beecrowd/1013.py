a, b, s = input().split()
a, b, s = int(a), int(b), int(s)

maiorAB = (a + b + abs(a-b)) / 2
maior = (maiorAB + s + abs(maiorAB - s)) / 2

print(int(maior) ,"eh o maior")
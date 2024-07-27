quantidade = int(input())

In = 0
Out = 0
n = 0

for i in range(quantidade):
    n = int(input())
    if n >= 10 and n <= 20:
        In += 1
    else:
        Out += 1
    
print(In, "in")
print(Out, "out")
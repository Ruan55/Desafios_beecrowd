tempoSegundo = int(input())

horas = tempoSegundo // 3600
minutos = ((tempoSegundo - (horas * 3600)) // 60)
segundos = tempoSegundo % 60

print("{}:{}:{}".format(horas, minutos, segundos))
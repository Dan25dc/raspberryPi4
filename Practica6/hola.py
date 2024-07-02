import time

contador=10

# Inicia el temporizador
start_time = time.time()

# Contar hasta que el pin se ponga en alto
while contador!=0:
    time.sleep(1)
    contador=contador-1

# Detiene el temporizador y calcula el tiempo transcurrido
elapsed_time = int(round(time.time() - start_time))

print(elapsed_time)
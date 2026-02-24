import time
import numpy as np

lista = list(range(15_000_000))
lista_np = np.arange(15_000_000, dtype=np.int64)


# funkcja - wydzielony fragment kodu możliwy do wykonania w dowolnym momencie
def sum_python():
    total = 0
    for i in lista:
        total += i
    print("Sum is:", total)


def sum_np():
    total = np.sum(lista_np)
    print("Sum is:", total)


# funkcje musimy wywołać by uruchomić
start_d = time.time()
sum_np()
print(time.time() - start_d)

start_d = time.time()
sum_python()
print(time.time() - start_d)
# Sum is: 112499992500000
# 0.005719661712646484
# Sum is: 112499992500000
# 0.24738693237304688

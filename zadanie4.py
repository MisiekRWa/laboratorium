from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]

start = time.time()


koniec = time.time() - start

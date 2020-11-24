from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]

#1
start = time.time()
for element in long_list:
    if element == -1:
        print ("-1 Należy do long_list")
        break
koniec = time.time() - start
print ("Pierwsze : " + str(koniec))

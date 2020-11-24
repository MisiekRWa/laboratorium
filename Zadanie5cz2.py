from random import randint
tab_dl= 5
tab2_dl = 4

rand_list = [[randint(1, 10) for element in range (tab2_dl)] for list2 in range (tab_dl)]
print(rand_list)
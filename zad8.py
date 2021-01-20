try:
    with open("jeden.txt", 'r') as plik1:
        with open("dwa.txt", 'w') as plik2:
            for linia in plik1:
                plik2.write(linia)
except IOError as ioe:
    print("Blad! {}".format(ioe))
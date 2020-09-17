def cautare_binara(lista, x):
    st = 0
    dr = len(lista)
    while st < dr:
        mijloc = (st + dr) // 2 # // => rezultatul impartirii va fi de tip int
        if lista[mijloc] == x:
            return True
        if x < lista[mijloc]:
            dr = mijloc
        else:
            st = mijloc
    return False



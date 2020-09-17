def cautare_binara_rec(lista,x,st,dr):
    if st > dr:
        return  False
    mijloc = (st + dr) // 2
    if x == lista[mijloc]:
        return  True
    if x < lista[mijloc]:
        return  cautare_binara_rec(lista,x,st,mijloc - 1)
    if x > lista[mijloc]:
        return  cautare_binara_rec(lista,x,mijloc + 1,dr)

def caut_binara_rec_cool(lista,x):
    st = 0
    dr = len(lista)
    if st == dr:
        return  False
    mijloc = (st + dr) // 2
    if x == lista[mijloc]:
        return True
    if x < lista[mijloc]:
        return caut_binara_rec_cool(lista[0:mijloc],x)
    if x > lista[mijloc]:
        return  caut_binara_rec_cool(lista[mijloc:len(lista)],x)
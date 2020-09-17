from timeit import default_timer as timer
from iterative_binary_search import cautare_binara
from recursive_binary_search import * # aduce tot ce se afla in fisierul recursive_binary_search

def main():
    min = 100
    print("Wellcome to binary search!")
    print("Do you want to use pre-defined values? If so, type 'Yes'")
    answere = input()
    if answere.lower() == "yes":
        print("Using pre-defined values...")
        lista = [5, 9, 78, 155, 998, 1327, 15005, 9, 78, 155, 998, 1327, 15005, 9, 78, 155, 998, 1327, 15005, 9, 78, 155,
             998, 1327, 15005, 9, 78, 155, 998, 1327, 15005, 9, 78, 155, 998, 1327, 15005, 9, 78, 155, 998, 1327, 1500]
        x = 5
    else:
        n = int(input("Enter list lenght: "))
        lista = []
        for i in range(n):
            data = int(input())
            lista.append(data)
        x = int(input("X :"))
    print("Searching in " + str(lista) + "and searching for " + str(x))
  # Execution time analysis

  # Iterative
    before = timer()
    result = cautare_binara(lista,x)
    after = timer()
    speed = after - before
    if cautare_binara(lista,x) == True:
        print(str(x) + " is located in the list")
    else:
        print(str(x) + " is not located in the list")
    print("cautare_binara executed in " + str(speed))
    if speed<min:
        min=speed
        algoritm = "cautare binara"

  #Recursive 1
    before = timer()
    result = cautare_binara_rec(lista,x,0,len(lista))
    after = timer()
    speed = after - before
    if cautare_binara_rec(lista,x,0,len(lista)) == True:
        print(str(x) + " is located in the list")
    else:
        print(str(x) + " is not located in the list")
    print("cautare_binara_rec executed in " + str(speed))
    if speed < min:
        min = speed
        algoritm = "cautare_binara_rec"

  #Recursive 2
    before = timer()
    result = caut_binara_rec_cool(lista,x)
    after = timer()
    speed = after - before
    if caut_binara_rec_cool(lista,x) == True:
        print(str(x) + " is located in the list")
    else:
        print(str(x) + " is not located in the list")
    print("caut_binara_rec_cool executed in " + str(speed))
    if speed < min:
        min = speed
        algoritm = "caut_binara_rec_cool"
    print("The fastest algorithm is " + str(algoritm))
main()
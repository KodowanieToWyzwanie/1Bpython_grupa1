import random
# obliczanie silni
# lista random
# min/ max element
# anagram - 1110001 1111000

#rozkład na czynniki pierwsza
# 100= 2 2  5 5

# liczba = int(input("podaj liczbe  "))
# lista_czynnikow = []
# dzielnik = 2
# while dzielnik <= liczba:  #liczba >= 1
#   while liczba % dzielnik == 0:
#     lista_czynnikow.append(dzielnik)
#     liczba //= dzielnik
#   dzielnik += 1

# print(lista_czynnikow)

lista = []
random.seed(2)
for _i in range(1, 50):
  lista.append(random.randint(1, 100))

print(lista)
# mini = lista[0]
# for i in range(1, len(lista)):
#   if mini > lista[i]:
#     mini = lista[i]
# print(f"najmniejszy element listy {mini}")
# # print(min(lista))
# maxi = lista[0]
# for i in range(1, len(lista)):
#   if maxi < lista[i]:
#     maxi = lista[i]
# print(f"największy element listy {maxi}")
# print(max(lista))

##sumę wszystkich elementów
# suma = 0
# for i in range(len(lista)):
#   suma += lista[i]

suma = 0
for i in lista:
  print(suma)
  suma += i

print(f"suma tablicy = {suma}")

#suma liczb parzystych / nieparzystych 

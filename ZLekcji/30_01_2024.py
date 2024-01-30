import random

#zadanie 4 
a,b = map(int,input().split())

while b != 0:
  a,b = b, a%b

print(a)


lista = []
for i in range(20):
  lista.append(bin(i)[2:])
# print(lista)


#zadanie 6
# Wylosuj tablicę 10 elementową liczb losowych. A następnie znajdź sumę elementów. Np. dla tablicy 1,2,3 suma = 6 

#sumuję o razu jak wstawiam do tablicy
lista = []
suma = 0
for i in range(10):
  liczba = random.randint(1,100)
  lista.append(liczba)
  suma += liczba
  
# print(*lista)
## dwie pętle 
lista = []
for i in range(10):
  lista.append(random.randint(1,100))
suma = 0
for i in lista:
  suma +=i


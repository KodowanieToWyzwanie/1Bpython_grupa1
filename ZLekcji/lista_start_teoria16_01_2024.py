
a = int(input())
napis = str(input()) #input()
f = float(input())

# False/True

lista = [1,2,3,4,5]
print(lista[0])
lista.append(6)
print(lista)
lista.pop(0) #w nawiasie podaję index elementu do usuniecia
print(lista)

lista_parzyste = [] #w przedziale 1 do 10
for i in range(2,11,2):
  lista_parzyste.append(i)

print(*lista_parzyste)
print(lista_parzyste)

#dlugosc listy
print(len(lista_parzyste))
#ostatni element
print(lista_parzyste[-1])

for element in lista_parzyste:
  print(element)

napis = "Jestem super programistą"
print(len(napis))
print(napis[::-1])
palindrom = "kajak"
if palindrom == palindrom[::-1]:
  print("jest")
else:
  print("nie jest")

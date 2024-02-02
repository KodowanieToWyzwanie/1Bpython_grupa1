import random

tab = []
wielkosc_tablicy = 50
max_elem = 50
for i in range(wielkosc_tablicy):
  tab.append(random.randint(1,max_elem))
  
print(tab)

maxi = tab[0]
for i in range(1, len(tab)):
  if maxi < tab[i]:
    maxi = tab[i]
  if tab[i] == max_elem:
    break
  # print(maxi)

maxi = tab[0]
suma = 0 
for element in tab:
  suma += element
  if maxi == element:
    maxi = element


liczba_do_sprawdzenia = maxi
licznik = 0
for element in tab:
  if liczba_do_sprawdzenia == element:
    licznik += 1
print("element tab[0] występuj ", licznik, "razy")



print("suma liczb w tab wynosi: ", suma)
print("największy element wynosi : ", maxi)

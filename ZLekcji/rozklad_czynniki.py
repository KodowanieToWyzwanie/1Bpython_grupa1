#rozkład na czynniki pierwsza
# 100= 2 2  5 5

 liczba = int(input("podaj liczbe  "))
 lista_czynnikow = []
 dzielnik = 2
 while dzielnik <= liczba:  #liczba >= 1
   while liczba % dzielnik == 0:
     lista_czynnikow.append(dzielnik)
     liczba //= dzielnik
   dzielnik += 1

 print(lista_czynnikow)

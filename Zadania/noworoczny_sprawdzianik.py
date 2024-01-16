#pobierz z ekranu swoje imię i wyświetl napis- "Twoje imię" - super, że jesteś

name = input("podaj swoje imię: ")
print(name + " - super, że jesteś!")


# Właśnie zakładasz stronę z treściami tylko dla dorosłych. Wyświetl na ekranie stosowny komunikat i spytaj się użytkownika o wiek - jeśli ma poniżej 18, w grzeczny sposób odmów dostępu do strony, w przeciwnym razie napisz, że użytkownik może korzystać ze strony.

wiek = int(input("Podaj swój wiek: "))
if wiek >=0 and wiek <=18:
  print("Przykro nam, ale ta strona jest tylko dla dorosłych ")
elif wiek >=18 and wiek <=120:
  print("Możesz korzystać ze strony ")
else:
  print("Nieprawidłowa wartość")


# Oblicz BMI - dla podanych przez użytkownika wartości wagi i wzrostu -należy podzielić wagę wyrażoną w kilogramach przez wzrost podniesiony do kwadratu, wyrażony w metrach, czyli w skrócie BMI = kg / m2.


waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi = waga / (wzrost **2)
print("Twoje bmi wynosi:", bmi)


# Zdrowy dorosły człowiek o prawidłowym stosunku wagi do wzrostu ma wskaźnik w granicach 18,5–24,9. BMI poniżej 18,5 informuje o niedowadze. Osoby ze wskaźnikiem BMI 25,0-29,9 cierpią na nadwagę. Współczynnik BMI powyżej 30,0 to już otyłość.Wyświetl odpowiedni komunikat do uzyskanego wyniku. 

if bmi < 18.5:
  print("Niedowaga")
elif bmi >= 18.5 and bmi <= 24.9:
  print("Prawidłowa waga")
elif bmi >= 25.0 and bmi <= 29.9:
  print("Nadwaga")
else:
  print("Otyłość")

# Wyświetl na ekranie liczby nieparzyste od 10 do 10 (włącznie) <10,20> w pętli for lub while

for i in range(11, 21, 2):
  print(i)

#Jesteś rekruterem stewardess do linii lotniczych. Chcesz by wszystkie dziewczyny w Twoim zespole miały wzrost od <167-180> . Sprawdź czy podane dane przez użytkownika spełniają ten warunek.

wzrost = int(input("Podaj wzrost w cm: "))
if wzrost >= 167 and wzrost <= 180:
  print("Wzrost spełnia warunek")
else:
  print("Wzrost nie spełnia warunku")

# Wyświetl na ekranie liczby parzyste od 0 do 10 (włącznie) <0,10> w pętli for lub while
# Jesteś geografem i chcesz przy pomocy komputera w szybki sposób policzyć jaka jest różnica między najwyższym a najniższym miejscem w podanym kraj. Najpierw policz jaka jest różnica w Polsce. depresja Marzęcino -2.2 Rysy 2499. Użytkownik podaje dwie liczby. Dla ułatwienia obliczeń najpierw podaje liczbę mniejszą(bądź też ujemną)


# Oblicz wartość bezwzględną z podanej przez użytkownika liczby
# jak Ci do śmiechu. na ekranie pojawia się tyle razy napis "Ha" ile razy wskazuje na to liczba podana przez użytkownika
# oblicz swoją średnią ocen z Informatyki? Czy, wg Ciebie, zasługujesz na dobrą ocenę? Obliczenia dokonaj w pętli najpierw podają liczbę ocen a potem po kolei pytając się o kolejną ocenę. zadanie 1. oblicz średnią arytmetyczną przyjmując, że oceny nie mają wag - np. 1,2,3 -> 2.0. 2. oblicz średnią ważoną - wynik zaokrąglić do 2 miejsc po przecinku (pytają się w pętli za każdym razem o wagę) , 1 w.3, 2 w.2, 3 w.1 -> 1.67
# Jesteś sędzią zawodów, właśnie odliczasz czas od 10 do 1. Wyświetl te liczby na ekranie za każdym razem z odpowiednią liczbą kropek
# 10 ……….
# 9  ………
# 8  ……..
# itd….
# Oblicz pole kwadratu dla podanej przez użytkownika długości boku (liczba całkowita).(dane 9 wynik 81)
# Oblicz pole koła dla podanego przez użytkownika długości promienia (dane 6, wynik po zaokrągleniu 37.7)
# Wczytaj długości boku prostokąta i oblicz pole (dane 4, 5 wynik 20)
# Wczytaj długości boku prostokąta i oblicz obwód (dane 4,5 wynik 18))


import os
# Funkcja konteks menadżera odczytu notatki
def odczyt_z_pliku(sciezka, flaga="r"):
    with open(sciezka, mode=flaga) as odczytany_plik:
        dane_odczytane_z_pliku = odczytany_plik.read()
        print(dane_odczytane_z_pliku)
# Funkcja konteks menadżera zapisu notatki
def zapis_do_pliku(sciezka, tekst_do_zapisu="", flaga="w"):
    with open(sciezka, mode=flaga) as plik_do_zapisu:
        plik_do_zapisu.write(tekst_do_zapisu)
# W tej funkcji wpisujemy tekst, który zostanie zapisany w nowej notatce lub dopisany na końcu notatki.
def generator_nowego_tekstu_notatki():
    wpis = input("Wpisz tekst, który ma być zapisany w notatce:\n")
    return wpis
# W tej funkcji wpisujemy nazwę pliku notatki.
def generator_nazwy_pliku_notatki():
    nazwa_notatki = input("Wpisz nazwę nowej notatki bez rozszerzenia czyli nazwę nowego pliku, w którym będzie zapisana notatka:\n")
    nazwa_pliku_notatki = nazwa_notatki + ".txt"
    return nazwa_pliku_notatki
# Funkcja odczytująca zawartość pliku lub zapisująca tekst do pliku
def operacja_na_pliku(typ_dzialania):
	sciezka_do_pliku = os.path.join("Dane", "tekst3.txt")
	try:
	    if typ_dzialania == "odczyt":
	        lista_notatek = os.listdir(os.path.join("Dane"))
	        print(lista_notatek)
	    elif typ_dzialania == "nowa":
	        sciezka_do_pliku = os.path.join("Dane", generator_nazwy_pliku_notatki())
	        zapis_do_pliku(sciezka=sciezka_do_pliku, tekst_do_zapisu=generator_nowego_tekstu_notatki())
	    elif typ_dzialania == "dopisek":
	        dopis = generator_nowego_tekstu_notatki()
	        zapis_do_pliku(sciezka=sciezka_do_pliku, tekst_do_zapisu=(f"\n" + f"{dopis}"),flaga="a")
	    elif typ_dzialania == "kasowanie":
	        zapis_do_pliku(sciezka=sciezka_do_pliku)
	except IOError as error:
	    print(f"Nie udało się dokonać operacji na pliku, błąd typu - {type(error)} - {error}")
	else:
	    print("Wszystko poszło prawidłowo")
	finally:
	    input("Koniec fazy pracy z plikiem, naciśnij ENTER i wracamy do MENU")
# Główne menu programy to w nim dokonujemy wyboru operacji na notatce
def program_notatnik():
    while True:
        os.system("clear")
        print(20 * "*" + " MENU PROGRAMU NOTATNIK " + 20 * "*")
        wybor_menu = input(
            "(1)Notatki\n(2)Nowa notatka\n(3)Dopisek do notatki\n(4)Kasowanie\n(5)Koniec pracy programu\nTwój wybór: ")
        if wybor_menu == "1":
            print("Odczyt notatki")
            operacja_na_pliku(typ_dzialania="odczyt")
        elif wybor_menu == "2":
            print("Nowa notatka")
            operacja_na_pliku(typ_dzialania="nowa")
        elif wybor_menu == "3":
            print("Dopisek do notatki")
            operacja_na_pliku(typ_dzialania="dopisek")
        elif wybor_menu == "4":
            print("Kasowanie notatki")
            operacja_na_pliku(typ_dzialania="kasowanie")
        elif wybor_menu == "5":
            input("Koniec pracy programu. Naciśnij ENTER aby zakończyć program.")
            exit()
        else:
            print("Zły wybór !!! Jeszcze raz.")
        input("Naciśnij ENTER aby kontynuować.")
if __name__ == "__main__":
    program_notatnik()
# TODO: Plan:
# TODO: Wersja 5 Chmura
# TODO: Wersja 4 Środowisko graficzne
# TODO: Wersja 3 Lista notatek gdzie nazwa pliku notatki ma być nazwą notatki i wszystkie wcześniejsze operacje<
# TODO: Wersja 2 Wybór notatki, którą się chce czytać, kasować, dopisywać zawartość poprzez jej wybranie i lub wpisanie
#  nazwy
# TODO: Wersja 1 Tworzenie notatki, dopisywanie do notatki, zapisywanie notatki, przeglądanie notatki

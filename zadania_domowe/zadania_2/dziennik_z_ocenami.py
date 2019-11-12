"""
    Dla podanego slownika reprezentujacego oceny, napisz 4 funkcje:
    a) pierwsza powinna zwracac liste wszystkich ocen ze slownika,
    b) druga powinna ustalic i zwrocic maksymalna ocene z dziennika,
    c) trzecia ustala ile osob nie zaliczylo przedmiotu (kazda osoba z ocena 2.0),
    d) czwarta powinna zwrocic imie osoby z najwyzsza ocena.
    Przykladowy "dziennik" reprezentuje slownik CLASS_REGISTER.
    Nazwy i parametry funkcji do wlasnego wyboru :)
"""

CLASS_REGISTER = {
    "Ania": 4.0,
    "Jakub": 3.5,
    "Roman": 4.0,
    "Kasia": 4.0,
    "Aneta": 4.5,
    "Wojtek": 2.0,
    "Ola": 2.0,
    "Monika": 3.0,
    "Ula": 5.0,
    "Mikolaj": 4.0,
    "Robert": 3.0
}


def get_all_rate(items):
    return [x for x in items.values()]


def get_max_rate(items):
    return max(get_all_rate(items))


def get_rate_equal_2(items):
    return sum(1 for x in items.values() if x == 2.0)


def get_name_with_best_rate(items):
    return max(items, key=items.get)


if __name__ == '__main__':
    print(get_all_rate(CLASS_REGISTER))
    print(get_max_rate(CLASS_REGISTER))
    print(get_rate_equal_2(CLASS_REGISTER))
    print(get_name_with_best_rate(CLASS_REGISTER))

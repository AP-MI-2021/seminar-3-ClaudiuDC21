from typing import List


def show_menu():
    print('1. Citirea unei liste de float-uri.')
    print('2. A fisarea numerelor intregi din lista. ')
    print('3. Afisarea celui mai mare numar divizibil citit de la tastatura. ')
    print('4. Afisare float-uri cu parte fractionara palindrom. ')
    print('5. Afisare lista prelucrata. ')
    print('x. Iesire. ')


def read_list() -> List[float]:
    lista_str = input('Dati numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    lista_float = []
    for i in lista_str_split:
        lista_float.append(float(i))
    return lista_float


def get_full_number(lst: List) -> List:
    '''
    Determina toate numerele intregi din lista.
    :param lst: Lista data
    :return: O lista cu toate numerele intregi
    '''
    result = []
    for num in lst:
        if num == int(num):
            result.append(num)
    return result


def test_get_full_number():
    assert get_full_number([]) == []
    assert get_full_number([2, 3.4, 245, 5.0, 6.0, 56.45, 345.2]) == [2, 245, 5.0, 6.0]
    assert get_full_number([1.2, 3.3, 4.56, 43.2, 34.2]) == []
    assert get_full_number([1, 2, 3.4, 34.4, 10, 23.0]) == [1, 2, 10, 23.0]


def get_biggest_number_div_by_k(lst: List, num: float) -> float:
    '''
    Determina cel mai mare numar divizibil cu un numar citit de la tastattura.
    :param lst: Lista in care se va cauta numarul.
    :param num: Numarul citit de la tastatura.
    :return: Cel mai mare numar divizibil cu un numar citit de la tastattura
    '''
    numar_mare = 0
    for i in lst:
        if i % num == 0 and numar_mare < i:
            numar_mare = i
    return numar_mare


def test_get_biggest_number_div_by_k():
    assert get_biggest_number_div_by_k([], 2) == 0
    assert get_biggest_number_div_by_k([1.3, 1.2, 3.2, 2.3,5,24, 23.2], 2) == 24
    assert get_biggest_number_div_by_k([1, 2, 3, 4, 5, 6, 8, 7, 65, 45, 36, 24, 35, 34], 3) == 45
    assert get_biggest_number_div_by_k([1.2, 9, 6, 3.4, 10, 23.43], 1) == 9


def main():
    lista = []
    while True:
        show_menu()
        optiunea = input('Alegeti o optiune: ')
        if optiunea == '1':
            lista = read_list()
        elif optiunea == '2':
            print(f'Numerele intregi din lista {lista} sunt: {get_full_number(lista)}. ')
        elif optiunea == '3':
            pass
        elif optiunea == '4':
            pass
        elif optiunea == '5':
            pass
        elif optiunea == 'x':
            break
        else:
            print('Optiune invalida! Incercati din nou!')


if __name__ == '__main__':
    test_get_biggest_number_div_by_k()
    test_get_full_number()
    main()

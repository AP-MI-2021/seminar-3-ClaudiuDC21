from typing import List
from math import sqrt


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
    assert get_biggest_number_div_by_k([1.3, 1.2, 3.2, 2.3, 5, 24, 23.2], 2) == 24
    assert get_biggest_number_div_by_k([1, 2, 3, 4, 5, 6, 8, 7, 65, 45, 36, 24, 35, 34], 3) == 45
    assert get_biggest_number_div_by_k([1.2, 9, 6, 3.4, 10, 23.43], 1) == 10


def get_all_fractionary_palindrom(lista: List[float]):
    '''
    Determina toate float-urile ale caror parte fractionara este palindrom
    :param lista: O lista data:
    :return: O noua lista cu float-uri cu partea fractionara palindrom.
    '''
    result = []
    for i in lista:
        str_i = str(i)
        if '.' in str_i:
            numar = str_i.split('.')[1]
            if numar == numar[::-1]:
                result.append(i)
    return result


def test_get_all_fractionary_palindrom():
    assert get_all_fractionary_palindrom([]) == []
    assert get_all_fractionary_palindrom([5, 2.45, 5.44, 3.423, 6.2442]) == [5.44, 6.2442]
    assert get_all_fractionary_palindrom([3.423, 3.2452]) == []


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(5) == True
    assert is_prime(12) == False
    assert is_prime(19) == True


def get_reverse_string_on_prime(lst):
    result = []
    for elem in lst:
        if elem >= 0:
            str_elem = str(elem)
            if is_prime(int(sqrt(elem))):
                result.append(str_elem[::-1])
            else:
                result.append(elem)
        else:
            result.append(elem)
    return result

def test_get_reverse_string_on_prime():
    assert get_reverse_string_on_prime([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert get_reverse_string_on_prime([]) == []
    assert get_reverse_string_on_prime([100.0]) == [100.0]

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
            n = int(input('Alegeti numarul: '))
            print(
                f'Cel mai mare num??r divizibil cu un num??r citit de la tastatur?? este {get_biggest_number_div_by_k(lista, n)}')
        elif optiunea == '4':
            print(f'Numerele cu partea zecimala palindrom din {lista} sunt {get_all_fractionary_palindrom(lista)}')
        elif optiunea == '5':
            print(f'Lista prelucrata a listei {lista} este {get_reverse_string_on_prime(lista)}')
        elif optiunea == 'x':
            break
        else:
            print('Optiune invalida! Incercati din nou!')


if __name__ == '__main__':
    test_get_all_fractionary_palindrom()
    test_get_biggest_number_div_by_k()
    test_get_full_number()
    test_is_prime()
    test_get_reverse_string_on_prime()
    main()
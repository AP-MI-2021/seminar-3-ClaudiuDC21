from typing import List

def show_menu():
    print('1. Citirea unei liste cu n siruri de caracetere. ')
    print('2. Determinarea daca un anumit sir se gaseste in lista. ')
    print('3. Afisare siruri de caractere ce se repeta. ')
    print('4. Afisare siruri de caractere care sunt palindrom. ')
    print('5. Afisare lista dupa inlocurie caracter ce predomina. ')
    print('x. Iesire. ')

def read_list():
    lst_str = input('Alegeti sirurile de caractere separate prin spatiu: ')
    lis_str_split = lst_str.split(' ')
    lista_str = []
    for i in lis_str_split:
        lista_str.append(str(i))
    return lista_str

def get_str_in_list(lst: List[str], n: str):
    '''
    Determina daca unsir de caractere se afla in lista
    :param lst: O lista data
    :param n: Sirul cautat
    :return: True daca sirul cautat este in lista, Fals in caz contrar.
    '''
    for i in lst:
        if n == i:
            return True
    return False

def test_get_str_in_list():
    assert get_str_in_list(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'drd') == True
    assert get_str_in_list([], 'asd') == False
    assert get_str_in_list(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'abc') == False

def main():
    lista = []
    while True:
        show_menu()
        optiunea = input('Alegeti o optiune: ')
        if optiunea == '1':
            lista = read_list()
        elif optiunea == '2':
            sir = str(input('Scrieti sirul de caractere comparabil: '))
            if get_str_in_list(lista, sir):
                print('DA')
            else:
                print('NU')
        elif optiunea == '3':
            pass
        elif optiunea == '4':
            pass
        elif optiunea == '5':
            pass
        elif optiunea == 'x':
            break
        else:
            print('Optiune incorecta, reincercati! ')


if __name__ == '__main__':
    test_get_str_in_list()
    main()
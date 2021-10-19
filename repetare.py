import copy
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

def get_list_with_multiple_str(lst: List[str]) -> List[str]:
    '''
    Determina sirurile dde caractere care se repeta.
    :param lst: Lista data
    :return: O lista cu sirurile de caractere ce se repeta.
    '''
    lungime = len(lst)
    result = []
    for st in range(lungime - 1):
        for dr in range(st + 1,lungime):
            if lst[st] == lst[dr]:
                result.append(str(lst[st]))
                dr = lungime
    return result


def test_get_list_with_multiple_str():
    assert get_list_with_multiple_str([]) == []
    assert get_list_with_multiple_str(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa']
    assert get_list_with_multiple_str(['aaa', 'bbb', 'cmtc', 'drd', 'ads', 'sfd']) == []

def get_str_palindrome(lst: List[str]) -> List[str]:
    '''
    Determina sirurile de caractere din lista care sunt un palindrom.
    :param lst: O lista data.
    :return: O lista cu siruri palindrom.
    '''
    result = []
    for i in lst:
        if i == i[::-1]:
            result.append(str(i))
    return result

def test_get_str_palindrome():
    assert get_str_palindrome([]) == []
    assert get_str_palindrome(['ada', 'abc', 'cmtc', 'drd', 'aaa']) == ['ada', 'drd', 'aaa']
    assert get_str_palindrome(['adsa', 'abc', 'cmtc', 'drsd', 'saa']) == []


def get_replace_with_number(lst: List[str], ) -> List[str]:
    '''
    Inlocuieste sirurile ce contine cel mai lung caracter din sir cu numarul de aparitii.
    :param lst: O lista data
    :return: Lista prelucrata
    '''
    sum_max = 0
    char_max = ''
    str_nou = ''
    for elem in lst:
        str_nou = str_nou + elem
    for i in range(len(str_nou)):
        sum = 0
        for num in range(len(str_nou)):
            if str_nou[num] == str_nou[i]:
                sum = sum + 1
        if sum > sum_max:
            sum_max = sum
            char_max = copy[(str_nou[i])]



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
            print(f'Sirurile de caractere din lista {lista} ce se repeta sunt: {get_list_with_multiple_str(lista)}')
        elif optiunea == '4':
            print(f'Sirurile de caractere palindrom din lista {lista} sunt: {get_str_palindrome(lista)} ')
        elif optiunea == '5':

            print(get_num_of_str_in_list(lista))
        elif optiunea == 'x':
            break
        else:
            print('Optiune incorecta, reincercati! ')


if __name__ == '__main__':
    test_get_str_in_list()
    test_get_list_with_multiple_str()
    test_get_str_palindrome()
    test_get_num_of_str_in_list()
    main()
import numpy as np
import itertools as it


def belongs_sort_list(number, list_):
    # marche si liste triée
    index_min, index_max = (0, len(list_) - 1)
    if number == list_[index_min] or number == list_[index_max]:
        return True
    if number < list_[index_min] or number > list_[index_max]:
            return False
    while index_max - index_min > 1:
        index_int = (index_min + index_max) // 2
        if number < list_[index_int]:
            index_max = index_int
        elif number > list_[index_int]:
            index_min = index_int
        else:
            return True
    return False


# nombre = somme de 2 nombres?
def sum_2_numbers(number, list_):
    length = len(list_)
    ppn = 0
    while number > list_[ppn] and ppn < length - 1:
        ppn += 1
    stop = False
    resultat = False
    j = 0
    while not stop:
        a = list_[j]
        b = list_[ppn]
        if number == a + b:
            stop = True
            resultat = True
        elif number > a + b:
            j += 1
        else:
            ppn -= 1
        if ppn < j:
            stop = True
    return resultat


# List of prime numbers until n
def prime_number(n):
    if n < 2:
        return []
    prime_numbers_list = [2]
    for i in range(3, n+1):
        a = 0
        longueur = 0
        while prime_numbers_list[longueur] <= np.sqrt(i) and a == 0:
            if i % prime_numbers_list[longueur] == 0:
                a = 1
            longueur += 1
        if a == 0:
            prime_numbers_list.append(i)
    return np.array(prime_numbers_list)


# linear algorithm non optimized
def dividor_list(n):
    if n % 2 == 1:
        dividors_list = [i for i in range(1, n // 2 + 1, 2) if n % i == 0]
    else:
        dividors_list = [i for i in range(1, n // 2 + 1) if n % i == 0]
    dividors_list.append(n)
    return dividors_list


def dividor_bis_number_dividors(n, only_numbers=False, prime_number_list=False):
    # list of dividors of n, and its length
    if n <= 3:
        dico = {n: 1}
    else:
        if prime_number_list is not None:
            list_ = prime_number_list
        else:
            list_ = prime_number(int(np.sqrt(n)))
        dico = {}
        i = 0
        a = list_[i]
        while n >= a and i < len(list_):
            a = list_[i]
            while n % a == 0:
                if a in dico:
                    dico[a] += 1
                else:
                    dico[a] = 1
                n = n // a
            i += 1
        if n > 1:
            dico[n] = 1
    if only_numbers:
        number_dividors = 1
        for power in dico.values():
            number_dividors *= (power + 1)
        return number_dividors

    dividors_list = []
    for prime_dividor, max_power in dico.items():
        # list of tuple for each prime dividor, [(1, 3, 9), (1, 5)] for {3 : 2, 5 : 1}
        dividors_list.append(tuple(prime_dividor ** i for i in range(max_power + 1)))
    result = [np.product(d) for d in it.product(*dividors_list)]
    return result, len(result)


def factoriel(n):
    if n > 1:
        return n * factoriel(n - 1)
    else:
        return 1

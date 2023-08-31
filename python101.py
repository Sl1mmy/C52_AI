from copy import deepcopy

# Version installée à l'école
# ----------------------------------------------------------------------------
import sys
import copy
print('Version : ', sys.version)


# Bonnes pratiques
# ----------------------------------------------------------------------------
# CALTAL - Code A Little | Test A Little
# DRY - Don't Repeat Yourself
# UMUD - yoU Must Use the Debugger!!!



# Norme de codage
# ----------------------------------------------------------------------------
# Une norme de codage présente :
# • un ensemble de plusieurs règles déterminant la pratique de rédaction du code;
# • des lignes directrices;
# • une convention;
# • ce qui est considéré comme une bonne pratique.
# Elle permet d'assurer une certaine qualité logicielle et une uniformisation de la pratique à travers :
# • les divers intervenants d’un projet;
# • le temps;
# • les technologies employées.
# Cette pratique du génie aide un logiciel à être davantage :
# • maintenable : peut évoluer plus facilement;
# • portable : il fonctionne similairement dans différents environnements;
# • testable : il peut être tester par des procédures standardisées à l'interne;
# • fiable : il fonctionne tel qu'attendu;
# • sûre et sécuritaire : ne peut causer de dommage et plus difficilement piratable;
# en offrant un code :
# • uniforme;
# • plus facile à lire;
# • plus facile à écrire;
# • respectant des guides établis par des développeurs expérimentés;
# • apportant les compromis nécessaires à une pratique de qualité.
# Sachez que dans l'industrie, une norme de codage peut être stricte, contraignante et détaillée ou
# complètement l'inverse. De plus, aucune norme est la meilleure. Les normes varient selon les entreprises,
# les projets, les développeurs, les langages de programmation, l’époque, les outils disponibles, ….

# Avec Python, sauf avis contraire (employeur, enseignant, ...), utilisez la norme de codage PEP8 : https://www.python.org/dev/peps/pep-0008/.
# C'est la règle d'usage dans le cours... et ça compte (sans être strict)!
#  -> PEP : Python Enhancement Proposals <- il y en a plusieurs, allez les consulter progressivement pendant votre formation et votre vie professionnelle.

# Résumé des éléments importants :
#   - disposition
#       - utilisation des espaces (pas de tab)
#       - indentation de 4 espaces
#       - lignes de 79 caractères (*)
#       - lignes vides (au minimum) :
#           - 2 avant la déclaration d'une fonction ou d'une classe
#           - 1 avant la déclaration d'une méthode
#       - 'import' au début du fichier dans l'ordre suivant : 
#           - librairies standards
#           - librairies externes
#           - librairies internes
#   - nommage
#       - types : PascalCase
#       - variables, fonctions, méthodes : snake_case
#       - constantes : CAPITAL_SNAKE_CASE --- les constantes n'existent pas en Python
#       - nom auto descriptif (auto-documentation)
#       
#   - on reviendra sur la notion de masquage en Python!!!
#
#   - commentaires 
#       - JAMAIS DE COMMENTAIRES TRADUISANT EXPLICITEMET LE CODE
#       - JAMAIS DE COMMENTAIRES CREUX
#       - les commentaires doivent ajouter des informations
#       - le docstring devrait prendre la plus grande partie des commentaires - et de loin!
# ----------------------------------------------------------------------------
# PEP8
# 

# Types fondamentaux
# ----------------------------------------------------------------------------
a = 10 # int
b = 3.14 # réel
c = True # bool
d = 'C52' # chaîne de caractères
e = None # NoneType
f = 1+2j # nombre complexe

print('a', type(a), a)
print('b', type(b), b)
print('c', type(c), c)
print('d', type(d), d)
print('e', type(e), e)
print('f', type(f), f)



# Conditionnel ternaire et opérateur ternaire
# ----------------------------------------------------------------------------
value = -5
print(0 <= value < 10) # condition ternaire équivalent à : value >= 0 and value < 10
print('positif' if value >= 0 else 'négatif') # opérateur ternaire (équivalent C/C++ de : value >= 0 ? "Positif" : "Négatif")


# Retour de fonction simple
def demo(value):
    return value == 10
# à éviter
#   if value == 10:
#       return True
#   else:
#       return False


# Structures de données
my_str = 'abc'
my_list = [1, 2]
my_tuple = (1, 2)
my_dict = { 'a': 1, 'b' : 2 }
my_set = { 1, 2 }


# basic data structure              |   mutable     |   subscriptable[read/write]   |   iterable    |   duplicate   |
# structures de données de base     |   modifiable  |   indexable[lecture/écriture] |   itérable    |   doublon     |
# immutable => sécurité et performance
my_str   = 'Hello world'        #   |   0           |   1/0                         |   1           |   1           | fixed size array
my_list  = [0, 1, 2, 3, 4]      #   |   1           |   1/1                         |   1           |   1           | variable size array
my_tuple = (0, 1, 2, 3, 4)      #   |   0           |   1/0                         |   1           |   1           | fixed size array
my_set   = {0, 1, 2, 3, 4}      #   |   1           |   0/0                         |   1           |   0           | hash table
my_dict  = {                    #   |   1           |   1/1                         |   1           |   0:1         | hash table
                0:'zéro', 
                1:'un', 
                2:'deux', 
                3:'trois', 
                4:'quatre'
            }


# slicing
# -----------------------------------------------------------
my_list = list(range(0, 10))
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[0:3])
print(my_list[4:6])
print(my_list[:6])
print(my_list[4:])
print(my_list[-10:])
print(my_list[2:8:2])
print(my_list[::-1])


# parcours
my_list_1 = list(range(0, 10))
my_list_2 = list(range(100, 110))

for value in my_list_2:
    print(value, end=' ')
print()


i = 0
for value in my_list_2:
    print(f'{i:^3} : {value=}')
    i += 1
print()

for value1, value2 in zip(my_list_1, my_list_2):
    print(f"{'?':^3} : {value1=} - {value2=}")
print()

for i, value2 in enumerate(my_list_1):
    print(f"{i:^3} : {value2=}")
print()


values = []
for i in range(10):
    if i % 2 == 0:
        values.append(i**2)
print(values)

values2 = [i**2 for i in range(10) if i % 2 == 0] # comprehension list
print(values2)

text = 'Hello world'
print('Text without "l" : ', [letter for letter in text if letter != 'l'])
print('Text without "l" : ', ''.join([i for i in text if i != 'l']))

print([i for i in range(10) if i % 2])
print([i if i % 2 else '!' for i in range(10) ])



# Référence et "garbage collector"
a = 5
b = 5
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 10
b = 5
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 5
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

b += 1
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 'Allo'
print(hex(id(a)))
a = a + ' monde'
print(hex(id(a)))


a = 'Allo'
b = a
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')
a = 'Cool'
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')


a = [0, 1, 2]
b = a
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')
a[0] = 10
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')


b = deepcopy(a)
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')



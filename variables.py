# l'opérateur d'affectation = permetd'injecter une valeur dans une variable

my_number1 = 123
my_number2 = -42
my_number6 = 0

print(my_number1)
print(my_number2)
print(type(my_number1))
print(type(my_number6))

my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0

print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number3))

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None, Valeur nulle

my_none = None
print(my_none)
print(type(my_none))

my_text1 = "Ceci est une chaîne de caractères"
my_text2 = 'Ceci est aussi une chaîne de caractères'

print(my_text1)
print(my_text2)

# Nouvelle ligne \n

my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "John \"Foo\" Doe"

print(my_text3)
print(my_text4)
print(my_text5)
print(type(my_text1))

my_text6 = """abc
def
ghi"""

print(my_text6)
print(type(my_text6))# transformer le nombre en caractère

# Permutation de la valeur des variables

a = 123
b = 42
a, b = b, a
print(a, b)

a = 123
b = 42
 
c = b
b = a
a = c

print(a)
print(b)

# Variante qu'avec des nombres

c = a + b
a = c - a
b = c - b
print(a, b)

# transtypage str vers int
foo = "123"
foo = int(foo)
print(type(foo))

# transtypage str vers float
foo = "123"
foo = float(foo)
print(type(foo))

# supprimer ce qu'il y a derrire la virgule Float vers int
foo = 3.14
foo = int(foo)
print(type(foo))

# Float vers str
foo = 3.14
foo = str(foo)
print(type(foo))

#
foo = 2.71

a = int(foo)
print(a)

b = foo - a
print(b)

# Estrura de Seleção Simples - if

x = 10
if x > 5:
    print("x é maior que 5.")

a = 10
b = 5
if (b < a):
    print("b é menor que a")

c = 10
d = 10
if (c >= d):
    print("c é maior ou igual a d")

e = 24
f = 69
if (e == 24):
    print("e é igual a 24.")

g = 69
h = 24
if (g != h):
    print("g é diferente de h.")

i = 666
j = 999
if (i > 665) and (j < 1000):
    print("i é maior que 665 e j é menor que 1000")

l = -24
m = -69
if (l < 24) or (m >= -68):
    print("l é menor que 24 ou m é maior ou igual a -68")

n = 10
if (not n == 5):
    print("A condição not n == 5, sendo n = 10, é verdadeira.")

o = 32
p = 23
if (o > 5 and p < 10) or not (p == 32):
    print("A condição (o > 5 and p < 10) or not (p == 32) é verdadeira.")


# Escopo global

n1 = 42
n2 = 96

def soma(n1, n2):

    print("O valor de n1 (Escopo local):", n1)
    print("O valor de n2 (Escopo local):", n2)

    # Escopo local
    n4 = 9

soma(24, 69)

print("O valor de n1 (Escopo global):", n1)
print("O valor de n2 (Escopo global):", n2)

# print("O valor de n4 (Escopo local):", n4)
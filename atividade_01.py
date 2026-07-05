#atividade_01

#Python/Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C.
a = int(input(f"Adicione um número para A: "))
b = int(input(f"\nAdicione um número para B: "))
c = int(input(f"\nAdicione um número para C: "))

d = a + b

print(f"\nOs valores digitados foram: A({a}), B({b}), C({c})")
print(f"\nA soma de A e B é {d}")

if d > c:
    print(f"\nA soma de A e B ({d}) é maior que C ({c})")
elif d < c:
    print(f"\nA soma de A e B ({d}) é menor que C ({c})")
else: 
    print(f"\nOs valores são iguais")
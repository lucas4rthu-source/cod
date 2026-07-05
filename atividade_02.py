#Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

a = int(input("Digite um número aleatório: "))
print(f"\nO número que você escolheu foi {a}")

if a % 2 == 0:
    print("\nO número é par")

else:
    print("\nO número é ímpar")

if a > 0:
    print("\nO número é positivo")

elif a < 0:
    print("\nO número é negativo")

else:
    print("\nO número é zero")
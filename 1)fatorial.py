def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
n = int(input("Digite um número inteiro não negativo: "))
if n < 0:
    print("Número inválido! Por favor, insira um número não negativo.")
else:
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")


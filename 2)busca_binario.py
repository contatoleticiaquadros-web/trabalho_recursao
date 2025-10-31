def busca_binaria(array, valor, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if array[meio] == valor:
        return meio
    elif valor < array[meio]:
        return busca_binaria(array, valor, inicio, meio - 1)
    else:
        return busca_binaria(array, valor, meio + 1, fim)

entrada = input("Digite os números da lista, separados por espaço: ")
lista = list(map(int, entrada.split()))
lista.sort()

valor = int(input("Digite o valor que deseja buscar: "))
resultado = busca_binaria(lista, valor, 0, len(lista) - 1)

if resultado != -1:
    print(f"Valor encontrado na posição {resultado}.")
else:
    print("Valor não encontrado.")

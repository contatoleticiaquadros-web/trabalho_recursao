def hanoi(N, origem, destino, auxiliar):
    if N == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
    else:
        hanoi(N - 1, origem, auxiliar, destino)
        print(f"Mover disco {N} de {origem} para {destino}")
        hanoi(N - 1, auxiliar, destino, origem)

# Exemplo de uso:
hanoi(3, 'A', 'C', 'B')

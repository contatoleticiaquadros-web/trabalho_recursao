RELATÓRIO TRABALHO RECURSÃO

Disciplina: Fundamentos Matemáticos para Computação
Prof. Jayor Teixeira
Aluna: Letícia Silveira Quadros
Matrícula: 25202695

Este relatório visa apresentar o desenvolvimento e análise de três algoritmos recursivos: cálculo fatorial, busca binária e o problema das Torres de Hanói. Cada exercício foi elaborado em linguagem Python e aqui apresentaremos uma explicação detalhada sobre os conceitos de recursividade aplicados.

1) Cálculo Fatorial Recursivo:

O cálculo fatorial é o produto de um número natural por todos os seus antecessores inteiros positivos até o número 1, muito utilizado em matemática para análises combinatórias, por exemplo, permutações. No meu código, primeiramente, foi definida a função fatorial, que recebe um parâmetro n. Após incluir o caso base: o fatorial de 0 é 1, o fatorial de 1 também é 1. Logo, se n for igual a 0 ou 1, a função retorna 1 diretamente, sem continuar chamando a si mesma. Isso é importante para parar a recursão, evitando chamadas infinitas. Em seguida foi utilizado o caso recursivo: caso n seja maior que 1, a função chama a si mesma. A ideia aqui é que o fatorial de um número n é o próprio n multiplicado pelo fatorial de n - 1. No meu código, optei por solicitar ao usuário que informe o número inteiro. Depois o código irá validar o número digitado; se for negativo, o programa avisa que o número é inválido e nem tenta calcular o fatorial. Se o número for válido (≥ 0), a função fatorial é chamada, e o valor retornado é armazenado na variável resultado. Por fim, o resultado é exibido com uma f-string. Considerando que o usuário informou o número 4, a função irá se desenrolar, retornando às multiplicações, até chegar ao resultado final. Exemplo prático:

fatorial(1) → 1
fatorial(2) → 2 * 1 = 2
fatorial(3) → 3 * 2 = 6
fatorial(4) → 4 * 6 = 24
fatorial(4) = 24

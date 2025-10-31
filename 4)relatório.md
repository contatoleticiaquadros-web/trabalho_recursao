RELATÓRIO TRABALHO RECURSÃO

Disciplina: Fundamentos Matemáticos para Computação
Prof. Jayor Teixeira
Aluna: Letícia Silveira Quadros
Matrícula: 25202695

Este relatório visa apresentar o desenvolvimento e análise de três algoritmos recursivos: cálculo fatorial, busca binária e o problema das Torres de Hanói. Cada exercício foi elaborado em linguagem Python e aqui apresentaremos uma explicação detalhada sobre os conceitos de recursividade aplicados.

1) Cálculo Fatorial Recursivo:

O cálculo fatorial é o produto de um número natural por todos os seus antecessores inteiros positivos até o número 1, muito utilizado em matemática para análises combinatórias, por exemplo, permutações. No meu código, primeiramente, foi definida a função fatorial, que recebe um parâmetro n. Após incluir o caso base: o fatorial de 0 é 1, o fatorial de 1 também é 1. Logo, se n for igual a 0 ou 1, a função retorna 1 diretamente, sem continuar chamando a si mesma. Isso é importante para parar a recursão, evitando chamadas infinitas. Em seguida foi utilizado o caso recursivo: caso n seja maior que 1, a função chama a si mesma. A ideia aqui é que o fatorial de um número n é o próprio n multiplicado pelo fatorial de n - 1. No meu código, optei por solicitar ao usuário que informe o número inteiro. Depois o código irá validar o número digitado; se for negativo, o programa avisa que o número é inválido e nem tenta calcular o fatorial. Se o número for válido (≥ 0), a função fatorial é chamada, e o valor retornado é armazenado na variável resultado. Por fim, o resultado é exibido com uma f-string. Considerando que o usuário informou o número 4, a função irá se desenrolar, retornando às multiplicações, até chegar ao resultado final. Exemplo prático:

fatorial(4)
4 * (3 * fatorial(2))
4 * (3 * (2 * fatorial(1)))
4 * (3 * (2 * 1))
4 * (3 * 2)
4 * 6
= 24

2) Busca Binária Recursiva:

A busca binária é um método para procurar um valor específico em uma lista ordenada, extremamente eficiente pois reduz o espaço de busca. A busca binária depende da ordenação da lista para funcionar corretamente, porque ela compara o valor procurado com o elemento central da lista e decide se deve continuar a busca na metade esquerda ou metade direita. Se a lista não estiver ordenada, não há garantia de que o valor procurado estará em uma das metades. Quanto ao caso recursivo: a cada chamada, a função calcula o índice do meio e compara o valor desejado com o elemento nessa posição: se o valor for menor, a busca continua na metade esquerda (- 1) até o fim e se for maior continua na metade direita (+ 1) até o fim. Ou seja, a cada chamada reduz o tamanho do problema pela metade.

Sucesso: Quando meio (array) == valor, o valor é encontrado e o índice é retornado.
Falha: Quando inicio > fim, significa que o valor não está presente na lista e a função retorna -1.

3) Torre de Hanói:

A função hanoi (N, origem, destino, auxiliar) resolve o problema das Torres de Hanói, que consiste em mover uma pilha de discos de um pino de origem para um pino de destino, utilizando um pino auxiliar. A solução recursiva segue três passos fundamentais: mover N-1 discos da origem para o auxiliar, mover o disco N da origem para o destino e mover os N-1 discos do auxiliar para o destino. Essa estrutura permite que o problema seja dividido em subproblemas menores, até que se atinja o caso base. O caso base é essencial para interromper a recursão e começar a desenrolar as chamadas. Isso significa que, quando há apenas um disco, o movimento é direto — não há necessidade de usar o pino auxiliar. Esse exemplo resolve o problema para 3 discos, movendo-os do pino A para o pino C, com B como auxiliar. A saída será uma sequência de 7 movimentos, que é exatamente 2^3-1.

>>> Pra concluir, percebe-se que a recursividade é uma técnica muito útil quando a gente precisa resolver problemas que podem ser divididos em partes menores e parecidas. Os três algoritmos fiz mostram bem como usar recursão de forma prática, desde contas mais simples até desafios clássicos da programação. O mais importante é entender bem os casos base e como as chamadas recursivas funcionam, porque se isso não estiver certo, o código pode acabar rodando pra sempre e travar tudo.



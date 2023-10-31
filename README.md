# Questão 3 - digitalRoot

 - Disciplina: Análise, Projeto e Desenvolvimento Ágil
 - Professor: Diogo Winck
 - Integrantes do Projeto: Beatriz Mayorka de Aguiar e Guilherme Victor Borges Pereira

## Explorando a Matemática da Raiz Digital com Python

A matemática muitas vezes nos reserva surpresas fascinantes, e um exemplo disso é a operação da raiz digital. A raiz digital de um número é obtida através da soma recursiva de seus dígitos até que reste apenas um dígito. Por exemplo, a raiz digital de 16 é 7, já que 1 + 6 = 7. Da mesma forma, a raiz digital de 942 é 6, pois 9 + 4 + 2 resulta em 15 e, subsequentemente, 1 + 5 leva ao dígito 6.

Neste projeto, exploraremos como podemos implementar a operação da raiz digital em Python e, ao mesmo tempo, aprenderemos sobre boas práticas de programação, além de criar testes unitários para verificar a precisão de nossa função.

## Implementando a Função Raiz Digital em Python

Para começar, vamos criar uma função chamada digital_root(n). Esta função receberá um número inteiro não negativo n como entrada e retornará o dígito único resultante após a aplicação do processo de soma recursiva. Aqui está a estrutura geral da função:

```ruby
python
def digital_root(n):
    # Implementação da raiz digital
    pass
```

## Explorando a Lógica

Para calcular a raiz digital, precisamos realizar a soma dos dígitos de n. No entanto, essa soma deve ser realizada de forma recursiva até que reste apenas um dígito. O processo pode ser resumido da seguinte forma:

1. Converta o número em uma sequência de dígitos.
2. Some todos os dígitos.
3. Se o resultado tiver mais de um dígito, repita o processo com o novo número. Caso contrário, retorne o único dígito encontrado.

## Testando a Função

Para garantir que nossa função digital_root está funcionando corretamente, é fundamental criar testes unitários que abranjam diversos cenários. Vamos criar quatro testes:

1. Um número com dois dígitos.
2. Um número com três dígitos.
3. Um número com seis dígitos.
4. Um número grande para testar a eficiência.

Cada teste verificará se a função produz o resultado esperado. Por exemplo, o primeiro teste será:

```ruby
python
def test_digital_root_two_digits():
    assert digital_root(16) == 7
```    

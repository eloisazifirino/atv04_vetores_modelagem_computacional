# Calculadora de Produto Misto e Volumes em 3D

## 1. Sobre o projeto

Este projeto foi desenvolvido como parte da atividade prática da disciplina de **Vetores e Geometria Analítica**. Seu objetivo é aplicar os conceitos de produto misto e cálculo de volumes de sólidos geométricos por meio de um programa desenvolvido em Python.

A aplicação recebe três vetores tridimensionais, calcula o produto misto, determina os volumes de um paralelepípedo e de um tetraedro e apresenta representações gráficas desses sólidos em três dimensões.

## 2. Objetivos

- Aplicar o produto misto no cálculo de volumes.
- Automatizar operações com vetores tridimensionais.
- Verificar propriedades matemáticas por meio de testes.
- Visualizar geometricamente os sólidos associados aos vetores.
- Relacionar os conceitos de Geometria Analítica à programação.

## 3. Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **NumPy:** biblioteca utilizada para operações vetoriais, produto vetorial e produto escalar.
- **Matplotlib:** biblioteca utilizada para construir as visualizações tridimensionais.

## 4. Fundamentação matemática

Dados três vetores tridimensionais \(\vec{u}\), \(\vec{v}\) e \(\vec{w}\), o produto misto é definido por:

$$
[\vec{u},\vec{v},\vec{w}]
= \vec{u}\cdot(\vec{v}\times\vec{w})
$$

Seu valor pode ser calculado por meio do determinante formado pelas coordenadas dos três vetores.

O volume do paralelepípedo definido por esses vetores é dado pelo módulo do produto misto:

$$
V_p = |\vec{u}\cdot(\vec{v}\times\vec{w})|
$$

O volume do tetraedro correspondente é igual a um sexto desse valor:

$$
V_t = \frac{1}{6}|\vec{u}\cdot(\vec{v}\times\vec{w})|
$$

O sinal do produto misto depende da ordem dos vetores e indica sua orientação. Já o volume geométrico é sempre não negativo. Quando o produto misto é zero, os vetores são linearmente dependentes e o sólido formado não possui volume tridimensional positivo.

## 5. Funcionalidades

O programa possui as seguintes funcionalidades:

1. Recebe as coordenadas de três vetores tridimensionais pelo terminal.
2. Verifica se cada vetor informado contém três coordenadas numéricas válidas.
3. Calcula o produto misto dos vetores.
4. Calcula o volume do paralelepípedo.
5. Calcula o volume do tetraedro.
6. Indica quando os vetores são linearmente dependentes, considerando a tolerância numérica utilizada pelo programa.
7. Gera representações gráficas tridimensionais do paralelepípedo e do tetraedro.
8. Executa testes automatizados para verificar os cálculos e propriedades do produto misto.

## 6. Instalação

É necessário ter o Python instalado no computador.

Com o terminal aberto na pasta do projeto, instale as bibliotecas necessárias:

```bash
python -m pip install numpy matplotlib
```

Caso o ambiente utilize o comando `python3`, execute:

```bash
python3 -m pip install numpy matplotlib
```

## 7. Como executar

O arquivo principal do programa é `vetores.py`.

No terminal, dentro da pasta em que o arquivo está localizado, execute:

```bash
python vetores.py
```

Ou, se necessário:

```bash
python3 vetores.py
```

O programa executará os testes automatizados e, em seguida, solicitará as coordenadas dos três vetores.

Informe cada vetor utilizando três números separados por vírgulas. Por exemplo:

```text
Vetor u: 3,0,0
Vetor v: 0,4,0
Vetor w: 1,1,5
```

Após inserir os dados, o programa apresentará os resultados numéricos e abrirá as visualizações tridimensionais dos sólidos.

## 8. Exemplo de execução

Considere os vetores:

$$
\vec{u}=(3,0,0),\quad
\vec{v}=(0,4,0),\quad
\vec{w}=(1,1,5)
$$

O produto misto é:

$$
\vec{u}\cdot(\vec{v}\times\vec{w})=60
$$

Assim, o volume do paralelepípedo é:

$$
V_p=|60|=60
$$

E o volume do tetraedro é:

$$
V_t=\frac{|60|}{6}=10
$$

Portanto, os resultados esperados são:

- **Produto misto:** 60
- **Volume do paralelepípedo:** 60 unidades cúbicas
- **Volume do tetraedro:** 10 unidades cúbicas

## 9. Testes realizados

O programa executa testes automatizados para verificar três situações:

- **Cálculo dos volumes:** utiliza vetores conhecidos para verificar o produto misto e os volumes resultantes.
- **Vetores coplanares:** verifica um caso em que o produto misto e os volumes são iguais a zero.
- **Troca de vetores:** verifica que a troca de dois vetores altera o sinal do produto misto, mas preserva o volume geométrico.

Esses testes ajudam a identificar erros nos cálculos e a confirmar propriedades matemáticas utilizadas na implementação.

## 10. Limitações

A aplicação trabalha com três vetores tridimensionais informados pelo usuário e calcula os volumes associados a eles. Ela não realiza, nesta versão, o cálculo de equações de planos nem a classificação da posição relativa entre planos.

As representações gráficas são utilizadas para auxiliar a visualização dos sólidos, enquanto os resultados numéricos são calculados pelas operações implementadas com NumPy.

## 11. Conclusão

O desenvolvimento deste programa demonstra como conceitos de Vetores e Geometria Analítica podem ser aplicados à resolução de problemas computacionais. A implementação permite relacionar as operações algébricas do produto misto ao cálculo de volumes e à visualização tridimensional, além de utilizar testes automatizados para verificar resultados e propriedades matemáticas.

Dessa forma, o projeto integra fundamentação matemática, programação e representação gráfica, contribuindo para a compreensão prática dos conteúdos estudados.

---

**Disciplina:** Vetores e Geometria Analítica

**Linguagem:** Python

**Bibliotecas:** NumPy e Matplotlib
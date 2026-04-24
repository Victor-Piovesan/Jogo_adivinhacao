# 🎯 Jogo da Adivinhação — Python

> Um jogo de adivinhação de números desenvolvido em Python com múltiplos níveis de dificuldade, sistema de pontuação dinâmico e ranking de jogadores.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Como Rodar o Projeto](#-como-rodar-o-projeto)
- [Como Jogar](#-como-jogar)
- [Níveis de Dificuldade](#-níveis-de-dificuldade)
- [Sistema de Pontuação](#-sistema-de-pontuação)
- [Ranking](#-ranking)
- [Estrutura do Código](#-estrutura-do-código)
- [Layout do Jogo (Diferencial)](#-layout-do-jogo-diferencial)

---

## 📖 Sobre o Projeto

O **Jogo da Adivinhação** é uma aplicação de terminal desenvolvida em Python que desafia o jogador a descobrir um número secreto gerado aleatoriamente. O projeto aplica conceitos de **Programação Orientada a Objetos (POO)**, incluindo classes abstratas, herança e encapsulamento.

---

## ✨ Funcionalidades

| # | Funcionalidade | Descrição |
|---|---|---|
| 1 | 👤 **Inserir nome do jogador** | O jogador informa seu nome antes de iniciar |
| 2 | 🎮 **Escolher nível de dificuldade** | Três níveis disponíveis: Fácil, Médio e Difícil |
| 3 | 🔢 **Jogar o jogo de adivinhação** | O jogador tenta descobrir o número secreto com dicas |
| 4 | 🏅 **Calcular pontuação** | Pontuação dinâmica descontada a cada tentativa errada |
| 5 | 💾 **Armazenar jogadores no ranking** | Todos os resultados são salvos ao final de cada partida |
| 6 | 🏆 **Exibir ranking ordenado** | Ranking completo exibido ao término de cada rodada |

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.7** ou superior

Verifique sua versão com:

```bash
python --version
```

> O projeto utiliza apenas bibliotecas nativas do Python (`random` e `abc`), **não sendo necessária nenhuma instalação adicional**.

---

## 🚀 Como Rodar o Projeto

**1. Clone o repositório ou baixe o arquivo:**

```bash
git clone https://github.com/seu-usuario/jogo-adivinhacao.git
cd jogo-adivinhacao
```

**2. Execute o jogo diretamente pelo terminal:**

```bash
python jogo_adivinhacao.py
```

> **Windows:** caso `python` não funcione, tente `py jogo_adivinhacao.py`

---

## 🕹️ Como Jogar

Após iniciar o jogo, siga os passos abaixo:

**Passo 1 — Inserir nome**

```
========================================
     JOGO DA ADIVINHAÇÃO
========================================

Qual o seu nome? Maria
```

> Se o campo for deixado em branco, o nome padrão **"Jogador"** será utilizado.

---

**Passo 2 — Escolher a dificuldade**

```
Escolha a dificuldade:
  1 - Fácil   (1–50,  15 tentativas, pontuação base 15)
  2 - Médio   (1–100, 10 tentativas, pontuação base 10)
  3 - Difícil (1–200,  5 tentativas, pontuação base 20)
Dificuldade (1/2/3): 2
```

---

**Passo 3 — Adivinhar o número**

A cada palpite, o jogo informa se o número secreto é **maior** ou **menor**:

```
Olá, Maria! Adivinhe o número entre 1 e 100.
Você tem 10 tentativas.

[10 restante(s)] Seu palpite: 50
⬆  O número secreto é MAIOR.

[9 restante(s)] Seu palpite: 75
⬇  O número secreto é MENOR.

[8 restante(s)] Seu palpite: 63
🎉 Parabéns, Maria! Você acertou!
   Tentativas usadas : 3
   Pontuação final   : 8
```

---

**Passo 4 — Ver o Ranking e jogar novamente**

Ao final de cada partida, o ranking é exibido automaticamente:

```
========================================
           🏆  RANKING
========================================
#    Nome            Pontos   Tentativas   Dificuldade
--------------------------------------------------
1    Maria           8        3            Médio
2    João            5        6            Difícil
========================================

Deseja jogar novamente?
(s) Sim  |  (n) Não:
```

---

## 🎯 Níveis de Dificuldade

| Nível | Intervalo | Tentativas | Pontuação Base |
|-------|-----------|------------|----------------|
| 🟢 Fácil | 1 a 50 | 15 | 15 pontos |
| 🟡 Médio | 1 a 100 | 10 | 10 pontos |
| 🔴 Difícil | 1 a 200 | 5 | 20 pontos |

> A dificuldade **Difícil** oferece a maior pontuação base, mas também o menor número de tentativas — ideal para jogadores experientes.

---

## 🏅 Sistema de Pontuação

A pontuação é calculada de forma dinâmica durante a partida:

- **Pontuação inicial** é definida pelo nível de dificuldade escolhido.
- **A cada tentativa errada**, 1 ponto é descontado da pontuação.
- **Se o jogador perder** (esgotar as tentativas), a pontuação final será **0**.

**Exemplo — Nível Médio (pontuação base: 10):**

| Tentativa | Resultado | Pontuação |
|-----------|-----------|-----------|
| 1ª | Errou | 9 |
| 2ª | Errou | 8 |
| 3ª | Acertou ✅ | **8** |

---

## 🏆 Ranking

O ranking é mantido em memória durante toda a sessão de jogo e exibido ao final de cada partida.

**Critérios de ordenação:**

1. **Maior pontuação** tem prioridade.
2. Em caso de empate, **menor número de tentativas** vence.

**Informações exibidas:**

- Posição no ranking
- Nome do jogador
- Pontuação final
- Número de tentativas usadas
- Nível de dificuldade escolhido

---

## 🗂️ Estrutura do Código

```
jogo_adivinhacao.py
│
├── ranking[]                  # Lista global com todos os jogadores
│
├── class Jogo (ABC)           # Classe abstrata base
│   ├── iniciar()              # Método abstrato
│   └── jogar()                # Método abstrato
│
├── class JogoAdivinhacao      # Implementação concreta do jogo
│   ├── iniciar()              # Coleta nome e dificuldade; gera número secreto
│   ├── jogar()                # Loop principal de tentativas e pontuação
│   └── _salvar_no_ranking()   # Persiste o resultado na lista global
│
├── exibir_ranking()           # Exibe o ranking ordenado no terminal
├── executar_jogo(jogo)        # Função auxiliar que chama iniciar() + jogar()
└── main()                     # Loop principal — gerencia múltiplas partidas
```

**Conceitos de POO aplicados:**

- **Abstração** — classe `Jogo` define a interface obrigatória via `ABC`
- **Herança** — `JogoAdivinhacao` herda de `Jogo`
- **Encapsulamento** — atributos protegidos com prefixo `_`
- **Polimorfismo** — `executar_jogo()` recebe qualquer instância de `Jogo`

---

## 🖥️ Layout do Jogo (Diferencial)

O jogo foi projetado com um layout visual cuidadoso para o terminal, utilizando separadores, emojis e formatação alinhada para tornar a experiência mais agradável.

**Tela de boas-vindas:**
```
========================================
     JOGO DA ADIVINHAÇÃO
========================================
```

**Dicas durante o jogo:**
```
⬆  O número secreto é MAIOR.
⬇  O número secreto é MENOR.
🎉 Parabéns! Você acertou!
😢 Suas tentativas acabaram!
✅ Resultado salvo no ranking!
```

**Ranking formatado:**
```
========================================
           🏆  RANKING
========================================
#    Nome            Pontos   Tentativas   Dificuldade
--------------------------------------------------
1    Maria           8        3            Médio
========================================
```

> O contador regressivo `[X restante(s)]` exibido antes de cada palpite mantém o jogador informado sobre quantas chances ainda restam, aumentando a tensão e o engajamento.

---

*Desenvolvido com 🐍 Python*

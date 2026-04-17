import random
from abc import ABC, abstractmethod


# ── Ranking global (armazena todos os jogadores) ──────────────────────────────
ranking = []


class Jogo(ABC):

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


class JogoAdivinhacao(Jogo):

    def __init__(self):
        self._numero_secreto = None
        self._tentativas = 0
        self._limite = 10          # será ajustado pela dificuldade
        self._nome = None
        self._pontuacao = 0        # será ajustado pela dificuldade
        self._dificuldade = 0
        self._range_max = 100      # será ajustado pela dificuldade

    # ── 1. Inserir nome  &  2. Escolher dificuldade ───────────────────────────
    def iniciar(self):
        print("=" * 40)
        print("     JOGO DA ADIVINHAÇÃO")
        print("=" * 40)

        # 1. Nome do jogador
        self._nome = input("\nQual o seu nome? ").strip()
        if not self._nome:
            self._nome = "Jogador"

        # 2. Nível de dificuldade
        print("\nEscolha a dificuldade:")
        print("  1 - Fácil   (1–50,  15 tentativas, pontuação base 15)")
        print("  2 - Médio   (1–100, 10 tentativas, pontuação base 10)")
        print("  3 - Difícil (1–200,  5 tentativas, pontuação base 20)")

        while True:
            escolha = input("Dificuldade (1/2/3): ").strip()
            if escolha in ("1", "2", "3"):
                self._dificuldade = int(escolha)
                break
            print("Opção inválida. Digite 1, 2 ou 3.")

        # Configura parâmetros conforme a dificuldade
        if self._dificuldade == 1:          # Fácil
            self._range_max = 50
            self._limite = 15
            self._pontuacao = 15
        elif self._dificuldade == 2:        # Médio
            self._range_max = 100
            self._limite = 10
            self._pontuacao = 10
        else:                               # Difícil
            self._range_max = 200
            self._limite = 5
            self._pontuacao = 20

        self._numero_secreto = random.randint(1, self._range_max)

        print(f"\nOlá, {self._nome}! Adivinhe o número entre 1 e {self._range_max}.")
        print(f"Você tem {self._limite} tentativas.\n")

    # ── 3. Jogar  &  4. Calcular pontuação ───────────────────────────────────
    def jogar(self):
        acertou = False

        while self._tentativas < self._limite:
            tentativas_restantes = self._limite - self._tentativas
            try:
                palpite = int(input(f"[{tentativas_restantes} restante(s)] Seu palpite: "))
            except ValueError:
                print("Digite um número válido.\n")
                continue

            self._tentativas += 1

            if palpite == self._numero_secreto:
                # 4. Pontuação: cada tentativa errada já descontou 1 ponto
                print(f"\n🎉 Parabéns, {self._nome}! Você acertou!")
                print(f"   Tentativas usadas : {self._tentativas}")
                print(f"   Pontuação final   : {self._pontuacao}")
                acertou = True
                break

            # Desconta 1 ponto por tentativa errada
            self._pontuacao -= 1

            if palpite < self._numero_secreto:
                print("⬆  O número secreto é MAIOR.\n")
            else:
                print("⬇  O número secreto é MENOR.\n")

        if not acertou:
            self._pontuacao = 0   # zera pontuação ao perder
            print(f"\n😢 Suas tentativas acabaram, {self._nome}!")
            print(f"   O número secreto era: {self._numero_secreto}")
            print(f"   Pontuação final      : {self._pontuacao}")

        # 5. Armazenar jogador no ranking
        self._salvar_no_ranking()

    # ── 5. Armazenar no ranking ───────────────────────────────────────────────
    def _salvar_no_ranking(self):
        niveis = {1: "Fácil", 2: "Médio", 3: "Difícil"}
        ranking.append({
            "nome": self._nome,
            "pontuacao": self._pontuacao,
            "tentativas": self._tentativas,
            "dificuldade": niveis[self._dificuldade],
        })
        print(f"\n✅ Resultado de {self._nome} salvo no ranking!")


# ── 6. Exibir ranking ordenado ────────────────────────────────────────────────
def exibir_ranking():
    print("\n" + "=" * 40)
    print("           🏆  RANKING")
    print("=" * 40)

    if not ranking:
        print("Nenhum jogador no ranking ainda.")
        return

    # Ordena por pontuação (maior primeiro); empate → menos tentativas
    ranking_ordenado = sorted(
        ranking,
        key=lambda x: (-x["pontuacao"], x["tentativas"])
    )

    print(f"{'#':<4} {'Nome':<15} {'Pontos':<8} {'Tentativas':<12} {'Dificuldade'}")
    print("-" * 50)
    for posicao, jogador in enumerate(ranking_ordenado, start=1):
        print(
            f"{posicao:<4} {jogador['nome']:<15} {jogador['pontuacao']:<8} "
            f"{jogador['tentativas']:<12} {jogador['dificuldade']}"
        )
    print("=" * 40)


# ── Função auxiliar de execução ───────────────────────────────────────────────
def executar_jogo(jogo: Jogo):
    jogo.iniciar()
    jogo.jogar()


# ── Loop principal ─────────────────────────────────────────────────────────────
def main():
    while True:
        jogo = JogoAdivinhacao()
        executar_jogo(jogo)

        exibir_ranking()

        print("\nDeseja jogar novamente?")
        resposta = input("(s) Sim  |  (n) Não: ").strip().lower()
        if resposta != "s":
            print("\nObrigado por jogar! Até a próxima! 👋")
            break


if __name__ == "__main__":
    main()
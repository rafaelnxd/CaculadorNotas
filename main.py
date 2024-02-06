from avgscripts import calcular_media_semestre, calcular_media_anual
import streamlit as st


def main():
    while True:
        escolha = int(input("1. Calcular média do semestre\n2. Calcular média anual\n3. Sair\nEscolha uma opção: "))

        if escolha == 1:
            media_semestre01 = calcular_media_semestre()
            print(media_semestre01)
        elif escolha == 2:
            media_semestre01 = calcular_media_semestre()
            print(media_semestre01)
            media_semestre02 = calcular_media_semestre()
            print(media_semestre02)
            media_anual = calcular_media_anual(media_semestre01, media_semestre02)
            print(media_anual)
        elif escolha == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()

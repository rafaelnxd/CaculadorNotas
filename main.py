from avgscripts import calcular_media_semestre, calcular_media_anual
import streamlit as st


def main():
    st.title("Calculadora de Média")
    st.header("Bem-vindo à Calculadora Faz o L")

    while True:
        escolha = st.selectbox("Escolha uma opção:", ["Calcular média do semestre", "Calcular média anual", "Sair"])

        if escolha == "Calcular média do semestre":
            st.subheader("Calcular Média do Semestre")
            media_semestre01 = calcular_media_semestre()
            st.write(f"A média do semestre é: {media_semestre01}")

        elif escolha == "Calcular média anual":
            st.subheader("Calcular Média Anual")
            media_semestre01 = calcular_media_semestre()
            media_semestre02 = calcular_media_semestre()
            media_anual = calcular_media_anual(media_semestre01, media_semestre02)
            st.write(f"A média anual é: {media_anual}")

        elif escolha == "Sair":
            st.write("Saindo...")
            break

if __name__ == "__main__":
    main()
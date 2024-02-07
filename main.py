from avgscripts import calcular_media_semestre, calcular_media_anual
import streamlit as st


st.set_page_config(
   
   page_title="Calculadora de Média",
    layout="centered",
    initial_sidebar_state="auto",

)

def main():
    st.title("Calculadora de Média")


    escolha = st.radio("Escolha uma opção:", ["Calcular média do semestre", "Calcular média anual"])

    if escolha == "Calcular média do semestre":
        st.subheader("Calcular Média do Semestre")

        # Gerando chaves únicas para os widgets
        chaves_semestre = [f"nota_checkpoint_{i}_semestre" for i in range(3)] + ["sp01_semestre", "sp02_semestre", "gs01_semestre"]

        media_semestre = calcular_media_semestre(chaves_semestre)
        st.write(f"A média do semestre é: {media_semestre}")

    if escolha == "Calcular média anual":
        st.subheader("Calcular Média Anual")

        # Gerando chaves únicas para os widgets
        chaves_semestre01 = [f"nota_checkpoint_{i}_semestre01" for i in range(3)] + ["sp01_semestre01", "sp02_semestre01", "gs01_semestre01"]
        chaves_semestre02 = [f"nota_checkpoint_{i}_semestre02" for i in range(3)] + ["sp01_semestre02", "sp02_semestre02", "gs01_semestre02"]

        media_semestre01 = calcular_media_semestre(chaves_semestre01)
        st.write("A média do Segundo Semestre foi:", media_semestre01)
        st.write ("----------------------------------------------------")
        media_semestre02 = calcular_media_semestre(chaves_semestre02)
        st.write("Média do Segundo Semestre foi:", media_semestre02)
        st.write ("----------------------------------------------------")

        media_anual = calcular_media_anual(media_semestre01, media_semestre02)
        st.write(f"A média anual é: {media_anual}")


   
        

if __name__ == "__main__":
    main()

import streamlit as st


def calcular_media_semestre(chaves):
    pesocpsp = 4
    peso_gs = 6

    notas_checkpoint = []
    for i in range(3):
        # Utilizamos as chaves fornecidas
        nota_checkpoint = st.number_input(f"Informe a nota do {i+1}º checkpoint:", key=chaves[i])
        notas_checkpoint.append(nota_checkpoint)

    menor_nota = min(notas_checkpoint)
    notas_checkpoint.remove(menor_nota)

    sp01 = st.number_input("Informe a nota da 1ª sprint:", key=chaves[3])
    sp02 = st.number_input("Informe a nota da 2ª sprint:", key=chaves[4])

    media_cpsp = (sum(notas_checkpoint) + sp01 + sp02) / 4
    st.write("Média dos Checkpoints e Sprints:", media_cpsp)

    gs01 = st.number_input("Informe a nota da Global Solution:", key=chaves[5])

    media_semestre = (media_cpsp * pesocpsp + gs01 * peso_gs) / (pesocpsp + peso_gs)

    return media_semestre


def calcular_media_anual(media_semestre01, media_semestre02):

    pesosemestre1 = 4
    pesosemestre2 = 6

    media_anual = (media_semestre01 * pesosemestre1 + media_semestre02 * pesosemestre2) / (pesosemestre1 + pesosemestre2)

    return media_anual






    




    



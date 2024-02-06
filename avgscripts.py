def calcular_media_semestre():

    # pesocpsp = 4
    # peso_gs = 6
    
    # cp0101 = float(input(f"Informe a nota do 1º checkpoint do primeiro semestre: "))
    # cp0201 = float(input(f"Informe a nota do 2º checkpoint do primeiro semestre: "))

    # sp01 = float(input(f"Informe a nota da 1ª sprint: "))
    # sp02 = float(input(f"Informe a nota da 2ª sprint: "))

    # media_cpsp = (cp0101 + cp0201 + sp01 + sp02) / 4
    
    # print("Média dos checkpoints e sprints:", media_cpsp)

    # gs01 = float(input(f"Informe a nota da Global Solution do primeiro semestre: "))

    # media_semestre = (media_cpsp * pesocpsp + gs01 * peso_gs) / (pesocpsp + peso_gs)

    
    # return media_semestre

    pesocpsp = 4
    peso_gs = 6

    notas_checkpoint = []
    for i in range(3):
        nota_checkpoint = float(input(f"Informe a nota do {i+1}º checkpoint: "))
        notas_checkpoint.append(nota_checkpoint)

    menor_nota = min(notas_checkpoint)
    notas_checkpoint.remove(menor_nota)

    sp01 = float(input(f"Informe a nota da 1ª sprint: "))
    sp02 = float(input(f"Informe a nota da 2ª sprint: "))

    media_cpsp = (sum(notas_checkpoint) + sp01 + sp02) / 4
    print("Média dos checkpoints e sprints:", media_cpsp)

    gs01 = float(input(f"Informe a nota da Global Solution: "))

    media_semestre = (media_cpsp * pesocpsp + gs01 * peso_gs) / (pesocpsp + peso_gs)

    return media_semestre



def calcular_media_anual(media_semestre01, media_semestre02):

    pesosemestre1 = 4
    pesosemestre2 = 6

    media_anual = (media_semestre01 * pesosemestre1 + media_semestre02 * pesosemestre2) / (pesosemestre1 + pesosemestre2)

    return media_anual






    




    



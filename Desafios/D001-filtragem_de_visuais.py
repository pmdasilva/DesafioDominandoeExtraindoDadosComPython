def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")

    # Normalize e remova duplicatas usando um conjunto
    # lista_normalizada = set(visual.lower() for visual in visuais) #Essa é a forma comprimida
    lista_normalizada = set()
    for visual in visuais:
        lista_normalizada.add(visual.lower())

    # Converta o conjunto de volta para uma lista ordenada:
    #lista_final = [visual.title() for visual in sorted(lista_normalizada)] #Essa é a forma comprimida
    lista_final = []
    for visual in sorted(lista_normalizada):
        lista_final.append(visual.title())

    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)


# Capturar a entrada do usuário
entrada_usuario = input()


# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)
qtd_linha = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linha:
    coluna = 1

    while coluna <= qtd_colunas:
        coluna += 1
        print(f"{linha=}, {coluna=}")
    linha += 1

print ("Acabou")
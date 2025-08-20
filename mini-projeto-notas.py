import os
#os.system('cls')
nomes = []
notas = []
while True:
    print("="*6+" Menu Principal "+"="*6)
    print("="*28)
    print("1 - CADASTRAR ALUNO E NOTA\n2 - ATUALIZAR DADOS\n3 - MOSTRAR MÉDIA DA TURMA\n4 - MOSTRAR DADOS\n5 - NOMES E NOTAS\n0 - SAIR")
    print("="*28)
    seletor = int(input("Digite aqui: "))
    os.system('cls')
    if seletor == 1:
        while True:

            print("="*6+" Menu Cadastro "+"="*6)
            print("="*27)
            print("1 - CADASTRAR ALUNO E NOTA\n0 - SAIR")
            print("="*27)

            seletor_cadastro = int(input("Digite aqui: "))
            if seletor_cadastro == 1:
                os.system('cls')
                nome_aluno = str(input("Digite o nome do aluno: "))
                nomes.append(nome_aluno)
                nota_aluno = float(input(f"Digite a nota do {nome_aluno}: "))
                notas.append(nota_aluno)
                os.system('cls')
                print(f"Aluno: {nome_aluno}\nNota: {nota_aluno}\nCADASTRADO!")

            elif seletor_cadastro == 0:
                os.system('cls')
                break

            else:
                print("Código inválido, tente novamente!")
                print("="*27)
                print("1 - CADASTRAR ALUNO E NOTA\n0 - SAIR")
                print("="*27)
                seletor_cadastro = int(input("Digite aqui: "))
                os.system('cls')  

    elif seletor == 2:
        while True:

            print("="*6+" Menu alter "+"="*6)
            print("="*27)
            print("1 - ALTERAR NOME ALUNO\n2 - ALTERAR NOTA\n0 - Sair")
            print("="*27)

            seletor_altera = int(input("Digite aqui: "))
            if seletor_altera == 1:

                elemento_nome = str(input("Digite o elemento (Nome) que você deseja alterar: "))
                

                if elemento_nome in nomes:
                    index_alterar = nomes.index(elemento_nome)

                    for i in range(0,len(nomes)):

                        if i == index_alterar:
                            novo_nome = str(input("Digite o novo nome: "))
                            nomes[i] = novo_nome
                            elemento_nome = novo_nome
                            os.system('cls')
                            print(f"Nome alterado!")
                            print("Deseja alterar a nota:\n1 - Sim\n0 - Não")
                            seletor_altera_nota = int(input("Digite aqui: "))
                            os.system('cls')

                            if seletor_altera_nota == 1:
                                nova_nota = float(input(f"Digite a nova nota de {nomes[i]}: "))
                                notas[i] = nova_nota
                                os.system('cls')
                                print(f"Nota Alterada!")
                                

                            elif seletor_altera_nota == 0:
                                os.system('cls')
                                break

                            else:
                                print("Código inválido, tente novamente!")
                                print("="*27)
                                print("1 - ALTERAR ALUNO E NOTA\n0 - SAIR")
                                print("="*27)
                                seletor_cadastro = int(input("Digite aqui: "))
                                os.system('cls')
                else:
                        print(f"{elemento_nome} não encontrado, tente novamente!")
                        elemento_nome = str(input("Digite o elemento (Nome) que você deseja alterar o nome: "))        

            elif seletor_altera == 2:

                
                elemento_nome = str(input("Digite o elemento (Nome) que você deseja alterar a nota: "))
                if elemento_nome in nomes:
                    index_alterar = nomes.index(elemento_nome) 
                    for i in range(0,len(notas)):
                        if i == index_alterar:
                            nova_nota = float(input(f"Digite uma nova nota para {nomes[index_alterar]}:"))   
                            notas[i] = nova_nota
                            os.system('cls')
                            print(f"Nota Alterada!")
                            break
                    else:
                        print(f"{elemento_nome} não encontrado, tente novamente!")
                        elemento_nome = str(input("Digite o elemento (Nome) que você deseja alterar a nota: "))

            elif seletor_altera == 0:
                os.system('cls')
                break

            else:
                print("="*6+" Menu Alteração "+"="*6)
                print("="*27)
                print("1 - ALTERAR NOME ALUNO\n2 - ALTERAR NOTA\n0 - Sair")
                print("="*27)
                seletor_altera = int(input("Digite aqui: "))                                                                                       

    elif seletor == 3:
        if len(notas) == 0:
            print("Nenhuma nota foi inserida.")
        else:    
            print(f"A média da turma foi: {sum(notas)/len(notas)}")

    elif seletor == 4:
        for i in range(len(notas)):
            if notas[i]>=7:
                print(f"O aluno {nomes[i]} ficou acima de média com {notas[i]} pontos.")
            else:
                print(f"O aluno {nomes[i]} ficou abaixo de média com {notas[i]} pontos.")   

    elif seletor == 5:
        print(nomes)
        print(notas)

    elif seletor == 0:
        break

    else:
        print("Código inválido!")
        print("="*27)
        print("1 - CADASTRAR ALUNO E NOTA\n2 - ATUALIZAR DADOS\n3 - MOSTRAR MÉDIA DA TURMA\n4 - MOSTRAR DADOS\n0 - SAIR")
        print("="*27)
        seletor = int(input("Digite aqui: "))                        



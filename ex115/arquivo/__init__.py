def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') ## w= write t= text + = cria um arquivo de texto
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo. Contate o adm.\033[31m')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
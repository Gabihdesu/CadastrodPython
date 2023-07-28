from ex115.utilidades import dados
from ex115.arquivo import *

arq = 'cadastros.txt'
if not arquivoExiste(arq):
    print('Arquivo não encontrado.')
    criarArquivo(arq)


while True:
    dados.titulo('MENU PRINCIPAL')
    print('''   \033[33m 1- \033[31mVer pessoas cadastradas
    \033[33m2- \033[31mCadastrar novas pessoas
    \033[33m3- \033[31mSair do Sistema\033[m''')
    print('-'*40)
    try:
        resp = dados.leiaInt('\033[34mSua opção: \033[m')
    except:
        print('Escolha um dos números do menu.')
    else:
        if resp == 1:
            dados.mostrar(arq)
        elif resp == 2:
            dados.titulo('NOVO CADASTRO')
            nome = str(input('Nome: ')).strip().capitalize()
            idade = dados.leiaInt('Idade: ')
            dados.cadastrar(arq, nome, idade)

        else:
            dados.titulo('Saindo do sistema.... Até logo')
            break


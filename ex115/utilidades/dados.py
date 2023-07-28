def leiaInt(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('\033[31mERRO! Valor digitado inválido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário preferiu não informar o valor.\033[m')
            return 0
        else:
            return n


def titulo(title):
    print('-' * 40)
    print(f'{title:^40}')
    print('-' * 40)


def mostrar(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'ERRO ao abrir o arquivo {erro.__cause__}')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(',')
            dado[1]= dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3}anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade= 0):
    try:
        a = open(arquivo, 'at') ## a = append t = arq de texto
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome}, {idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print('Novo registro adicionado.')
            a.close()

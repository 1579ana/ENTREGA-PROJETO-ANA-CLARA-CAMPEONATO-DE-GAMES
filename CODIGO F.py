def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'reset': '\033[0m'}
    return cores.get(cor, '') + texto + cores['reset']


def banner_campeonato():
    print()
    print(cor_texto(" ██████╗  █████╗ ███╗   ███╗██████╗ ███████╗ ██████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ",'azul'))
    print(cor_texto("██╔════╝ ██╔══██╗████╗ ████║██╔══██ ██╔════╝██╔═══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗",'azul'))
    print(cor_texto("██║      ███████║██╔████╔██║██║██║  █████╗  ██║   ██║██╔██╗ ██║███████║   ██║   ██║   ██║",'azul'))
    print(cor_texto("██║      ██╔══██║██║╚██╔╝██║██║     ██╔══╝  ██║   ██║██║╚██╗██║██╔══██║   ██║   ██║   ██║",'azul'))
    print(cor_texto("╚██████╔╝██║  ██║██║ ╚═╝ ██║██      ███████╗╚██████╔╝██║ ╚████║██║  ██║   ██║   ╚██████╔╝",'azul'))
    print(cor_texto(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═      ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ",'azul'))
    print()
    print(cor_texto('Seja bem-vindo ao Sistema de Campeonato de Games — '
                    'Uma plataforma desenvolvida especialmente para organizar e '
                    'gerenciar competições entre jogadores!','azul'))
banner_campeonato()


campeonato = []

def mostrar_jogos():
    print('-' * 18)
    print(cor_texto('JOGOS DISPONÍVEIS','azul'))
    print('-' * 18)

    print('-' * 18)
    print(cor_texto('FREE FIRE', 'vermelho'))
    print('Plataforma: Mobile\n'
          'Regras : Battle Royale, Solo, Partida Única, Sobrevive o Último')
    print('-' * 18)

    print('-' * 18)
    print(cor_texto('LEAGUE OF LEGENDS', 'amarelo'))
    print('Plataforma: PC\n'
    'Regras : 5x5, Eliminar Nexus Inimigo, Tempo Limite 40 Minutos')

    print('-' * 18)
    print(cor_texto('FIFA', 'verde'))
    print('Plataforma : PlayStation\n'
    'Regras : 1x1, Duas Partidas de 6 Minutos Cada, Soma de Gols')
    print('-' * 18)


def cadastrar_alunos():
    print('-' * 18) # Decoração
    print(cor_texto('CADASTRAR ALUNOS','azul')) # Intro
    print('-' * 18) # Decoração
    nome = str(input('Nome do(a) Aluno(a): ')) # Add Nome do Aluno
    idade = int(input('Idade do(a) Aluno(a): ')) # Add Idade do Aluno
    jogo = str(input('Jogo Escolhido: ')) # Add Jogo Escolhido
    cadastro = {'Nome':nome, # Dicionario das Informações do Cadastro
              'Idade':idade,
              'Jogo':jogo}

    campeonato.append(cadastro)
    print(cor_texto('Cadastro dos Alunos Realizada com Sucesso!\n','azul'))
    #\n para pular uma linha - estética


def consultar_cadastros():
    print("CONSULTAR CADASTROS – CAMPEONATO DE JOGOS ESTUDANTIL")
    print('-.-' * 13)
    if len(campeonato) == 0: #se eu tenho a minha lista vazia
        print("Nenhuma sessão cadastrada \n")
        return #se for verdadeira sai da ssesao
    numero = 1 #numerar as sessoes
    for inscricao in campeonato:
        print(f"[{numero}] Nome: {inscricao['Nome']} | Idade: {inscricao['Idade']} | "
              f"Jogo: {inscricao['Jogo']}")
        numero += 1
    print()


def buscar_por_nome():
    termo = str(input('Qual o Nome do Jogador Deseja Buscar?:')).lower()
    encontrados = []
    for cadastro in campeonato:  # varredura, para comparar
        if (termo in cadastro['Nome'].lower()):
            encontrados.append(cadastro)

    if len(encontrados) == 0:
        print('Nenhum Jogador encontrado.\n')
        return  # para sair/finalizar a função

    numero = 1  # localização/índice
    for cadastro in encontrados:
        print(f"[{numero}] Nome: {cadastro['Nome']} Idade:{cadastro['Idade']} Jogo:{cadastro['Jogo']} ")
    numero += 1
    print()


def buscar_jogo():
    termo = str(input('Qual Jogo Deseja Buscar? (Free Fire - League of Leages - FIFA):')).lower()
    encontrados = []
    for cadastro in campeonato: #varredura, para comparar
        if (termo in cadastro['Jogo'].lower()):
            encontrados.append(cadastro)

    if len(encontrados) == 0:
        print('Nenhum Jogo Encontrado.\n')
        return #para sair/finalizar a função

    numero = 1 #localização/índice
    for cadastro in encontrados:
        print(f"[{numero}] Jogo: {cadastro['Nome']} Idade:{cadastro['Idade']} ")
    numero += 1
    print()

vencedorfreefire =''
vencedorleagueoflegends=''
vencedorfifa=''
def registro_vencedores():
    print('-' * 18)  # Decoração
    print(cor_texto('REGISTRAR VENCEDORES', 'azul'))  # Intro
    print('-' * 18)  # Decoração
    global vencedorfreefire

    vencedorfreefire = input('Vencedor do Game Free Fire:')

    global vencedorleagueoflegends

    vencedorleagueoflegends = input('Vencedor do Game League of Legends:')

    global vencedorfifa
    vencedorfifa = input('Vencedor do Game Fifa:')

def exibir_vencedores():

    print('-' * 18)  # Decoração
    print(cor_texto('MOSTRAR VENCEDORES', 'roxo'))  # Intro
    print('-' * 18)  # Decoração

    print("\n" + "=" * 55)
    print("           🏆 GANHADOR(A) DO JOGO FREE FIRE 🏆          ")
    print("=" * 55)
    print(cor_texto("""
               ___________
              '._==_==_=_.'
              .-\\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \\::.    /
                 '::. .'
                   ) (
                 _.' '._
                `\"\"\"\"\"\"\"`
        """, "amarelo"))
    print(f"🏅 Parabéns, {vencedorfreefire}! Você é o(a) grande campeão(a)! 🏅")
    print("=" * 55 + "\n")

    print("\n" + "=" * 55)
    print("           🏆 GANHADOR(A) DO JOGO LOL 🏆          ")
    print("=" * 55)
    print(cor_texto("""
               ___________
              '._==_==_=_.'
              .-\\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \\::.    /
                 '::. .'
                   ) (
                 _.' '._
                `\"\"\"\"\"\"\"`
        """, "amarelo"))
    print(f"🏅 Parabéns, {vencedorleagueoflegends}! Você é o(a) grande campeão(a)! 🏅")
    print("=" * 55 + "\n")

    print("\n" + "=" * 55)
    print("           🏆 GANHADOR(A) DO JOGO FIFA 🏆          ")
    print("=" * 55)
    print(cor_texto("""
               ___________
              '._==_==_=_.'
              .-\\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \\::.    /
                 '::. .'
                   ) (
                 _.' '._
                `\"\"\"\"\"\"\"`
        """, "amarelo"))
    print(f"🏅 Parabéns, {vencedorfifa}! Você é o(a) grande campeão(a)! 🏅")
    print("=" * 55 + "\n")


def exibir_menu():
    while True:
        print('-' * 18)
        print(cor_texto('Menu Do Campeonato','azul'))
        print('-' * 18)
        print(cor_texto('1. Mostrar Jogos Disponíveis','amarelo'))
        print(cor_texto('2. Cadastrar Jogadores','amarelo'))
        print(cor_texto('3. Mostrar Jogadores Cadastrados','amarelo'))
        print(cor_texto('4. Buscar Por Jogadores','amarelo'))
        print(cor_texto('5. Buscar Por Jogo','amarelo'))
        print(cor_texto('6. Registrar Vencedor','amarelo'))
        print(cor_texto('7. Exibir Vencedores','amarelo'))
        print(cor_texto('0. Sair','amarelo'))
        opcao = str(input(cor_texto('Escolha uma opção: ','azul')))

        if opcao == '1':
            mostrar_jogos()
        elif opcao == '2':
            cadastrar_alunos()
        elif opcao == '3':
            consultar_cadastros()
        elif opcao == '4':
            buscar_por_nome()
        elif opcao == '5':
            buscar_jogo()
        elif opcao == '6':
            registro_vencedores()
        elif opcao == '7':
            exibir_vencedores()
        elif opcao == '0':
            print(cor_texto('Encerrando o sistema. Até logo!','vermelho'))
            break
        else:
            print(cor_texto('Opção inválida. Tente novamente.','vermelho'))




exibir_menu()
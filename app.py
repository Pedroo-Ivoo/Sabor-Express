import os

restaurantes = [
    {'nome':'Pizzaria do Mario', 'categoria': 'Pizza', 'ativo':False},
    {'nome':'Coxinha Feliz', 'categoria': 'Salgadinho', 'ativo':True},
    {'nome':'Casa do Kame', 'categoria': 'Oriental', 'ativo': False}
]


def exibir_nome_do_programa():
    '''Essa função é responsável por mostrar o nome do programa.'''
    print('𝘚𝘢𝘣𝘰𝘳 𝘌𝘹𝘱𝘳𝘦𝘴𝘴\n')

def exibir_menu():
    '''Essa função exibe as opções disponiveis para o usuário do programa'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função quando chamada encerra o programa.'''
    os.system('cls') # essa função limpa a tela do comando
    print('Finalizando o app\n')

def voltar_ao_menu():
    '''Essa função é responsável por retornar ao menu principal'''
    input('\nDigite qualquer tecla para voltar para o menu principal:')
    main()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtitulo da tela quando acessada pelo usuário'''
    os.system('cls')
    linha = '\n' + '*' * (len(texto))+'\n'
    print(linha)
    print(texto)
    print(linha)
    print()
    
def exibir_informacoes(texto):
    '''Essa função foi projetada para que quando chamada exiba um texto com informações e orientações do uso da opção.'''
    print(texto)
    print()
    
def cadastrar_novo_restaurante():
    '''Essa função cadastra novos restaurantes no programa'''
    
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    exibir_informacoes("Ao cadastrar o restaurante deve escrever o nome dele e após será pedido a sua categoria.\n")
    
    nome_do_restaurante = input('Digite o Nome e a categoria do Restaurante que deseja cadastrar: ').title()
        
    if nome_do_restaurante.strip() == "":
        print('Não foi possivel cadastrar restaurante que não tenha nenhum caracter. Espaço em branco também não é permitido. Tente novamente!')
        voltar_ao_menu()
    else:
        categoria = input(f'\nDigite o nome da categoria do Restaurante {nome_do_restaurante}: ').title()
        dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
        restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
        def opcoes_de_cadastro():
            '''Essa função pergunta ao usuário se quer continuar cadastrando novos restaurantes ou não'''
            
            continuar = int(input('Quer continuar cadastrando mais restaurante?\n 1 = Para continuar\n 2 = Para sair\n Opção:'))
            if continuar not in range(1,3):
                raise ValueError
            if continuar == 1:
                cadastrar_novo_restaurante()
            else:
                main()    
        try:
            opcoes_de_cadastro()
            
        except (ValueError):
            print('Opção inválida! Escolha novamente.')
            input('Precione qualquer tecla para continuar')
            os.system('cls')
            opcoes_de_cadastro()
        
def exibir_restaurantes():
    '''Essa função exibe os nomes dos resturantes cadastrados'''
    exibir_subtitulo('Todos os restaurantes cadastrados: ')
    exibir_informacoes("Nesta tela é apresentado todos os Restaurantes cadastrados no sistema com a suas informações.")
    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') 
    voltar_ao_menu()

def alternar_estado_do_restaurante():
    '''Essa função permite alterar o estado do restaurante para ativado ou desativado'''
    exibir_subtitulo('Alternando estado do Restaurante')
    exibir_informacoes("Para alterar o status do Restaurante o nome deve estar correte. Caso digite errado não será possível a ativar ou desativar")
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja alterar o estado: ').title()
    if nome_do_restaurante.strip() == "":
        print('Erro! Informe o Nome do restaurante. "Espaço em branco" ou "Enter" não são dados aceitos.')
        voltar_ao_menu()
    else:
        restaurante_encontrado = False
        
        for restaurante in restaurantes:
            if nome_do_restaurante == restaurante['nome']:
                restaurante_encontrado = True
                restaurante["ativo"] = not restaurante['ativo']
                mensagem = f'O Restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O Restaurante {nome_do_restaurante} foi desativado com sucesso!'
                print(mensagem)
        if not restaurante_encontrado:
            print(f'O resturante {nome_do_restaurante} não foi encontrado')
            
        voltar_ao_menu() 
         
def escolher_opcoes():
    '''Essa função é do menu principal em que o usuário pode escolher as opções'''    
    try:
        opcao_escolhida = int(input('Digite: '))
        if opcao_escolhida not in range(1, 5): #verifica se o valor digitado está de acordo com as opções
            raise ValueError
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                exibir_restaurantes()
            case 3:
                alternar_estado_do_restaurante()
            case 4:
                exibir_subtitulo("Finalizar app")
                
    except (ValueError) : #caso o valor digitado não seja um número valido ele caira no except
        print('Opção inválida!\n')
        voltar_ao_menu()

    
        
            
    
def main():
    '''Essa função quando chamada mostra tela principal do nosso sistema.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcoes()
    
    

if __name__ == '__main__':
    main()
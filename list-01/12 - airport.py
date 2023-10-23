# Questão 12 - Programa para simular controlador de voos:
# Listar o número de aviões esperando para decolar;
# Autorizar a decolagem do primeiro avião na fila;
# Adicionar um avião na fila de espera;
# Listar todos os aviões que estão na lista de espera;
# Listar as características do primeiro avião da fila;
# Cada avião possui um nome, um identificador, uma origem e um destino.

# Definindo a classe Avião
class Aviao:
    def __init__(self, nome, identificador, origem, destino):
        self.nome = nome
        self.identificador = identificador
        self.origem = origem
        self.destino = destino

# Definindo a classe Aeroporto
class Aeroporto:
    def __init__(self):
        self.fila_de_espera = []

    # Método para adicionar aviões
    def adicionar_aviao(self, aviao):
        # Verifica se o identificador já está em uso
        for aviao_na_fila in self.fila_de_espera:
            if aviao_na_fila.identificador == aviao.identificador:
                print('Erro: O identificador {} já está em uso. Por favor, escolha outro identificador.'.format(aviao.identificador))
                return
        
        # Adiciona o avião na fila de espera se o identificador não estiver em uso
        self.fila_de_espera.append(aviao)
        print('Avião {} adicionado à fila de espera.'.format(aviao.nome))

    # Método para criar a lista de espera
    def lista_de_espera(self):
        print('\nAviões na fila de espera: ')
        for aviao in self.fila_de_espera:
            print('Nome: {}, Identificador: {}'.format(aviao.nome,aviao.identificador))

    # Método para caracterizar os aviões
    def primeiro_aviao(self):
        if self.fila_de_espera:
            aviao = self.fila_de_espera[0]
            print('Nome: {}'.format(aviao.nome))
            print('Identificador: {}'.format(aviao.identificador))
            print('Origem: {}'.format(aviao.origem))
            print('Destino: {}'.format(aviao.destino))
        else:
            print('Não há aviões na fila de espera.')

    # Método para autorizar decolagem
    def autorizar_decolagem(self):
        if self.fila_de_espera:
            aviao = self.fila_de_espera.pop(0)
            print('Autorizando decolagem do avião {}.'.format(aviao.nome))
        else:
            print("Não há aviões na fila de espera.")

aeroporto = Aeroporto()

# Mostrando as opções
while True:
    print('\nEscolha uma opção: ')
    print('1 - Adicionar avião na fila de espera')
    print('2 - Listar aviões na fila de espera')
    print('3 - Listar número de aviões esperando para decolar')
    print('4 - Listar características do primeiro avião na fila')  
    print('5 - Autorizar decolagem do primeiro avião na fila')
    print('6 - Sair')
    
    # Recebendo a opção do usuário
    opcao = int(input('\nDigite a opção desejada: '))

    if opcao == 1:
        nome = str(input('Nome do avião: '))
        identificador = input('Identificador do avião: ')
        origem = str(input('Origem do avião: '))
        destino = str(input('Destino do avião: '))
        aviao = Aviao(nome, identificador, origem, destino)
        aeroporto.adicionar_aviao(aviao)
    elif opcao == 2:
        aeroporto.lista_de_espera()
    elif opcao == 3:    
        print('\nNúmero de aviões esperando para decolar: {}'.format(len(aeroporto.fila_de_espera)))
    elif opcao == 4:
        aeroporto.primeiro_aviao()
    elif opcao == 5:
        aeroporto.autorizar_decolagem()
    elif opcao == 6:
        print('\nFim do programa. Boa viagem!')
        break
    else:
        print('\nOpção inválida. Tente novamente.')
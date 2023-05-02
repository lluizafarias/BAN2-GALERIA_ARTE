## Alunos: LUIZA E OTÁVIO

import psycopg2
from tabulate import tabulate

###         Conexão Banco           ###
dbname='database_galeria_arte'    # Nome Banco
user='postgres'             # Usuário
password='1234'             # Senha
conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
cursor = conn.cursor()
###         ###         ###

###         Menus           ###
def menu():
    print('\n')
    print("|| Olá! Bem-vindo a galeria de arte ||")
    print('\n')
    print("Escolha uma opção para começar:")
    print('\n')
    print("1 - Consultar Dados")
    print("2 - Cadastrar Dados")
    print("3 - Excluir Dados")
    print("4 - Atualizar Dados")
    print("5 - Relatórios")
    print("0 - Sair")
    print('\n')

def menuTabela():    
    print('\n')
    print("Agora, escolha uma tabela para realizar a ação:")
    print('\n')
    print("1 - Artistas")
    print("2 - Obras")
    print("3 - Clientes")
    print("4 - Ordens")
    print("5 - Pagamentos")    
    print("6 - Exibições")
    print("0 - Voltar")
    print('\n')

def menuRelatorios():
    print('\n')
    print("Aqui estão alguns relatórios!")
    print('\n')
    print("Escolha o relatório que deseja acessar:")
    print('\n')
    print("1 - Compras por Cliente")
    print("2 - Exibição de Obras")
    print("3 - Obras por Artista")
    print("0 - Voltar")
    print('\n')
###         ###         ###


menu()
print('\n')
opcao = int(input("Escreva aqui sua opção: "))
print('\n')

while opcao != 0:
    if opcao == 1:
        print("Opção 1 - Consultar Dados")
        menuTabela()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                cursor.execute('SELECT * FROM ARTISTA')
                query   = cursor.fetchall()
                header  = ['Nome Artista', 'ID Artista', 'E-mail', 'País']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                cursor.execute('SELECT * FROM OBRA')
                query   = cursor.fetchall()
                header  = ['Nome Obra', 'ID Obra', 'Nome Artista', 'ID Artista', 'Tipo de Arte', 'Data Criação', 'Preço']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                cursor.execute('SELECT * FROM CLIENTE')
                query   = cursor.fetchall()
                header  = ['ID Cliente', 'Nome Cliente', 'Telefone', 'Preferência Arte', 'Endereço', 'País']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                cursor.execute('SELECT * FROM ORDENS')
                query   = cursor.fetchall()
                header  = ['ID Obra', 'ID Cliente', 'Data Ordem', 'Data Envio']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                cursor.execute('SELECT * FROM PAGAMENTO')
                query   = cursor.fetchall()
                header  = ['ID Obra', 'ID Cliente', 'Valor Obra']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                cursor.execute('SELECT * FROM EXIBICAO')
                query   = cursor.fetchall()
                header  = ['ID Obra', 'Local Exibição', 'Data Exibição']
                print(tabulate(query, headers=header))
            else:
                print("Opção invalida!")
            
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 2:
        print("Opção 2 - Cadastrar Dados")
        menuTabela()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                print('Exemplo:Leonerdo Da Vinci, 1, no emailid, Italy')                
                print('\n')
                nome_artista        = input("Nome Artista: ")
                id_artista          = input("ID Artista: ")
                email               = input("E-mail: ")
                pais                = input("País: ")
                cursor.execute("INSERT INTO ARTISTA (nome_artista, id_artista, email, pais) VALUES (%s, %s, %s, %s);", (nome_artista, id_artista, email, pais))
                conn.commit()
            elif opcaoExibir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                print('Exemplo:The Mona Lisa, mona002, Leonerdo Da Vinci, 1, Portrait, 10-jan-1517, 200000')                
                print('\n')
                nome_obra           = input("Nome Obra: ")
                id_obra             = input("ID Obra: ")
                nome_artista        = input("Nome Artista: ")
                id_artista          = input("ID Artista: ")
                tipo_arte           = input("Tipo Arte: ")
                data_criacao        = input("Data Criação: ")
                preco               = int(input("Preço: "))
                cursor.execute("INSERT INTO OBRA (nome_obra, id_obra, nome_artista, id_artista, tipo_arte, data_criacao, preco) VALUES (%s, %s, %s, %s, %s, %s, %s);", (nome_obra, id_obra, nome_artista, id_artista, tipo_arte, data_criacao, preco))
                conn.commit()
            elif opcaoExibir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                print('Exemplo:C01, Mr.Arif Hossain, 01724777840, Abstract, Gulshan 1, Bangladesh')                
                print('\n')
                id_cliente          = input("ID Cliente: ")
                cliente_nome        = input("Nome Cliente: ")
                telefone            = int(input("Telefone: "))
                preferencia_arte    = input("Preferência Arte: ")
                cliente_endereco    = input("Endereço: ")
                cliente_pais        = input("País: ")
                cursor.execute("INSERT INTO CLIENTE (id_cliente, cliente_nome, telefone, preferencia_arte, cliente_endereco, cliente_pais) VALUES (%s, %s, %s, %s, %s, %s);", (id_cliente, cliente_nome, telefone, preferencia_arte, cliente_endereco, cliente_pais))
                conn.commit()
            elif opcaoExibir == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                print('Exemplo:mona002, C01, 28-August-2021, 01-September-2021')                
                print('\n')
                id_obra             = input("ID Obra: ")
                id_cliente          = input("ID Cliente: ")
                data_ordem          = input("Data Ordem: ")
                data_envio          = input("Data Envio: ")
                cursor.execute("INSERT INTO ORDENS (id_obra, id_cliente, data_ordem, data_envio) VALUES (%s, %s, %s, %s);", (id_obra, id_cliente, data_ordem, data_envio))
                conn.commit()
            elif opcaoExibir == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                print('Exemplo:mona002, C01, 200000')                
                print('\n')
                id_obra             = input("ID Obra: ")
                id_cliente          = input("ID Cliente: ")
                valor               = int(input("Valor: "))
                cursor.execute("INSERT INTO PAGAMENTO (id_obra, id_cliente, valor) VALUES (%s, %s, %s);", (id_obra, id_cliente, valor))
                conn.commit()
            elif opcaoExibir == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                print('Exemplo: mona002, Gulshan Audetorium, 28-August-2021')                
                print('\n')
                id_obra             = input("ID Obra: ")
                local_exibicao      = input("Local Exibição: ")
                data_exibicao       = input("Data Exibição: ")
                cursor.execute("INSERT INTO EXIBICAO (id_obra, local_exibicao, data_exibicao) VALUES (%s, %s, %s);", (id_obra, local_exibicao, data_exibicao))
                conn.commit()
            else:
                print("Opção invalida!")
            
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 3:
        print("Opção 3 - Excluir Dados")
        menuTabela()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n') 
                chave = input("Digite ID do Artista a ser excluído: ")
                cursor.execute("DELETE FROM ARTISTA WHERE ID_ARTISTA=%s", (chave,))
                conn.commit()                        
            elif opcaoExibir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')    
                chave = input("Digite ID da Obra a ser excluída: ")
                cursor.execute("DELETE FROM OBRA WHERE ID_OBRA=%s", (chave,))
                conn.commit()
            elif opcaoExibir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')       
                chave = input("Digite ID do Cliente a ser excluído: ")
                cursor.execute("DELETE FROM CLIENTE WHERE ID_CLIENTE=%s", (chave,))
                conn.commit()
            elif opcaoExibir == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')      
                chave = input("Digite ID da Obra a ser excluída: ")
                cursor.execute("DELETE FROM ORDENS WHERE ID_OBRA=%s", (chave,))
                conn.commit()               
            elif opcaoExibir == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')      
                chave = input("Digite ID da Obra a ser excluída: ")
                cursor.execute("DELETE FROM PAGAMENTO WHERE ID_OBRA=%s", (chave,))
                conn.commit()                  
            elif opcaoExibir == 5:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')      
                chave = input("Digite ID da Obra a ser excluída: ")
                cursor.execute("DELETE FROM EXIBICAO WHERE ID_OBRA=%s", (chave,))
                conn.commit()       
            else:
                print("Opção invalida!")
            
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 4:
        print("Opção 4 - Atualizar Dados")
        menuTabela()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:   
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                print('Exemplo:Leonerdo Da Vinci, no emailid, Italy')                
                print('\n')           
                chave = int(input("Digite o ID do Artista a ser atualizado: "))
                nome_artista        = input("Nome Artista: ")
                email               = input("E-mail: ")
                pais                = input("País: ")
                cursor.execute("UPDATE ARTISTA SET nome_artista = %s, email = %s, pais = %s WHERE id_artista = %s", (nome_artista, email, pais, chave))
                conn.commit()                        
            elif opcaoExibir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                print('Exemplo:The Mona Lisa, Leonerdo Da Vinci, 1, Portrait, 10-jan-1517, 200000')                
                print('\n')
                chave = int(input("Digite o ID da Obra a ser Atualizada: "))
                nome_obra           = input("Nome Obra: ")
                nome_artista        = input("Nome Artista: ")
                id_artista          = input("ID Artista: ")
                tipo_arte           = input("Tipo Arte: ")
                data_criacao        = input("Data Criação: ")
                preco               = int(input("Preço: "))
                cursor.execute("UPDATE OBRA SET nome_obra = %s, nome_artista = %s, id_artista = %s, tipo_arte = %s, data_criacao = %s, preco = %s WHERE id_obra = %s", (nome_obra, nome_artista, id_artista, tipo_arte, data_criacao, preco, chave))
                conn.commit()
            elif opcaoExibir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                print('Exemplo: Mr.Arif Hossain, 01724777840, Abstract, Gulshan 1, Bangladesh')                
                print('\n')
                chave = int(input("Digite o ID do Cliente a ser atualizado: "))
                cliente_nome        = input("Nome Cliente: ")
                telefone            = input("Telefone: ")
                preferencia_arte    = input("Preferência Arte: ")
                cliente_endereco    = input("Endereço: ")
                cliente_pais        = input("País: ")
                cursor.execute("UPDATE CLIENTE SET cliente_nome = %s, telefone = %s, preferencia_arte = %s, cliente_endereco = %s, cliente_pais = %s WHERE id_cliente = %s", (cliente_nome, telefone, preferencia_arte, cliente_endereco, cliente_pais, chave))
                conn.commit()
            elif opcaoExibir == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                print('Exemplo: C01, 28-August-2021, 01-September-2021')                
                print('\n')
                chave = int(input("Digite o ID da Obra a ser atualizada: "))
                id_cliente          = input("ID Cliente: ")
                data_ordem          = input("Data Ordem: ")
                data_envio          = input("Data Envio: ")
                cursor.execute("UPDATE ORDENS SET id_cliente = %s, data_ordem = %s, data_envio = %s WHERE id_obra = %s", (id_cliente, data_ordem, data_envio, chave))
                conn.commit()               
            elif opcaoExibir == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                print('Exemplo: C01, 200000')                
                print('\n')
                chave = int(input("Digite o ID da Obra a ser atualizada: "))
                id_cliente          = input("ID Cliente: ")
                valor               = int(input("Valor: "))
                cursor.execute("UPDATE PAGAMENTO SET id_cliente = %s, valor = %s WHERE id_obra = %s", (id_cliente, valor, chave))
                conn.commit()
            elif opcaoExibir == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                print('Exemplo: Gulshan Audetorium, 28-August-2021')                
                print('\n')
                chave = int(input("Digite o ID da Obra a ser atualizada: "))
                local_exibicao      = input("Local Exibição: ")
                data_exibicao       = input("Data Exibição: ")
                cursor.execute("UPDATE EXIBICAO SET local_exibicao = %s, data_exibicao = %s WHERE id_obra = %s", (local_exibicao, data_exibicao, chave))
                conn.commit()
            else:
                    print("Opção invalida!")
                
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 5:
        print("Opção 5 - Relatórios")
        menuRelatorios()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                print('\n')
                print('Compras por Cliente!')                
                print('\n')
                chave = input("Digite o ID do Cliente a ser pesquisado: ")
                cursor.execute('SELECT 	C.CLIENTE_NOME, OB.NOME_OBRA, P.VALOR, O.DATA_ORDEM FROM CLIENTE AS C INNER JOIN ORDENS AS O ON C.ID_CLIENTE = O.ID_CLIENTE INNER JOIN OBRA AS OB ON O.ID_OBRA = OB.ID_OBRA INNER JOIN PAGAMENTO AS P ON O.ID_OBRA = P.ID_OBRA WHERE C.ID_CLIENTE =  = %s',(chave,))
                query = cursor.fetchall()
                header = ['Nome Cliente', 'Nome Obra', 'Valor']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 2:
                print('\n')
                print('Exibição de Obras!')                
                print('\n')
                chave = input("Digite o ID da Obra a ser pesquisada: ")
                cursor.execute('SELECT O.NOME_OBRA, A.NOME_ARTISTA, A.PAIS, E.LOCAL_EXIBICAO, E.DATA_EXIBICAO FROM OBRA AS O INNER JOIN EXIBICAO AS E ON O.ID_OBRA = E.ID_OBRA INNER JOIN ARTISTA AS A ON O.ID_ARTISTA = A.ID_ARTISTA WHERE O.ID_OBRA =  %s',(chave,))
                query = cursor.fetchall()
                header = ['Nome Obra', 'Nome Artista', 'País', 'Local Exibição', 'Data Exibição']
                print(tabulate(query, headers=header))                
            elif opcaoExibir == 3:
                print('\n')
                print('Obras por Artista!')                
                print('\n')
                cursor.execute('SELECT A.NOME_ARTISTA, A.PAIS, O.NOME_OBRA, O.TIPO_ARTE, O.DATA_CRIACAO FROM ARTISTA AS A INNER JOIN OBRA AS O ON A.ID_ARTISTA = O.ID_ARTISTA')
                query = cursor.fetchall()
                header = ['Nome Artista', 'País', 'Nome Obra', 'Tipo Arte', 'Data Criação']
                print(tabulate(query, headers=header))
            else:
                print("Opção invalida!")            
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: ")) 


    menu()    
    print('\n')
    opcao = int(input("Escreva aqui sua opção: "))
    print('\n')

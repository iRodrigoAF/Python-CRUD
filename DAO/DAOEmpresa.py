from Model.Empresa import Empresa
from conexao import Conexao

class DAOEmpresa:
    def __init__(self):
        print("in init")

    def adicionarEmpresa(self):

        try:
            razaoSocial = input('RazãoSocial:')
            endereco = input('Endereço:')
            novaEmpresa = Empresa(razaoSocial, endereco)
            # Adiciona Banco
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            query = "INSERT INTO empresa(razao_social, endereco) VALUES(%s,%s)"
            dados = novaEmpresa.getRazaoSocial(), novaEmpresa.getEndereco()
            cursor.execute(query, dados)
            con.commit()

        except TypeError as error:
            print("Failed to delete record from table: {}".format(error))

        finally:
            cursor.close()
            con.close()
            print("MySQL connection is closed")


    def listaEmpresas(self):

        try:
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            query = "select * from empresa"
            cursor.execute(query)
            # get all records
            records = cursor.fetchall()

            print("\n Mostra dados")
            for row in records:
                print("Id = ", row[0], )
                print("Nome = ", row[1])
                print("Endereco  = ", row[2])

        except TypeError as error:
            print("Failed to delete record from table: {}".format(error))

        finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")

    def deletaEmpresa(self):
        try:
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            nomeEmpresa = input('Nome da Empresa:')
            query = "DELETE from empresa WHERE razao_social = %s"
            cursor.execute(query, (nomeEmpresa))
            con.commit()
        except TypeError as error:
            print("Failed to delete record from table: {}".format(error))

        finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")

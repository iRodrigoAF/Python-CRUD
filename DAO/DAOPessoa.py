from Model.Pessoa import Pessoa
from conexao import Conexao

class DAOPessoa:
    def __init__(self):
        print("in init")

    def adicionarPessoa(self):

        nome = input('Nome:')
        endereco = input('Endereço:')
        bairro = input('Bairro:')
        cep = input('CEP:')
        cidade = input('Cidade:')
        estado = input('Estado:')

        cadastrarFuncionarioEmpresa = input('Deseja vincular esse funcionario a empresa?')
        if(cadastrarFuncionarioEmpresa == "S"):

            id_empresa = input('Digite o id da empresa ')
            novaPessoa = Pessoa(nome, endereco, bairro, cep, cidade, estado, id_empresa)

        #Adiciona Banco
        con = Conexao.getConnection('Estalecendo Conexao')
        cursor = con.cursor()
        query = "INSERT INTO pessoa(nome, endereco, bairro, cep, cidade, estado, id_empresa) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        dados = novaPessoa.getNome(), novaPessoa.getEndereco(), novaPessoa.getBairro(), novaPessoa.getCEP(), novaPessoa.getCidade(), novaPessoa.getEstado(), novaPessoa.getIdEmpresa()
        cursor.execute(query, dados)
        con.commit()

    def listaPessoas(self):
            try:
                con = Conexao.getConnection('Estalecendo Conexao')
                cursor = con.cursor()
                query = "select * from pessoa"
                cursor.execute(query)
                # get all records
                records = cursor.fetchall()

                print("\n Mostra dados")
                for row in records:
                    print("Id = ", row[0], )
                    print("Nome = ", row[1])
                    print("Endereco  = ", row[3])
                    print("Bairro = ", row[4], )
                    print("Cep = ", row[5])
                    print("Cidade  = ", row[6])
                    print("Estado = ", row[7])

            except TypeError as error:
                print("Failed to delete record from table: {}".format(error))

            finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")

    def deletaPessoa(self):
            try:
                con = Conexao.getConnection('Estalecendo Conexao')
                cursor = con.cursor()
                nomePessoa = input('Nome da Empresa:')
                query = "DELETE from pessoa WHERE nome = %s"
                cursor.execute(query, (nomePessoa))
                con.commit()
            except TypeError as error:
                print("Failed to delete record from table: {}".format(error))

            finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")

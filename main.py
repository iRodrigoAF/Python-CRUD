from DAO.DAOPessoa import DAOPessoa
from DAO.DAOEmpresa import DAOEmpresa


def menu():
    while True:
        opcao = input('1 - Adicionar /  2 - Remover  / 3 - Lista Empresas e Funcionários')
        if (opcao == "1"):
            opcao = input('1 - Adicionar Funcionário 2 - Adicionar Empresas')
            if (opcao == "1"):
                daoPessoa = DAOPessoa
                daoPessoa.adicionarPessoa('teste')
            elif(opcao == "2"):
                daoEmpresa = DAOEmpresa
                daoEmpresa.adicionarEmpresa('teste')
        elif (opcao == "2"):
            opcao = input('1 - Remover Funcionário 2 - Remover Empresas')
            if (opcao == "1"):
                daoPessoa = DAOPessoa
                daoPessoa.deletaPessoa('teste')
            elif (opcao == "2"):
                daoEmpresa = DAOEmpresa
                daoEmpresa.deletaEmpresa('teste')
        elif (opcao == "3"):
            opcao = input('1 - Lista Funcionários 2 - Lista Empresas')
            if (opcao == "1"):
                daoPessoa = DAOPessoa
                daoPessoa.listaPessoas('teste')
            elif (opcao == "2"):
                daoEmpresa = DAOEmpresa
                daoEmpresa.listaEmpresas('teste')

if __name__ == '__main__':
    menu()

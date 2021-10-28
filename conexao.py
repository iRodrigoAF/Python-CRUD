import pymysql
class Conexao:
    def __init__(self):
        print("in init")
    def getConnection(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='empresa')

        return con;

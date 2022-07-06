
import pyodbc 

dados_conexao = (
"Driver={SQL Server};"
"Server=DESKTOP-8I8BEK2;"
"Database=Ubuntuwhatsdatabase;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")
cursor = conexao.cursor()

id = input(" Digite seu ID")
nome = input(" Digite seu nome")
numero = input(" Digite seu numero")
polo = input(" Digite seu polo")
turma = input(" Digite sua turma")

comando = f"""insert into aluno (id, nome, numero, polo, turma) values ({id}, '{nome}', '{numero}', '{polo}', '{turma}');"""
cursor.execute(comando)
cursor.commit()


print(id)

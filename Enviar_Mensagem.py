import time
from selenium import webdriver
import pyodbc
import webbrowser 

dados_conexao = (
"Driver={SQL Server};"
"Server=DESKTOP-8I8BEK2;"
"Database=Ubuntuwhatsdatabase;"
)

class WhatsappBot():
    def __init__(self):

     conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")
 
conexao = pyodbc.connect(dados_conexao)
comando = "select * from aluno;"
cursor = conexao.cursor()
cursor.execute(comando)
linhas = cursor.fetchall()
print("Número total de registros retornados: ", cursor.rowcount)

for linha in linhas:

        print("id:", linha[0])
        print("nome:", linha[1])
        print("numero:", linha[2])
        print("polo:", linha[3])
        print("turma:", linha[4],"\n")    

webbrowser.open('https://web.whatsapp.com/send?phone=' + linha[2] + '&text&app_absent=0')        
       
time.sleep(25)
mesagem = "Olá ", linha[1], "essa mensagem é automatizada"      
driver = webdriver.Edge()      
chat_box = driver.find_element_by_class_name('p3_M1')
chat_box.send_keys(mesagem)
botao_enviar = driver.find_element_by_xpath("//span[@data-icon='send']")
time.sleep(3)
botao_enviar.click()
time.sleep(5)

cursor.execute(comando)
cursor.commit()





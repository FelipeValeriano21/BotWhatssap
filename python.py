import pyodbc 
from selenium import webdriver
import time
import array as arr 
dados_conexao = (
"Driver={SQL Server};"
"Server=DESKTOP-8I8BEK2;"
"Database=Ubuntuwhatsdatabase;"
)

def EnviarMensagens(self):
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

cursor.execute(comando)
cursor.commit()


class WhatsappBot:
    def __init__(self):
      
        # Parte 1 - A mensagem que você quer enviar
       
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        
       
        for linha in linhas:

         self.driver.get('https://web.whatsapp.com/send?phone=' + linha[2] + '&text&app_absent=0')
         self.mensagem = "Fala *", linha[1],"* do polo *", linha[3],"* e turma *",linha[4], "*. Estamos passando para avisar que você receberá recados do cursinho por um whatssap automatizado " 
         print (self.mensagem)
         print('https://web.whatsapp.com/send?phone=' + linha[2] + '&text&app_absent=0')
         time.sleep(25)
         chat_box = self.driver.find_element_by_class_name('p3_M1')
         chat_box.click()
         chat_box.send_keys(self.mensagem)
         botao_enviar = self.driver.find_element_by_xpath(
         "//span[@data-icon='send']")
         time.sleep(3)
         botao_enviar.click()
         time.sleep(5)



  
      
bot = WhatsappBot()
bot.EnviarMensagens()




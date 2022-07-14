import csv 
from selenium import webdriver
import time

with open ('alunos.csv', mode = 'r') as arq:
   leitor = csv.reader(arq, delimiter=',')
   linhas = 0 

   for coluna in leitor: 
     if linhas == 0: 
       print(f'colunas: {" ".join(coluna)}')
       linhas+= 1
     else: 
        print(f'\taluno {coluna[0]} tem o numero {coluna[1]}.')
        linhas += 1

class WhatsappBot:
    def __init__(self):
      
        # Parte 1 - A mensagem que você quer enviar
       
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
  
    def EnviarMensagens(self):

      with open ('alunos.csv', mode = 'r') as arq:
        leitor = csv.reader(arq, delimiter=',')
        linhas = 0
        for coluna in leitor:    
       
           self.mensagem = "Boa tarde *", str(coluna[0]), "*. Essa mensagem automatizada com importação csv" 
           print (self.mensagem)
           print(coluna[1])
           self.driver.get('https://web.whatsapp.com/send?phone=' + coluna[1]+ '&text&app_absent=0')
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

# -*- coding: cp1252 -*-
import os;
from veiculo import veiculo;
#import MySQLdb
from pessoa import pessoa
#from pymongo import Connection
from pymongo import MongoClient
conn = MongoClient('localhost', 27017) # or cliente = MongoClient('mongodb://localhost:27017/')
db = conn.RoubaramMeuVeiculo
collection = db.veiculo



"""
from jython import JFrame,import JOptionPane
from javax.swing import JFrame, JMenuBar, JMenu, JMenuItem, JTextField
from java.awt import BorderLayout
from javax.swing import JOptionPane
"""

os.system('cls||clear');
os.system("cat /etc/issue | cut -d' ' -f1,2");
print "Bem Vindos ao RobaramMeuVeículo!.\nAqui vc poderá ajudar a recuperar seu vecíulo roubado com alguns simples clicks.";
veic=veiculo()
p1=pessoa()

  
def inserirDados(veic,p1):
  db.veiculo.insert({"tipo":veic.tipo,"nome":veic.nome,"placa":veic.placa,"cor":veic.cor})
  db.pessoa.insert({"nome":p1.nome,"email":p1.email,"telefone":p1.tel})
    
def limpar():
  os.system('cls||clear');
  ##revisar alguns conceitos
def notificarUsuario():
  print "enviando informações para o proprietário...\n"
  print "nome"+p1.nome+"\nemail:"+p1.email+"\ntel:"+p1.tel
  
def cadastrar():
  veic.tipo=raw_input("tipo do veículo:|carro|moto:\n")
  limpar()
  if veic.tipo=="carro":
    veic.marca=raw_input("marca do "+veic.tipo+":\n")
    limpar()
    veic.nome=raw_input("Nome do "+veic.tipo+":\n")
    limpar()
    veic.placa=raw_input("Placa do "+veic.tipo+":\n")
    limpar()
    veic.cor=raw_input("Cor do "+veic.tipo+":\n")
    limpar()
    p1.nome=raw_input("Nome do dono do veiculo:\n")
    limpar()
    p1.email=raw_input("email para contato:\n")
    limpar()
    p1.tel=raw_input("telefone ou whatsapp para contato:\n")
    inserirDados(veic,p1)
    limpar()
    print "Cadastrado com sucesso!"
  else:
    veic.marca=raw_input("marca da "+veic.tipo+":\n")
    limpar()
    veic.nome=raw_input("Marca da "+veic.tipo+":\n")
    limpar()
    veic.placa=raw_input("Placa da "+veic.tipo+":\n")
    limpar()
    veic.cor=raw_input("Cor da "+veic.tipo+":\n")
    p1.nome=raw_input("Nome do dono do veiculo:\n")
    inserirDados(veic,p1)
    print "Cadastrado com sucesso!"
    limpar()
    
    
def imprimir():
    '''
    print 'veiculo do tipo:'+veic.tipo
    print veic.tipo + ' da marca:'+veic.marca,veic.nome
    print 'placa:'+veic.placa
    print 'cor:'+veic.cor
    print 'Proprietario do veiculo:'+p1.nome
    '''
    print db.veiculo.count(),"valores na colação(tabela) 'veiculo'\n"
    print db.veiculo.find_one();
    print "\n\n"
    print db.pessoa.count(),"valores na colação(tabela) 'pessoa'\n"
    print db.pessoa.find_one()
    
def consulta():
  cc=raw_input("placa a ser consultada:") 
  if(db.veiculo.count({"placa":cc})>0):
    #veic.veicu()
    print "Veiculo encontrado:",db.veiculo.find_one({"placa":cc})   
  else:
   print "Nenhum carro encontrado com essa descrição"
print" @@@@@@@@@@@@@@@@@";
print"@                 @";
print"@  1-cadastrar    @";
print"@  2-consultar    @";
print"@                 @";
print" @@@@@@@@@@@@@@@@@";
opt=raw_input();
if opt == '1':
    limpar() 
    cadastrar()
     
elif opt=='2':
    limpar()
    consulta()
elif opt=='5':
    limpar()
    imprimir()
else:
    print "\nbad\n"#consultar no banco mongo
    print "carro encontrado"+db.veiculo.find_one()
  
  
  
  
  
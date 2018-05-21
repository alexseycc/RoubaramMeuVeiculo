# -*- coding: cp1252 -*-
import os;
from veiculo import veiculo;
from pessoa import pessoa
"""
from jython import JFrame,import JOptionPane
from javax.swing import JFrame, JMenuBar, JMenu, JMenuItem, JTextField
from java.awt import BorderLayout
from javax.swing import JOptionPane
"""

os.system('cls||clear');
os.system("cat /etc/issue | cut -d' ' -f1,2");
print "Bem Vindos ao RobaramMeuVeículo!.\nAqui vc poderá ajudar a recuperar seu vecíulo roubado com alguns simples clicks.";
#veic=veiculo('carro','honda','civic','als-0212','azul')
veic=veiculo()
p1=pessoa()

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
    veic.nome=raw_input("nome do "+veic.tipo+":\n")
    limpar()
    veic.placa=raw_input("placa do "+veic.tipo+":\n")
    limpar()
    veic.cor=raw_input("cor do "+veic.tipo+":\n")
    limpar()
    p1.nome=raw_input("nome do dono do veiculo:\n")
    limpar()
  else:
    veic.marca=raw_input("marca da "+veic.tipo+":\n")
    limpar()
    veic.nome=raw_input("marca da "+veic.tipo+":\n")
    limpar()
    veic.placa=raw_input("placa da "+veic.tipo+":\n")
    limpar()
    veic.cor=raw_input("cor da "+veic.tipo+":\n")
    p1.nome=raw_input("nome do dono do veiculo:\n")
    limpar()
  
  #veic.dono=raw_input("haha")
  #veic.contato=raw_input("haha")

def imprimir():
  print 'veiculo do tipo:'+veic.tipo
  print veic.tipo + ' da marca:'+veic.marca,veic.nome
  print 'placa:'+veic.placa
  print 'cor:'+veic.cor
  print 'Proprietario do veiculo:'+p1.nome
  
print" @@@@@@@@@@@@@@@@@";
print"@                 @";
print"@  1-cadastrar    @";
print"@  2-consultar    @";
print"@                 @";
print" @@@@@@@@@@@@@@@@@";
#print veic.cor,veic.marca;
opt=raw_input();
if opt == '1':
    limpar() 
    cadastrar()
     
elif opt=='2':
    limpar()
    imprimir()

else:
    print "\nbad\n"#consultar no banco mongo
    

    
  
  
  
  
  
  
  
  
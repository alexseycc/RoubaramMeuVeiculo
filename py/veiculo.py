class veiculo:
  tipo="";
  placa="";
  cor="";
  marca="";
  nome="";

  
  
   

  def __init__(self,tipo,marca,nome,placa,cor):
    self.tipo=tipo
    self.marca=marca
    self.nome=nome
    self.placa=placa
    self.cor=cor
  
  
  def veiculo(self,tipo,marca,nome,placa,cor):
    self.tipo=tipo
    self.marca=marca
    self.nome=nome
    self.placa=placa
    self.cor=cor
    
  def setTipo(self,tipo):
    self.tipo
    
  def getTipo(self):
    return self.tipo
  
  def setMarca(self,marca):
    self.marca=marca
    
  def getMarca(self):
    return self.marca
  
  def setNome(self,nome):
    self.nome=nome
    
  def getNome(self):
    return self.nome
  
  def setPlaca(self,placa):
    self.placa=placa
    
  def getPlaca(self):
    return self.placa
  
  def setCor(self,cor):
    self.cor=cor
    
  def getCor(self):
    return self.cor
class pessoa:
  
  nome=""
  email=""
  tel=""
  
  
  '''
    def __init__(self,nome,email,tel):
    self.nome=nome
    self.email=email
    self.tel=tel
  '''  
    #def __init__(self):
    
  def pessoa(self,nome,email,tel):
    self.nome=nome
    self.email=email
    self.tel=tel
    
  def setEmail(self,email):
    self.email=email  
    
  def getEmail(self):
    return self.email
  
  def setNome(self,nome):
    self.nome=nome
    
  def getNome(self):
    return self.nome
  
  def setTel(self,email):
    self.email=email
    
  def getTel(self):
    return self.tel
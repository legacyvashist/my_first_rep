class GeeksforGeeks:
  def __init__(self,h='nhi bheja') :
    self.geek = h

  def print_Geek(self) :
    print(self)
    print(self.geek)

objet = GeeksforGeeks("hiii")
objet2 = GeeksforGeeks()
objet.print_Geek()
objet2.print_Geek()
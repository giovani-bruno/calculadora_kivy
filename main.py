from kivy.app import App
from kivy.lang import Builder

class MainApp(App):


  def build(self):
    return Builder.load_file("main.kv")
  

  def botao_apertado(self, valor):
    display = self.root.ids.display
    display.text += valor


  def calcular_resultado(self):
    try:
      display = self.root.ids.display
      conta = display.text
      if '+' in conta:
        conta = conta.split("+")
        resultado = 0
        for numero in conta:
          resultado += int(numero)
      elif '-' in conta:
        conta = conta.split("-")
        resultado = int(conta[0])
        for i in range(1, len(conta)):
          resultado -= int(conta[i])
      elif '*' in conta:
        conta = conta.split("*")
        resultado = int(conta[0])
        for i in range(1, len(conta)):
          resultado *= int(conta[i])
      elif '/' in conta:
        conta = conta.split("/")
        resultado = int(conta[0])
        for i in range(1, len(conta)):
          resultado /= int(conta[i])
      display.text = str(int(resultado))
    except UnboundLocalError:
      pass


  def limpar(self):
    display = self.root.ids.display
    display.text = ""

MainApp().run()

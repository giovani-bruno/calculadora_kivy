from kivy.app import App
from kivy.lang import Builder

class MainApp(App):
  def build(self):
    return Builder.load_file("main.kv")
  

  def botao_apertado(self, numero):
    display = self.root.ids.display
    display.text += numero


  def operacao(self, operacao):
    self.operacao_selecionada = operacao
    display = self.root.ids.display
    display.text += operacao


  def calcular_resultado(self):
    try:
      display = self.root.ids.display
      conta = display.text
      if '+' in conta:
        operacao_index = conta.find('+')
        primeiro_numero = conta[:operacao_index]
        segundo_numero = conta[operacao_index + 1:]
        resultado = int(primeiro_numero) + int(segundo_numero)
      elif '-' in conta:
        operacao_index = conta.find('-')
        primeiro_numero = conta[:operacao_index]
        segundo_numero = conta[operacao_index + 1:]
        resultado = int(primeiro_numero) - int(segundo_numero)
      elif '*' in conta:
        operacao_index = conta.find('*')
        primeiro_numero = conta[:operacao_index]
        segundo_numero = conta[operacao_index + 1:]
        resultado = int(primeiro_numero) * int(segundo_numero)
      elif '/' in conta:
        operacao_index = conta.find('/')
        primeiro_numero = conta[:operacao_index]
        segundo_numero = conta[operacao_index + 1:]
        resultado = int(primeiro_numero) / int(segundo_numero)
      display.text = str(resultado)
    except UnboundLocalError:
      pass


  def limpar(self):
    display = self.root.ids.display
    display.text = ""

MainApp().run()

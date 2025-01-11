from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.lang import Builder


class MainApp(App):

  def build(self):
    Window.size = (360, 640)
    
    return Builder.load_file("main.kv")
  

  def botao_apertado(self, valor):
    display = self.root.ids.display
    display.text += valor


  def calcular_resultado(self):
    try:
      display = self.root.ids.display
      conta = display.text
      if conta:
        if "x" in conta:
          conta = conta.replace("x", "*")
        display.text = str(eval(conta))
    except UnboundLocalError:
      pass


  def limpar(self):
    display = self.root.ids.display
    display.text = ""


class ImageButton(ButtonBehavior, Image):
  pass

MainApp().run()

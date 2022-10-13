from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
import os
import main as pl
import entraWeb.main as web



Window.size = (500,600)

class gui(MDScreen):
    def pesquisa(self):
        placa = self.ids['placa'].text


        dicionario = web.pesquisa(placa)
        print(dicionario)
        if dicionario != 'documento em ordem':
            self.ids['nome'].text = f"nome:{dicionario['nome']}"
            self.ids['localidade'].text = f"localidade:{dicionario['localidade']}"
            self.ids['valor'].text = f"valor:{dicionario['valores'][0]}"
            self.ids['descricao'].text = dicionario['detalhesDebitos'][0]
            self.ids['valor2'].text = ''
            self.ids['descricao2'].text = ''
            if len(dicionario['valores']) >1:
                self.ids['valor2'].text = f"valor:{dicionario['valores'][1]}"
                self.ids['descricao2'].text = dicionario['detalhesDebitos'][1]
        else:
            self.ids['nome'].text = ''
            self.ids['localidade'].text = ''
            self.ids['valor'].text = ''
            self.ids['descricao'].text = dicionario
            self.ids['valor2'].text = ''
            self.ids['descricao2'].text = ''


    def clear(self):
        self.ids['nome'].text = ''
        self.ids['localidade'].text = ''
        self.ids['tipodebito'].text = ''
        self.ids['valor'].text = ''
        self.ids['descricao'].text = ''
        self.ids['tipodebito2'].text = ''
        self.ids['valor2'].text = ''
        self.ids['descricao2'].text = ''
        self.ids['placa'].text = ''



class tela(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Blue"
        return gui()

    def file_manager_open(self):

        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def exit_manager(self, *args):

        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path: str):
        self.exit_manager()
        placa = pl.placa(path)
        self.root.ids['placa'].text = placa


    def events(self, instance, keyboard, keycode, text, modifiers):

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


tela().run()


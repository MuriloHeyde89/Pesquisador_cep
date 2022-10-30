from tkinter import Button, mainloop
from winsound import PlaySound
import PySimpleGUI as sg
import requests as req
import time
from playsound import playsound

#Interface da classe e ligação com viacep
class Interface:
    def __Search(self):
        try:
            url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
            request = req.get(url)
            response_data = request.json()
            print("Endereço: {}".format(response_data['logradouro']))
            print("Bairro: {}".format(response_data['bairro']))
            print("Cidade: {}".format(response_data['localidade']))
            print("Estado: {}".format(response_data['uf']))
            print("País: Brasil")
            print("Código de Endereçamento Postal (CEP): {}".format(response_data['cep']))
            print("DDD: {}".format(response_data['ddd']))
        except Exception as error:
            print("Erro: {}".format(error))

#Criação do layout do app em pysimplegui    
    def __init__(self):
        sg.theme('LightBlue1')
        playsound('dropsound.mp3', block=False)
        app_layout = [
            [sg.Text("Código Postal: (insira o seu código)"), sg.Input(key=("input"), size=(12))],
            [sg.Button("Procurar")],
            [sg.Output(size=(50,10))],
            [sg.Button('Sair', size=(15,1))]
        ]
#Nome do aplicativo
        self.janela = sg.Window("Rastreador de Código Postal By Murilo Heyde").layout(app_layout)
#Iniciando procura
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            event = self.janela.read_closed_window_count
            self.cep = self.values['input']
            self.__Search()
            if event == 1:
                break
#Criação botão sair
    def botão_sair(self, Sair):
        self.botao_sair = Button(self.janela, text= 'Sair', command=self.janela.quit)
        self.botao.pack()
        slef.botao_sair.pack()
        mainloop()


app = Interface()
app.Iniciar()
app.Search()
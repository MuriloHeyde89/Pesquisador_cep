import PySimpleGUI as sg
import requests as req
import time

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
        app_layout = [
            [sg.Text("Código Postal: "), sg.Input(key=("input"), size=(10))],
            [sg.Button("Submit")],
            [sg.Output(size=(50,10))],
        ]

        self.janela = sg.Window("Rastreador de Código Postal").layout(app_layout)
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            event = self.janela.read_closed_window_count
            self.cep = self.values['input']
            self.__Search()
            if event == 1:
                break


app = Interface()
app.Iniciar()
app.Search()
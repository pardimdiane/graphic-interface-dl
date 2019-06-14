# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:43:58 2019

@author: caleb
"""

from tkinter import filedialog
from tkinter import *
import gatoCachorroCode

training_set = '/'
test_set = '/'

def load_directory():
    dirName = filedialog.askdirectory()
    return dirName
    
def load_file():
    fileName = filedialog.askopenfilename()
    return fileName

class Janela:
 

    
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()
        self.titulo=Label(self.frame,text='Interface IA',
                          font=('Verdana','22','bold'))
        self.titulo.pack(pady = 20)
        self.msg=Label(self.frame,
                        text = 'Este programa treina uma CNN para reconhecimento de gatos e cachorros',
                        font=('Verdana','16'))
        self.infor=Label(self.frame,
                        text = '...',
                        font=('Verdana','14','bold'))
        self.msg.focus_force()
        self.msg.pack(pady = 20)
        self.infor.pack(pady = 150)
        # Definindo o botão 1
        self.b01=Button(self.frame2,text='Abrir pasta de treino')
        self.b01['padx'],self.b01['pady'] = 10, 5
        self.b01['bg']='deepskyblue'
        self.b01.bind("<Any-Button>",self.button01)
        self.b01.bind("<FocusOut>",self.fout01)
        self.b01['relief']=RIDGE
        self.b01.pack(padx = 20, ipadx = 30, ipady = 30, side=LEFT)
        # Definindo o botão 2
        self.b02=Button(self.frame2,text='Abrir pasta de teste')
        self.b02['padx'],self.b02['pady'] = 10, 5
        self.b02['bg']='deepskyblue'
        self.b02.bind("<Any-Button>",self.button02)
        self.b02.bind("<FocusIn>",self.fin02)
        self.b02.bind("<FocusOut>",self.fout02)
        self.b02['relief']=RIDGE
        self.b02.pack(padx = 20, ipadx = 30, ipady = 30, side=LEFT)
        # Definindo o botão 3
        self.b03=Button(self.frame2,text='Treinar')
        self.b03['padx'],self.b03['pady'] = 10, 5
        self.b03['bg']='deepskyblue'
        self.b03.bind("<Any-Button>",self.button03)
        self.b03.bind("<FocusIn>",self.fin03)
        self.b03.bind("<FocusOut>",self.fout03)
        self.b03['relief']=RIDGE
        self.b03.pack(padx = 20, ipadx = 30, ipady = 30, side=LEFT)
        self.b03.config(bg = '#fc8888')
                        

       
    
    def button01(self,event):
        global training_set
        training_set = load_directory()
    def button02(self,event):
        global test_set
        test_set = load_directory()
    def fin01(self,event): self.b01['relief']=FLAT
    def fout01(self,event): self.b01['relief']=RIDGE
    def fin02(self,event): self.b02['relief']=FLAT
    def fout02(self,event): self.b02['relief']=RIDGEE
    def fin03(self,event): self.b03['relief']=FLAT
    def fout03(self,event): self.b03['relief']=RIDGE


    
    def button03(self,event):

        global training_set
        global test_set
        start = gatoCachorroCode.treaining_and_test(training_set, test_set)
        if (start == -1):
            self.infor.config(text='Selecione ambas as pastas de treino e teste.', foreground = 'red')
        elif(start == -2):
            self.infor.config(text='Houve um erro ao carregar os arquivos.', foreground = 'red')
        else:
            self.infor.config(text= 'Treinamento bem sucedido!', foreground = 'red')
        
    
        

    
raiz=Tk()
raiz.title("IA classificador de imagens")


window_height = 600
window_width = 900

screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

raiz.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


Janela(raiz)
raiz.mainloop()
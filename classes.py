from tkinter import *
from tkinter import ttk

class Widget_de_tarefa:
    def __init__(self,widget,lista_tarefas):
        self.username = StringVar()
        self.tarefa_concluida = BooleanVar(value=False)
        self.Nome_Tarefa = ttk.Entry(widget,width=100,textvariable=self.username)
        self.Marcador_Tarefa = ttk.Checkbutton(widget, variable=self.tarefa_concluida)
        self.Botao_remover = ttk.Button(widget,text="remover",command=lambda: remover_tarefa(self,lista_tarefas))


def criar_tarefa(lista_tarefas,widget):
    nova_tarefa = Widget_de_tarefa(widget,lista_tarefas)

    lista_tarefas.append(nova_tarefa)

    lista_tarefas[len(lista_tarefas)-1].Nome_Tarefa.grid(row=len(lista_tarefas),column=1)
    lista_tarefas[len(lista_tarefas)-1].Botao_remover.grid(row=len(lista_tarefas),column=2)
    lista_tarefas[len(lista_tarefas)-1].Marcador_Tarefa.grid(row=len(lista_tarefas),column=3)


def remover_tarefa(tarefa_widget,lista_tarefas):
    tarefa_widget.Nome_Tarefa.grid_forget()
    tarefa_widget.Marcador_Tarefa.grid_forget()
    tarefa_widget.Botao_remover.grid_forget()
    
    if tarefa_widget in lista_tarefas:
        lista_tarefas.remove(tarefa_widget)
    
    for i, tarefa in enumerate(lista_tarefas):
        tarefa.Nome_Tarefa.grid(row=i+1, column=1)
        tarefa.Botao_remover.grid(row=i+1, column=2)
        tarefa.Marcador_Tarefa.grid(row=i+1, column=3)
from tkinter import *
from tkinter import ttk

class Widget_de_tarefa:
    def __init__(self,widget,lista_tarefas):
        self.linha = len(lista_tarefas) + 1 #linha onde está o botão da tarefa
        self.botao_da_tarefa = ttk.Button(widget,text="nova_tarefa",command=lambda:mostrar_tasks(self))  # Mudou de widget_menu para widget
        self.username = StringVar()
        self.tarefa_concluida = BooleanVar(value=False)
        self.Nome_Tarefa = ttk.Entry(widget,width=60,textvariable=self.username)
        self.Marcador_Tarefa = ttk.Checkbutton(widget, variable=self.tarefa_concluida)
        self.Botao_remover = ttk.Button(widget,text="remover",command=lambda: remover_tarefa(self,lista_tarefas))


def criar_tarefa(lista_tarefas,widget):
    nova_tarefa = Widget_de_tarefa(widget,lista_tarefas)
    lista_tarefas.append(nova_tarefa)

    #botao para abrir as tarefas
    lista_tarefas[len(lista_tarefas)-1].botao_da_tarefa.grid(row=len(lista_tarefas),column=0)


def mostrar_tasks(tarefa):
    tarefa.Nome_Tarefa.grid(row=tarefa.linha,column=1)
    tarefa.Botao_remover.grid(row=tarefa.linha,column=3)
    tarefa.Marcador_Tarefa.grid(row=tarefa.linha,column=2)


def remover_tarefa(tarefa_widget,lista_tarefas):
    tarefa_widget.Nome_Tarefa.grid_forget()
    tarefa_widget.Marcador_Tarefa.grid_forget()
    tarefa_widget.Botao_remover.grid_forget()
    
    if tarefa_widget in lista_tarefas:
        tarefa_widget.botao_da_tarefa.grid_forget()
        lista_tarefas.remove(tarefa_widget)
    
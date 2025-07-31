from tkinter import *
from tkinter import ttk

class Widget_de_tarefa:
    def __init__(self,widget,lista_tarefas):
        self.username = StringVar()
        self.tarefa_concluida = BooleanVar(value=False)
        self.Nome_Tarefa = ttk.Entry(widget,width=60,textvariable=self.username)
        self.Marcador_Tarefa = ttk.Checkbutton(widget, variable=self.tarefa_concluida)
        self.Botao_remover = ttk.Button(widget,text="remover",command=lambda: remover_tarefa(self))

class widget_das_subtarefas:
    def __init__(self,widget,lista_tarefas):
        self.NUM_TAREFAS = 5
        self.linha = len(lista_tarefas) + 1 #linha onde está o botão da tarefa 
        self.botao_da_tarefa = ttk.Button(widget,text="nova_tarefa",command=lambda:mostrar_tasks(self))# Mudou de widget_menu para widget
        self.linhas = []
        for i in range(self.NUM_TAREFAS):
            task = Widget_de_tarefa(widget,lista_tarefas)
            self.linhas.append(task)


def criar_tarefa(lista_tarefas,widget):
    nova_tarefa = widget_das_subtarefas(widget,lista_tarefas)
    lista_tarefas.append(nova_tarefa)

    #botao para abrir as tarefas
    lista_tarefas[len(lista_tarefas)-1].botao_da_tarefa.grid(row=len(lista_tarefas),column=0)


def mostrar_tasks(tarefa):
    for i in range(tarefa.NUM_TAREFAS):
        tarefa.linhas[i].Nome_Tarefa.grid(row=i+1,column=1)
        tarefa.linhas[i].Marcador_Tarefa.grid(row=i+1,column=2)
        tarefa.linhas[i].Botao_remover.grid(row=i+1,column=3)

def remover_tarefa(tarefa_widget):
    tarefa_widget.Nome_Tarefa.destroy()
    tarefa_widget.Marcador_Tarefa.destroy()
    tarefa_widget.Botao_remover.destroy()
    
    
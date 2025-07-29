from tkinter import *
from tkinter import ttk

def criar_tarefa(widgit_das_tarefas,widgets_dos_botoes,vetor):
    def adcionar():
        linha = len(vetor)+2

        nova_tarefa = ttk.Entry(widgit_das_tarefas,textvariable=len(vetor),width=100)
        botao_concluir = ttk.Checkbutton(widgets_dos_botoes)
        botao_remover = ttk.Button()

        vetor.append(nova_tarefa)
        nova_tarefa.grid(column=1,row = linha,pady= 10)

        vetor.append(botao_concluir)
        botao_concluir.grid(column=3,row= linha,pady=10)

    return adcionar

#def remover_tarefa():



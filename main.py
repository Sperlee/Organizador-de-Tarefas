from classes import *
from tkinter import *
from tkinter import ttk


lista_tarefas = []

root = Tk()
root.title("Organizador de Tarefas")


widget_principal = ttk.Frame(root)
widget_tarefas = ttk.Frame(widget_principal)
widget_menu = ttk.Frame(widget_principal)


botão_criar_tarefa = ttk.Button(widget_menu,text="Nova Task",command=lambda: criar_tarefa(lista_tarefas,widget_tarefas))


widget_principal.grid(row=0,column=0)
widget_menu.grid(row=0,column=0, sticky="ew")  # Menu no topo
botão_criar_tarefa.grid(row=0,column=0)
widget_tarefas.grid(row=1,column=0, sticky="ew")  # Tarefas logo abaixo


root.geometry("600x800")
root.mainloop()
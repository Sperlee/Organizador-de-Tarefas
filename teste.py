from classes import *
from tkinter import *
from tkinter import ttk

lista_tarefas = []

root = Tk()

widget_principal = ttk.Frame(root)
widget_tarefas = ttk.Frame(widget_principal)
widget_menu = ttk.Frame(widget_principal)


botão_criar_tarefa = ttk.Button(widget_menu,text="Nova Task",command=lambda: criar_tarefa(lista_tarefas,widget_tarefas))


widget_principal.grid(row=0,column=0)
widget_menu.grid(row=0,column=0)
botão_criar_tarefa.grid()
widget_tarefas.grid(row=2,column=1)


root.geometry("800x600")
root.mainloop()
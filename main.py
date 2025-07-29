from tkinter import *
from tkinter import ttk
from funções import *

tarefas = []

root = Tk()

quadro_principal = ttk.Frame(root,width=200,height=200)

widget_do_menu = ttk.Frame(quadro_principal)
widget_das_tarefas = ttk.Frame(quadro_principal)
widget_meio = ttk.Frame(quadro_principal)
widget_dos_botões = ttk.Frame(quadro_principal)


gerador_nova_tarefa = ttk.Button(widget_do_menu,text= "Nova Tarefa",command=criar_tarefa(widget_das_tarefas,widget_dos_botões,tarefas))

quadro_principal.grid(column=0,row=0)



widget_do_menu.grid(column=0,row=0)
gerador_nova_tarefa.grid()

widget_das_tarefas.grid(column=1,row=1)
widget_meio.grid(column=2,row=1,padx=100)
widget_dos_botões.grid(column=3,row=1)


root.mainloop()
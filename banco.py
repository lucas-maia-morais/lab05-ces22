from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from tokenize import Double

class Command(ABC):

    @abstractmethod
    def execute(self)-> None:
        pass

class Saldo(Command):

    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.invokeSaldo()

class Update(Command):

    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.invokeUpdate()

class Extrato(Command):

    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.invokeExtrato()

    
class Conta:
    def __init__(self, saldo: Double) -> None:
        self.saldo = saldo
        self.historico = []

    def setGUI(self, gui: GUI):
        self.gui = gui

    def getSaldo(self):
        return self.saldo

    def updateSaldo(self, valor):
        self.historico.append(valor)
        self.saldo += valor
        return self.saldo

    def getExtrato(self):
        return 'Histórico:\n'+''.join(['{}\n'.format(v) for v in self.historico])

    def invokeSaldo(self):
        self.gui.show_saldo()

    def invokeUpdate(self):
        self.gui.do_update()

    def invokeExtrato(self):
        self.gui.show_extrato()

class GUI:
    def __init__(self, conta: Conta) -> None:
        self.conta = conta
        self.visor = 0
        self.saldoCommand = Saldo(self.conta)
        self.updateCommand = Update(self.conta)
        self.extratoCommand = Extrato(self.conta)
        self.root = None


    def show_system(self):
        root = tk.Tk()
        self.root = root
        frm = ttk.Frame(root, padding=50)
        root.title('BankApp')
        frm.grid()

        def retrieve_update():
            self.visor = visor.get()
            self.updateCommand.execute()

        visor = tk.DoubleVar()
        ttk.Label(frm, text='SALDO ATUAL').grid(column=1, row=0)
        ttk.Label(frm, text=str(self.conta.getSaldo())).grid(column=1,row=1, sticky="nse")
        ttk.Entry(frm, textvariable=visor).grid(column=1, row=2, sticky="nsew")
        ttk.Button(frm, text="Saldo", command=self.saldoCommand.execute).grid(column=0, row=3)
        ttk.Button(frm, text="Dep/Ret", command=retrieve_update).grid(column=1, row=3)
        ttk.Button(frm, text="Extrato", command=self.extratoCommand.execute).grid(column=2, row=3)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
        root.mainloop()

    def show_extrato(self):
        root = tk.Tk()
        frm = ttk.Frame(root, padding=50)
        root.title('Extrato')
        frm.grid()

        ttk.Label(frm, text=self.conta.getExtrato()).grid(column=0,row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
        root.mainloop()

    def show_saldo(self):
        root = tk.Tk()
        frm = ttk.Frame(root, padding=50)
        root.title('Saldo')
        frm.grid()

        ttk.Label(frm, text=self.conta.getSaldo()).grid(column=0,row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
        root.mainloop()

    def do_update(self):
        self.conta.updateSaldo(self.visor)
        self.root.destroy()
        self.show_system()


if __name__ == '__main__':

    c = Conta(30)
    g = GUI(c)
    c.setGUI(g)
    g.show_system()


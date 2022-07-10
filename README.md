# lab05-ces22

## Banco

Inicialmente vamos fazer uma aplicação bem simples de banco na qual não há transferencia entre contas, mas saque e deposito, consulta de extrato e saldo. Fizemos com design pattern Command.
- Invoker: Classe GUI responsável por renderizar as páginas e fazer a chamada para os botões
- Command: Classes do tipo Command que chamam o receiver
- Receiver: Classe Conta recebe os pedidos e também interage com a classe GUI para receber os parâmetros por exemplo de realizar update.

### Diagrama de classes
![Alt text](./imagens/banco-lab5.svg)

### Funcionamento da Aplicação

O Client será a main do arquivo banco.py que define as classes do problema. Nele criamos o objetos que interagem no sistema. Observe a main abaixo:
```
if __name__ == '__main__':

    c = Conta(30)
    g = GUI(c)
    c.setGUI(g)
    g.show_system()
```

- Agora observe a tela inicial:

![Alt text](./imagens/tela_inicial.png)

- Veja a tela de saldo:

![Alt text](./imagens/saldo.png)

- A seguir veja o antes e depois de um deposito de R$ 10,00
Antes:

![Alt text](./imagens/pre-add.png)

Depois:

![Alt text](./imagens/pos-add.png)

- A seguir veja o antes e depois de um saque de R$ 20,00
Antes:

![Alt text](./imagens/pre-rem.png)

Depois:

![Alt text](./imagens/pos-rem.png)

- Por último veja a tela de Extrato ao clicar extrato:

![Alt text](./imagens/extrato.png)


import tkinter as tk              # para criar a janela
import keyboard as kb             # para usar o ESC para fechar a janela


# ---------------------------------------------------------------------------------------------------------------------
def motion(event):  # posiciona a barra em relação à seta na janela
    x = event.x
    if 50 <= x <= 250:  # esse IF faz com que a barra não saia pelo cantos
        barra_btn.place(x=x-50)


# ---------------------------------------------------------------------------------------------------------------------
def cor_bola():  # função para mudar a cor da bola conforme avança nos níveis
    x = int(menu_var.get())  # tranformar o str em inteiro para usar nos ifs mais facieis
    if 5 <= x <= 10:
        bola_btn['bg'] = 'green'
    elif 2 <= x <= 4:
        bola_btn['bg'] = 'yellow'
    else:
        bola_btn['bg'] = 'red'


# ---------------------------------------------------------------------------------------------------------------------
def cronometro():  # função de repetição e validação
    x = bola_btn.winfo_x()  # pega a posição da bola
    y = bola_btn.winfo_y()  # pega a posição da bola
    # -----------------------------
    if x == 0 or y == 0:  # inicia a bola no centro e embaixo
        x, y = 150, 280
    # -----------------------------
    if bola_btn.winfo_y() == 30:  # se a bola estiver na mesma altura da barra
        if barra_btn.winfo_x() - 5 <= bola_btn.winfo_x() <= barra_btn.winfo_x() + 105:  # se a bola está na mesma linha
            placar2_num['text'] = str(int(placar2_num['text']) + 1)  # contabiliza uma defesa
            um_controle_y['text'] = 0  # muda o controlador para descer a bola
            y += 1.5  # joga a bola para baixo

            if menu_var.get() != '1':  # limita para não passar no nível 1
                menu_var.set(str(int(menu_var.get()) - 1))  # seta no menu e na velocidade o nível
                cor_bola()  # muda a cor da bola conforme o nível

    # -----------------------------
    if x == 280:  # quando alcança o limite direto
        um_controle_x['text'] = 1  # muda o controlador para a bola poder voltar

    if x == 10:  # quando alcança o limite esquerdo
        um_controle_x['text'] = 0  # muda o controlador para a bola poder voltar

    if um_controle_x['text'] == 0:  # testa se deve adicionar ou subtrair a posição da bola
        x += 1.5  # usando 1,5 deixa mais aleatório a movimentação da bola
    else:
        x -= 1.5
    # -----------------------------
    if y == 280:  # quando alcança o limite de baixo
        um_controle_y['text'] = 1  # muda o controlador para a bola poder voltar
        y -= 1.5

    if y == 10:  # quando passa pela barra marca um golo
        placar_num['text'] = str(int(placar_num['text']) + 1)  # acrescenta um golo na janela
        um_controle_y['text'] = 1  # muda o controlador para a bola poder voltar
        y = 280  # inicia a bola na parte de baixo

        if menu_var.get() != '10':  # limita para não passar no nível 10
            menu_var.set(str(int(menu_var.get()) + 1))  # seta no menu e na velocidade o nível
            cor_bola()  # muda a cor da bola conforme o nível

    if um_controle_y['text'] == 0:  # testa se deve adicionar ou subtrair a posição da bola
        y += 1
    else:
        y -= 1
    # -----------------------------
    bola_btn.place(x=x, y=y)  # recebe a nova posição da bola

    janela.after(int(menu_var.get()), lambda: cronometro())  # função de espera/repetição do tkinter


# ---------------------------------------------------------------------------------------------------------------------
# criação e configuração da janela
janela = tk.Tk()                             # cria o objeto janela
janela.resizable(width=False, height=False)  # desativa a mudança de tamanho
janela.title('Pong')

# tamanho: 325X250, posição: calula e posiciona
janela.geometry("%dx%d%d%d" % (300, 300, float(300 / 2 - janela.winfo_screenwidth() / 2),
                               float(300 / 2 - janela.winfo_screenheight() / 2)))
# ---------------------------------------------------------------------------------------------------------------------
texto = tk.Label(janela, text='Nível')  # objeto de texto
texto.place(x=210, y=5)                 # posicionando o texto
# ---------------------------------------------------------------------------------------------------------------------
placar = tk.Label(janela, text='Gols:')  # objeto de texto
placar.place(x=10, y=5)                  # posicionando o texto

placar_num = tk.Label(janela, text='0')  # objeto de texto
placar_num.place(x=40, y=5)              # posicionando o texto
# ---------------------------------------------------------------------------------------------------------------------
placar2 = tk.Label(janela, text='Defesas:')  # objeto de texto
placar2.place(x=80, y=5)                     # posicionando o texto

placar2_num = tk.Label(janela, text='0')  # objeto de texto
placar2_num.place(x=130, y=5)             # posicionando o texto
# ---------------------------------------------------------------------------------------------------------------------
menu_var = tk.StringVar(janela)  # objeto de menu
menu_var.set('10')               # inicia o menu no 10

menu = tk.OptionMenu(janela, menu_var, '10', '9', '8', '7', '6', '5', '4', '3', '2', '1')  # monta o menu com as opções
menu.place(x=240, y=0)  # posicionando o texto
# ---------------------------------------------------------------------------------------------------------------------
bola_btn = tk.Button(janela, bg='green')  # criando objeto botão
bola_btn.place(width=10, height=10)       # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
barra_btn = tk.Button(janela, bg='blue')     # criando objeto botão
barra_btn.place(width=100, height=10, y=30)  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
# variaveis de controle para saber se a bola deve subir ou descer
um_controle_x = tk.Label(text=0)
um_controle_y = tk.Label(text=0)
# ---------------------------------------------------------------------------------------------------------------------
cronometro()  # função de repetição e validação
# ---------------------------------------------------------------------------------------------------------------------
kb.on_press_key('ESC', lambda _: janela.destroy())
# ---------------------------------------------------------------------------------------------------------------------
janela.bind('<Motion>', motion)  # posiciona a barra em relação à seta na janela
janela.mainloop()  # mantem a janela aberta

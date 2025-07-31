import os
import webbrowser
from tkinter import Toplevel, Label, Button
from PIL import ImageTk, Image
import PySimpleGUI as sg

# Fonte padrão centralizada
FONT_PADRAO = ("Arial", 11, "bold")

def exibir():
    root = Toplevel()
    root.title("Rodovias")
    root.geometry("500x600")

    assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
    images = [
        "rodovia(1).png", "rodovia(2).png", "rodovia(3).png",
        "rodovia(4).png", "rodovia(5).png", "rodovia(6).png"
    ]
    image_list = [
        ImageTk.PhotoImage(
            Image.open(os.path.join(assets_dir, img)).resize((500, 550))
        ) for img in images
    ]

    counter = 0

    def ChangeImage():
        nonlocal counter
        counter = (counter + 1) % len(image_list)
        imageLabel.config(image=image_list[counter])
        infoLabel.config(text=f"Imagem {counter + 1} de {len(image_list)}")

    imageLabel = Label(root, image=image_list[0])
    infoLabel = Label(root, text="Imagem 1 de 6", font=("Arial", 10))
    button = Button(root, text="Próximo", width=10, height=1, bg="purple", fg="white", command=ChangeImage)

    imageLabel.pack()
    infoLabel.pack()
    button.pack(side="bottom", pady=3)

    root.protocol('wm_delete_window', root.destroy)
    root.mainloop()

def tela_inicial():
    sg.theme('DarkGrey9')
    button_graph = {'size': (15, 2), 'pad': (16, 5), 'button_color': ("white", "#F4564F")}
    text_graph = {'pad': (0, 100), 'font': 'Any 15 bold'}
    layout = [
        [sg.Text('APOIO 190', **text_graph)],
        [
            sg.Button('Nota Cartográfica', key="nota", **button_graph),
            sg.Button('Mapa CPI-2', key="mapa", **button_graph)
        ],
        [
            sg.Button('Rodovias CPI-2', key="rodovia", **button_graph),
            sg.Button('Rancho', key="rancho", **button_graph)
        ],
        [
            sg.Button('Ramais', key="ramais", **button_graph),
            sg.Button('SISBOL', key="sisbol", **button_graph)
        ],
        [
            sg.Button('Telefones', key="telefones", **button_graph),
            sg.Button('Pesquisar ID Dejem', key="dejem", **button_graph)
        ]
    ]

    janela = sg.Window(
        'APOIO 190', layout, size=(500, 600),
        element_justification='c', finalize=True, font=FONT_PADRAO
    )

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        elif eventos in ['nota', 'telefones', 'ramais']:
            manage_secondary_windows(eventos, janela)
            break  # Evita múltiplas janelas após retorno
        elif eventos == 'rodovia':
            exibir()
        elif eventos == 'mapa':
            webbrowser.open(
                "https://www.google.com/maps/d/u/0/viewer?hl=pt-BR&mid=16KbTEVrLWKzLdamU_juPp-XvpbBiTSgF&ll=-23.021202234164612%2C-46.7070392565535&z=10"
            )
        elif eventos == 'rancho':
            webbrowser.open(
                "http://weblinux.intranet.policiamilitar.sp.gov.br/35bpmi/rancho/"
            )
        elif eventos == 'sisbol':
            webbrowser.open(
                "http://sisbol.intranet.policiamilitar.sp.gov.br/_sisbolsc8/frmlogin/"
            )
        elif eventos == 'dejem':
            webbrowser.open(
                "http://www.copom.intranet.policiamilitar.sp.gov.br/tecnologia/controle_dejem_por_id/"
            )

    janela.close()

def manage_secondary_windows(event, janela):
    layout = get_layout(event)
    janela.close()
    secondary_window = sg.Window(event, layout, font=FONT_PADRAO)
    while True:
        evt, vals = secondary_window.read()
        if evt in (sg.WINDOW_CLOSED, 'Voltar'):
            secondary_window.close()
            tela_inicial()
            break

def get_layout(event):
    assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

    imagens = {
        'nota': "cong.png",
        'telefones': "telefones.png",
        'ramais': "ramais.png"
    }

    if event in imagens:
        return [
            [sg.Image(filename=os.path.join(assets_dir, imagens[event]))],
            [sg.Button('Voltar', key="Voltar")]
        ]
    else:
        return [[sg.Text('Evento não suportado.')], [sg.Button('Voltar', key="Voltar")]]

if __name__ == "__main__":
    tela_inicial()
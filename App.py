import tkinter as tk # Resposta 2a: adicionei a biblioteca tkinter
from BancoDeDados import BancoDeDados
from Jogador import Jogador
from TelaSelecaoIdioma import TelaSelecaoIdioma
from Musica import Musica


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor_fundo = "#ECECEC"
        self.cor_texto = "#333333"
        self.cor_botao = "#4CAF50"
        self.cor_texto_botao = "#FFFFFF"

        self.title("Quiz Igualdade de Gênero")
        # Janela para perguntas
        self.geometry("1000x550")
        self.configure(bg=self.cor_fundo)
        self.option_add('*Font', 'Arial')

        # Cria gerenciador de música
        self.musica = Musica()
        # Cria botão de som no canto superior direito
        self.btn_som = tk.Button(
            self, text="🔊🎵", font=("Arial", 14, "bold"),
            bg="white", fg="black", command=self.alternar_musica
        )
        self.btn_som.place(x=925, y=20, width=55, height=40)

        # Aplica imagem a janela
        try:
            self.icone_app = tk.PhotoImage(file='logo2.png')
            self.label_icone = tk.Label(self, image=self.icone_app, bg=self.cor_fundo)
            self.label_icone.pack(pady=10)
        except:
            pass

        self.db = BancoDeDados(
            host='sql7.freemysqlhosting.net',
            user='sql7749196',
            password='Sucesso$Arte999',
            database='sql7749196',
            port=3306
        )
        self.jogador = Jogador()
        self.quiz = None

        self._frame_atual = None
        self.mudar_tela(TelaSelecaoIdioma)

    def alternar_musica(self):
        #Liga ou desliga a música de fundo e atualiza o botão.
        self.musica.alternar_musica()
        self.btn_som.config(text='🔊🎵' if self.musica.musica_ativa else '🔇🎵')

    def mudar_tela(self, classe_tela):
        if self._frame_atual is not None:
            self._frame_atual.destroy()
        self._frame_atual = classe_tela(self)
        self._frame_atual.pack(pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()


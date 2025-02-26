import pygame # Resposta 2a: adicionei a biblioteca pygame

class Musica:
    def __init__(self, arquivo="musica_instrumental.mp3", volume=0.3):
        pygame.mixer.init()
        self.musica_ativa = True
        self.arquivo = arquivo
        self.volume = volume

        pygame.mixer.music.load(self.arquivo)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)  # -1 significa tocar em loop

    def alternar_musica(self):
        #Liga ou desliga a música de fundo.
        if self.musica_ativa:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.musica_ativa = not self.musica_ativa
